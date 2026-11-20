# coding: utf-8

# flake8: noqa

"""
    TIDAL API

    The TIDAL API is a [JSON:API](https://jsonapi.org/)-compliant web API exposing TIDAL's music catalogue, metadata, and user functionality. Guides, authorization documentation, and API key management live at [developer.tidal.com](https://developer.tidal.com).  All endpoints exchange `application/vnd.api+json` documents per the [JSON:API specification](https://jsonapi.org/format/): [resource objects](https://jsonapi.org/format/#document-resource-objects) with `attributes` and `relationships`, [compound documents](https://jsonapi.org/format/#document-compound-documents) via `include`, and standard [error objects](https://jsonapi.org/format/#error-objects).  ### Authentication and authorization  Every request requires an OAuth 2.0 access token in the `Authorization: Bearer` header. Tokens are issued at `https://auth.tidal.com/v1/oauth2/token` via the client-credentials flow (server-to-server) or the authorization-code + PKCE flow (user context; authorize at `https://login.tidal.com/authorize`). Each endpoint documents which flows it accepts, the access tier it requires, and the scopes that apply. Scopes protect private user data: fields you are not authorized to read are redacted from the response rather than causing an error, and resources you cannot access at all behave as if they do not exist. See the [authorization guide](https://developer.tidal.com/documentation/api-sdk/api-sdk-authorization) for details.  ### Common wire types and compatibility  Each property's schema is authoritative for its allowed values, format, requiredness, nullability, and constraints. A standard defines how a value is represented; an individual schema may support only a documented subset.  - **Enums** use `UPPER_CASE_UNDERSCORE`, except JSON:API resource types, which use plural camelCase names such as `playlistGenerationSchedules`. New values can be added to any enum at any time, so treat unknown values as forward-compatible rather than errors. - **Resource IDs** are opaque strings. A few resources document well-known IDs for permanent system singleton instances; compare those IDs by exact value. Never parse, construct, or infer meaning from any other `id`, even when its current representation resembles an integer, UUID, or another recognizable value. Other properties explicitly marked with OpenAPI `format: uuid` are UUIDs. - **Dates and times** use ISO 8601. Date-times use the OpenAPI `date-time` format (`2024-05-01T12:00:00Z`), dates use `YYYY-MM-DD`, and durations use values such as `PT3M5S`. - **Recurrence frequencies** use RFC 5545 `FREQ` names such as `DAILY`, `WEEKLY`, and `MONTHLY`. The property's enum lists the frequencies that field currently supports. - **Weekdays** use `MONDAY` through `SUNDAY`. - **Time zones** use IANA Time Zone Database identifiers such as `Europe/Stockholm`, not abbreviations or raw UTC offsets for recurring civil-time schedules. - **Country codes** use ISO 3166-1 alpha-2; the shared country type also accepts `WW` for worldwide. **Locales** use IETF BCP 47 language tags such as `en-US`. - **Currencies** use ISO 4217 codes. Monetary amounts are decimal strings; each field defines its sign and precision constraints. - **Colors** use three- or six-digit hexadecimal strings (`#RGB` or `#RRGGBB`). Resource links to external URLs use JSON:API link objects with an `href` member.  ### Resource identifiers  Where supported, `filter[subject]=tracks:123` matches a related resource by type and ID; `filter[subject.id]=123` and `filter[subject.type]=tracks` match either component. Where multiple identifiers are accepted, comma-separated values match any complete pair. When a member path names a to-many relationship, at least one related resource must match; filtering does not trim that relationship. On collection and to-many relationship reads, the reserved root `self` (`filter[self]=tracks:123`) filters primary data itself. Each endpoint lists its supported filters and types.  Where supported, `me` aliases the authenticated user's dedicated resource ID for the referenced resource type. It works in paths, resource-ID filters, compact identifiers (`type:me`), resource PATCH primary IDs and standalone relationship mutation identifiers, with the same meaning as the resolved ID. Reads using the alias are `no-store`.  ### Relationships and includes  [Relationships](https://jsonapi.org/format/#document-resource-object-relationships) are returned only on request: [`include`](https://jsonapi.org/format/#fetching-includes) selects linkage and related content, while `includeLinkage` selects authorized linkage only. A relationship that was not requested is absent from the response, not empty. The full set of relationships a resource supports is documented in its schema.  For INTERNAL clients on resource GET endpoints, `includeLinkage` accepts comma-separated direct relationship names, for example `includeLinkage=subject,viewer`. It does not load related resources or add an `included` section. Nested paths and type qualifiers are unsupported. To-many linkage retains its normal pagination and relationship `next` links. Selecting the same relationship with both parameters applies full include behavior and reads the relationship once.  Request related resources in one round trip with `?include=`, a comma-separated list of dot-separated relationship paths — e.g. `include=coverArt,artists.profileArt` on an album. A nested path automatically embeds its intermediate resources: `artists.profileArt` includes the artists as well as their profile art. Include paths are always relative to the request's root resource, also on relationship endpoints. Including a relationship never changes the primary data; the related resources are added to `included`.  Include paths are validated: a path that cannot be resolved against the resources' documented relationships is rejected with `400`. Include trees are also bounded in path depth (default 3 levels) and in the total number of distinct resources they name (default 10); individual endpoints may apply different limits. Both selectors share the include-node limit, counting overlapping roots once. A request exceeding either limit is rejected with `400`, with the effective limit stated in the error.  ### Filtering, sorting, pagination  - [`filter[<memberPath>]=value`](https://jsonapi.org/format/#fetching-filtering) filters primary data by equality. Each endpoint lists its available filters; most collections require at least one. - Where explicitly documented, `filter[<memberPath>][ne]=value` negates the complete equality predicate. When the member path names a to-many relationship, no related ID may match any supplied value; a known-empty relationship matches. Operators are separate from values. Supplied comparisons combine with AND. For a required filter with multiple supported comparisons, at least one must be supplied; the parameter descriptions identify these alternatives. Unsupported operators and groups return `400`. - Where documented, `filter[<path>][<operator>]=value` applies an endpoint-defined operator, such as `filter[self][matchesQuery]`. Its meaning is described per endpoint, and it combines with other filters by AND. - [`sort=<memberPath>`](https://jsonapi.org/format/#fetching-sorting) sorts ascending, `-<memberPath>` descending (`sort=-addedAt`). Filter and sort member paths are relative to primary data. - Parameters an endpoint cannot honor are rejected with `400`: a `filter[...]` parameter the endpoint does not document (the error lists the available filters), or `sort` on an endpoint that documents no sort values. - [Pagination](https://jsonapi.org/format/#fetching-pagination) is cursor-based: responses carry `links.self` and, while more pages exist, `links.next` with an opaque `page[cursor]`. Follow `next` until absent — there are no offset or total-page parameters. Collection sizes, when available, appear as `meta.total` and may be approximate.  ### Type qualifiers  Where a relationship can contain several resource types, a path segment may be prefixed with a concrete type to scope which type's member is accessed. A playlist's `items` are `tracks` or `videos`: `GET /playlists/{id}?include=items.tracks:albums` resolves `albums` only for the items that are tracks. Qualifiers scope member access — they never filter which resources appear in a relationship — and can be chained.  The same syntax applies to `filter` and `sort` member paths on endpoints that support it; where supported, the qualified member is listed among the endpoint's documented filters and sort values. The syntax follows JSON:API proposal [json-api#1695](https://github.com/json-api/json-api/issues/1695).  ### Mutations  - [Partial updates](https://jsonapi.org/format/#crud-updating-resource-attributes) distinguish three wire states for nullable attributes: omission leaves the current value unchanged, an explicit `null` clears it, and a concrete value updates it. - Every mutation accepts an [`Idempotency-Key`](https://www.ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-07.html) header. Keys are scoped to the client and the authenticated user. Once the original request has completed, retrying it with the same key, method, path, query and payload within one hour replays its response; a retry while it is still processing is rejected with `409`, and the same key with a different method, path, query or payload with `422`. - After a successful write, your own subsequent reads reflect the change; other clients may observe it with a delay.  ### Revisions and concurrent editing  Where supported, `attributes.revision` identifies the resource's documented aggregate state; a separately versioned relationship collection uses document `meta.revision`. Revisions are nonnegative integers that increase when covered state changes. Compare them only within the same identity and scope, preserve the exact value, and never calculate the next revision. Related content, viewer projections and independent sources are not automatically covered. Domain fields named `version`, such as a music edition, are distinct; existing endpoints retain their documented contracts.  Guarded mutations accept the observed value as top-level `meta.expectedRevision`. Each operation declares its scope and whether the precondition is required. A mismatch returns `409`; missing required input returns `400`. Refresh and reconcile after a conflict, then submit a new operation with a new idempotency key. An identical retry with the original key replays a recorded success under the idempotency contract. These revisions are not HTTP ETags.  Returned revisions describe observed snapshots, not reservations for later writes. Background changes can advance them immediately after a successful response.  ### Media resource replacements - BETA Internal only  Media resources (`tracks`, `videos`, and `albums`) can become unavailable in a country when licensing rights change. By default, TIDAL API returns the resource identifiers originally stored in a collection. This keeps ordinary reads predictable and consistent.  If a stored media resource is unavailable for the effective country, TIDAL may identify a contextually applicable alternative that is available there. Replacement is best effort, so an alternative is not always available. Replacement never changes the stored collection.  TIDAL API provides two ways to work with replacements:  1. **Inspect the `replacement` relationship.** A media resource can expose its applicable alternative through the `replacement` relationship. Include this relationship when a client needs both the original and replacement identifiers or wants to decide whether to use the replacement.  2. **Apply replacements with `replaceMedia`.** Clients can use `replaceMedia` to substitute applicable replacements directly into selected relationship data. The parameter accepts relationship paths using the same syntax as `include`. Projection affects only the response and preserves relationship order and metadata. Each identifier includes `meta.replacement` describing whether it was `ORIGINAL`, `REPLACED`, or `NOT_REPLACED`.  For example, `GET /playlists/{id}?include=items&replaceMedia=items` applies replacements to media identifiers in the playlist's `items` relationship.  ### Compression  Responses are gzip-compressed when the request includes `Accept-Encoding: gzip` (bodies over 2 KB).  ### Deprecation  Deprecated endpoints, parameters, and fields are marked `deprecated` in this specification, with the replacement noted in their description. Deprecated functionality keeps working for at least six months after being marked, and is only removed once a replacement is generally available.

    The version of the OpenAPI document: 1.10.254
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# Define package exports
__all__ = [
    "AcceptedTermsApi",
    "AlbumStatisticsApi",
    "AlbumsApi",
    "AppreciationsApi",
    "ArtistBiographiesApi",
    "ArtistClaimStatusesApi",
    "ArtistClaimsApi",
    "ArtistRolesApi",
    "ArtistSalesStatisticsApi",
    "ArtistStreamsStatisticsApi",
    "ArtistsApi",
    "ArtworkLibrariesApi",
    "ArtworksApi",
    "ClientCertificatesApi",
    "ClientsApi",
    "CollaborationInviteRedemptionsApi",
    "CollaborationInvitesApi",
    "CommentSummariesApi",
    "CommentsApi",
    "ContentClaimsApi",
    "CreditsApi",
    "DownloadsApi",
    "DspSharingLinksApi",
    "DynamicModulesApi",
    "DynamicPagesApi",
    "FolderItemsApi",
    "FoldersApi",
    "GenresApi",
    "GroupsApi",
    "InstallationsApi",
    "LyricsApi",
    "ManualArtistClaimsApi",
    "OfflineTasksApi",
    "PlayQueuesApi",
    "PlaylistGenerationSchedulesApi",
    "PlaylistGenerationsApi",
    "PlaylistsApi",
    "PriceConfigurationsApi",
    "ProviderOwnersApi",
    "ProviderProductInfosApi",
    "ProvidersApi",
    "PurchasesApi",
    "ReactionSummariesApi",
    "ReactionsApi",
    "ResourceGrantInvitationsApi",
    "ResourceGrantsApi",
    "SavedSharesApi",
    "ScopesApi",
    "SearchHistoryEntriesApi",
    "SearchResultsApi",
    "SearchSuggestionsApi",
    "SharesApi",
    "SharingSummariesApi",
    "SquareConnectionsApi",
    "SquareItemVariationPhysicalCountsApi",
    "SquareItemVariationsApi",
    "SquareItemsApi",
    "SquareSitesApi",
    "StripeConnectionsApi",
    "StripeDashboardLinksApi",
    "StudioHomeEventTilesApi",
    "StudioHomeInsightTilesApi",
    "StudioHomeMerchTilesApi",
    "StudioHomeMusicTilesApi",
    "SubscriptionPriceChangeDecisionsApi",
    "TemporaryUserTokensApi",
    "TermsApi",
    "TrackFilesApi",
    "TrackManifestsApi",
    "TrackSourceFilesApi",
    "TrackStatisticsApi",
    "TracksApi",
    "TracksMetadataStatusApi",
    "UsageRulesApi",
    "UserCollectionAlbumsApi",
    "UserCollectionArtistsApi",
    "UserCollectionFoldersApi",
    "UserCollectionPlaylistsApi",
    "UserCollectionSaveForLatersApi",
    "UserCollectionTracksApi",
    "UserCollectionVideosApi",
    "UserDailyMixesApi",
    "UserDataExportRequestsApi",
    "UserDataExportsApi",
    "UserDiscoveryMixesApi",
    "UserFeedItemsApi",
    "UserFeedsApi",
    "UserNewReleaseMixesApi",
    "UserOfflineMixesApi",
    "UserPlaybackStatesApi",
    "UserRecommendationBlocksApi",
    "UserReportsApi",
    "UserSubscriptionPriceChangesApi",
    "UsersApi",
    "VideoManifestsApi",
    "VideosApi",
    "ViewerContextsApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "AcceptedTermsAttributes",
    "AcceptedTermsCreateOperationPayload",
    "AcceptedTermsCreateOperationPayloadData",
    "AcceptedTermsCreateOperationPayloadDataRelationships",
    "AcceptedTermsCreateOperationPayloadDataRelationshipsTerms",
    "AcceptedTermsCreateOperationPayloadDataRelationshipsTermsData",
    "AcceptedTermsCreateSingleResourceDataDocument",
    "AcceptedTermsMultiResourceDataDocument",
    "AcceptedTermsOwnersMultiRelationshipDataDocument",
    "AcceptedTermsRelationships",
    "AcceptedTermsResourceObject",
    "AcceptedTermsTermsSingleRelationshipDataDocument",
    "AlbumStatisticsAttributes",
    "AlbumStatisticsOwnersMultiRelationshipDataDocument",
    "AlbumStatisticsRelationships",
    "AlbumStatisticsResourceObject",
    "AlbumStatisticsSingleResourceDataDocument",
    "AlbumsAlbumStatisticsSingleRelationshipDataDocument",
    "AlbumsArtistsMultiRelationshipDataDocument",
    "AlbumsArtistsRelationshipUpdateOperationPayload",
    "AlbumsArtistsRelationshipUpdateOperationPayloadData",
    "AlbumsArtistsRelationshipUpdateOperationPayloadMeta",
    "AlbumsAttributes",
    "AlbumsCoverArtMultiRelationshipDataDocument",
    "AlbumsCoverArtRelationshipUpdateOperationPayload",
    "AlbumsCoverArtRelationshipUpdateOperationPayloadData",
    "AlbumsCreateOperationPayload",
    "AlbumsCreateOperationPayloadData",
    "AlbumsCreateOperationPayloadDataAttributes",
    "AlbumsCreateOperationPayloadDataRelationships",
    "AlbumsCreateOperationPayloadDataRelationshipsArtists",
    "AlbumsCreateOperationPayloadDataRelationshipsArtistsData",
    "AlbumsCreateOperationPayloadDataRelationshipsGenres",
    "AlbumsCreateOperationPayloadDataRelationshipsGenresData",
    "AlbumsCreateSingleResourceDataDocument",
    "AlbumsGenresMultiRelationshipDataDocument",
    "AlbumsItemsMultiRelationshipDataDocument",
    "AlbumsItemsRelationshipUpdateOperationPayload",
    "AlbumsItemsRelationshipUpdateOperationPayloadData",
    "AlbumsItemsRelationshipUpdateOperationPayloadMeta",
    "AlbumsItemsResourceIdentifier",
    "AlbumsItemsResourceIdentifierMeta",
    "AlbumsMultiResourceDataDocument",
    "AlbumsOwnersMultiRelationshipDataDocument",
    "AlbumsPriceConfigSingleRelationshipDataDocument",
    "AlbumsProvidersMultiRelationshipDataDocument",
    "AlbumsRelationships",
    "AlbumsReplacementResourceIdentifier",
    "AlbumsReplacementResourceIdentifierMeta",
    "AlbumsReplacementSingleRelationshipDataDocument",
    "AlbumsResourceObject",
    "AlbumsSharesMultiRelationshipDataDocument",
    "AlbumsSimilarAlbumsMultiRelationshipDataDocument",
    "AlbumsSimilarAlbumsResourceIdentifier",
    "AlbumsSimilarAlbumsResourceIdentifierMeta",
    "AlbumsSingleResourceDataDocument",
    "AlbumsSuggestedCoverArtsMultiRelationshipDataDocument",
    "AlbumsSuggestedCoverArtsMultiRelationshipDataDocumentMeta",
    "AlbumsSuggestedCoverArtsResourceIdentifier",
    "AlbumsSuggestedCoverArtsResourceIdentifierMeta",
    "AlbumsUpdateOperationPayload",
    "AlbumsUpdateOperationPayloadData",
    "AlbumsUpdateOperationPayloadDataAttributes",
    "AlbumsUpdateOperationPayloadDataRelationships",
    "AlbumsUpdateOperationPayloadDataRelationshipsGenres",
    "AlbumsUpdateOperationPayloadDataRelationshipsGenresData",
    "AlbumsUsageRulesSingleRelationshipDataDocument",
    "AppreciationsAttributes",
    "AppreciationsCreateOperationPayload",
    "AppreciationsCreateOperationPayloadData",
    "AppreciationsCreateOperationPayloadDataRelationships",
    "AppreciationsCreateOperationPayloadDataRelationshipsAppreciatedItem",
    "AppreciationsCreateOperationPayloadDataRelationshipsAppreciatedItemData",
    "AppreciationsCreateOperationPayloadMeta",
    "AppreciationsCreateSingleResourceDataDocument",
    "AppreciationsResourceObject",
    "ArtistBiographiesAttributes",
    "ArtistBiographiesOwnersMultiRelationshipDataDocument",
    "ArtistBiographiesRelationships",
    "ArtistBiographiesResourceObject",
    "ArtistBiographiesSingleResourceDataDocument",
    "ArtistBiographiesUpdateOperationPayload",
    "ArtistBiographiesUpdateOperationPayloadData",
    "ArtistBiographiesUpdateOperationPayloadDataAttributes",
    "ArtistClaimStatusesAttributes",
    "ArtistClaimStatusesMultiResourceDataDocument",
    "ArtistClaimStatusesResourceObject",
    "ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument",
    "ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload",
    "ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayloadData",
    "ArtistClaimsAttributes",
    "ArtistClaimsCreateOperationPayload",
    "ArtistClaimsCreateOperationPayloadData",
    "ArtistClaimsCreateOperationPayloadDataAttributes",
    "ArtistClaimsCreateOperationPayloadMeta",
    "ArtistClaimsCreateSingleResourceDataDocument",
    "ArtistClaimsMultiResourceDataDocument",
    "ArtistClaimsOwnersMultiRelationshipDataDocument",
    "ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument",
    "ArtistClaimsRelationships",
    "ArtistClaimsResourceObject",
    "ArtistClaimsSingleResourceDataDocument",
    "ArtistClaimsUpdateOperationPayload",
    "ArtistClaimsUpdateOperationPayloadData",
    "ArtistClaimsUpdateOperationPayloadMeta",
    "ArtistRolesAttributes",
    "ArtistRolesResourceObject",
    "ArtistRolesSingleResourceDataDocument",
    "ArtistSalesStatisticsArtistSingleRelationshipDataDocument",
    "ArtistSalesStatisticsAttributes",
    "ArtistSalesStatisticsBuyerSourceShare",
    "ArtistSalesStatisticsBuyerSources",
    "ArtistSalesStatisticsByType",
    "ArtistSalesStatisticsMultiResourceDataDocument",
    "ArtistSalesStatisticsNetSales",
    "ArtistSalesStatisticsRefunds",
    "ArtistSalesStatisticsRelationships",
    "ArtistSalesStatisticsResourceObject",
    "ArtistSalesStatisticsSeries",
    "ArtistSalesStatisticsSeriesPoint",
    "ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument",
    "ArtistSalesStatisticsTopSellersMultiRelationshipDataDocumentMeta",
    "ArtistSalesStatisticsTopSellersResourceIdentifier",
    "ArtistSalesStatisticsTopSellersResourceIdentifierMeta",
    "ArtistStatisticsBucketPeriod",
    "ArtistStatisticsWindowPeriod",
    "ArtistStreamsStatisticsArtistSingleRelationshipDataDocument",
    "ArtistStreamsStatisticsAttributes",
    "ArtistStreamsStatisticsCount",
    "ArtistStreamsStatisticsCountryListeners",
    "ArtistStreamsStatisticsMultiResourceDataDocument",
    "ArtistStreamsStatisticsOtherPlays",
    "ArtistStreamsStatisticsPlays",
    "ArtistStreamsStatisticsPlaysBySource",
    "ArtistStreamsStatisticsRelationships",
    "ArtistStreamsStatisticsResourceObject",
    "ArtistStreamsStatisticsSeries",
    "ArtistStreamsStatisticsSeriesPoint",
    "ArtistStreamsStatisticsSourcePlays",
    "ArtistStreamsStatisticsTopCountries",
    "ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument",
    "ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocumentMeta",
    "ArtistStreamsStatisticsTopTracksResourceIdentifier",
    "ArtistStreamsStatisticsTopTracksResourceIdentifierMeta",
    "ArtistsAlbumsMultiRelationshipDataDocument",
    "ArtistsAlbumsResourceIdentifier",
    "ArtistsAlbumsResourceIdentifierMeta",
    "ArtistsAttributes",
    "ArtistsBannerArtMultiRelationshipDataDocument",
    "ArtistsBannerArtRelationshipUpdateOperationPayload",
    "ArtistsBannerArtRelationshipUpdateOperationPayloadData",
    "ArtistsBiographySingleRelationshipDataDocument",
    "ArtistsClaimStatusSingleRelationshipDataDocument",
    "ArtistsCreateOperationPayload",
    "ArtistsCreateOperationPayloadData",
    "ArtistsCreateOperationPayloadDataAttributes",
    "ArtistsCreateOperationPayloadMeta",
    "ArtistsCreateSingleResourceDataDocument",
    "ArtistsFollowersMultiRelationshipDataDocument",
    "ArtistsFollowersResourceIdentifier",
    "ArtistsFollowersResourceIdentifierMeta",
    "ArtistsFollowersResourceMetaViewerContext",
    "ArtistsFollowingMultiRelationshipDataDocument",
    "ArtistsFollowingRelationshipAddOperationPayload",
    "ArtistsFollowingRelationshipAddOperationPayloadData",
    "ArtistsFollowingRelationshipRemoveOperationPayload",
    "ArtistsFollowingRelationshipRemoveOperationPayloadData",
    "ArtistsFollowingResourceIdentifier",
    "ArtistsFollowingResourceIdentifierMeta",
    "ArtistsLogoArtMultiRelationshipDataDocument",
    "ArtistsLogoArtRelationshipUpdateOperationPayload",
    "ArtistsLogoArtRelationshipUpdateOperationPayloadData",
    "ArtistsMultiResourceDataDocument",
    "ArtistsOwnersMultiRelationshipDataDocument",
    "ArtistsProfileArtMultiRelationshipDataDocument",
    "ArtistsProfileArtRelationshipUpdateOperationPayload",
    "ArtistsProfileArtRelationshipUpdateOperationPayloadData",
    "ArtistsRadioMultiRelationshipDataDocument",
    "ArtistsRelationships",
    "ArtistsResourceObject",
    "ArtistsRolesMultiRelationshipDataDocument",
    "ArtistsSimilarArtistsMultiRelationshipDataDocument",
    "ArtistsSingleResourceDataDocument",
    "ArtistsTrackProvidersMultiRelationshipDataDocument",
    "ArtistsTrackProvidersResourceIdentifier",
    "ArtistsTrackProvidersResourceIdentifierMeta",
    "ArtistsTracksMultiRelationshipDataDocument",
    "ArtistsTracksResourceIdentifier",
    "ArtistsTracksResourceIdentifierMeta",
    "ArtistsUpdateOperationPayload",
    "ArtistsUpdateOperationPayloadData",
    "ArtistsUpdateOperationPayloadDataAttributes",
    "ArtistsUpdateOperationPayloadMeta",
    "ArtistsVideosMultiRelationshipDataDocument",
    "ArtistsVideosResourceIdentifier",
    "ArtistsVideosResourceIdentifierMeta",
    "Artwork",
    "ArtworkFile",
    "ArtworkFileMeta",
    "ArtworkLibrariesArtworksMultiRelationshipDataDocument",
    "ArtworkLibrariesArtworksResourceIdentifier",
    "ArtworkLibrariesArtworksResourceIdentifierMeta",
    "ArtworkLibrariesAttributes",
    "ArtworkLibrariesMultiResourceDataDocument",
    "ArtworkLibrariesRandomArtworkResourceIdentifier",
    "ArtworkLibrariesRandomArtworkResourceIdentifierMeta",
    "ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument",
    "ArtworkLibrariesRelationships",
    "ArtworkLibrariesResourceObject",
    "ArtworkLibrariesSingleResourceDataDocument",
    "ArtworkSourceFile",
    "ArtworkVisualMetadata",
    "ArtworksAttributes",
    "ArtworksCreateOperationPayload",
    "ArtworksCreateOperationPayloadData",
    "ArtworksCreateOperationPayloadDataAttributes",
    "ArtworksCreateOperationPayloadDataAttributesSourceFile",
    "ArtworksCreateSingleResourceDataDocument",
    "ArtworksMultiResourceDataDocument",
    "ArtworksOwnersMultiRelationshipDataDocument",
    "ArtworksRelationships",
    "ArtworksResourceObject",
    "ArtworksSingleResourceDataDocument",
    "AtomicOperations400ResponseBody",
    "AtomicOperations400ResponseBodyErrorsInner",
    "AtomicOperations403ResponseBody",
    "AtomicOperations403ResponseBodyErrorsInner",
    "AtomicOperations404ResponseBody",
    "AtomicOperations404ResponseBodyErrorsInner",
    "AtomicOperations405ResponseBody",
    "AtomicOperations405ResponseBodyErrorsInner",
    "AtomicOperations406ResponseBody",
    "AtomicOperations406ResponseBodyErrorsInner",
    "AtomicOperations409ResponseBody",
    "AtomicOperations409ResponseBodyErrorsInner",
    "AtomicOperations415ResponseBody",
    "AtomicOperations415ResponseBodyErrorsInner",
    "AtomicOperations422ResponseBody",
    "AtomicOperations422ResponseBodyErrorsInner",
    "AtomicOperations429ResponseBody",
    "AtomicOperations429ResponseBodyErrorsInner",
    "AtomicOperations500ResponseBody",
    "AtomicOperations500ResponseBodyErrorsInner",
    "AtomicOperations503ResponseBody",
    "AtomicOperations503ResponseBodyErrorsInner",
    "AtomicOperationsRequest",
    "AtomicOperationsRequestAtomicOperationsInner",
    "AtomicOperationsRequestAtomicOperationsInnerOneOf",
    "AtomicOperationsRequestAtomicOperationsInnerOneOf1",
    "AtomicOperationsResponse",
    "AtomicOperationsResponseAtomicResultsInner",
    "AtomicOperationsResponseAtomicResultsInnerOneOf",
    "AtomicOperationsResponseAtomicResultsInnerOneOf1",
    "Audio",
    "AudioNormalizationData",
    "ChangeEventStreamsAttributes",
    "ChangeEventStreamsResourceObject",
    "ClientCertificatesAttributes",
    "ClientCertificatesCreateOperationPayload",
    "ClientCertificatesCreateOperationPayloadData",
    "ClientCertificatesCreateOperationPayloadDataRelationships",
    "ClientCertificatesCreateOperationPayloadDataRelationshipsClient",
    "ClientCertificatesCreateOperationPayloadDataRelationshipsClientData",
    "ClientCertificatesCreateSingleResourceDataDocument",
    "ClientCertificatesOwnersMultiRelationshipDataDocument",
    "ClientCertificatesRelationships",
    "ClientCertificatesResourceObject",
    "ClientCertificatesSingleResourceDataDocument",
    "ClientsAttributes",
    "ClientsCertificatesMultiRelationshipDataDocument",
    "ClientsCreateOperationPayload",
    "ClientsCreateOperationPayloadData",
    "ClientsCreateOperationPayloadDataAttributes",
    "ClientsCreateSingleResourceDataDocument",
    "ClientsMultiResourceDataDocument",
    "ClientsOwnersMultiRelationshipDataDocument",
    "ClientsRelationships",
    "ClientsResourceObject",
    "ClientsSingleResourceDataDocument",
    "ClientsUpdateOperationPayload",
    "ClientsUpdateOperationPayloadData",
    "ClientsUpdateOperationPayloadDataAttributes",
    "ClientsUpdateSingleResourceDataDocument",
    "CollaborationInviteRedemptionsAttributes",
    "CollaborationInviteRedemptionsCreateOperationPayload",
    "CollaborationInviteRedemptionsCreateOperationPayloadData",
    "CollaborationInviteRedemptionsCreateOperationPayloadDataRelationships",
    "CollaborationInviteRedemptionsCreateOperationPayloadDataRelationshipsInvite",
    "CollaborationInviteRedemptionsCreateOperationPayloadDataRelationshipsInviteData",
    "CollaborationInviteRedemptionsCreateSingleResourceDataDocument",
    "CollaborationInviteRedemptionsResourceObject",
    "CollaborationInvitesAttributes",
    "CollaborationInvitesCreateOperationPayload",
    "CollaborationInvitesCreateOperationPayloadData",
    "CollaborationInvitesCreateOperationPayloadDataRelationships",
    "CollaborationInvitesCreateOperationPayloadDataRelationshipsSubject",
    "CollaborationInvitesCreateOperationPayloadDataRelationshipsSubjectData",
    "CollaborationInvitesCreateSingleResourceDataDocument",
    "CollaborationInvitesMultiResourceDataDocument",
    "CollaborationInvitesOwnersMultiRelationshipDataDocument",
    "CollaborationInvitesRelationships",
    "CollaborationInvitesResourceObject",
    "CollaborationInvitesSingleResourceDataDocument",
    "CollaborationInvitesSubjectSingleRelationshipDataDocument",
    "CommentSummariesAttributes",
    "CommentSummariesMultiResourceDataDocument",
    "CommentSummariesRelationships",
    "CommentSummariesResourceObject",
    "CommentSummariesSubjectSingleRelationshipDataDocument",
    "CommentsAttributes",
    "CommentsAuthorSingleRelationshipDataDocument",
    "CommentsCommentSummarySingleRelationshipDataDocument",
    "CommentsCreateOperationPayload",
    "CommentsCreateOperationPayloadData",
    "CommentsCreateOperationPayloadDataAttributes",
    "CommentsCreateOperationPayloadDataRelationships",
    "CommentsCreateOperationPayloadDataRelationshipsSubject",
    "CommentsCreateOperationPayloadDataRelationshipsSubjectData",
    "CommentsCreateSingleResourceDataDocument",
    "CommentsMultiResourceDataDocument",
    "CommentsOwnersMultiRelationshipDataDocument",
    "CommentsReactionSummarySingleRelationshipDataDocument",
    "CommentsRelationships",
    "CommentsResourceObject",
    "CommentsRootSubjectSingleRelationshipDataDocument",
    "CommentsSingleResourceDataDocument",
    "CommentsSubjectSingleRelationshipDataDocument",
    "CommentsUpdateOperationPayload",
    "CommentsUpdateOperationPayloadData",
    "CommentsUpdateOperationPayloadDataAttributes",
    "ContentClaimsAttributes",
    "ContentClaimsClaimedResourceResourceIdentifier",
    "ContentClaimsClaimedResourceResourceIdentifierMeta",
    "ContentClaimsClaimedResourceSingleRelationshipDataDocument",
    "ContentClaimsClaimingArtistSingleRelationshipDataDocument",
    "ContentClaimsCreateOperationPayload",
    "ContentClaimsCreateOperationPayloadData",
    "ContentClaimsCreateOperationPayloadDataAttributes",
    "ContentClaimsCreateOperationPayloadDataRelationships",
    "ContentClaimsCreateOperationPayloadDataRelationshipsClaimedResource",
    "ContentClaimsCreateOperationPayloadDataRelationshipsClaimedResourceData",
    "ContentClaimsCreateOperationPayloadDataRelationshipsClaimingArtist",
    "ContentClaimsCreateOperationPayloadDataRelationshipsClaimingArtistData",
    "ContentClaimsCreateSingleResourceDataDocument",
    "ContentClaimsMultiResourceDataDocument",
    "ContentClaimsOwnersMultiRelationshipDataDocument",
    "ContentClaimsRelationships",
    "ContentClaimsResourceObject",
    "ContentClaimsSingleResourceDataDocument",
    "Copyright",
    "CreditsArtistSingleRelationshipDataDocument",
    "CreditsAttributes",
    "CreditsCategorySingleRelationshipDataDocument",
    "CreditsRelationships",
    "CreditsResourceObject",
    "CreditsSingleResourceDataDocument",
    "Default400ResponseBody",
    "Default404ResponseBody",
    "Default405ResponseBody",
    "Default406ResponseBody",
    "Default415ResponseBody",
    "Default429ResponseBody",
    "Default500ResponseBody",
    "Default503ResponseBody",
    "DownloadLink",
    "DownloadLinkMeta",
    "DownloadsAttributes",
    "DownloadsMultiResourceDataDocument",
    "DownloadsOwnersMultiRelationshipDataDocument",
    "DownloadsRelationships",
    "DownloadsResourceObject",
    "DownloadsSingleResourceDataDocument",
    "DrmData",
    "DspSharingLinksAttributes",
    "DspSharingLinksMultiResourceDataDocument",
    "DspSharingLinksRelationships",
    "DspSharingLinksResourceObject",
    "DspSharingLinksSubjectResourceIdentifier",
    "DspSharingLinksSubjectResourceIdentifierMeta",
    "DspSharingLinksSubjectSingleRelationshipDataDocument",
    "DynamicModulesAttributes",
    "DynamicModulesItemsMultiRelationshipDataDocument",
    "DynamicModulesItemsResourceIdentifier",
    "DynamicModulesItemsResourceIdentifierMeta",
    "DynamicModulesMultiResourceDataDocument",
    "DynamicModulesRelationships",
    "DynamicModulesResourceObject",
    "DynamicModulesSeedItemResourceIdentifier",
    "DynamicModulesSeedItemResourceIdentifierMeta",
    "DynamicModulesSeedItemSingleRelationshipDataDocument",
    "DynamicModulesSingleResourceDataDocument",
    "DynamicPagesAttributes",
    "DynamicPagesModulesMultiRelationshipDataDocument",
    "DynamicPagesMultiResourceDataDocument",
    "DynamicPagesRelationships",
    "DynamicPagesResourceObject",
    "DynamicPagesSubjectResourceIdentifier",
    "DynamicPagesSubjectResourceIdentifierMeta",
    "DynamicPagesSubjectSingleRelationshipDataDocument",
    "EffectiveRole",
    "ErrorObject",
    "ErrorObjectSource",
    "ErrorsDocument",
    "ExternalLink",
    "ExternalLinkMeta",
    "ExternalLinkPayload",
    "FileStatus",
    "FileUploadLink",
    "FileUploadLinkMeta",
    "FolderItemsAttributes",
    "FolderItemsBreadcrumbMultiRelationshipDataDocument",
    "FolderItemsCreateOperationPayload",
    "FolderItemsCreateOperationPayloadData",
    "FolderItemsCreateOperationPayloadDataRelationships",
    "FolderItemsCreateOperationPayloadDataRelationshipsParent",
    "FolderItemsCreateOperationPayloadDataRelationshipsParentData",
    "FolderItemsCreateOperationPayloadDataRelationshipsSubject",
    "FolderItemsCreateOperationPayloadDataRelationshipsSubjectData",
    "FolderItemsCreateResource400ResponseBody",
    "FolderItemsCreateResource400ResponseBodyErrorsInner",
    "FolderItemsCreateSingleResourceDataDocument",
    "FolderItemsMultiResourceDataDocument",
    "FolderItemsOwnersMultiRelationshipDataDocument",
    "FolderItemsParentRelationshipUpdateOperationPayload",
    "FolderItemsParentRelationshipUpdateOperationPayloadData",
    "FolderItemsParentSingleRelationshipDataDocument",
    "FolderItemsParentUpdateResourceIdentifier",
    "FolderItemsParentUpdateSingleDataRelationship400ResponseBody",
    "FolderItemsParentUpdateSingleRelationshipDataDocument",
    "FolderItemsRelationships",
    "FolderItemsResourceObject",
    "FolderItemsSharingSummarySingleRelationshipDataDocument",
    "FolderItemsSingleResourceDataDocument",
    "FolderItemsSubjectResourceIdentifier",
    "FolderItemsSubjectResourceIdentifierMeta",
    "FolderItemsSubjectSingleRelationshipDataDocument",
    "FoldersAttributes",
    "FoldersChildrenMultiRelationshipDataDocument",
    "FoldersCreateOperationPayload",
    "FoldersCreateOperationPayloadData",
    "FoldersCreateOperationPayloadDataAttributes",
    "FoldersCreateOperationPayloadDataRelationships",
    "FoldersCreateOperationPayloadDataRelationshipsParent",
    "FoldersCreateSingleResourceDataDocument",
    "FoldersDeleteResource400ResponseBody",
    "FoldersDeleteResource400ResponseBodyErrorsInner",
    "FoldersMultiResourceDataDocument",
    "FoldersOwnersMultiRelationshipDataDocument",
    "FoldersParentIdentifier",
    "FoldersParentSingleRelationshipDataDocument",
    "FoldersPreviewMultiRelationshipDataDocument",
    "FoldersRelationships",
    "FoldersResourceObject",
    "FoldersSharesMultiRelationshipDataDocument",
    "FoldersSingleResourceDataDocument",
    "FoldersUpdateOperationPayload",
    "FoldersUpdateOperationPayloadData",
    "FoldersUpdateOperationPayloadDataAttributes",
    "FoldersUpdateResource400ResponseBody",
    "FoldersUpdateSingleResourceDataDocument",
    "GenresAttributes",
    "GenresMultiResourceDataDocument",
    "GenresResourceObject",
    "GenresSingleResourceDataDocument",
    "GroupsAttributes",
    "GroupsMultiResourceDataDocument",
    "GroupsResourceObject",
    "GroupsSingleResourceDataDocument",
    "Idempotency409ResponseBody",
    "Idempotency409ResponseBodyErrorsInner",
    "Idempotency422ResponseBody",
    "IncludedInner",
    "InstallationsAttributes",
    "InstallationsCreateOperationPayload",
    "InstallationsCreateOperationPayloadData",
    "InstallationsCreateOperationPayloadDataAttributes",
    "InstallationsCreateSingleResourceDataDocument",
    "InstallationsMultiResourceDataDocument",
    "InstallationsOfflineInventoryItemIdentifier",
    "InstallationsOfflineInventoryMultiRelationshipDataDocument",
    "InstallationsOfflineInventoryRelationshipAddOperationPayload",
    "InstallationsOfflineInventoryRelationshipRemoveOperationPayload",
    "InstallationsOfflineInventoryResourceIdentifier",
    "InstallationsOfflineInventoryResourceIdentifierMeta",
    "InstallationsOwnersMultiRelationshipDataDocument",
    "InstallationsRelationships",
    "InstallationsResourceObject",
    "InstallationsSingleResourceDataDocument",
    "Item",
    "ItemArtwork",
    "ItemVariation",
    "LegacyBarcodeId",
    "LegacySource",
    "LinkObject",
    "Links",
    "LinksMeta",
    "LyricsAttributes",
    "LyricsCreateOperationPayload",
    "LyricsCreateOperationPayloadData",
    "LyricsCreateOperationPayloadDataAttributes",
    "LyricsCreateOperationPayloadDataRelationships",
    "LyricsCreateOperationPayloadDataRelationshipsTrack",
    "LyricsCreateOperationPayloadDataRelationshipsTrackData",
    "LyricsCreateOperationPayloadMeta",
    "LyricsCreateSingleResourceDataDocument",
    "LyricsOwnersMultiRelationshipDataDocument",
    "LyricsProvider",
    "LyricsRelationships",
    "LyricsResourceObject",
    "LyricsSingleResourceDataDocument",
    "LyricsTrackResourceIdentifier",
    "LyricsTrackResourceIdentifierMeta",
    "LyricsTrackSingleRelationshipDataDocument",
    "LyricsUpdateOperationPayload",
    "LyricsUpdateOperationPayloadData",
    "LyricsUpdateOperationPayloadDataAttributes",
    "ManualArtistClaimsAttributes",
    "ManualArtistClaimsCreateOperationPayload",
    "ManualArtistClaimsCreateOperationPayloadData",
    "ManualArtistClaimsCreateOperationPayloadDataAttributes",
    "ManualArtistClaimsCreateSingleResourceDataDocument",
    "ManualArtistClaimsExternalLink",
    "ManualArtistClaimsResourceObject",
    "MissingTermsMeta",
    "MutationResponseDocument",
    "OfflineTasksAttributes",
    "OfflineTasksCollectionResourceIdentifier",
    "OfflineTasksCollectionResourceIdentifierMeta",
    "OfflineTasksCollectionSingleRelationshipDataDocument",
    "OfflineTasksItemResourceIdentifier",
    "OfflineTasksItemResourceIdentifierMeta",
    "OfflineTasksItemSingleRelationshipDataDocument",
    "OfflineTasksMultiResourceDataDocument",
    "OfflineTasksOwnersMultiRelationshipDataDocument",
    "OfflineTasksRelationships",
    "OfflineTasksResourceObject",
    "OfflineTasksSingleResourceDataDocument",
    "OfflineTasksUpdateOperationPayload",
    "OfflineTasksUpdateOperationPayloadData",
    "OfflineTasksUpdateOperationPayloadDataAttributes",
    "PlayQueuesAttributes",
    "PlayQueuesChangeEventStreamSingleRelationshipDataDocument",
    "PlayQueuesCreateOperationPayload",
    "PlayQueuesCreateOperationPayloadData",
    "PlayQueuesCreateSingleResourceDataDocument",
    "PlayQueuesCreateSingleResourceDataDocumentMeta",
    "PlayQueuesCurrentRelationshipUpdateOperationPayload",
    "PlayQueuesCurrentRelationshipUpdateOperationPayloadData",
    "PlayQueuesCurrentRelationshipUpdateOperationPayloadDataMeta",
    "PlayQueuesCurrentResourceIdentifier",
    "PlayQueuesCurrentResourceIdentifierMeta",
    "PlayQueuesCurrentSingleRelationshipDataDocument",
    "PlayQueuesCurrentUpdateResourceIdentifier",
    "PlayQueuesCurrentUpdateResourceIdentifierMeta",
    "PlayQueuesCurrentUpdateSingleRelationshipDataDocument",
    "PlayQueuesCurrentUpdateSingleRelationshipDataDocumentMeta",
    "PlayQueuesFutureAddMultiRelationshipDataDocument",
    "PlayQueuesFutureAddMultiRelationshipDataDocumentMeta",
    "PlayQueuesFutureAddResourceIdentifier",
    "PlayQueuesFutureMultiRelationshipDataDocument",
    "PlayQueuesFutureRelationshipAddOperationPayload",
    "PlayQueuesFutureRelationshipAddOperationPayloadData",
    "PlayQueuesFutureRelationshipAddOperationPayloadMeta",
    "PlayQueuesFutureRelationshipRemoveOperationPayload",
    "PlayQueuesFutureRelationshipRemoveOperationPayloadData",
    "PlayQueuesFutureRelationshipRemoveOperationPayloadDataMeta",
    "PlayQueuesFutureRelationshipSource",
    "PlayQueuesFutureRelationshipUpdateOperationPayload",
    "PlayQueuesFutureRelationshipUpdateOperationPayloadData",
    "PlayQueuesFutureRelationshipUpdateOperationPayloadDataMeta",
    "PlayQueuesFutureRelationshipUpdateOperationPayloadMeta",
    "PlayQueuesFutureResourceIdentifier",
    "PlayQueuesFutureResourceIdentifierMeta",
    "PlayQueuesFutureUpdateMultiRelationshipDataDocument",
    "PlayQueuesFutureUpdateMultiRelationshipDataDocumentMeta",
    "PlayQueuesFutureUpdateResourceIdentifier",
    "PlayQueuesMultiResourceDataDocument",
    "PlayQueuesOwnersMultiRelationshipDataDocument",
    "PlayQueuesPastMultiRelationshipDataDocument",
    "PlayQueuesPastResourceIdentifier",
    "PlayQueuesPastResourceIdentifierMeta",
    "PlayQueuesRelationships",
    "PlayQueuesResourceObject",
    "PlayQueuesSingleResourceDataDocument",
    "PlayQueuesUpdateOperationCurrent",
    "PlayQueuesUpdateOperationCurrentMeta",
    "PlayQueuesUpdateOperationFuture",
    "PlayQueuesUpdateOperationFutureData",
    "PlayQueuesUpdateOperationFutureMeta",
    "PlayQueuesUpdateOperationPayload",
    "PlayQueuesUpdateOperationPayloadData",
    "PlayQueuesUpdateOperationPayloadDataAttributes",
    "PlayQueuesUpdateOperationPayloadDataRelationships",
    "PlayQueuesUpdateSingleResourceDataDocument",
    "PlayQueuesUpdateSingleResourceDataDocumentMeta",
    "PlaylistGenerationProgress",
    "PlaylistGenerationSchedulesAttributes",
    "PlaylistGenerationSchedulesCreateOperationPayload",
    "PlaylistGenerationSchedulesCreateOperationPayloadData",
    "PlaylistGenerationSchedulesCreateOperationPayloadDataAttributes",
    "PlaylistGenerationSchedulesCreateOperationPayloadDataRelationships",
    "PlaylistGenerationSchedulesCreateOperationPayloadDataRelationshipsPlaylist",
    "PlaylistGenerationSchedulesCreateOperationPayloadDataRelationshipsPlaylistData",
    "PlaylistGenerationSchedulesCreateResource403ResponseBody",
    "PlaylistGenerationSchedulesCreateResource403ResponseBodyErrorsInner",
    "PlaylistGenerationSchedulesCreateSingleResourceDataDocument",
    "PlaylistGenerationSchedulesMultiResourceDataDocument",
    "PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument",
    "PlaylistGenerationSchedulesRelationships",
    "PlaylistGenerationSchedulesResourceObject",
    "PlaylistGenerationSchedulesSingleResourceDataDocument",
    "PlaylistGenerationSchedulesUpdateOperationPayload",
    "PlaylistGenerationSchedulesUpdateOperationPayloadData",
    "PlaylistGenerationSchedulesUpdateOperationPayloadDataAttributes",
    "PlaylistGenerationSchedulesUpdateSingleResourceDataDocument",
    "PlaylistGenerationsAttributes",
    "PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument",
    "PlaylistGenerationsCreateOperationPayload",
    "PlaylistGenerationsCreateOperationPayloadData",
    "PlaylistGenerationsCreateOperationPayloadDataAttributes",
    "PlaylistGenerationsCreateOperationPayloadDataRelationships",
    "PlaylistGenerationsCreateOperationPayloadDataRelationshipsBaseGeneration",
    "PlaylistGenerationsCreateOperationPayloadDataRelationshipsBaseGenerationData",
    "PlaylistGenerationsCreateOperationPayloadDataRelationshipsPlaylist",
    "PlaylistGenerationsCreateOperationPayloadDataRelationshipsPlaylistData",
    "PlaylistGenerationsCreateResource409ResponseBody",
    "PlaylistGenerationsCreateResource409ResponseBodyErrorsInner",
    "PlaylistGenerationsCreateSingleResourceDataDocument",
    "PlaylistGenerationsMultiResourceDataDocument",
    "PlaylistGenerationsPlaylistSingleRelationshipDataDocument",
    "PlaylistGenerationsRelationships",
    "PlaylistGenerationsResourceObject",
    "PlaylistGenerationsSingleResourceDataDocument",
    "PlaylistGenerationsTrackPreferencesAddMultiDataRelationshipWithResponse409ResponseBody",
    "PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocument",
    "PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocumentMeta",
    "PlaylistGenerationsTrackPreferencesAddResourceIdentifier",
    "PlaylistGenerationsTrackPreferencesAddResourceIdentifierMeta",
    "PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument",
    "PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocumentMeta",
    "PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload",
    "PlaylistGenerationsTrackPreferencesRelationshipPayloadData",
    "PlaylistGenerationsTrackPreferencesRelationshipPayloadDataMeta",
    "PlaylistGenerationsTrackPreferencesRelationshipPayloadMeta",
    "PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload",
    "PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayloadData",
    "PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload",
    "PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayloadMeta",
    "PlaylistGenerationsTrackPreferencesRemoveMultiDataRelationship409ResponseBody",
    "PlaylistGenerationsTrackPreferencesResourceIdentifier",
    "PlaylistGenerationsTrackPreferencesResourceIdentifierMeta",
    "PlaylistGenerationsTrackPreferencesUpdateMultiDataRelationship409ResponseBody",
    "PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocument",
    "PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocumentMeta",
    "PlaylistGenerationsTrackPreferencesUpdateResourceIdentifier",
    "PlaylistGenerationsTrackPreferencesUpdateResourceIdentifierMeta",
    "PlaylistsAttributes",
    "PlaylistsCollaboratorProfilesMultiRelationshipDataDocument",
    "PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload",
    "PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayloadData",
    "PlaylistsCollaboratorsMultiRelationshipDataDocument",
    "PlaylistsCoverArtMultiRelationshipDataDocument",
    "PlaylistsCoverArtRelationshipUpdateOperationPayload",
    "PlaylistsCoverArtRelationshipUpdateOperationPayloadData",
    "PlaylistsCreateOperationPayload",
    "PlaylistsCreateOperationPayloadData",
    "PlaylistsCreateOperationPayloadDataAttributes",
    "PlaylistsCreateSingleResourceDataDocument",
    "PlaylistsCuratorsMultiRelationshipDataDocument",
    "PlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBody",
    "PlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner",
    "PlaylistsItemsAddMultiRelationshipDataDocument",
    "PlaylistsItemsAddMultiRelationshipDataDocumentMeta",
    "PlaylistsItemsAddResourceIdentifier",
    "PlaylistsItemsAddResourceIdentifierMeta",
    "PlaylistsItemsMultiRelationshipDataDocument",
    "PlaylistsItemsRelationshipAddOperationPayload",
    "PlaylistsItemsRelationshipAddOperationPayloadData",
    "PlaylistsItemsRelationshipAddOperationPayloadDataMeta",
    "PlaylistsItemsRelationshipAddOperationPayloadMeta",
    "PlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem",
    "PlaylistsItemsRelationshipRemoveOperationPayload",
    "PlaylistsItemsRelationshipRemoveOperationPayloadData",
    "PlaylistsItemsRelationshipRemoveOperationPayloadDataMeta",
    "PlaylistsItemsRelationshipUpdateOperationPayload",
    "PlaylistsItemsRelationshipUpdateOperationPayloadData",
    "PlaylistsItemsRelationshipUpdateOperationPayloadDataMeta",
    "PlaylistsItemsRelationshipUpdateOperationPayloadMeta",
    "PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf",
    "PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf1",
    "PlaylistsItemsResourceIdentifier",
    "PlaylistsItemsResourceIdentifierMeta",
    "PlaylistsMultiResourceDataDocument",
    "PlaylistsOwnerProfilesMultiRelationshipDataDocument",
    "PlaylistsOwnersMultiRelationshipDataDocument",
    "PlaylistsRelationships",
    "PlaylistsResourceObject",
    "PlaylistsSingleResourceDataDocument",
    "PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument",
    "PlaylistsSuggestedCoverArtsResourceIdentifier",
    "PlaylistsSuggestedCoverArtsResourceIdentifierMeta",
    "PlaylistsUpdateOperationPayload",
    "PlaylistsUpdateOperationPayloadData",
    "PlaylistsUpdateOperationPayloadDataAttributes",
    "PlaylistsUpdateSingleResourceDataDocument",
    "PriceConfigurationsAttributes",
    "PriceConfigurationsCreateOperationPayload",
    "PriceConfigurationsCreateOperationPayloadData",
    "PriceConfigurationsCreateOperationPayloadDataAttributes",
    "PriceConfigurationsCreateOperationPayloadDataRelationships",
    "PriceConfigurationsCreateOperationPayloadDataRelationshipsSubjects",
    "PriceConfigurationsCreateOperationPayloadSubjects",
    "PriceConfigurationsCreateSingleResourceDataDocument",
    "PriceConfigurationsMultiResourceDataDocument",
    "PriceConfigurationsResourceObject",
    "PriceConfigurationsSingleResourceDataDocument",
    "ProviderOwnersAttributes",
    "ProviderOwnersMultiResourceDataDocument",
    "ProviderOwnersOwnersMultiRelationshipDataDocument",
    "ProviderOwnersProviderSingleRelationshipDataDocument",
    "ProviderOwnersRelationships",
    "ProviderOwnersResourceObject",
    "ProviderProductInfosAttributes",
    "ProviderProductInfosMultiResourceDataDocument",
    "ProviderProductInfosProviderSingleRelationshipDataDocument",
    "ProviderProductInfosRelationships",
    "ProviderProductInfosResourceObject",
    "ProviderProductInfosSubjectResourceIdentifier",
    "ProviderProductInfosSubjectResourceIdentifierMeta",
    "ProviderProductInfosSubjectSingleRelationshipDataDocument",
    "ProvidersAttributes",
    "ProvidersResourceObject",
    "ProvidersSingleResourceDataDocument",
    "PurchasesAttributes",
    "PurchasesMultiResourceDataDocument",
    "PurchasesOwnersMultiRelationshipDataDocument",
    "PurchasesRelationships",
    "PurchasesResourceObject",
    "PurchasesSubjectResourceIdentifier",
    "PurchasesSubjectResourceIdentifierMeta",
    "PurchasesSubjectSingleRelationshipDataDocument",
    "ReactionSummariesAttributes",
    "ReactionSummariesMultiResourceDataDocument",
    "ReactionSummariesRelationships",
    "ReactionSummariesResourceObject",
    "ReactionSummariesSubjectSingleRelationshipDataDocument",
    "ReactionsAttributes",
    "ReactionsAuthorSingleRelationshipDataDocument",
    "ReactionsCreateOperationPayload",
    "ReactionsCreateOperationPayloadData",
    "ReactionsCreateOperationPayloadDataAttributes",
    "ReactionsCreateOperationPayloadDataRelationships",
    "ReactionsCreateOperationPayloadDataRelationshipsSubject",
    "ReactionsCreateOperationPayloadDataRelationshipsSubjectData",
    "ReactionsCreateSingleResourceDataDocument",
    "ReactionsMultiResourceDataDocument",
    "ReactionsOwnersMultiRelationshipDataDocument",
    "ReactionsRelationships",
    "ReactionsResourceObject",
    "ReactionsSubjectSingleRelationshipDataDocument",
    "ReplacementOriginalIdentifier",
    "ReplacementProvenance",
    "ResourceGrantInvitationsAttributes",
    "ResourceGrantInvitationsCreateOperationPayload",
    "ResourceGrantInvitationsCreateOperationPayloadData",
    "ResourceGrantInvitationsCreateOperationPayloadDataAttributes",
    "ResourceGrantInvitationsCreateOperationPayloadDataRelationships",
    "ResourceGrantInvitationsCreateOperationPayloadDataRelationshipsSubject",
    "ResourceGrantInvitationsCreateOperationPayloadDataRelationshipsSubjectData",
    "ResourceGrantInvitationsCreateSingleResourceDataDocument",
    "ResourceGrantInvitationsMultiResourceDataDocument",
    "ResourceGrantInvitationsOwnersMultiRelationshipDataDocument",
    "ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument",
    "ResourceGrantInvitationsRelationships",
    "ResourceGrantInvitationsResourceObject",
    "ResourceGrantInvitationsSingleResourceDataDocument",
    "ResourceGrantInvitationsSubjectResourceIdentifier",
    "ResourceGrantInvitationsSubjectResourceIdentifierMeta",
    "ResourceGrantInvitationsSubjectSingleRelationshipDataDocument",
    "ResourceGrantInvitationsUpdateOperationPayload",
    "ResourceGrantInvitationsUpdateOperationPayloadData",
    "ResourceGrantInvitationsUpdateOperationPayloadDataAttributes",
    "ResourceGrantInvitationsUpdateSingleResourceDataDocument",
    "ResourceGrantsAttributes",
    "ResourceGrantsCreateOperationPayload",
    "ResourceGrantsCreateOperationPayloadData",
    "ResourceGrantsCreateOperationPayloadDataAttributes",
    "ResourceGrantsCreateOperationPayloadDataRelationships",
    "ResourceGrantsCreateOperationPayloadMeta",
    "ResourceGrantsCreateResource403ResponseBody",
    "ResourceGrantsCreateResource403ResponseBodyErrorsInner",
    "ResourceGrantsCreateResource429ResponseBody",
    "ResourceGrantsCreateResource429ResponseBodyErrorsInner",
    "ResourceGrantsCreateSingleResourceDataDocument",
    "ResourceGrantsGrantee",
    "ResourceGrantsGranteeLinkage",
    "ResourceGrantsGranteeSingleRelationshipDataDocument",
    "ResourceGrantsInvitation",
    "ResourceGrantsInvitationLinkage",
    "ResourceGrantsInvitationSingleRelationshipDataDocument",
    "ResourceGrantsMultiResourceDataDocument",
    "ResourceGrantsRelationships",
    "ResourceGrantsResourceObject",
    "ResourceGrantsSingleResourceDataDocument",
    "ResourceGrantsSubject",
    "ResourceGrantsSubjectLinkage",
    "ResourceGrantsSubjectResourceIdentifier",
    "ResourceGrantsSubjectResourceIdentifierMeta",
    "ResourceGrantsSubjectSingleRelationshipDataDocument",
    "ResourceGrantsUpdateOperationPayload",
    "ResourceGrantsUpdateOperationPayloadData",
    "ResourceGrantsUpdateOperationPayloadDataAttributes",
    "ResourceGrantsUpdateSingleResourceDataDocument",
    "ResourceIdentifier",
    "ResourceObjectObjectObject",
    "SavedSharesAttributes",
    "SavedSharesCreateOperationPayload",
    "SavedSharesCreateOperationPayloadData",
    "SavedSharesCreateOperationPayloadDataRelationships",
    "SavedSharesCreateOperationPayloadDataRelationshipsShare",
    "SavedSharesCreateOperationPayloadDataRelationshipsShareData",
    "SavedSharesCreateOperationPayloadMeta",
    "SavedSharesCreateResource403ResponseBody",
    "SavedSharesCreateResource403ResponseBodyErrorsInner",
    "SavedSharesCreateResource429ResponseBody",
    "SavedSharesCreateResource429ResponseBodyErrorsInner",
    "SavedSharesCreateSingleResourceDataDocument",
    "SavedSharesResourceObject",
    "ScopesAttributes",
    "ScopesMultiResourceDataDocument",
    "ScopesResourceObject",
    "SearchHistoryEntriesAttributes",
    "SearchHistoryEntriesResourceObject",
    "SearchResultsAlbumsMultiRelationshipDataDocument",
    "SearchResultsAlbumsResourceIdentifier",
    "SearchResultsAlbumsResourceIdentifierMeta",
    "SearchResultsArtistsMultiRelationshipDataDocument",
    "SearchResultsAttributes",
    "SearchResultsMultiResourceDataDocument",
    "SearchResultsPlaylistsMultiRelationshipDataDocument",
    "SearchResultsRelationships",
    "SearchResultsResourceObject",
    "SearchResultsTopHitsMultiRelationshipDataDocument",
    "SearchResultsTopHitsResourceIdentifier",
    "SearchResultsTopHitsResourceIdentifierMeta",
    "SearchResultsTracksMultiRelationshipDataDocument",
    "SearchResultsTracksResourceIdentifier",
    "SearchResultsTracksResourceIdentifierMeta",
    "SearchResultsVideosMultiRelationshipDataDocument",
    "SearchResultsVideosResourceIdentifier",
    "SearchResultsVideosResourceIdentifierMeta",
    "SearchSuggestionsAttributes",
    "SearchSuggestionsDirectHitsMultiRelationshipDataDocument",
    "SearchSuggestionsDirectHitsResourceIdentifier",
    "SearchSuggestionsDirectHitsResourceIdentifierMeta",
    "SearchSuggestionsHighlights",
    "SearchSuggestionsHistoryMultiRelationshipDataDocument",
    "SearchSuggestionsMultiResourceDataDocument",
    "SearchSuggestionsRelationships",
    "SearchSuggestionsResourceObject",
    "SearchSuggestionsSuggestions",
    "SharesAttributes",
    "SharesCreateOperationPayload",
    "SharesCreateOperationPayloadData",
    "SharesCreateOperationPayloadDataAttributes",
    "SharesCreateOperationPayloadDataRelationships",
    "SharesCreateOperationPayloadDataRelationshipsSharedResources",
    "SharesCreateOperationPayloadDataRelationshipsSharedResourcesData",
    "SharesCreateSingleResourceDataDocument",
    "SharesMultiResourceDataDocument",
    "SharesOwnersMultiRelationshipDataDocument",
    "SharesRelationships",
    "SharesResourceObject",
    "SharesSharedResourcesMultiRelationshipDataDocument",
    "SharesSharedResourcesResourceIdentifier",
    "SharesSharedResourcesResourceIdentifierMeta",
    "SharesSingleResourceDataDocument",
    "SharesUpdateOperationPayload",
    "SharesUpdateOperationPayloadData",
    "SharesUpdateOperationPayloadDataAttributes",
    "SharesUpdateSingleResourceDataDocument",
    "SharingSummariesAttributes",
    "SharingSummariesMultiResourceDataDocument",
    "SharingSummariesRelationships",
    "SharingSummariesResourceObject",
    "SharingSummariesSubjectResourceIdentifier",
    "SharingSummariesSubjectResourceIdentifierMeta",
    "SharingSummariesSubjectSingleRelationshipDataDocument",
    "Site",
    "SourceProcessing",
    "SquareConnectionsAttributes",
    "SquareConnectionsCapability",
    "SquareConnectionsCreateOperationPayload",
    "SquareConnectionsCreateOperationPayloadData",
    "SquareConnectionsCreateOperationPayloadMeta",
    "SquareConnectionsCreateSingleResourceDataDocument",
    "SquareConnectionsReadById403ResponseBody",
    "SquareConnectionsRelationships",
    "SquareConnectionsResourceObject",
    "SquareConnectionsSelectedSiteReadSingleDataRelationship403ResponseBody",
    "SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload",
    "SquareConnectionsSelectedSiteRelationshipUpdateOperationPayloadData",
    "SquareConnectionsSelectedSiteSingleRelationshipDataDocument",
    "SquareConnectionsSelectedSiteUpdateResourceIdentifier",
    "SquareConnectionsSelectedSiteUpdateSingleDataRelationship403ResponseBody",
    "SquareConnectionsSelectedSiteUpdateSingleDataRelationship409ResponseBody",
    "SquareConnectionsSelectedSiteUpdateSingleDataRelationship409ResponseBodyErrorsInner",
    "SquareConnectionsSelectedSiteUpdateSingleRelationshipDataDocument",
    "SquareConnectionsSingleResourceDataDocument",
    "SquareConnectionsSitesMultiRelationshipDataDocument",
    "SquareConnectionsSitesReadMultiDataRelationship403ResponseBody",
    "SquareItemVariationPhysicalCountsAttributes",
    "SquareItemVariationPhysicalCountsCreateOperationPayload",
    "SquareItemVariationPhysicalCountsCreateOperationPayloadData",
    "SquareItemVariationPhysicalCountsCreateOperationPayloadDataAttributes",
    "SquareItemVariationPhysicalCountsCreateOperationPayloadDataRelationships",
    "SquareItemVariationPhysicalCountsCreateOperationPayloadDataRelationshipsVariations",
    "SquareItemVariationPhysicalCountsCreateResource403ResponseBody",
    "SquareItemVariationPhysicalCountsCreateResource409ResponseBody",
    "SquareItemVariationPhysicalCountsCreateResource409ResponseBodyErrorsInner",
    "SquareItemVariationPhysicalCountsCreateSingleResourceDataDocument",
    "SquareItemVariationPhysicalCountsResourceObject",
    "SquareItemVariationsArtworksMultiRelationshipDataDocument",
    "SquareItemVariationsArtworksMultiRelationshipDataDocumentMeta",
    "SquareItemVariationsArtworksReadMultiDataRelationship403ResponseBody",
    "SquareItemVariationsArtworksReadMultiDataRelationship409ResponseBody",
    "SquareItemVariationsArtworksReadMultiDataRelationship409ResponseBodyErrorsInner",
    "SquareItemVariationsArtworksRelationshipUpdateOperationPayload",
    "SquareItemVariationsArtworksRelationshipUpdateOperationPayloadMeta",
    "SquareItemVariationsArtworksUpdateMultiDataRelationship403ResponseBody",
    "SquareItemVariationsArtworksUpdateMultiDataRelationship409ResponseBody",
    "SquareItemVariationsArtworksUpdateMultiDataRelationship409ResponseBodyErrorsInner",
    "SquareItemVariationsArtworksUpdateMultiDataRelationship413ResponseBody",
    "SquareItemVariationsArtworksUpdateMultiDataRelationship413ResponseBodyErrorsInner",
    "SquareItemVariationsArtworksUpdateMultiRelationshipDataDocument",
    "SquareItemVariationsArtworksUpdateMultiRelationshipDataDocumentMeta",
    "SquareItemVariationsArtworksUpdateResourceIdentifier",
    "SquareItemVariationsAttributes",
    "SquareItemVariationsCreateOperationPayload",
    "SquareItemVariationsCreateOperationPayloadData",
    "SquareItemVariationsCreateOperationPayloadDataAttributes",
    "SquareItemVariationsCreateOperationPayloadDataRelationships",
    "SquareItemVariationsCreateOperationPayloadDataRelationshipsItems",
    "SquareItemVariationsCreateOperationPayloadLocal",
    "SquareItemVariationsCreateOperationPayloadLocalData",
    "SquareItemVariationsCreateOperationPayloadLocalDataRelationships",
    "SquareItemVariationsCreateOperationPayloadLocalDataRelationshipsItems",
    "SquareItemVariationsCreateOperationPayloadLocalItem",
    "SquareItemVariationsCreateResource403ResponseBody",
    "SquareItemVariationsCreateResource409ResponseBody",
    "SquareItemVariationsCreateResource409ResponseBodyErrorsInner",
    "SquareItemVariationsCreateSingleResourceDataDocument",
    "SquareItemVariationsCreateSingleResourceDataDocumentMeta",
    "SquareItemVariationsDeleteResource403ResponseBody",
    "SquareItemVariationsDeleteResource409ResponseBody",
    "SquareItemVariationsDeleteResource409ResponseBodyErrorsInner",
    "SquareItemVariationsExpectedItemRevision",
    "SquareItemVariationsOwnersMultiRelationshipDataDocument",
    "SquareItemVariationsReadById403ResponseBody",
    "SquareItemVariationsReadById409ResponseBody",
    "SquareItemVariationsReadById409ResponseBodyErrorsInner",
    "SquareItemVariationsRelationships",
    "SquareItemVariationsResourceObject",
    "SquareItemVariationsSingleResourceDataDocument",
    "SquareItemVariationsUpdateOperationPayload",
    "SquareItemVariationsUpdateOperationPayloadData",
    "SquareItemVariationsUpdateOperationPayloadDataAttributes",
    "SquareItemVariationsUpdateOperationPayloadMeta",
    "SquareItemVariationsUpdateResource403ResponseBody",
    "SquareItemVariationsUpdateResource409ResponseBody",
    "SquareItemVariationsUpdateResource409ResponseBodyErrorsInner",
    "SquareItemVariationsUpdateSingleResourceDataDocument",
    "SquareItemsArtworksMultiRelationshipDataDocument",
    "SquareItemsArtworksReadMultiDataRelationship409ResponseBody",
    "SquareItemsArtworksRelationshipUpdateOperationPayload",
    "SquareItemsArtworksRelationshipUpdateOperationPayloadMeta",
    "SquareItemsArtworksUpdateMultiDataRelationship403ResponseBody",
    "SquareItemsArtworksUpdateMultiDataRelationship409ResponseBody",
    "SquareItemsArtworksUpdateMultiDataRelationship409ResponseBodyErrorsInner",
    "SquareItemsArtworksUpdateMultiDataRelationship413ResponseBody",
    "SquareItemsArtworksUpdateMultiRelationshipDataDocument",
    "SquareItemsArtworksUpdateMultiRelationshipDataDocumentMeta",
    "SquareItemsArtworksUpdateResourceIdentifier",
    "SquareItemsAttributes",
    "SquareItemsCreateOperationPayload",
    "SquareItemsCreateOperationPayloadData",
    "SquareItemsCreateOperationPayloadDataAttributes",
    "SquareItemsCreateOperationPayloadDataRelationships",
    "SquareItemsCreateOperationPayloadDataRelationshipsSites",
    "SquareItemsDeleteResource403ResponseBody",
    "SquareItemsDeleteResource409ResponseBody",
    "SquareItemsDeleteResource409ResponseBodyErrorsInner",
    "SquareItemsMultiResourceDataDocument",
    "SquareItemsOwnersMultiRelationshipDataDocument",
    "SquareItemsReadByFilter403ResponseBody",
    "SquareItemsReadByFilter409ResponseBody",
    "SquareItemsReadById403ResponseBody",
    "SquareItemsReadById409ResponseBody",
    "SquareItemsRelationships",
    "SquareItemsResourceObject",
    "SquareItemsSingleResourceDataDocument",
    "SquareItemsUpdateOperationPayload",
    "SquareItemsUpdateOperationPayloadData",
    "SquareItemsUpdateOperationPayloadDataAttributes",
    "SquareItemsUpdateOperationPayloadMeta",
    "SquareItemsUpdateResource403ResponseBody",
    "SquareItemsUpdateResource409ResponseBody",
    "SquareItemsUpdateSingleResourceDataDocument",
    "SquareItemsVariationsMultiRelationshipDataDocument",
    "SquareItemsVariationsReadMultiDataRelationship403ResponseBody",
    "SquareItemsVariationsReadMultiDataRelationship409ResponseBody",
    "SquareItemsVariationsRelationshipUpdateOperationPayload",
    "SquareItemsVariationsRelationshipUpdateOperationPayloadMeta",
    "SquareItemsVariationsUpdateMultiDataRelationship403ResponseBody",
    "SquareItemsVariationsUpdateMultiDataRelationship409ResponseBody",
    "SquareItemsVariationsUpdateMultiRelationshipDataDocument",
    "SquareItemsVariationsUpdateMultiRelationshipDataDocumentMeta",
    "SquareItemsVariationsUpdateResourceIdentifier",
    "SquareSitesAttributes",
    "SquareSitesItemsAddMultiDataRelationship403ResponseBody",
    "SquareSitesItemsAddMultiDataRelationship409ResponseBody",
    "SquareSitesItemsAddMultiDataRelationship409ResponseBodyErrorsInner",
    "SquareSitesItemsMultiRelationshipDataDocument",
    "SquareSitesItemsReadMultiDataRelationship403ResponseBody",
    "SquareSitesItemsReadMultiDataRelationship409ResponseBody",
    "SquareSitesItemsReadMultiDataRelationship409ResponseBodyErrorsInner",
    "SquareSitesItemsRelationshipAddOperationPayload",
    "SquareSitesItemsRelationshipAddOperationPayloadData",
    "SquareSitesItemsRelationshipRemoveOperationPayload",
    "SquareSitesItemsRelationshipRemoveOperationPayloadData",
    "SquareSitesItemsRemoveMultiDataRelationship403ResponseBody",
    "SquareSitesItemsRemoveMultiDataRelationship409ResponseBody",
    "SquareSitesRelationships",
    "SquareSitesResourceObject",
    "StripeConnectionsAttributes",
    "StripeConnectionsCreateOperationPayload",
    "StripeConnectionsCreateOperationPayloadData",
    "StripeConnectionsCreateOperationPayloadDataAttributes",
    "StripeConnectionsCreateOperationPayloadMeta",
    "StripeConnectionsCreateSingleResourceDataDocument",
    "StripeConnectionsMultiResourceDataDocument",
    "StripeConnectionsOwnersMultiRelationshipDataDocument",
    "StripeConnectionsRelationships",
    "StripeConnectionsResourceObject",
    "StripeDashboardLinksAttributes",
    "StripeDashboardLinksMultiResourceDataDocument",
    "StripeDashboardLinksOwnersMultiRelationshipDataDocument",
    "StripeDashboardLinksRelationships",
    "StripeDashboardLinksResourceObject",
    "StudioHomeEventTilesAttributes",
    "StudioHomeEventTilesResourceObject",
    "StudioHomeEventTilesSingleResourceDataDocument",
    "StudioHomeInsightTilesAttributes",
    "StudioHomeInsightTilesResourceObject",
    "StudioHomeInsightTilesSingleResourceDataDocument",
    "StudioHomeMerchTilesAttributes",
    "StudioHomeMerchTilesItemsMultiRelationshipDataDocument",
    "StudioHomeMerchTilesRelationships",
    "StudioHomeMerchTilesResourceObject",
    "StudioHomeMerchTilesSingleResourceDataDocument",
    "StudioHomeMusicTilesAttributes",
    "StudioHomeMusicTilesResourceObject",
    "StudioHomeMusicTilesSingleResourceDataDocument",
    "SubscriptionPriceChangeDecisionsAttributes",
    "SubscriptionPriceChangeDecisionsCreateOperationPayload",
    "SubscriptionPriceChangeDecisionsCreateOperationPayloadData",
    "SubscriptionPriceChangeDecisionsCreateOperationPayloadDataAttributes",
    "SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationships",
    "SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationshipsPriceChange",
    "SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationshipsPriceChangeData",
    "SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument",
    "SubscriptionPriceChangeDecisionsMultiResourceDataDocument",
    "SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument",
    "SubscriptionPriceChangeDecisionsRelationships",
    "SubscriptionPriceChangeDecisionsResourceObject",
    "SubscriptionPriceChangeDecisionsUpdateOperationPayload",
    "SubscriptionPriceChangeDecisionsUpdateOperationPayloadData",
    "SubscriptionPriceChangeDecisionsUpdateOperationPayloadDataAttributes",
    "SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument",
    "TemporaryUserTokensCreateOperationPayload",
    "TemporaryUserTokensCreateOperationPayloadData",
    "TemporaryUserTokensCreateSingleResourceDataDocument",
    "TemporaryUserTokensOwnersMultiRelationshipDataDocument",
    "TemporaryUserTokensRelationships",
    "TemporaryUserTokensResourceObject",
    "TemporaryUserTokensSingleResourceDataDocument",
    "TermsAttributes",
    "TermsMultiResourceDataDocument",
    "TermsResourceObject",
    "TermsResourceObjectMeta",
    "TermsSingleResourceDataDocument",
    "ThirdPartyLyricsProvider",
    "TidalLyricsProvider",
    "TrackFilesAttributes",
    "TrackFilesReadById403ResponseBody",
    "TrackFilesReadById403ResponseBodyErrorsInner",
    "TrackFilesReadById404ResponseBody",
    "TrackFilesReadById404ResponseBodyErrorsInner",
    "TrackFilesResourceObject",
    "TrackFilesSingleResourceDataDocument",
    "TrackInfo",
    "TrackManifestsAttributes",
    "TrackManifestsReadById403ResponseBody",
    "TrackManifestsReadById404ResponseBody",
    "TrackManifestsResourceObject",
    "TrackManifestsSingleResourceDataDocument",
    "TrackSourceFilesAttributes",
    "TrackSourceFilesCommentSummarySingleRelationshipDataDocument",
    "TrackSourceFilesCreateOperationPayload",
    "TrackSourceFilesCreateOperationPayloadData",
    "TrackSourceFilesCreateOperationPayloadDataAttributes",
    "TrackSourceFilesCreateOperationPayloadDataRelationships",
    "TrackSourceFilesCreateOperationPayloadDataRelationshipsTrack",
    "TrackSourceFilesCreateOperationPayloadDataRelationshipsTrackData",
    "TrackSourceFilesCreateSingleResourceDataDocument",
    "TrackSourceFilesOwnersMultiRelationshipDataDocument",
    "TrackSourceFilesReactionSummarySingleRelationshipDataDocument",
    "TrackSourceFilesRelationships",
    "TrackSourceFilesResourceObject",
    "TrackSourceFilesSingleResourceDataDocument",
    "TrackStatisticsAttributes",
    "TrackStatisticsOwnersMultiRelationshipDataDocument",
    "TrackStatisticsRelationships",
    "TrackStatisticsResourceObject",
    "TrackStatisticsSingleResourceDataDocument",
    "TracksAlbumsMultiRelationshipDataDocument",
    "TracksAlbumsRelationshipUpdateOperationPayload",
    "TracksAlbumsRelationshipUpdateOperationPayloadData",
    "TracksAlbumsResourceIdentifier",
    "TracksAlbumsResourceIdentifierMeta",
    "TracksArtistsMultiRelationshipDataDocument",
    "TracksArtistsRelationshipUpdateOperationPayload",
    "TracksArtistsRelationshipUpdateOperationPayloadData",
    "TracksAttributes",
    "TracksCreateOperationPayload",
    "TracksCreateOperationPayloadData",
    "TracksCreateOperationPayloadDataAttributes",
    "TracksCreateOperationPayloadDataRelationships",
    "TracksCreateOperationPayloadDataRelationshipsAlbums",
    "TracksCreateOperationPayloadDataRelationshipsAlbumsData",
    "TracksCreateOperationPayloadDataRelationshipsArtists",
    "TracksCreateOperationPayloadDataRelationshipsArtistsData",
    "TracksCreateOperationPayloadDataRelationshipsGenres",
    "TracksCreateOperationPayloadDataRelationshipsGenresData",
    "TracksCreateSingleResourceDataDocument",
    "TracksCreditsMultiRelationshipDataDocument",
    "TracksDownloadSingleRelationshipDataDocument",
    "TracksGenresMultiRelationshipDataDocument",
    "TracksLyricsMultiRelationshipDataDocument",
    "TracksMetadataStatusAttributes",
    "TracksMetadataStatusResourceObject",
    "TracksMetadataStatusSingleRelationshipDataDocument",
    "TracksMetadataStatusSingleResourceDataDocument",
    "TracksMultiResourceDataDocument",
    "TracksOwnersMultiRelationshipDataDocument",
    "TracksPriceConfigSingleRelationshipDataDocument",
    "TracksProvidersMultiRelationshipDataDocument",
    "TracksRadioMultiRelationshipDataDocument",
    "TracksRelationships",
    "TracksReplacementResourceIdentifier",
    "TracksReplacementResourceIdentifierMeta",
    "TracksReplacementSingleRelationshipDataDocument",
    "TracksResourceObject",
    "TracksSharesMultiRelationshipDataDocument",
    "TracksSimilarTracksMultiRelationshipDataDocument",
    "TracksSimilarTracksResourceIdentifier",
    "TracksSimilarTracksResourceIdentifierMeta",
    "TracksSingleResourceDataDocument",
    "TracksSourceFileSingleRelationshipDataDocument",
    "TracksSuggestedTracksMultiRelationshipDataDocument",
    "TracksSuggestedTracksResourceIdentifier",
    "TracksSuggestedTracksResourceIdentifierMeta",
    "TracksTrackStatisticsSingleRelationshipDataDocument",
    "TracksUpdateOperationPayload",
    "TracksUpdateOperationPayloadData",
    "TracksUpdateOperationPayloadDataAttributes",
    "TracksUpdateOperationPayloadDataRelationships",
    "TracksUpdateOperationPayloadDataRelationshipsGenres",
    "TracksUpdateOperationPayloadDataRelationshipsGenresData",
    "TracksUsageRulesSingleRelationshipDataDocument",
    "UsageRulesAttributes",
    "UsageRulesCreateOperationPayload",
    "UsageRulesCreateOperationPayloadData",
    "UsageRulesCreateOperationPayloadDataAttributes",
    "UsageRulesCreateOperationPayloadDataRelationships",
    "UsageRulesCreateOperationPayloadDataRelationshipsSubject",
    "UsageRulesCreateOperationPayloadSubject",
    "UsageRulesCreateResource403ResponseBody",
    "UsageRulesCreateResource403ResponseBodyErrorsInner",
    "UsageRulesCreateSingleResourceDataDocument",
    "UsageRulesResourceObject",
    "UsageRulesSingleResourceDataDocument",
    "UserCollection",
    "UserCollectionAlbumsAttributes",
    "UserCollectionAlbumsItemsAddMultiDataRelationshipWithResponse409ResponseBody",
    "UserCollectionAlbumsItemsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner",
    "UserCollectionAlbumsItemsAddMultiRelationshipDataDocument",
    "UserCollectionAlbumsItemsAddMultiRelationshipDataDocumentMeta",
    "UserCollectionAlbumsItemsAddResourceIdentifier",
    "UserCollectionAlbumsItemsAddResourceIdentifierMeta",
    "UserCollectionAlbumsItemsMultiRelationshipDataDocument",
    "UserCollectionAlbumsItemsReadMultiDataRelationship403ResponseBody",
    "UserCollectionAlbumsItemsReadMultiDataRelationship403ResponseBodyErrorsInner",
    "UserCollectionAlbumsItemsRelationshipAddOperationPayload",
    "UserCollectionAlbumsItemsRelationshipAddOperationPayloadData",
    "UserCollectionAlbumsItemsRelationshipAddOperationPayloadDataMeta",
    "UserCollectionAlbumsItemsRelationshipAddOperationResponseMetaSkippedItem",
    "UserCollectionAlbumsItemsRelationshipRemoveOperationPayload",
    "UserCollectionAlbumsItemsRelationshipRemoveOperationPayloadData",
    "UserCollectionAlbumsItemsResourceIdentifier",
    "UserCollectionAlbumsItemsResourceIdentifierMeta",
    "UserCollectionAlbumsOwnersMultiRelationshipDataDocument",
    "UserCollectionAlbumsRelationships",
    "UserCollectionAlbumsResourceObject",
    "UserCollectionAlbumsSingleResourceDataDocument",
    "UserCollectionArtistsAttributes",
    "UserCollectionArtistsItemsAddMultiDataRelationshipWithResponse409ResponseBody",
    "UserCollectionArtistsItemsAddMultiRelationshipDataDocument",
    "UserCollectionArtistsItemsAddMultiRelationshipDataDocumentMeta",
    "UserCollectionArtistsItemsAddResourceIdentifier",
    "UserCollectionArtistsItemsAddResourceIdentifierMeta",
    "UserCollectionArtistsItemsMultiRelationshipDataDocument",
    "UserCollectionArtistsItemsReadMultiDataRelationship403ResponseBody",
    "UserCollectionArtistsItemsRelationshipAddOperationPayload",
    "UserCollectionArtistsItemsRelationshipAddOperationPayloadData",
    "UserCollectionArtistsItemsRelationshipAddOperationPayloadDataMeta",
    "UserCollectionArtistsItemsRelationshipAddOperationResponseMetaSkippedItem",
    "UserCollectionArtistsItemsRelationshipRemoveOperationPayload",
    "UserCollectionArtistsItemsRelationshipRemoveOperationPayloadData",
    "UserCollectionArtistsItemsResourceIdentifier",
    "UserCollectionArtistsItemsResourceIdentifierMeta",
    "UserCollectionArtistsOwnersMultiRelationshipDataDocument",
    "UserCollectionArtistsRelationships",
    "UserCollectionArtistsResourceObject",
    "UserCollectionArtistsSingleResourceDataDocument",
    "UserCollectionFoldersAttributes",
    "UserCollectionFoldersCreateOperationPayload",
    "UserCollectionFoldersCreateOperationPayloadData",
    "UserCollectionFoldersCreateOperationPayloadDataAttributes",
    "UserCollectionFoldersCreateOperationPayloadDataRelationships",
    "UserCollectionFoldersCreateOperationPayloadDataRelationshipsUserCollection",
    "UserCollectionFoldersCreateSingleResourceDataDocument",
    "UserCollectionFoldersDeleteResource400ResponseBody",
    "UserCollectionFoldersDeleteResource400ResponseBodyErrorsInner",
    "UserCollectionFoldersItemsMultiRelationshipDataDocument",
    "UserCollectionFoldersItemsRelationshipAddOperationPayload",
    "UserCollectionFoldersItemsRelationshipAddOperationPayloadData",
    "UserCollectionFoldersItemsRelationshipRemoveOperationPayload",
    "UserCollectionFoldersItemsRelationshipRemoveOperationPayloadData",
    "UserCollectionFoldersItemsResourceIdentifier",
    "UserCollectionFoldersItemsResourceIdentifierMeta",
    "UserCollectionFoldersMultiResourceDataDocument",
    "UserCollectionFoldersOwnersMultiRelationshipDataDocument",
    "UserCollectionFoldersRelationships",
    "UserCollectionFoldersResourceObject",
    "UserCollectionFoldersSingleResourceDataDocument",
    "UserCollectionFoldersUpdateOperationPayload",
    "UserCollectionFoldersUpdateOperationPayloadData",
    "UserCollectionFoldersUpdateOperationPayloadDataAttributes",
    "UserCollectionFoldersUserCollectionSingleRelationshipDataDocument",
    "UserCollectionPlaylistsAttributes",
    "UserCollectionPlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBody",
    "UserCollectionPlaylistsItemsAddMultiRelationshipDataDocument",
    "UserCollectionPlaylistsItemsAddMultiRelationshipDataDocumentMeta",
    "UserCollectionPlaylistsItemsAddResourceIdentifier",
    "UserCollectionPlaylistsItemsAddResourceIdentifierMeta",
    "UserCollectionPlaylistsItemsMultiRelationshipDataDocument",
    "UserCollectionPlaylistsItemsReadMultiDataRelationship403ResponseBody",
    "UserCollectionPlaylistsItemsRelationshipAddOperationPayload",
    "UserCollectionPlaylistsItemsRelationshipAddOperationPayloadData",
    "UserCollectionPlaylistsItemsRelationshipAddOperationPayloadDataMeta",
    "UserCollectionPlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem",
    "UserCollectionPlaylistsItemsRelationshipRemoveOperationPayload",
    "UserCollectionPlaylistsItemsRelationshipRemoveOperationPayloadData",
    "UserCollectionPlaylistsItemsResourceIdentifier",
    "UserCollectionPlaylistsItemsResourceIdentifierMeta",
    "UserCollectionPlaylistsOwnersMultiRelationshipDataDocument",
    "UserCollectionPlaylistsRelationships",
    "UserCollectionPlaylistsResourceObject",
    "UserCollectionPlaylistsSingleResourceDataDocument",
    "UserCollectionSaveForLatersAttributes",
    "UserCollectionSaveForLatersItemsAddMultiDataRelationshipWithResponse409ResponseBody",
    "UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocument",
    "UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocumentMeta",
    "UserCollectionSaveForLatersItemsAddResourceIdentifier",
    "UserCollectionSaveForLatersItemsAddResourceIdentifierMeta",
    "UserCollectionSaveForLatersItemsMultiRelationshipDataDocument",
    "UserCollectionSaveForLatersItemsRelationshipAddOperationPayload",
    "UserCollectionSaveForLatersItemsRelationshipAddOperationPayloadData",
    "UserCollectionSaveForLatersItemsRelationshipAddOperationResponseMetaSkippedItem",
    "UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayload",
    "UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayloadData",
    "UserCollectionSaveForLatersItemsResourceIdentifier",
    "UserCollectionSaveForLatersItemsResourceIdentifierMeta",
    "UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument",
    "UserCollectionSaveForLatersRelationships",
    "UserCollectionSaveForLatersResourceObject",
    "UserCollectionSaveForLatersSingleResourceDataDocument",
    "UserCollectionTracksAttributes",
    "UserCollectionTracksItemsAddMultiDataRelationshipWithResponse409ResponseBody",
    "UserCollectionTracksItemsAddMultiRelationshipDataDocument",
    "UserCollectionTracksItemsAddMultiRelationshipDataDocumentMeta",
    "UserCollectionTracksItemsAddResourceIdentifier",
    "UserCollectionTracksItemsAddResourceIdentifierMeta",
    "UserCollectionTracksItemsMultiRelationshipDataDocument",
    "UserCollectionTracksItemsReadMultiDataRelationship403ResponseBody",
    "UserCollectionTracksItemsRelationshipAddOperationPayload",
    "UserCollectionTracksItemsRelationshipAddOperationPayloadData",
    "UserCollectionTracksItemsRelationshipAddOperationPayloadDataMeta",
    "UserCollectionTracksItemsRelationshipAddOperationResponseMetaSkippedItem",
    "UserCollectionTracksItemsRelationshipRemoveOperationPayload",
    "UserCollectionTracksItemsRelationshipRemoveOperationPayloadData",
    "UserCollectionTracksItemsResourceIdentifier",
    "UserCollectionTracksItemsResourceIdentifierMeta",
    "UserCollectionTracksOwnersMultiRelationshipDataDocument",
    "UserCollectionTracksRelationships",
    "UserCollectionTracksResourceObject",
    "UserCollectionTracksSingleResourceDataDocument",
    "UserCollectionVideosAttributes",
    "UserCollectionVideosItemsAddMultiDataRelationshipWithResponse409ResponseBody",
    "UserCollectionVideosItemsAddMultiRelationshipDataDocument",
    "UserCollectionVideosItemsAddMultiRelationshipDataDocumentMeta",
    "UserCollectionVideosItemsAddResourceIdentifier",
    "UserCollectionVideosItemsAddResourceIdentifierMeta",
    "UserCollectionVideosItemsMultiRelationshipDataDocument",
    "UserCollectionVideosItemsReadMultiDataRelationship403ResponseBody",
    "UserCollectionVideosItemsRelationshipAddOperationPayload",
    "UserCollectionVideosItemsRelationshipAddOperationPayloadData",
    "UserCollectionVideosItemsRelationshipAddOperationPayloadDataMeta",
    "UserCollectionVideosItemsRelationshipAddOperationResponseMetaSkippedItem",
    "UserCollectionVideosItemsRelationshipRemoveOperationPayload",
    "UserCollectionVideosItemsRelationshipRemoveOperationPayloadData",
    "UserCollectionVideosItemsResourceIdentifier",
    "UserCollectionVideosItemsResourceIdentifierMeta",
    "UserCollectionVideosOwnersMultiRelationshipDataDocument",
    "UserCollectionVideosRelationships",
    "UserCollectionVideosResourceObject",
    "UserCollectionVideosSingleResourceDataDocument",
    "UserDailyMixesItemsMultiRelationshipDataDocument",
    "UserDailyMixesRelationships",
    "UserDailyMixesResourceObject",
    "UserDailyMixesSingleResourceDataDocument",
    "UserDataExportRequestsAttributes",
    "UserDataExportRequestsCreateOperationPayload",
    "UserDataExportRequestsCreateOperationPayloadData",
    "UserDataExportRequestsCreateOperationPayloadDataAttributes",
    "UserDataExportRequestsCreateSingleResourceDataDocument",
    "UserDataExportRequestsResourceObject",
    "UserDataExportsAttributes",
    "UserDataExportsCreateOperationPayload",
    "UserDataExportsCreateOperationPayloadData",
    "UserDataExportsCreateOperationPayloadDataAttributes",
    "UserDataExportsCreateOperationPayloadMeta",
    "UserDataExportsCreateResource400ResponseBody",
    "UserDataExportsCreateResource400ResponseBodyErrorsInner",
    "UserDataExportsCreateResource409ResponseBody",
    "UserDataExportsCreateResource409ResponseBodyErrorsInner",
    "UserDataExportsCreateSingleResourceDataDocument",
    "UserDataExportsMultiResourceDataDocument",
    "UserDataExportsOwnersMultiRelationshipDataDocument",
    "UserDataExportsRelationships",
    "UserDataExportsResourceObject",
    "UserDataExportsSingleResourceDataDocument",
    "UserDiscoveryMixesItemsMultiRelationshipDataDocument",
    "UserDiscoveryMixesRelationships",
    "UserDiscoveryMixesResourceObject",
    "UserDiscoveryMixesSingleResourceDataDocument",
    "UserFeedItemActivityDetails",
    "UserFeedItemAlbumFavouritedDetails",
    "UserFeedItemAlbumReleasedDetails",
    "UserFeedItemAlbumSharedDetails",
    "UserFeedItemArtistFollowedDetails",
    "UserFeedItemCommentRepliedDetails",
    "UserFeedItemCopyrightFlaggedDetails",
    "UserFeedItemHistoryMixReadyDetails",
    "UserFeedItemPlaylistUpdatedDetails",
    "UserFeedItemTrackFavouritedDetails",
    "UserFeedItemTrackPlayMilestoneDetails",
    "UserFeedItemTrackPlaylistedDetails",
    "UserFeedItemTrackSourceFileCommentedDetails",
    "UserFeedItemsActorsMultiRelationshipDataDocument",
    "UserFeedItemsAttributes",
    "UserFeedItemsMultiResourceDataDocument",
    "UserFeedItemsMultiResourceDataDocumentMeta",
    "UserFeedItemsRelationships",
    "UserFeedItemsResourceObject",
    "UserFeedItemsSubjectResourceIdentifier",
    "UserFeedItemsSubjectResourceIdentifierMeta",
    "UserFeedItemsSubjectSingleRelationshipDataDocument",
    "UserFeedsAttributes",
    "UserFeedsAttributesFeed",
    "UserFeedsAttributesInbox",
    "UserFeedsResourceObject",
    "UserFeedsSingleResourceDataDocument",
    "UserFeedsUpdateOperationPayload",
    "UserFeedsUpdateOperationPayloadData",
    "UserFeedsUpdateOperationPayloadDataAttributes",
    "UserFeedsUpdateOperationPayloadDataAttributesFeed",
    "UserFeedsUpdateOperationPayloadDataAttributesInbox",
    "UserFeedsUpdateSingleResourceDataDocument",
    "UserNewReleaseMixesItemsMultiRelationshipDataDocument",
    "UserNewReleaseMixesRelationships",
    "UserNewReleaseMixesResourceObject",
    "UserNewReleaseMixesSingleResourceDataDocument",
    "UserOfflineMixesItemsMultiRelationshipDataDocument",
    "UserOfflineMixesRelationships",
    "UserOfflineMixesResourceObject",
    "UserOfflineMixesSingleResourceDataDocument",
    "UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload",
    "UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayloadData",
    "UserPlaybackStatesActivePlayerSingleRelationshipDataDocument",
    "UserPlaybackStatesActivePlayerUpdateResourceIdentifier",
    "UserPlaybackStatesActivePlayerUpdateSingleRelationshipDataDocument",
    "UserPlaybackStatesAttributes",
    "UserPlaybackStatesAvailablePlayersAddMultiRelationshipDataDocument",
    "UserPlaybackStatesAvailablePlayersAddResourceIdentifier",
    "UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument",
    "UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload",
    "UserPlaybackStatesAvailablePlayersRelationshipOperationPayloadData",
    "UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload",
    "UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument",
    "UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload",
    "UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayloadData",
    "UserPlaybackStatesPlayQueueSingleRelationshipDataDocument",
    "UserPlaybackStatesPlayQueueUpdateResourceIdentifier",
    "UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument",
    "UserPlaybackStatesRelationships",
    "UserPlaybackStatesResourceObject",
    "UserPlaybackStatesSingleResourceDataDocument",
    "UserPlaybackStatesUpdateOperationPayload",
    "UserPlaybackStatesUpdateOperationPayloadData",
    "UserPlaybackStatesUpdateOperationPayloadDataAttributes",
    "UserPlaybackStatesUpdateSingleResourceDataDocument",
    "UserRecommendationBlocksArtistsAddMultiDataRelationshipWithResponse409ResponseBody",
    "UserRecommendationBlocksArtistsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner",
    "UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument",
    "UserRecommendationBlocksArtistsAddResourceIdentifier",
    "UserRecommendationBlocksArtistsMultiRelationshipDataDocument",
    "UserRecommendationBlocksArtistsRelationshipAddOperationPayload",
    "UserRecommendationBlocksArtistsRelationshipAddOperationPayloadData",
    "UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload",
    "UserRecommendationBlocksArtistsRelationshipRemoveOperationPayloadData",
    "UserRecommendationBlocksArtistsResourceIdentifier",
    "UserRecommendationBlocksArtistsResourceIdentifierMeta",
    "UserRecommendationBlocksOwnersMultiRelationshipDataDocument",
    "UserRecommendationBlocksRelationships",
    "UserRecommendationBlocksResourceObject",
    "UserRecommendationBlocksSingleResourceDataDocument",
    "UserRecommendationBlocksTracksAddMultiDataRelationshipWithResponse409ResponseBody",
    "UserRecommendationBlocksTracksAddMultiRelationshipDataDocument",
    "UserRecommendationBlocksTracksAddResourceIdentifier",
    "UserRecommendationBlocksTracksMultiRelationshipDataDocument",
    "UserRecommendationBlocksTracksRelationshipAddOperationPayload",
    "UserRecommendationBlocksTracksRelationshipAddOperationPayloadData",
    "UserRecommendationBlocksTracksRelationshipRemoveOperationPayload",
    "UserRecommendationBlocksTracksRelationshipRemoveOperationPayloadData",
    "UserRecommendationBlocksTracksResourceIdentifier",
    "UserRecommendationBlocksTracksResourceIdentifierMeta",
    "UserRecommendationBlocksVideosAddMultiDataRelationshipWithResponse409ResponseBody",
    "UserRecommendationBlocksVideosAddMultiRelationshipDataDocument",
    "UserRecommendationBlocksVideosAddResourceIdentifier",
    "UserRecommendationBlocksVideosMultiRelationshipDataDocument",
    "UserRecommendationBlocksVideosRelationshipAddOperationPayload",
    "UserRecommendationBlocksVideosRelationshipAddOperationPayloadData",
    "UserRecommendationBlocksVideosRelationshipRemoveOperationPayload",
    "UserRecommendationBlocksVideosRelationshipRemoveOperationPayloadData",
    "UserRecommendationBlocksVideosResourceIdentifier",
    "UserRecommendationBlocksVideosResourceIdentifierMeta",
    "UserReportsAttributes",
    "UserReportsCreateOperationPayload",
    "UserReportsCreateOperationPayloadData",
    "UserReportsCreateOperationPayloadDataAttributes",
    "UserReportsCreateOperationPayloadDataRelationships",
    "UserReportsCreateOperationPayloadDataRelationshipsReportedResources",
    "UserReportsCreateOperationPayloadDataRelationshipsReportedResourcesData",
    "UserReportsCreateResource403ResponseBody",
    "UserReportsCreateResource403ResponseBodyErrorsInner",
    "UserReportsCreateSingleResourceDataDocument",
    "UserReportsResourceObject",
    "UserSubscriptionPriceChangesAttributes",
    "UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument",
    "UserSubscriptionPriceChangesMultiResourceDataDocument",
    "UserSubscriptionPriceChangesRelationships",
    "UserSubscriptionPriceChangesResourceObject",
    "UsersArtistSingleRelationshipDataDocument",
    "UsersAttributes",
    "UsersRelationships",
    "UsersResourceObject",
    "UsersSingleResourceDataDocument",
    "Variation",
    "VideoManifestsAttributes",
    "VideoManifestsReadById403ResponseBody",
    "VideoManifestsReadById404ResponseBody",
    "VideoManifestsResourceObject",
    "VideoManifestsSingleResourceDataDocument",
    "VideosAlbumsMultiRelationshipDataDocument",
    "VideosAlbumsResourceIdentifier",
    "VideosAlbumsResourceIdentifierMeta",
    "VideosArtistsMultiRelationshipDataDocument",
    "VideosAttributes",
    "VideosCreditsMultiRelationshipDataDocument",
    "VideosMultiResourceDataDocument",
    "VideosProvidersMultiRelationshipDataDocument",
    "VideosRelationships",
    "VideosReplacementResourceIdentifier",
    "VideosReplacementResourceIdentifierMeta",
    "VideosReplacementSingleRelationshipDataDocument",
    "VideosResourceObject",
    "VideosSimilarVideosMultiRelationshipDataDocument",
    "VideosSimilarVideosResourceIdentifier",
    "VideosSimilarVideosResourceIdentifierMeta",
    "VideosSingleResourceDataDocument",
    "VideosSuggestedVideosMultiRelationshipDataDocument",
    "VideosSuggestedVideosResourceIdentifier",
    "VideosSuggestedVideosResourceIdentifierMeta",
    "VideosThumbnailArtMultiRelationshipDataDocument",
    "VideosUsageRulesSingleRelationshipDataDocument",
    "ViewerContextsAttributes",
    "ViewerContextsCommentsMultiRelationshipDataDocument",
    "ViewerContextsMultiResourceDataDocument",
    "ViewerContextsReactionsMultiRelationshipDataDocument",
    "ViewerContextsRelationships",
    "ViewerContextsResourceObject",
    "ViewerContextsSingleResourceDataDocument",
    "ViewerContextsSubjectResourceIdentifier",
    "ViewerContextsSubjectResourceIdentifierMeta",
    "ViewerContextsSubjectSingleRelationshipDataDocument",
    "ViewerContextsViewerSingleRelationshipDataDocument",
    "Waveform",
]

# import apis into sdk package
from tidal.api.accepted_terms_api import AcceptedTermsApi as AcceptedTermsApi
from tidal.api.album_statistics_api import AlbumStatisticsApi as AlbumStatisticsApi
from tidal.api.albums_api import AlbumsApi as AlbumsApi
from tidal.api.appreciations_api import AppreciationsApi as AppreciationsApi
from tidal.api.artist_biographies_api import ArtistBiographiesApi as ArtistBiographiesApi
from tidal.api.artist_claim_statuses_api import ArtistClaimStatusesApi as ArtistClaimStatusesApi
from tidal.api.artist_claims_api import ArtistClaimsApi as ArtistClaimsApi
from tidal.api.artist_roles_api import ArtistRolesApi as ArtistRolesApi
from tidal.api.artist_sales_statistics_api import ArtistSalesStatisticsApi as ArtistSalesStatisticsApi
from tidal.api.artist_streams_statistics_api import ArtistStreamsStatisticsApi as ArtistStreamsStatisticsApi
from tidal.api.artists_api import ArtistsApi as ArtistsApi
from tidal.api.artwork_libraries_api import ArtworkLibrariesApi as ArtworkLibrariesApi
from tidal.api.artworks_api import ArtworksApi as ArtworksApi
from tidal.api.client_certificates_api import ClientCertificatesApi as ClientCertificatesApi
from tidal.api.clients_api import ClientsApi as ClientsApi
from tidal.api.collaboration_invite_redemptions_api import CollaborationInviteRedemptionsApi as CollaborationInviteRedemptionsApi
from tidal.api.collaboration_invites_api import CollaborationInvitesApi as CollaborationInvitesApi
from tidal.api.comment_summaries_api import CommentSummariesApi as CommentSummariesApi
from tidal.api.comments_api import CommentsApi as CommentsApi
from tidal.api.content_claims_api import ContentClaimsApi as ContentClaimsApi
from tidal.api.credits_api import CreditsApi as CreditsApi
from tidal.api.downloads_api import DownloadsApi as DownloadsApi
from tidal.api.dsp_sharing_links_api import DspSharingLinksApi as DspSharingLinksApi
from tidal.api.dynamic_modules_api import DynamicModulesApi as DynamicModulesApi
from tidal.api.dynamic_pages_api import DynamicPagesApi as DynamicPagesApi
from tidal.api.folder_items_api import FolderItemsApi as FolderItemsApi
from tidal.api.folders_api import FoldersApi as FoldersApi
from tidal.api.genres_api import GenresApi as GenresApi
from tidal.api.groups_api import GroupsApi as GroupsApi
from tidal.api.installations_api import InstallationsApi as InstallationsApi
from tidal.api.lyrics_api import LyricsApi as LyricsApi
from tidal.api.manual_artist_claims_api import ManualArtistClaimsApi as ManualArtistClaimsApi
from tidal.api.offline_tasks_api import OfflineTasksApi as OfflineTasksApi
from tidal.api.play_queues_api import PlayQueuesApi as PlayQueuesApi
from tidal.api.playlist_generation_schedules_api import PlaylistGenerationSchedulesApi as PlaylistGenerationSchedulesApi
from tidal.api.playlist_generations_api import PlaylistGenerationsApi as PlaylistGenerationsApi
from tidal.api.playlists_api import PlaylistsApi as PlaylistsApi
from tidal.api.price_configurations_api import PriceConfigurationsApi as PriceConfigurationsApi
from tidal.api.provider_owners_api import ProviderOwnersApi as ProviderOwnersApi
from tidal.api.provider_product_infos_api import ProviderProductInfosApi as ProviderProductInfosApi
from tidal.api.providers_api import ProvidersApi as ProvidersApi
from tidal.api.purchases_api import PurchasesApi as PurchasesApi
from tidal.api.reaction_summaries_api import ReactionSummariesApi as ReactionSummariesApi
from tidal.api.reactions_api import ReactionsApi as ReactionsApi
from tidal.api.resource_grant_invitations_api import ResourceGrantInvitationsApi as ResourceGrantInvitationsApi
from tidal.api.resource_grants_api import ResourceGrantsApi as ResourceGrantsApi
from tidal.api.saved_shares_api import SavedSharesApi as SavedSharesApi
from tidal.api.scopes_api import ScopesApi as ScopesApi
from tidal.api.search_history_entries_api import SearchHistoryEntriesApi as SearchHistoryEntriesApi
from tidal.api.search_results_api import SearchResultsApi as SearchResultsApi
from tidal.api.search_suggestions_api import SearchSuggestionsApi as SearchSuggestionsApi
from tidal.api.shares_api import SharesApi as SharesApi
from tidal.api.sharing_summaries_api import SharingSummariesApi as SharingSummariesApi
from tidal.api.square_connections_api import SquareConnectionsApi as SquareConnectionsApi
from tidal.api.square_item_variation_physical_counts_api import SquareItemVariationPhysicalCountsApi as SquareItemVariationPhysicalCountsApi
from tidal.api.square_item_variations_api import SquareItemVariationsApi as SquareItemVariationsApi
from tidal.api.square_items_api import SquareItemsApi as SquareItemsApi
from tidal.api.square_sites_api import SquareSitesApi as SquareSitesApi
from tidal.api.stripe_connections_api import StripeConnectionsApi as StripeConnectionsApi
from tidal.api.stripe_dashboard_links_api import StripeDashboardLinksApi as StripeDashboardLinksApi
from tidal.api.studio_home_event_tiles_api import StudioHomeEventTilesApi as StudioHomeEventTilesApi
from tidal.api.studio_home_insight_tiles_api import StudioHomeInsightTilesApi as StudioHomeInsightTilesApi
from tidal.api.studio_home_merch_tiles_api import StudioHomeMerchTilesApi as StudioHomeMerchTilesApi
from tidal.api.studio_home_music_tiles_api import StudioHomeMusicTilesApi as StudioHomeMusicTilesApi
from tidal.api.subscription_price_change_decisions_api import SubscriptionPriceChangeDecisionsApi as SubscriptionPriceChangeDecisionsApi
from tidal.api.temporary_user_tokens_api import TemporaryUserTokensApi as TemporaryUserTokensApi
from tidal.api.terms_api import TermsApi as TermsApi
from tidal.api.track_files_api import TrackFilesApi as TrackFilesApi
from tidal.api.track_manifests_api import TrackManifestsApi as TrackManifestsApi
from tidal.api.track_source_files_api import TrackSourceFilesApi as TrackSourceFilesApi
from tidal.api.track_statistics_api import TrackStatisticsApi as TrackStatisticsApi
from tidal.api.tracks_api import TracksApi as TracksApi
from tidal.api.tracks_metadata_status_api import TracksMetadataStatusApi as TracksMetadataStatusApi
from tidal.api.usage_rules_api import UsageRulesApi as UsageRulesApi
from tidal.api.user_collection_albums_api import UserCollectionAlbumsApi as UserCollectionAlbumsApi
from tidal.api.user_collection_artists_api import UserCollectionArtistsApi as UserCollectionArtistsApi
from tidal.api.user_collection_folders_api import UserCollectionFoldersApi as UserCollectionFoldersApi
from tidal.api.user_collection_playlists_api import UserCollectionPlaylistsApi as UserCollectionPlaylistsApi
from tidal.api.user_collection_save_for_laters_api import UserCollectionSaveForLatersApi as UserCollectionSaveForLatersApi
from tidal.api.user_collection_tracks_api import UserCollectionTracksApi as UserCollectionTracksApi
from tidal.api.user_collection_videos_api import UserCollectionVideosApi as UserCollectionVideosApi
from tidal.api.user_daily_mixes_api import UserDailyMixesApi as UserDailyMixesApi
from tidal.api.user_data_export_requests_api import UserDataExportRequestsApi as UserDataExportRequestsApi
from tidal.api.user_data_exports_api import UserDataExportsApi as UserDataExportsApi
from tidal.api.user_discovery_mixes_api import UserDiscoveryMixesApi as UserDiscoveryMixesApi
from tidal.api.user_feed_items_api import UserFeedItemsApi as UserFeedItemsApi
from tidal.api.user_feeds_api import UserFeedsApi as UserFeedsApi
from tidal.api.user_new_release_mixes_api import UserNewReleaseMixesApi as UserNewReleaseMixesApi
from tidal.api.user_offline_mixes_api import UserOfflineMixesApi as UserOfflineMixesApi
from tidal.api.user_playback_states_api import UserPlaybackStatesApi as UserPlaybackStatesApi
from tidal.api.user_recommendation_blocks_api import UserRecommendationBlocksApi as UserRecommendationBlocksApi
from tidal.api.user_reports_api import UserReportsApi as UserReportsApi
from tidal.api.user_subscription_price_changes_api import UserSubscriptionPriceChangesApi as UserSubscriptionPriceChangesApi
from tidal.api.users_api import UsersApi as UsersApi
from tidal.api.video_manifests_api import VideoManifestsApi as VideoManifestsApi
from tidal.api.videos_api import VideosApi as VideosApi
from tidal.api.viewer_contexts_api import ViewerContextsApi as ViewerContextsApi

# import ApiClient
from tidal.api_response import ApiResponse as ApiResponse
from tidal.api_client import ApiClient as ApiClient
from tidal.configuration import Configuration as Configuration
from tidal.exceptions import OpenApiException as OpenApiException
from tidal.exceptions import ApiTypeError as ApiTypeError
from tidal.exceptions import ApiValueError as ApiValueError
from tidal.exceptions import ApiKeyError as ApiKeyError
from tidal.exceptions import ApiAttributeError as ApiAttributeError
from tidal.exceptions import ApiException as ApiException

# import models into sdk package
from tidal.models.accepted_terms_attributes import AcceptedTermsAttributes as AcceptedTermsAttributes
from tidal.models.accepted_terms_create_operation_payload import AcceptedTermsCreateOperationPayload as AcceptedTermsCreateOperationPayload
from tidal.models.accepted_terms_create_operation_payload_data import AcceptedTermsCreateOperationPayloadData as AcceptedTermsCreateOperationPayloadData
from tidal.models.accepted_terms_create_operation_payload_data_relationships import AcceptedTermsCreateOperationPayloadDataRelationships as AcceptedTermsCreateOperationPayloadDataRelationships
from tidal.models.accepted_terms_create_operation_payload_data_relationships_terms import AcceptedTermsCreateOperationPayloadDataRelationshipsTerms as AcceptedTermsCreateOperationPayloadDataRelationshipsTerms
from tidal.models.accepted_terms_create_operation_payload_data_relationships_terms_data import AcceptedTermsCreateOperationPayloadDataRelationshipsTermsData as AcceptedTermsCreateOperationPayloadDataRelationshipsTermsData
from tidal.models.accepted_terms_create_single_resource_data_document import AcceptedTermsCreateSingleResourceDataDocument as AcceptedTermsCreateSingleResourceDataDocument
from tidal.models.accepted_terms_multi_resource_data_document import AcceptedTermsMultiResourceDataDocument as AcceptedTermsMultiResourceDataDocument
from tidal.models.accepted_terms_owners_multi_relationship_data_document import AcceptedTermsOwnersMultiRelationshipDataDocument as AcceptedTermsOwnersMultiRelationshipDataDocument
from tidal.models.accepted_terms_relationships import AcceptedTermsRelationships as AcceptedTermsRelationships
from tidal.models.accepted_terms_resource_object import AcceptedTermsResourceObject as AcceptedTermsResourceObject
from tidal.models.accepted_terms_terms_single_relationship_data_document import AcceptedTermsTermsSingleRelationshipDataDocument as AcceptedTermsTermsSingleRelationshipDataDocument
from tidal.models.album_statistics_attributes import AlbumStatisticsAttributes as AlbumStatisticsAttributes
from tidal.models.album_statistics_owners_multi_relationship_data_document import AlbumStatisticsOwnersMultiRelationshipDataDocument as AlbumStatisticsOwnersMultiRelationshipDataDocument
from tidal.models.album_statistics_relationships import AlbumStatisticsRelationships as AlbumStatisticsRelationships
from tidal.models.album_statistics_resource_object import AlbumStatisticsResourceObject as AlbumStatisticsResourceObject
from tidal.models.album_statistics_single_resource_data_document import AlbumStatisticsSingleResourceDataDocument as AlbumStatisticsSingleResourceDataDocument
from tidal.models.albums_album_statistics_single_relationship_data_document import AlbumsAlbumStatisticsSingleRelationshipDataDocument as AlbumsAlbumStatisticsSingleRelationshipDataDocument
from tidal.models.albums_artists_multi_relationship_data_document import AlbumsArtistsMultiRelationshipDataDocument as AlbumsArtistsMultiRelationshipDataDocument
from tidal.models.albums_artists_relationship_update_operation_payload import AlbumsArtistsRelationshipUpdateOperationPayload as AlbumsArtistsRelationshipUpdateOperationPayload
from tidal.models.albums_artists_relationship_update_operation_payload_data import AlbumsArtistsRelationshipUpdateOperationPayloadData as AlbumsArtistsRelationshipUpdateOperationPayloadData
from tidal.models.albums_artists_relationship_update_operation_payload_meta import AlbumsArtistsRelationshipUpdateOperationPayloadMeta as AlbumsArtistsRelationshipUpdateOperationPayloadMeta
from tidal.models.albums_attributes import AlbumsAttributes as AlbumsAttributes
from tidal.models.albums_cover_art_multi_relationship_data_document import AlbumsCoverArtMultiRelationshipDataDocument as AlbumsCoverArtMultiRelationshipDataDocument
from tidal.models.albums_cover_art_relationship_update_operation_payload import AlbumsCoverArtRelationshipUpdateOperationPayload as AlbumsCoverArtRelationshipUpdateOperationPayload
from tidal.models.albums_cover_art_relationship_update_operation_payload_data import AlbumsCoverArtRelationshipUpdateOperationPayloadData as AlbumsCoverArtRelationshipUpdateOperationPayloadData
from tidal.models.albums_create_operation_payload import AlbumsCreateOperationPayload as AlbumsCreateOperationPayload
from tidal.models.albums_create_operation_payload_data import AlbumsCreateOperationPayloadData as AlbumsCreateOperationPayloadData
from tidal.models.albums_create_operation_payload_data_attributes import AlbumsCreateOperationPayloadDataAttributes as AlbumsCreateOperationPayloadDataAttributes
from tidal.models.albums_create_operation_payload_data_relationships import AlbumsCreateOperationPayloadDataRelationships as AlbumsCreateOperationPayloadDataRelationships
from tidal.models.albums_create_operation_payload_data_relationships_artists import AlbumsCreateOperationPayloadDataRelationshipsArtists as AlbumsCreateOperationPayloadDataRelationshipsArtists
from tidal.models.albums_create_operation_payload_data_relationships_artists_data import AlbumsCreateOperationPayloadDataRelationshipsArtistsData as AlbumsCreateOperationPayloadDataRelationshipsArtistsData
from tidal.models.albums_create_operation_payload_data_relationships_genres import AlbumsCreateOperationPayloadDataRelationshipsGenres as AlbumsCreateOperationPayloadDataRelationshipsGenres
from tidal.models.albums_create_operation_payload_data_relationships_genres_data import AlbumsCreateOperationPayloadDataRelationshipsGenresData as AlbumsCreateOperationPayloadDataRelationshipsGenresData
from tidal.models.albums_create_single_resource_data_document import AlbumsCreateSingleResourceDataDocument as AlbumsCreateSingleResourceDataDocument
from tidal.models.albums_genres_multi_relationship_data_document import AlbumsGenresMultiRelationshipDataDocument as AlbumsGenresMultiRelationshipDataDocument
from tidal.models.albums_items_multi_relationship_data_document import AlbumsItemsMultiRelationshipDataDocument as AlbumsItemsMultiRelationshipDataDocument
from tidal.models.albums_items_relationship_update_operation_payload import AlbumsItemsRelationshipUpdateOperationPayload as AlbumsItemsRelationshipUpdateOperationPayload
from tidal.models.albums_items_relationship_update_operation_payload_data import AlbumsItemsRelationshipUpdateOperationPayloadData as AlbumsItemsRelationshipUpdateOperationPayloadData
from tidal.models.albums_items_relationship_update_operation_payload_meta import AlbumsItemsRelationshipUpdateOperationPayloadMeta as AlbumsItemsRelationshipUpdateOperationPayloadMeta
from tidal.models.albums_items_resource_identifier import AlbumsItemsResourceIdentifier as AlbumsItemsResourceIdentifier
from tidal.models.albums_items_resource_identifier_meta import AlbumsItemsResourceIdentifierMeta as AlbumsItemsResourceIdentifierMeta
from tidal.models.albums_multi_resource_data_document import AlbumsMultiResourceDataDocument as AlbumsMultiResourceDataDocument
from tidal.models.albums_owners_multi_relationship_data_document import AlbumsOwnersMultiRelationshipDataDocument as AlbumsOwnersMultiRelationshipDataDocument
from tidal.models.albums_price_config_single_relationship_data_document import AlbumsPriceConfigSingleRelationshipDataDocument as AlbumsPriceConfigSingleRelationshipDataDocument
from tidal.models.albums_providers_multi_relationship_data_document import AlbumsProvidersMultiRelationshipDataDocument as AlbumsProvidersMultiRelationshipDataDocument
from tidal.models.albums_relationships import AlbumsRelationships as AlbumsRelationships
from tidal.models.albums_replacement_resource_identifier import AlbumsReplacementResourceIdentifier as AlbumsReplacementResourceIdentifier
from tidal.models.albums_replacement_resource_identifier_meta import AlbumsReplacementResourceIdentifierMeta as AlbumsReplacementResourceIdentifierMeta
from tidal.models.albums_replacement_single_relationship_data_document import AlbumsReplacementSingleRelationshipDataDocument as AlbumsReplacementSingleRelationshipDataDocument
from tidal.models.albums_resource_object import AlbumsResourceObject as AlbumsResourceObject
from tidal.models.albums_shares_multi_relationship_data_document import AlbumsSharesMultiRelationshipDataDocument as AlbumsSharesMultiRelationshipDataDocument
from tidal.models.albums_similar_albums_multi_relationship_data_document import AlbumsSimilarAlbumsMultiRelationshipDataDocument as AlbumsSimilarAlbumsMultiRelationshipDataDocument
from tidal.models.albums_similar_albums_resource_identifier import AlbumsSimilarAlbumsResourceIdentifier as AlbumsSimilarAlbumsResourceIdentifier
from tidal.models.albums_similar_albums_resource_identifier_meta import AlbumsSimilarAlbumsResourceIdentifierMeta as AlbumsSimilarAlbumsResourceIdentifierMeta
from tidal.models.albums_single_resource_data_document import AlbumsSingleResourceDataDocument as AlbumsSingleResourceDataDocument
from tidal.models.albums_suggested_cover_arts_multi_relationship_data_document import AlbumsSuggestedCoverArtsMultiRelationshipDataDocument as AlbumsSuggestedCoverArtsMultiRelationshipDataDocument
from tidal.models.albums_suggested_cover_arts_multi_relationship_data_document_meta import AlbumsSuggestedCoverArtsMultiRelationshipDataDocumentMeta as AlbumsSuggestedCoverArtsMultiRelationshipDataDocumentMeta
from tidal.models.albums_suggested_cover_arts_resource_identifier import AlbumsSuggestedCoverArtsResourceIdentifier as AlbumsSuggestedCoverArtsResourceIdentifier
from tidal.models.albums_suggested_cover_arts_resource_identifier_meta import AlbumsSuggestedCoverArtsResourceIdentifierMeta as AlbumsSuggestedCoverArtsResourceIdentifierMeta
from tidal.models.albums_update_operation_payload import AlbumsUpdateOperationPayload as AlbumsUpdateOperationPayload
from tidal.models.albums_update_operation_payload_data import AlbumsUpdateOperationPayloadData as AlbumsUpdateOperationPayloadData
from tidal.models.albums_update_operation_payload_data_attributes import AlbumsUpdateOperationPayloadDataAttributes as AlbumsUpdateOperationPayloadDataAttributes
from tidal.models.albums_update_operation_payload_data_relationships import AlbumsUpdateOperationPayloadDataRelationships as AlbumsUpdateOperationPayloadDataRelationships
from tidal.models.albums_update_operation_payload_data_relationships_genres import AlbumsUpdateOperationPayloadDataRelationshipsGenres as AlbumsUpdateOperationPayloadDataRelationshipsGenres
from tidal.models.albums_update_operation_payload_data_relationships_genres_data import AlbumsUpdateOperationPayloadDataRelationshipsGenresData as AlbumsUpdateOperationPayloadDataRelationshipsGenresData
from tidal.models.albums_usage_rules_single_relationship_data_document import AlbumsUsageRulesSingleRelationshipDataDocument as AlbumsUsageRulesSingleRelationshipDataDocument
from tidal.models.appreciations_attributes import AppreciationsAttributes as AppreciationsAttributes
from tidal.models.appreciations_create_operation_payload import AppreciationsCreateOperationPayload as AppreciationsCreateOperationPayload
from tidal.models.appreciations_create_operation_payload_data import AppreciationsCreateOperationPayloadData as AppreciationsCreateOperationPayloadData
from tidal.models.appreciations_create_operation_payload_data_relationships import AppreciationsCreateOperationPayloadDataRelationships as AppreciationsCreateOperationPayloadDataRelationships
from tidal.models.appreciations_create_operation_payload_data_relationships_appreciated_item import AppreciationsCreateOperationPayloadDataRelationshipsAppreciatedItem as AppreciationsCreateOperationPayloadDataRelationshipsAppreciatedItem
from tidal.models.appreciations_create_operation_payload_data_relationships_appreciated_item_data import AppreciationsCreateOperationPayloadDataRelationshipsAppreciatedItemData as AppreciationsCreateOperationPayloadDataRelationshipsAppreciatedItemData
from tidal.models.appreciations_create_operation_payload_meta import AppreciationsCreateOperationPayloadMeta as AppreciationsCreateOperationPayloadMeta
from tidal.models.appreciations_create_single_resource_data_document import AppreciationsCreateSingleResourceDataDocument as AppreciationsCreateSingleResourceDataDocument
from tidal.models.appreciations_resource_object import AppreciationsResourceObject as AppreciationsResourceObject
from tidal.models.artist_biographies_attributes import ArtistBiographiesAttributes as ArtistBiographiesAttributes
from tidal.models.artist_biographies_owners_multi_relationship_data_document import ArtistBiographiesOwnersMultiRelationshipDataDocument as ArtistBiographiesOwnersMultiRelationshipDataDocument
from tidal.models.artist_biographies_relationships import ArtistBiographiesRelationships as ArtistBiographiesRelationships
from tidal.models.artist_biographies_resource_object import ArtistBiographiesResourceObject as ArtistBiographiesResourceObject
from tidal.models.artist_biographies_single_resource_data_document import ArtistBiographiesSingleResourceDataDocument as ArtistBiographiesSingleResourceDataDocument
from tidal.models.artist_biographies_update_operation_payload import ArtistBiographiesUpdateOperationPayload as ArtistBiographiesUpdateOperationPayload
from tidal.models.artist_biographies_update_operation_payload_data import ArtistBiographiesUpdateOperationPayloadData as ArtistBiographiesUpdateOperationPayloadData
from tidal.models.artist_biographies_update_operation_payload_data_attributes import ArtistBiographiesUpdateOperationPayloadDataAttributes as ArtistBiographiesUpdateOperationPayloadDataAttributes
from tidal.models.artist_claim_statuses_attributes import ArtistClaimStatusesAttributes as ArtistClaimStatusesAttributes
from tidal.models.artist_claim_statuses_multi_resource_data_document import ArtistClaimStatusesMultiResourceDataDocument as ArtistClaimStatusesMultiResourceDataDocument
from tidal.models.artist_claim_statuses_resource_object import ArtistClaimStatusesResourceObject as ArtistClaimStatusesResourceObject
from tidal.models.artist_claims_accepted_artists_multi_relationship_data_document import ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument as ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument
from tidal.models.artist_claims_accepted_artists_relationship_update_operation_payload import ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload as ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload
from tidal.models.artist_claims_accepted_artists_relationship_update_operation_payload_data import ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayloadData as ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayloadData
from tidal.models.artist_claims_attributes import ArtistClaimsAttributes as ArtistClaimsAttributes
from tidal.models.artist_claims_create_operation_payload import ArtistClaimsCreateOperationPayload as ArtistClaimsCreateOperationPayload
from tidal.models.artist_claims_create_operation_payload_data import ArtistClaimsCreateOperationPayloadData as ArtistClaimsCreateOperationPayloadData
from tidal.models.artist_claims_create_operation_payload_data_attributes import ArtistClaimsCreateOperationPayloadDataAttributes as ArtistClaimsCreateOperationPayloadDataAttributes
from tidal.models.artist_claims_create_operation_payload_meta import ArtistClaimsCreateOperationPayloadMeta as ArtistClaimsCreateOperationPayloadMeta
from tidal.models.artist_claims_create_single_resource_data_document import ArtistClaimsCreateSingleResourceDataDocument as ArtistClaimsCreateSingleResourceDataDocument
from tidal.models.artist_claims_multi_resource_data_document import ArtistClaimsMultiResourceDataDocument as ArtistClaimsMultiResourceDataDocument
from tidal.models.artist_claims_owners_multi_relationship_data_document import ArtistClaimsOwnersMultiRelationshipDataDocument as ArtistClaimsOwnersMultiRelationshipDataDocument
from tidal.models.artist_claims_recommended_artists_multi_relationship_data_document import ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument as ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument
from tidal.models.artist_claims_relationships import ArtistClaimsRelationships as ArtistClaimsRelationships
from tidal.models.artist_claims_resource_object import ArtistClaimsResourceObject as ArtistClaimsResourceObject
from tidal.models.artist_claims_single_resource_data_document import ArtistClaimsSingleResourceDataDocument as ArtistClaimsSingleResourceDataDocument
from tidal.models.artist_claims_update_operation_payload import ArtistClaimsUpdateOperationPayload as ArtistClaimsUpdateOperationPayload
from tidal.models.artist_claims_update_operation_payload_data import ArtistClaimsUpdateOperationPayloadData as ArtistClaimsUpdateOperationPayloadData
from tidal.models.artist_claims_update_operation_payload_meta import ArtistClaimsUpdateOperationPayloadMeta as ArtistClaimsUpdateOperationPayloadMeta
from tidal.models.artist_roles_attributes import ArtistRolesAttributes as ArtistRolesAttributes
from tidal.models.artist_roles_resource_object import ArtistRolesResourceObject as ArtistRolesResourceObject
from tidal.models.artist_roles_single_resource_data_document import ArtistRolesSingleResourceDataDocument as ArtistRolesSingleResourceDataDocument
from tidal.models.artist_sales_statistics_artist_single_relationship_data_document import ArtistSalesStatisticsArtistSingleRelationshipDataDocument as ArtistSalesStatisticsArtistSingleRelationshipDataDocument
from tidal.models.artist_sales_statistics_attributes import ArtistSalesStatisticsAttributes as ArtistSalesStatisticsAttributes
from tidal.models.artist_sales_statistics_buyer_source_share import ArtistSalesStatisticsBuyerSourceShare as ArtistSalesStatisticsBuyerSourceShare
from tidal.models.artist_sales_statistics_buyer_sources import ArtistSalesStatisticsBuyerSources as ArtistSalesStatisticsBuyerSources
from tidal.models.artist_sales_statistics_by_type import ArtistSalesStatisticsByType as ArtistSalesStatisticsByType
from tidal.models.artist_sales_statistics_multi_resource_data_document import ArtistSalesStatisticsMultiResourceDataDocument as ArtistSalesStatisticsMultiResourceDataDocument
from tidal.models.artist_sales_statistics_net_sales import ArtistSalesStatisticsNetSales as ArtistSalesStatisticsNetSales
from tidal.models.artist_sales_statistics_refunds import ArtistSalesStatisticsRefunds as ArtistSalesStatisticsRefunds
from tidal.models.artist_sales_statistics_relationships import ArtistSalesStatisticsRelationships as ArtistSalesStatisticsRelationships
from tidal.models.artist_sales_statistics_resource_object import ArtistSalesStatisticsResourceObject as ArtistSalesStatisticsResourceObject
from tidal.models.artist_sales_statistics_series import ArtistSalesStatisticsSeries as ArtistSalesStatisticsSeries
from tidal.models.artist_sales_statistics_series_point import ArtistSalesStatisticsSeriesPoint as ArtistSalesStatisticsSeriesPoint
from tidal.models.artist_sales_statistics_top_sellers_multi_relationship_data_document import ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument as ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument
from tidal.models.artist_sales_statistics_top_sellers_multi_relationship_data_document_meta import ArtistSalesStatisticsTopSellersMultiRelationshipDataDocumentMeta as ArtistSalesStatisticsTopSellersMultiRelationshipDataDocumentMeta
from tidal.models.artist_sales_statistics_top_sellers_resource_identifier import ArtistSalesStatisticsTopSellersResourceIdentifier as ArtistSalesStatisticsTopSellersResourceIdentifier
from tidal.models.artist_sales_statistics_top_sellers_resource_identifier_meta import ArtistSalesStatisticsTopSellersResourceIdentifierMeta as ArtistSalesStatisticsTopSellersResourceIdentifierMeta
from tidal.models.artist_statistics_bucket_period import ArtistStatisticsBucketPeriod as ArtistStatisticsBucketPeriod
from tidal.models.artist_statistics_window_period import ArtistStatisticsWindowPeriod as ArtistStatisticsWindowPeriod
from tidal.models.artist_streams_statistics_artist_single_relationship_data_document import ArtistStreamsStatisticsArtistSingleRelationshipDataDocument as ArtistStreamsStatisticsArtistSingleRelationshipDataDocument
from tidal.models.artist_streams_statistics_attributes import ArtistStreamsStatisticsAttributes as ArtistStreamsStatisticsAttributes
from tidal.models.artist_streams_statistics_count import ArtistStreamsStatisticsCount as ArtistStreamsStatisticsCount
from tidal.models.artist_streams_statistics_country_listeners import ArtistStreamsStatisticsCountryListeners as ArtistStreamsStatisticsCountryListeners
from tidal.models.artist_streams_statistics_multi_resource_data_document import ArtistStreamsStatisticsMultiResourceDataDocument as ArtistStreamsStatisticsMultiResourceDataDocument
from tidal.models.artist_streams_statistics_other_plays import ArtistStreamsStatisticsOtherPlays as ArtistStreamsStatisticsOtherPlays
from tidal.models.artist_streams_statistics_plays import ArtistStreamsStatisticsPlays as ArtistStreamsStatisticsPlays
from tidal.models.artist_streams_statistics_plays_by_source import ArtistStreamsStatisticsPlaysBySource as ArtistStreamsStatisticsPlaysBySource
from tidal.models.artist_streams_statistics_relationships import ArtistStreamsStatisticsRelationships as ArtistStreamsStatisticsRelationships
from tidal.models.artist_streams_statistics_resource_object import ArtistStreamsStatisticsResourceObject as ArtistStreamsStatisticsResourceObject
from tidal.models.artist_streams_statistics_series import ArtistStreamsStatisticsSeries as ArtistStreamsStatisticsSeries
from tidal.models.artist_streams_statistics_series_point import ArtistStreamsStatisticsSeriesPoint as ArtistStreamsStatisticsSeriesPoint
from tidal.models.artist_streams_statistics_source_plays import ArtistStreamsStatisticsSourcePlays as ArtistStreamsStatisticsSourcePlays
from tidal.models.artist_streams_statistics_top_countries import ArtistStreamsStatisticsTopCountries as ArtistStreamsStatisticsTopCountries
from tidal.models.artist_streams_statistics_top_tracks_multi_relationship_data_document import ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument as ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument
from tidal.models.artist_streams_statistics_top_tracks_multi_relationship_data_document_meta import ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocumentMeta as ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocumentMeta
from tidal.models.artist_streams_statistics_top_tracks_resource_identifier import ArtistStreamsStatisticsTopTracksResourceIdentifier as ArtistStreamsStatisticsTopTracksResourceIdentifier
from tidal.models.artist_streams_statistics_top_tracks_resource_identifier_meta import ArtistStreamsStatisticsTopTracksResourceIdentifierMeta as ArtistStreamsStatisticsTopTracksResourceIdentifierMeta
from tidal.models.artists_albums_multi_relationship_data_document import ArtistsAlbumsMultiRelationshipDataDocument as ArtistsAlbumsMultiRelationshipDataDocument
from tidal.models.artists_albums_resource_identifier import ArtistsAlbumsResourceIdentifier as ArtistsAlbumsResourceIdentifier
from tidal.models.artists_albums_resource_identifier_meta import ArtistsAlbumsResourceIdentifierMeta as ArtistsAlbumsResourceIdentifierMeta
from tidal.models.artists_attributes import ArtistsAttributes as ArtistsAttributes
from tidal.models.artists_banner_art_multi_relationship_data_document import ArtistsBannerArtMultiRelationshipDataDocument as ArtistsBannerArtMultiRelationshipDataDocument
from tidal.models.artists_banner_art_relationship_update_operation_payload import ArtistsBannerArtRelationshipUpdateOperationPayload as ArtistsBannerArtRelationshipUpdateOperationPayload
from tidal.models.artists_banner_art_relationship_update_operation_payload_data import ArtistsBannerArtRelationshipUpdateOperationPayloadData as ArtistsBannerArtRelationshipUpdateOperationPayloadData
from tidal.models.artists_biography_single_relationship_data_document import ArtistsBiographySingleRelationshipDataDocument as ArtistsBiographySingleRelationshipDataDocument
from tidal.models.artists_claim_status_single_relationship_data_document import ArtistsClaimStatusSingleRelationshipDataDocument as ArtistsClaimStatusSingleRelationshipDataDocument
from tidal.models.artists_create_operation_payload import ArtistsCreateOperationPayload as ArtistsCreateOperationPayload
from tidal.models.artists_create_operation_payload_data import ArtistsCreateOperationPayloadData as ArtistsCreateOperationPayloadData
from tidal.models.artists_create_operation_payload_data_attributes import ArtistsCreateOperationPayloadDataAttributes as ArtistsCreateOperationPayloadDataAttributes
from tidal.models.artists_create_operation_payload_meta import ArtistsCreateOperationPayloadMeta as ArtistsCreateOperationPayloadMeta
from tidal.models.artists_create_single_resource_data_document import ArtistsCreateSingleResourceDataDocument as ArtistsCreateSingleResourceDataDocument
from tidal.models.artists_followers_multi_relationship_data_document import ArtistsFollowersMultiRelationshipDataDocument as ArtistsFollowersMultiRelationshipDataDocument
from tidal.models.artists_followers_resource_identifier import ArtistsFollowersResourceIdentifier as ArtistsFollowersResourceIdentifier
from tidal.models.artists_followers_resource_identifier_meta import ArtistsFollowersResourceIdentifierMeta as ArtistsFollowersResourceIdentifierMeta
from tidal.models.artists_followers_resource_meta_viewer_context import ArtistsFollowersResourceMetaViewerContext as ArtistsFollowersResourceMetaViewerContext
from tidal.models.artists_following_multi_relationship_data_document import ArtistsFollowingMultiRelationshipDataDocument as ArtistsFollowingMultiRelationshipDataDocument
from tidal.models.artists_following_relationship_add_operation_payload import ArtistsFollowingRelationshipAddOperationPayload as ArtistsFollowingRelationshipAddOperationPayload
from tidal.models.artists_following_relationship_add_operation_payload_data import ArtistsFollowingRelationshipAddOperationPayloadData as ArtistsFollowingRelationshipAddOperationPayloadData
from tidal.models.artists_following_relationship_remove_operation_payload import ArtistsFollowingRelationshipRemoveOperationPayload as ArtistsFollowingRelationshipRemoveOperationPayload
from tidal.models.artists_following_relationship_remove_operation_payload_data import ArtistsFollowingRelationshipRemoveOperationPayloadData as ArtistsFollowingRelationshipRemoveOperationPayloadData
from tidal.models.artists_following_resource_identifier import ArtistsFollowingResourceIdentifier as ArtistsFollowingResourceIdentifier
from tidal.models.artists_following_resource_identifier_meta import ArtistsFollowingResourceIdentifierMeta as ArtistsFollowingResourceIdentifierMeta
from tidal.models.artists_logo_art_multi_relationship_data_document import ArtistsLogoArtMultiRelationshipDataDocument as ArtistsLogoArtMultiRelationshipDataDocument
from tidal.models.artists_logo_art_relationship_update_operation_payload import ArtistsLogoArtRelationshipUpdateOperationPayload as ArtistsLogoArtRelationshipUpdateOperationPayload
from tidal.models.artists_logo_art_relationship_update_operation_payload_data import ArtistsLogoArtRelationshipUpdateOperationPayloadData as ArtistsLogoArtRelationshipUpdateOperationPayloadData
from tidal.models.artists_multi_resource_data_document import ArtistsMultiResourceDataDocument as ArtistsMultiResourceDataDocument
from tidal.models.artists_owners_multi_relationship_data_document import ArtistsOwnersMultiRelationshipDataDocument as ArtistsOwnersMultiRelationshipDataDocument
from tidal.models.artists_profile_art_multi_relationship_data_document import ArtistsProfileArtMultiRelationshipDataDocument as ArtistsProfileArtMultiRelationshipDataDocument
from tidal.models.artists_profile_art_relationship_update_operation_payload import ArtistsProfileArtRelationshipUpdateOperationPayload as ArtistsProfileArtRelationshipUpdateOperationPayload
from tidal.models.artists_profile_art_relationship_update_operation_payload_data import ArtistsProfileArtRelationshipUpdateOperationPayloadData as ArtistsProfileArtRelationshipUpdateOperationPayloadData
from tidal.models.artists_radio_multi_relationship_data_document import ArtistsRadioMultiRelationshipDataDocument as ArtistsRadioMultiRelationshipDataDocument
from tidal.models.artists_relationships import ArtistsRelationships as ArtistsRelationships
from tidal.models.artists_resource_object import ArtistsResourceObject as ArtistsResourceObject
from tidal.models.artists_roles_multi_relationship_data_document import ArtistsRolesMultiRelationshipDataDocument as ArtistsRolesMultiRelationshipDataDocument
from tidal.models.artists_similar_artists_multi_relationship_data_document import ArtistsSimilarArtistsMultiRelationshipDataDocument as ArtistsSimilarArtistsMultiRelationshipDataDocument
from tidal.models.artists_single_resource_data_document import ArtistsSingleResourceDataDocument as ArtistsSingleResourceDataDocument
from tidal.models.artists_track_providers_multi_relationship_data_document import ArtistsTrackProvidersMultiRelationshipDataDocument as ArtistsTrackProvidersMultiRelationshipDataDocument
from tidal.models.artists_track_providers_resource_identifier import ArtistsTrackProvidersResourceIdentifier as ArtistsTrackProvidersResourceIdentifier
from tidal.models.artists_track_providers_resource_identifier_meta import ArtistsTrackProvidersResourceIdentifierMeta as ArtistsTrackProvidersResourceIdentifierMeta
from tidal.models.artists_tracks_multi_relationship_data_document import ArtistsTracksMultiRelationshipDataDocument as ArtistsTracksMultiRelationshipDataDocument
from tidal.models.artists_tracks_resource_identifier import ArtistsTracksResourceIdentifier as ArtistsTracksResourceIdentifier
from tidal.models.artists_tracks_resource_identifier_meta import ArtistsTracksResourceIdentifierMeta as ArtistsTracksResourceIdentifierMeta
from tidal.models.artists_update_operation_payload import ArtistsUpdateOperationPayload as ArtistsUpdateOperationPayload
from tidal.models.artists_update_operation_payload_data import ArtistsUpdateOperationPayloadData as ArtistsUpdateOperationPayloadData
from tidal.models.artists_update_operation_payload_data_attributes import ArtistsUpdateOperationPayloadDataAttributes as ArtistsUpdateOperationPayloadDataAttributes
from tidal.models.artists_update_operation_payload_meta import ArtistsUpdateOperationPayloadMeta as ArtistsUpdateOperationPayloadMeta
from tidal.models.artists_videos_multi_relationship_data_document import ArtistsVideosMultiRelationshipDataDocument as ArtistsVideosMultiRelationshipDataDocument
from tidal.models.artists_videos_resource_identifier import ArtistsVideosResourceIdentifier as ArtistsVideosResourceIdentifier
from tidal.models.artists_videos_resource_identifier_meta import ArtistsVideosResourceIdentifierMeta as ArtistsVideosResourceIdentifierMeta
from tidal.models.artwork import Artwork as Artwork
from tidal.models.artwork_file import ArtworkFile as ArtworkFile
from tidal.models.artwork_file_meta import ArtworkFileMeta as ArtworkFileMeta
from tidal.models.artwork_libraries_artworks_multi_relationship_data_document import ArtworkLibrariesArtworksMultiRelationshipDataDocument as ArtworkLibrariesArtworksMultiRelationshipDataDocument
from tidal.models.artwork_libraries_artworks_resource_identifier import ArtworkLibrariesArtworksResourceIdentifier as ArtworkLibrariesArtworksResourceIdentifier
from tidal.models.artwork_libraries_artworks_resource_identifier_meta import ArtworkLibrariesArtworksResourceIdentifierMeta as ArtworkLibrariesArtworksResourceIdentifierMeta
from tidal.models.artwork_libraries_attributes import ArtworkLibrariesAttributes as ArtworkLibrariesAttributes
from tidal.models.artwork_libraries_multi_resource_data_document import ArtworkLibrariesMultiResourceDataDocument as ArtworkLibrariesMultiResourceDataDocument
from tidal.models.artwork_libraries_random_artwork_resource_identifier import ArtworkLibrariesRandomArtworkResourceIdentifier as ArtworkLibrariesRandomArtworkResourceIdentifier
from tidal.models.artwork_libraries_random_artwork_resource_identifier_meta import ArtworkLibrariesRandomArtworkResourceIdentifierMeta as ArtworkLibrariesRandomArtworkResourceIdentifierMeta
from tidal.models.artwork_libraries_random_artwork_single_relationship_data_document import ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument as ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument
from tidal.models.artwork_libraries_relationships import ArtworkLibrariesRelationships as ArtworkLibrariesRelationships
from tidal.models.artwork_libraries_resource_object import ArtworkLibrariesResourceObject as ArtworkLibrariesResourceObject
from tidal.models.artwork_libraries_single_resource_data_document import ArtworkLibrariesSingleResourceDataDocument as ArtworkLibrariesSingleResourceDataDocument
from tidal.models.artwork_source_file import ArtworkSourceFile as ArtworkSourceFile
from tidal.models.artwork_visual_metadata import ArtworkVisualMetadata as ArtworkVisualMetadata
from tidal.models.artworks_attributes import ArtworksAttributes as ArtworksAttributes
from tidal.models.artworks_create_operation_payload import ArtworksCreateOperationPayload as ArtworksCreateOperationPayload
from tidal.models.artworks_create_operation_payload_data import ArtworksCreateOperationPayloadData as ArtworksCreateOperationPayloadData
from tidal.models.artworks_create_operation_payload_data_attributes import ArtworksCreateOperationPayloadDataAttributes as ArtworksCreateOperationPayloadDataAttributes
from tidal.models.artworks_create_operation_payload_data_attributes_source_file import ArtworksCreateOperationPayloadDataAttributesSourceFile as ArtworksCreateOperationPayloadDataAttributesSourceFile
from tidal.models.artworks_create_single_resource_data_document import ArtworksCreateSingleResourceDataDocument as ArtworksCreateSingleResourceDataDocument
from tidal.models.artworks_multi_resource_data_document import ArtworksMultiResourceDataDocument as ArtworksMultiResourceDataDocument
from tidal.models.artworks_owners_multi_relationship_data_document import ArtworksOwnersMultiRelationshipDataDocument as ArtworksOwnersMultiRelationshipDataDocument
from tidal.models.artworks_relationships import ArtworksRelationships as ArtworksRelationships
from tidal.models.artworks_resource_object import ArtworksResourceObject as ArtworksResourceObject
from tidal.models.artworks_single_resource_data_document import ArtworksSingleResourceDataDocument as ArtworksSingleResourceDataDocument
from tidal.models.atomic_operations400_response_body import AtomicOperations400ResponseBody as AtomicOperations400ResponseBody
from tidal.models.atomic_operations400_response_body_errors_inner import AtomicOperations400ResponseBodyErrorsInner as AtomicOperations400ResponseBodyErrorsInner
from tidal.models.atomic_operations403_response_body import AtomicOperations403ResponseBody as AtomicOperations403ResponseBody
from tidal.models.atomic_operations403_response_body_errors_inner import AtomicOperations403ResponseBodyErrorsInner as AtomicOperations403ResponseBodyErrorsInner
from tidal.models.atomic_operations404_response_body import AtomicOperations404ResponseBody as AtomicOperations404ResponseBody
from tidal.models.atomic_operations404_response_body_errors_inner import AtomicOperations404ResponseBodyErrorsInner as AtomicOperations404ResponseBodyErrorsInner
from tidal.models.atomic_operations405_response_body import AtomicOperations405ResponseBody as AtomicOperations405ResponseBody
from tidal.models.atomic_operations405_response_body_errors_inner import AtomicOperations405ResponseBodyErrorsInner as AtomicOperations405ResponseBodyErrorsInner
from tidal.models.atomic_operations406_response_body import AtomicOperations406ResponseBody as AtomicOperations406ResponseBody
from tidal.models.atomic_operations406_response_body_errors_inner import AtomicOperations406ResponseBodyErrorsInner as AtomicOperations406ResponseBodyErrorsInner
from tidal.models.atomic_operations409_response_body import AtomicOperations409ResponseBody as AtomicOperations409ResponseBody
from tidal.models.atomic_operations409_response_body_errors_inner import AtomicOperations409ResponseBodyErrorsInner as AtomicOperations409ResponseBodyErrorsInner
from tidal.models.atomic_operations415_response_body import AtomicOperations415ResponseBody as AtomicOperations415ResponseBody
from tidal.models.atomic_operations415_response_body_errors_inner import AtomicOperations415ResponseBodyErrorsInner as AtomicOperations415ResponseBodyErrorsInner
from tidal.models.atomic_operations422_response_body import AtomicOperations422ResponseBody as AtomicOperations422ResponseBody
from tidal.models.atomic_operations422_response_body_errors_inner import AtomicOperations422ResponseBodyErrorsInner as AtomicOperations422ResponseBodyErrorsInner
from tidal.models.atomic_operations429_response_body import AtomicOperations429ResponseBody as AtomicOperations429ResponseBody
from tidal.models.atomic_operations429_response_body_errors_inner import AtomicOperations429ResponseBodyErrorsInner as AtomicOperations429ResponseBodyErrorsInner
from tidal.models.atomic_operations500_response_body import AtomicOperations500ResponseBody as AtomicOperations500ResponseBody
from tidal.models.atomic_operations500_response_body_errors_inner import AtomicOperations500ResponseBodyErrorsInner as AtomicOperations500ResponseBodyErrorsInner
from tidal.models.atomic_operations503_response_body import AtomicOperations503ResponseBody as AtomicOperations503ResponseBody
from tidal.models.atomic_operations503_response_body_errors_inner import AtomicOperations503ResponseBodyErrorsInner as AtomicOperations503ResponseBodyErrorsInner
from tidal.models.atomic_operations_request import AtomicOperationsRequest as AtomicOperationsRequest
from tidal.models.atomic_operations_request_atomic_operations_inner import AtomicOperationsRequestAtomicOperationsInner as AtomicOperationsRequestAtomicOperationsInner
from tidal.models.atomic_operations_request_atomic_operations_inner_one_of import AtomicOperationsRequestAtomicOperationsInnerOneOf as AtomicOperationsRequestAtomicOperationsInnerOneOf
from tidal.models.atomic_operations_request_atomic_operations_inner_one_of1 import AtomicOperationsRequestAtomicOperationsInnerOneOf1 as AtomicOperationsRequestAtomicOperationsInnerOneOf1
from tidal.models.atomic_operations_response import AtomicOperationsResponse as AtomicOperationsResponse
from tidal.models.atomic_operations_response_atomic_results_inner import AtomicOperationsResponseAtomicResultsInner as AtomicOperationsResponseAtomicResultsInner
from tidal.models.atomic_operations_response_atomic_results_inner_one_of import AtomicOperationsResponseAtomicResultsInnerOneOf as AtomicOperationsResponseAtomicResultsInnerOneOf
from tidal.models.atomic_operations_response_atomic_results_inner_one_of1 import AtomicOperationsResponseAtomicResultsInnerOneOf1 as AtomicOperationsResponseAtomicResultsInnerOneOf1
from tidal.models.audio import Audio as Audio
from tidal.models.audio_normalization_data import AudioNormalizationData as AudioNormalizationData
from tidal.models.change_event_streams_attributes import ChangeEventStreamsAttributes as ChangeEventStreamsAttributes
from tidal.models.change_event_streams_resource_object import ChangeEventStreamsResourceObject as ChangeEventStreamsResourceObject
from tidal.models.client_certificates_attributes import ClientCertificatesAttributes as ClientCertificatesAttributes
from tidal.models.client_certificates_create_operation_payload import ClientCertificatesCreateOperationPayload as ClientCertificatesCreateOperationPayload
from tidal.models.client_certificates_create_operation_payload_data import ClientCertificatesCreateOperationPayloadData as ClientCertificatesCreateOperationPayloadData
from tidal.models.client_certificates_create_operation_payload_data_relationships import ClientCertificatesCreateOperationPayloadDataRelationships as ClientCertificatesCreateOperationPayloadDataRelationships
from tidal.models.client_certificates_create_operation_payload_data_relationships_client import ClientCertificatesCreateOperationPayloadDataRelationshipsClient as ClientCertificatesCreateOperationPayloadDataRelationshipsClient
from tidal.models.client_certificates_create_operation_payload_data_relationships_client_data import ClientCertificatesCreateOperationPayloadDataRelationshipsClientData as ClientCertificatesCreateOperationPayloadDataRelationshipsClientData
from tidal.models.client_certificates_create_single_resource_data_document import ClientCertificatesCreateSingleResourceDataDocument as ClientCertificatesCreateSingleResourceDataDocument
from tidal.models.client_certificates_owners_multi_relationship_data_document import ClientCertificatesOwnersMultiRelationshipDataDocument as ClientCertificatesOwnersMultiRelationshipDataDocument
from tidal.models.client_certificates_relationships import ClientCertificatesRelationships as ClientCertificatesRelationships
from tidal.models.client_certificates_resource_object import ClientCertificatesResourceObject as ClientCertificatesResourceObject
from tidal.models.client_certificates_single_resource_data_document import ClientCertificatesSingleResourceDataDocument as ClientCertificatesSingleResourceDataDocument
from tidal.models.clients_attributes import ClientsAttributes as ClientsAttributes
from tidal.models.clients_certificates_multi_relationship_data_document import ClientsCertificatesMultiRelationshipDataDocument as ClientsCertificatesMultiRelationshipDataDocument
from tidal.models.clients_create_operation_payload import ClientsCreateOperationPayload as ClientsCreateOperationPayload
from tidal.models.clients_create_operation_payload_data import ClientsCreateOperationPayloadData as ClientsCreateOperationPayloadData
from tidal.models.clients_create_operation_payload_data_attributes import ClientsCreateOperationPayloadDataAttributes as ClientsCreateOperationPayloadDataAttributes
from tidal.models.clients_create_single_resource_data_document import ClientsCreateSingleResourceDataDocument as ClientsCreateSingleResourceDataDocument
from tidal.models.clients_multi_resource_data_document import ClientsMultiResourceDataDocument as ClientsMultiResourceDataDocument
from tidal.models.clients_owners_multi_relationship_data_document import ClientsOwnersMultiRelationshipDataDocument as ClientsOwnersMultiRelationshipDataDocument
from tidal.models.clients_relationships import ClientsRelationships as ClientsRelationships
from tidal.models.clients_resource_object import ClientsResourceObject as ClientsResourceObject
from tidal.models.clients_single_resource_data_document import ClientsSingleResourceDataDocument as ClientsSingleResourceDataDocument
from tidal.models.clients_update_operation_payload import ClientsUpdateOperationPayload as ClientsUpdateOperationPayload
from tidal.models.clients_update_operation_payload_data import ClientsUpdateOperationPayloadData as ClientsUpdateOperationPayloadData
from tidal.models.clients_update_operation_payload_data_attributes import ClientsUpdateOperationPayloadDataAttributes as ClientsUpdateOperationPayloadDataAttributes
from tidal.models.clients_update_single_resource_data_document import ClientsUpdateSingleResourceDataDocument as ClientsUpdateSingleResourceDataDocument
from tidal.models.collaboration_invite_redemptions_attributes import CollaborationInviteRedemptionsAttributes as CollaborationInviteRedemptionsAttributes
from tidal.models.collaboration_invite_redemptions_create_operation_payload import CollaborationInviteRedemptionsCreateOperationPayload as CollaborationInviteRedemptionsCreateOperationPayload
from tidal.models.collaboration_invite_redemptions_create_operation_payload_data import CollaborationInviteRedemptionsCreateOperationPayloadData as CollaborationInviteRedemptionsCreateOperationPayloadData
from tidal.models.collaboration_invite_redemptions_create_operation_payload_data_relationships import CollaborationInviteRedemptionsCreateOperationPayloadDataRelationships as CollaborationInviteRedemptionsCreateOperationPayloadDataRelationships
from tidal.models.collaboration_invite_redemptions_create_operation_payload_data_relationships_invite import CollaborationInviteRedemptionsCreateOperationPayloadDataRelationshipsInvite as CollaborationInviteRedemptionsCreateOperationPayloadDataRelationshipsInvite
from tidal.models.collaboration_invite_redemptions_create_operation_payload_data_relationships_invite_data import CollaborationInviteRedemptionsCreateOperationPayloadDataRelationshipsInviteData as CollaborationInviteRedemptionsCreateOperationPayloadDataRelationshipsInviteData
from tidal.models.collaboration_invite_redemptions_create_single_resource_data_document import CollaborationInviteRedemptionsCreateSingleResourceDataDocument as CollaborationInviteRedemptionsCreateSingleResourceDataDocument
from tidal.models.collaboration_invite_redemptions_resource_object import CollaborationInviteRedemptionsResourceObject as CollaborationInviteRedemptionsResourceObject
from tidal.models.collaboration_invites_attributes import CollaborationInvitesAttributes as CollaborationInvitesAttributes
from tidal.models.collaboration_invites_create_operation_payload import CollaborationInvitesCreateOperationPayload as CollaborationInvitesCreateOperationPayload
from tidal.models.collaboration_invites_create_operation_payload_data import CollaborationInvitesCreateOperationPayloadData as CollaborationInvitesCreateOperationPayloadData
from tidal.models.collaboration_invites_create_operation_payload_data_relationships import CollaborationInvitesCreateOperationPayloadDataRelationships as CollaborationInvitesCreateOperationPayloadDataRelationships
from tidal.models.collaboration_invites_create_operation_payload_data_relationships_subject import CollaborationInvitesCreateOperationPayloadDataRelationshipsSubject as CollaborationInvitesCreateOperationPayloadDataRelationshipsSubject
from tidal.models.collaboration_invites_create_operation_payload_data_relationships_subject_data import CollaborationInvitesCreateOperationPayloadDataRelationshipsSubjectData as CollaborationInvitesCreateOperationPayloadDataRelationshipsSubjectData
from tidal.models.collaboration_invites_create_single_resource_data_document import CollaborationInvitesCreateSingleResourceDataDocument as CollaborationInvitesCreateSingleResourceDataDocument
from tidal.models.collaboration_invites_multi_resource_data_document import CollaborationInvitesMultiResourceDataDocument as CollaborationInvitesMultiResourceDataDocument
from tidal.models.collaboration_invites_owners_multi_relationship_data_document import CollaborationInvitesOwnersMultiRelationshipDataDocument as CollaborationInvitesOwnersMultiRelationshipDataDocument
from tidal.models.collaboration_invites_relationships import CollaborationInvitesRelationships as CollaborationInvitesRelationships
from tidal.models.collaboration_invites_resource_object import CollaborationInvitesResourceObject as CollaborationInvitesResourceObject
from tidal.models.collaboration_invites_single_resource_data_document import CollaborationInvitesSingleResourceDataDocument as CollaborationInvitesSingleResourceDataDocument
from tidal.models.collaboration_invites_subject_single_relationship_data_document import CollaborationInvitesSubjectSingleRelationshipDataDocument as CollaborationInvitesSubjectSingleRelationshipDataDocument
from tidal.models.comment_summaries_attributes import CommentSummariesAttributes as CommentSummariesAttributes
from tidal.models.comment_summaries_multi_resource_data_document import CommentSummariesMultiResourceDataDocument as CommentSummariesMultiResourceDataDocument
from tidal.models.comment_summaries_relationships import CommentSummariesRelationships as CommentSummariesRelationships
from tidal.models.comment_summaries_resource_object import CommentSummariesResourceObject as CommentSummariesResourceObject
from tidal.models.comment_summaries_subject_single_relationship_data_document import CommentSummariesSubjectSingleRelationshipDataDocument as CommentSummariesSubjectSingleRelationshipDataDocument
from tidal.models.comments_attributes import CommentsAttributes as CommentsAttributes
from tidal.models.comments_author_single_relationship_data_document import CommentsAuthorSingleRelationshipDataDocument as CommentsAuthorSingleRelationshipDataDocument
from tidal.models.comments_comment_summary_single_relationship_data_document import CommentsCommentSummarySingleRelationshipDataDocument as CommentsCommentSummarySingleRelationshipDataDocument
from tidal.models.comments_create_operation_payload import CommentsCreateOperationPayload as CommentsCreateOperationPayload
from tidal.models.comments_create_operation_payload_data import CommentsCreateOperationPayloadData as CommentsCreateOperationPayloadData
from tidal.models.comments_create_operation_payload_data_attributes import CommentsCreateOperationPayloadDataAttributes as CommentsCreateOperationPayloadDataAttributes
from tidal.models.comments_create_operation_payload_data_relationships import CommentsCreateOperationPayloadDataRelationships as CommentsCreateOperationPayloadDataRelationships
from tidal.models.comments_create_operation_payload_data_relationships_subject import CommentsCreateOperationPayloadDataRelationshipsSubject as CommentsCreateOperationPayloadDataRelationshipsSubject
from tidal.models.comments_create_operation_payload_data_relationships_subject_data import CommentsCreateOperationPayloadDataRelationshipsSubjectData as CommentsCreateOperationPayloadDataRelationshipsSubjectData
from tidal.models.comments_create_single_resource_data_document import CommentsCreateSingleResourceDataDocument as CommentsCreateSingleResourceDataDocument
from tidal.models.comments_multi_resource_data_document import CommentsMultiResourceDataDocument as CommentsMultiResourceDataDocument
from tidal.models.comments_owners_multi_relationship_data_document import CommentsOwnersMultiRelationshipDataDocument as CommentsOwnersMultiRelationshipDataDocument
from tidal.models.comments_reaction_summary_single_relationship_data_document import CommentsReactionSummarySingleRelationshipDataDocument as CommentsReactionSummarySingleRelationshipDataDocument
from tidal.models.comments_relationships import CommentsRelationships as CommentsRelationships
from tidal.models.comments_resource_object import CommentsResourceObject as CommentsResourceObject
from tidal.models.comments_root_subject_single_relationship_data_document import CommentsRootSubjectSingleRelationshipDataDocument as CommentsRootSubjectSingleRelationshipDataDocument
from tidal.models.comments_single_resource_data_document import CommentsSingleResourceDataDocument as CommentsSingleResourceDataDocument
from tidal.models.comments_subject_single_relationship_data_document import CommentsSubjectSingleRelationshipDataDocument as CommentsSubjectSingleRelationshipDataDocument
from tidal.models.comments_update_operation_payload import CommentsUpdateOperationPayload as CommentsUpdateOperationPayload
from tidal.models.comments_update_operation_payload_data import CommentsUpdateOperationPayloadData as CommentsUpdateOperationPayloadData
from tidal.models.comments_update_operation_payload_data_attributes import CommentsUpdateOperationPayloadDataAttributes as CommentsUpdateOperationPayloadDataAttributes
from tidal.models.content_claims_attributes import ContentClaimsAttributes as ContentClaimsAttributes
from tidal.models.content_claims_claimed_resource_resource_identifier import ContentClaimsClaimedResourceResourceIdentifier as ContentClaimsClaimedResourceResourceIdentifier
from tidal.models.content_claims_claimed_resource_resource_identifier_meta import ContentClaimsClaimedResourceResourceIdentifierMeta as ContentClaimsClaimedResourceResourceIdentifierMeta
from tidal.models.content_claims_claimed_resource_single_relationship_data_document import ContentClaimsClaimedResourceSingleRelationshipDataDocument as ContentClaimsClaimedResourceSingleRelationshipDataDocument
from tidal.models.content_claims_claiming_artist_single_relationship_data_document import ContentClaimsClaimingArtistSingleRelationshipDataDocument as ContentClaimsClaimingArtistSingleRelationshipDataDocument
from tidal.models.content_claims_create_operation_payload import ContentClaimsCreateOperationPayload as ContentClaimsCreateOperationPayload
from tidal.models.content_claims_create_operation_payload_data import ContentClaimsCreateOperationPayloadData as ContentClaimsCreateOperationPayloadData
from tidal.models.content_claims_create_operation_payload_data_attributes import ContentClaimsCreateOperationPayloadDataAttributes as ContentClaimsCreateOperationPayloadDataAttributes
from tidal.models.content_claims_create_operation_payload_data_relationships import ContentClaimsCreateOperationPayloadDataRelationships as ContentClaimsCreateOperationPayloadDataRelationships
from tidal.models.content_claims_create_operation_payload_data_relationships_claimed_resource import ContentClaimsCreateOperationPayloadDataRelationshipsClaimedResource as ContentClaimsCreateOperationPayloadDataRelationshipsClaimedResource
from tidal.models.content_claims_create_operation_payload_data_relationships_claimed_resource_data import ContentClaimsCreateOperationPayloadDataRelationshipsClaimedResourceData as ContentClaimsCreateOperationPayloadDataRelationshipsClaimedResourceData
from tidal.models.content_claims_create_operation_payload_data_relationships_claiming_artist import ContentClaimsCreateOperationPayloadDataRelationshipsClaimingArtist as ContentClaimsCreateOperationPayloadDataRelationshipsClaimingArtist
from tidal.models.content_claims_create_operation_payload_data_relationships_claiming_artist_data import ContentClaimsCreateOperationPayloadDataRelationshipsClaimingArtistData as ContentClaimsCreateOperationPayloadDataRelationshipsClaimingArtistData
from tidal.models.content_claims_create_single_resource_data_document import ContentClaimsCreateSingleResourceDataDocument as ContentClaimsCreateSingleResourceDataDocument
from tidal.models.content_claims_multi_resource_data_document import ContentClaimsMultiResourceDataDocument as ContentClaimsMultiResourceDataDocument
from tidal.models.content_claims_owners_multi_relationship_data_document import ContentClaimsOwnersMultiRelationshipDataDocument as ContentClaimsOwnersMultiRelationshipDataDocument
from tidal.models.content_claims_relationships import ContentClaimsRelationships as ContentClaimsRelationships
from tidal.models.content_claims_resource_object import ContentClaimsResourceObject as ContentClaimsResourceObject
from tidal.models.content_claims_single_resource_data_document import ContentClaimsSingleResourceDataDocument as ContentClaimsSingleResourceDataDocument
from tidal.models.copyright import Copyright as Copyright
from tidal.models.credits_artist_single_relationship_data_document import CreditsArtistSingleRelationshipDataDocument as CreditsArtistSingleRelationshipDataDocument
from tidal.models.credits_attributes import CreditsAttributes as CreditsAttributes
from tidal.models.credits_category_single_relationship_data_document import CreditsCategorySingleRelationshipDataDocument as CreditsCategorySingleRelationshipDataDocument
from tidal.models.credits_relationships import CreditsRelationships as CreditsRelationships
from tidal.models.credits_resource_object import CreditsResourceObject as CreditsResourceObject
from tidal.models.credits_single_resource_data_document import CreditsSingleResourceDataDocument as CreditsSingleResourceDataDocument
from tidal.models.default400_response_body import Default400ResponseBody as Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody as Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody as Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody as Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody as Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody as Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody as Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody as Default503ResponseBody
from tidal.models.download_link import DownloadLink as DownloadLink
from tidal.models.download_link_meta import DownloadLinkMeta as DownloadLinkMeta
from tidal.models.downloads_attributes import DownloadsAttributes as DownloadsAttributes
from tidal.models.downloads_multi_resource_data_document import DownloadsMultiResourceDataDocument as DownloadsMultiResourceDataDocument
from tidal.models.downloads_owners_multi_relationship_data_document import DownloadsOwnersMultiRelationshipDataDocument as DownloadsOwnersMultiRelationshipDataDocument
from tidal.models.downloads_relationships import DownloadsRelationships as DownloadsRelationships
from tidal.models.downloads_resource_object import DownloadsResourceObject as DownloadsResourceObject
from tidal.models.downloads_single_resource_data_document import DownloadsSingleResourceDataDocument as DownloadsSingleResourceDataDocument
from tidal.models.drm_data import DrmData as DrmData
from tidal.models.dsp_sharing_links_attributes import DspSharingLinksAttributes as DspSharingLinksAttributes
from tidal.models.dsp_sharing_links_multi_resource_data_document import DspSharingLinksMultiResourceDataDocument as DspSharingLinksMultiResourceDataDocument
from tidal.models.dsp_sharing_links_relationships import DspSharingLinksRelationships as DspSharingLinksRelationships
from tidal.models.dsp_sharing_links_resource_object import DspSharingLinksResourceObject as DspSharingLinksResourceObject
from tidal.models.dsp_sharing_links_subject_resource_identifier import DspSharingLinksSubjectResourceIdentifier as DspSharingLinksSubjectResourceIdentifier
from tidal.models.dsp_sharing_links_subject_resource_identifier_meta import DspSharingLinksSubjectResourceIdentifierMeta as DspSharingLinksSubjectResourceIdentifierMeta
from tidal.models.dsp_sharing_links_subject_single_relationship_data_document import DspSharingLinksSubjectSingleRelationshipDataDocument as DspSharingLinksSubjectSingleRelationshipDataDocument
from tidal.models.dynamic_modules_attributes import DynamicModulesAttributes as DynamicModulesAttributes
from tidal.models.dynamic_modules_items_multi_relationship_data_document import DynamicModulesItemsMultiRelationshipDataDocument as DynamicModulesItemsMultiRelationshipDataDocument
from tidal.models.dynamic_modules_items_resource_identifier import DynamicModulesItemsResourceIdentifier as DynamicModulesItemsResourceIdentifier
from tidal.models.dynamic_modules_items_resource_identifier_meta import DynamicModulesItemsResourceIdentifierMeta as DynamicModulesItemsResourceIdentifierMeta
from tidal.models.dynamic_modules_multi_resource_data_document import DynamicModulesMultiResourceDataDocument as DynamicModulesMultiResourceDataDocument
from tidal.models.dynamic_modules_relationships import DynamicModulesRelationships as DynamicModulesRelationships
from tidal.models.dynamic_modules_resource_object import DynamicModulesResourceObject as DynamicModulesResourceObject
from tidal.models.dynamic_modules_seed_item_resource_identifier import DynamicModulesSeedItemResourceIdentifier as DynamicModulesSeedItemResourceIdentifier
from tidal.models.dynamic_modules_seed_item_resource_identifier_meta import DynamicModulesSeedItemResourceIdentifierMeta as DynamicModulesSeedItemResourceIdentifierMeta
from tidal.models.dynamic_modules_seed_item_single_relationship_data_document import DynamicModulesSeedItemSingleRelationshipDataDocument as DynamicModulesSeedItemSingleRelationshipDataDocument
from tidal.models.dynamic_modules_single_resource_data_document import DynamicModulesSingleResourceDataDocument as DynamicModulesSingleResourceDataDocument
from tidal.models.dynamic_pages_attributes import DynamicPagesAttributes as DynamicPagesAttributes
from tidal.models.dynamic_pages_modules_multi_relationship_data_document import DynamicPagesModulesMultiRelationshipDataDocument as DynamicPagesModulesMultiRelationshipDataDocument
from tidal.models.dynamic_pages_multi_resource_data_document import DynamicPagesMultiResourceDataDocument as DynamicPagesMultiResourceDataDocument
from tidal.models.dynamic_pages_relationships import DynamicPagesRelationships as DynamicPagesRelationships
from tidal.models.dynamic_pages_resource_object import DynamicPagesResourceObject as DynamicPagesResourceObject
from tidal.models.dynamic_pages_subject_resource_identifier import DynamicPagesSubjectResourceIdentifier as DynamicPagesSubjectResourceIdentifier
from tidal.models.dynamic_pages_subject_resource_identifier_meta import DynamicPagesSubjectResourceIdentifierMeta as DynamicPagesSubjectResourceIdentifierMeta
from tidal.models.dynamic_pages_subject_single_relationship_data_document import DynamicPagesSubjectSingleRelationshipDataDocument as DynamicPagesSubjectSingleRelationshipDataDocument
from tidal.models.effective_role import EffectiveRole as EffectiveRole
from tidal.models.error_object import ErrorObject as ErrorObject
from tidal.models.error_object_source import ErrorObjectSource as ErrorObjectSource
from tidal.models.errors_document import ErrorsDocument as ErrorsDocument
from tidal.models.external_link import ExternalLink as ExternalLink
from tidal.models.external_link_meta import ExternalLinkMeta as ExternalLinkMeta
from tidal.models.external_link_payload import ExternalLinkPayload as ExternalLinkPayload
from tidal.models.file_status import FileStatus as FileStatus
from tidal.models.file_upload_link import FileUploadLink as FileUploadLink
from tidal.models.file_upload_link_meta import FileUploadLinkMeta as FileUploadLinkMeta
from tidal.models.folder_items_attributes import FolderItemsAttributes as FolderItemsAttributes
from tidal.models.folder_items_breadcrumb_multi_relationship_data_document import FolderItemsBreadcrumbMultiRelationshipDataDocument as FolderItemsBreadcrumbMultiRelationshipDataDocument
from tidal.models.folder_items_create_operation_payload import FolderItemsCreateOperationPayload as FolderItemsCreateOperationPayload
from tidal.models.folder_items_create_operation_payload_data import FolderItemsCreateOperationPayloadData as FolderItemsCreateOperationPayloadData
from tidal.models.folder_items_create_operation_payload_data_relationships import FolderItemsCreateOperationPayloadDataRelationships as FolderItemsCreateOperationPayloadDataRelationships
from tidal.models.folder_items_create_operation_payload_data_relationships_parent import FolderItemsCreateOperationPayloadDataRelationshipsParent as FolderItemsCreateOperationPayloadDataRelationshipsParent
from tidal.models.folder_items_create_operation_payload_data_relationships_parent_data import FolderItemsCreateOperationPayloadDataRelationshipsParentData as FolderItemsCreateOperationPayloadDataRelationshipsParentData
from tidal.models.folder_items_create_operation_payload_data_relationships_subject import FolderItemsCreateOperationPayloadDataRelationshipsSubject as FolderItemsCreateOperationPayloadDataRelationshipsSubject
from tidal.models.folder_items_create_operation_payload_data_relationships_subject_data import FolderItemsCreateOperationPayloadDataRelationshipsSubjectData as FolderItemsCreateOperationPayloadDataRelationshipsSubjectData
from tidal.models.folder_items_create_resource400_response_body import FolderItemsCreateResource400ResponseBody as FolderItemsCreateResource400ResponseBody
from tidal.models.folder_items_create_resource400_response_body_errors_inner import FolderItemsCreateResource400ResponseBodyErrorsInner as FolderItemsCreateResource400ResponseBodyErrorsInner
from tidal.models.folder_items_create_single_resource_data_document import FolderItemsCreateSingleResourceDataDocument as FolderItemsCreateSingleResourceDataDocument
from tidal.models.folder_items_multi_resource_data_document import FolderItemsMultiResourceDataDocument as FolderItemsMultiResourceDataDocument
from tidal.models.folder_items_owners_multi_relationship_data_document import FolderItemsOwnersMultiRelationshipDataDocument as FolderItemsOwnersMultiRelationshipDataDocument
from tidal.models.folder_items_parent_relationship_update_operation_payload import FolderItemsParentRelationshipUpdateOperationPayload as FolderItemsParentRelationshipUpdateOperationPayload
from tidal.models.folder_items_parent_relationship_update_operation_payload_data import FolderItemsParentRelationshipUpdateOperationPayloadData as FolderItemsParentRelationshipUpdateOperationPayloadData
from tidal.models.folder_items_parent_single_relationship_data_document import FolderItemsParentSingleRelationshipDataDocument as FolderItemsParentSingleRelationshipDataDocument
from tidal.models.folder_items_parent_update_resource_identifier import FolderItemsParentUpdateResourceIdentifier as FolderItemsParentUpdateResourceIdentifier
from tidal.models.folder_items_parent_update_single_data_relationship400_response_body import FolderItemsParentUpdateSingleDataRelationship400ResponseBody as FolderItemsParentUpdateSingleDataRelationship400ResponseBody
from tidal.models.folder_items_parent_update_single_relationship_data_document import FolderItemsParentUpdateSingleRelationshipDataDocument as FolderItemsParentUpdateSingleRelationshipDataDocument
from tidal.models.folder_items_relationships import FolderItemsRelationships as FolderItemsRelationships
from tidal.models.folder_items_resource_object import FolderItemsResourceObject as FolderItemsResourceObject
from tidal.models.folder_items_sharing_summary_single_relationship_data_document import FolderItemsSharingSummarySingleRelationshipDataDocument as FolderItemsSharingSummarySingleRelationshipDataDocument
from tidal.models.folder_items_single_resource_data_document import FolderItemsSingleResourceDataDocument as FolderItemsSingleResourceDataDocument
from tidal.models.folder_items_subject_resource_identifier import FolderItemsSubjectResourceIdentifier as FolderItemsSubjectResourceIdentifier
from tidal.models.folder_items_subject_resource_identifier_meta import FolderItemsSubjectResourceIdentifierMeta as FolderItemsSubjectResourceIdentifierMeta
from tidal.models.folder_items_subject_single_relationship_data_document import FolderItemsSubjectSingleRelationshipDataDocument as FolderItemsSubjectSingleRelationshipDataDocument
from tidal.models.folders_attributes import FoldersAttributes as FoldersAttributes
from tidal.models.folders_children_multi_relationship_data_document import FoldersChildrenMultiRelationshipDataDocument as FoldersChildrenMultiRelationshipDataDocument
from tidal.models.folders_create_operation_payload import FoldersCreateOperationPayload as FoldersCreateOperationPayload
from tidal.models.folders_create_operation_payload_data import FoldersCreateOperationPayloadData as FoldersCreateOperationPayloadData
from tidal.models.folders_create_operation_payload_data_attributes import FoldersCreateOperationPayloadDataAttributes as FoldersCreateOperationPayloadDataAttributes
from tidal.models.folders_create_operation_payload_data_relationships import FoldersCreateOperationPayloadDataRelationships as FoldersCreateOperationPayloadDataRelationships
from tidal.models.folders_create_operation_payload_data_relationships_parent import FoldersCreateOperationPayloadDataRelationshipsParent as FoldersCreateOperationPayloadDataRelationshipsParent
from tidal.models.folders_create_single_resource_data_document import FoldersCreateSingleResourceDataDocument as FoldersCreateSingleResourceDataDocument
from tidal.models.folders_delete_resource400_response_body import FoldersDeleteResource400ResponseBody as FoldersDeleteResource400ResponseBody
from tidal.models.folders_delete_resource400_response_body_errors_inner import FoldersDeleteResource400ResponseBodyErrorsInner as FoldersDeleteResource400ResponseBodyErrorsInner
from tidal.models.folders_multi_resource_data_document import FoldersMultiResourceDataDocument as FoldersMultiResourceDataDocument
from tidal.models.folders_owners_multi_relationship_data_document import FoldersOwnersMultiRelationshipDataDocument as FoldersOwnersMultiRelationshipDataDocument
from tidal.models.folders_parent_identifier import FoldersParentIdentifier as FoldersParentIdentifier
from tidal.models.folders_parent_single_relationship_data_document import FoldersParentSingleRelationshipDataDocument as FoldersParentSingleRelationshipDataDocument
from tidal.models.folders_preview_multi_relationship_data_document import FoldersPreviewMultiRelationshipDataDocument as FoldersPreviewMultiRelationshipDataDocument
from tidal.models.folders_relationships import FoldersRelationships as FoldersRelationships
from tidal.models.folders_resource_object import FoldersResourceObject as FoldersResourceObject
from tidal.models.folders_shares_multi_relationship_data_document import FoldersSharesMultiRelationshipDataDocument as FoldersSharesMultiRelationshipDataDocument
from tidal.models.folders_single_resource_data_document import FoldersSingleResourceDataDocument as FoldersSingleResourceDataDocument
from tidal.models.folders_update_operation_payload import FoldersUpdateOperationPayload as FoldersUpdateOperationPayload
from tidal.models.folders_update_operation_payload_data import FoldersUpdateOperationPayloadData as FoldersUpdateOperationPayloadData
from tidal.models.folders_update_operation_payload_data_attributes import FoldersUpdateOperationPayloadDataAttributes as FoldersUpdateOperationPayloadDataAttributes
from tidal.models.folders_update_resource400_response_body import FoldersUpdateResource400ResponseBody as FoldersUpdateResource400ResponseBody
from tidal.models.folders_update_single_resource_data_document import FoldersUpdateSingleResourceDataDocument as FoldersUpdateSingleResourceDataDocument
from tidal.models.genres_attributes import GenresAttributes as GenresAttributes
from tidal.models.genres_multi_resource_data_document import GenresMultiResourceDataDocument as GenresMultiResourceDataDocument
from tidal.models.genres_resource_object import GenresResourceObject as GenresResourceObject
from tidal.models.genres_single_resource_data_document import GenresSingleResourceDataDocument as GenresSingleResourceDataDocument
from tidal.models.groups_attributes import GroupsAttributes as GroupsAttributes
from tidal.models.groups_multi_resource_data_document import GroupsMultiResourceDataDocument as GroupsMultiResourceDataDocument
from tidal.models.groups_resource_object import GroupsResourceObject as GroupsResourceObject
from tidal.models.groups_single_resource_data_document import GroupsSingleResourceDataDocument as GroupsSingleResourceDataDocument
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody as Idempotency409ResponseBody
from tidal.models.idempotency409_response_body_errors_inner import Idempotency409ResponseBodyErrorsInner as Idempotency409ResponseBodyErrorsInner
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody as Idempotency422ResponseBody
from tidal.models.included_inner import IncludedInner as IncludedInner
from tidal.models.installations_attributes import InstallationsAttributes as InstallationsAttributes
from tidal.models.installations_create_operation_payload import InstallationsCreateOperationPayload as InstallationsCreateOperationPayload
from tidal.models.installations_create_operation_payload_data import InstallationsCreateOperationPayloadData as InstallationsCreateOperationPayloadData
from tidal.models.installations_create_operation_payload_data_attributes import InstallationsCreateOperationPayloadDataAttributes as InstallationsCreateOperationPayloadDataAttributes
from tidal.models.installations_create_single_resource_data_document import InstallationsCreateSingleResourceDataDocument as InstallationsCreateSingleResourceDataDocument
from tidal.models.installations_multi_resource_data_document import InstallationsMultiResourceDataDocument as InstallationsMultiResourceDataDocument
from tidal.models.installations_offline_inventory_item_identifier import InstallationsOfflineInventoryItemIdentifier as InstallationsOfflineInventoryItemIdentifier
from tidal.models.installations_offline_inventory_multi_relationship_data_document import InstallationsOfflineInventoryMultiRelationshipDataDocument as InstallationsOfflineInventoryMultiRelationshipDataDocument
from tidal.models.installations_offline_inventory_relationship_add_operation_payload import InstallationsOfflineInventoryRelationshipAddOperationPayload as InstallationsOfflineInventoryRelationshipAddOperationPayload
from tidal.models.installations_offline_inventory_relationship_remove_operation_payload import InstallationsOfflineInventoryRelationshipRemoveOperationPayload as InstallationsOfflineInventoryRelationshipRemoveOperationPayload
from tidal.models.installations_offline_inventory_resource_identifier import InstallationsOfflineInventoryResourceIdentifier as InstallationsOfflineInventoryResourceIdentifier
from tidal.models.installations_offline_inventory_resource_identifier_meta import InstallationsOfflineInventoryResourceIdentifierMeta as InstallationsOfflineInventoryResourceIdentifierMeta
from tidal.models.installations_owners_multi_relationship_data_document import InstallationsOwnersMultiRelationshipDataDocument as InstallationsOwnersMultiRelationshipDataDocument
from tidal.models.installations_relationships import InstallationsRelationships as InstallationsRelationships
from tidal.models.installations_resource_object import InstallationsResourceObject as InstallationsResourceObject
from tidal.models.installations_single_resource_data_document import InstallationsSingleResourceDataDocument as InstallationsSingleResourceDataDocument
from tidal.models.item import Item as Item
from tidal.models.item_artwork import ItemArtwork as ItemArtwork
from tidal.models.item_variation import ItemVariation as ItemVariation
from tidal.models.legacy_barcode_id import LegacyBarcodeId as LegacyBarcodeId
from tidal.models.legacy_source import LegacySource as LegacySource
from tidal.models.link_object import LinkObject as LinkObject
from tidal.models.links import Links as Links
from tidal.models.links_meta import LinksMeta as LinksMeta
from tidal.models.lyrics_attributes import LyricsAttributes as LyricsAttributes
from tidal.models.lyrics_create_operation_payload import LyricsCreateOperationPayload as LyricsCreateOperationPayload
from tidal.models.lyrics_create_operation_payload_data import LyricsCreateOperationPayloadData as LyricsCreateOperationPayloadData
from tidal.models.lyrics_create_operation_payload_data_attributes import LyricsCreateOperationPayloadDataAttributes as LyricsCreateOperationPayloadDataAttributes
from tidal.models.lyrics_create_operation_payload_data_relationships import LyricsCreateOperationPayloadDataRelationships as LyricsCreateOperationPayloadDataRelationships
from tidal.models.lyrics_create_operation_payload_data_relationships_track import LyricsCreateOperationPayloadDataRelationshipsTrack as LyricsCreateOperationPayloadDataRelationshipsTrack
from tidal.models.lyrics_create_operation_payload_data_relationships_track_data import LyricsCreateOperationPayloadDataRelationshipsTrackData as LyricsCreateOperationPayloadDataRelationshipsTrackData
from tidal.models.lyrics_create_operation_payload_meta import LyricsCreateOperationPayloadMeta as LyricsCreateOperationPayloadMeta
from tidal.models.lyrics_create_single_resource_data_document import LyricsCreateSingleResourceDataDocument as LyricsCreateSingleResourceDataDocument
from tidal.models.lyrics_owners_multi_relationship_data_document import LyricsOwnersMultiRelationshipDataDocument as LyricsOwnersMultiRelationshipDataDocument
from tidal.models.lyrics_provider import LyricsProvider as LyricsProvider
from tidal.models.lyrics_relationships import LyricsRelationships as LyricsRelationships
from tidal.models.lyrics_resource_object import LyricsResourceObject as LyricsResourceObject
from tidal.models.lyrics_single_resource_data_document import LyricsSingleResourceDataDocument as LyricsSingleResourceDataDocument
from tidal.models.lyrics_track_resource_identifier import LyricsTrackResourceIdentifier as LyricsTrackResourceIdentifier
from tidal.models.lyrics_track_resource_identifier_meta import LyricsTrackResourceIdentifierMeta as LyricsTrackResourceIdentifierMeta
from tidal.models.lyrics_track_single_relationship_data_document import LyricsTrackSingleRelationshipDataDocument as LyricsTrackSingleRelationshipDataDocument
from tidal.models.lyrics_update_operation_payload import LyricsUpdateOperationPayload as LyricsUpdateOperationPayload
from tidal.models.lyrics_update_operation_payload_data import LyricsUpdateOperationPayloadData as LyricsUpdateOperationPayloadData
from tidal.models.lyrics_update_operation_payload_data_attributes import LyricsUpdateOperationPayloadDataAttributes as LyricsUpdateOperationPayloadDataAttributes
from tidal.models.manual_artist_claims_attributes import ManualArtistClaimsAttributes as ManualArtistClaimsAttributes
from tidal.models.manual_artist_claims_create_operation_payload import ManualArtistClaimsCreateOperationPayload as ManualArtistClaimsCreateOperationPayload
from tidal.models.manual_artist_claims_create_operation_payload_data import ManualArtistClaimsCreateOperationPayloadData as ManualArtistClaimsCreateOperationPayloadData
from tidal.models.manual_artist_claims_create_operation_payload_data_attributes import ManualArtistClaimsCreateOperationPayloadDataAttributes as ManualArtistClaimsCreateOperationPayloadDataAttributes
from tidal.models.manual_artist_claims_create_single_resource_data_document import ManualArtistClaimsCreateSingleResourceDataDocument as ManualArtistClaimsCreateSingleResourceDataDocument
from tidal.models.manual_artist_claims_external_link import ManualArtistClaimsExternalLink as ManualArtistClaimsExternalLink
from tidal.models.manual_artist_claims_resource_object import ManualArtistClaimsResourceObject as ManualArtistClaimsResourceObject
from tidal.models.missing_terms_meta import MissingTermsMeta as MissingTermsMeta
from tidal.models.mutation_response_document import MutationResponseDocument as MutationResponseDocument
from tidal.models.offline_tasks_attributes import OfflineTasksAttributes as OfflineTasksAttributes
from tidal.models.offline_tasks_collection_resource_identifier import OfflineTasksCollectionResourceIdentifier as OfflineTasksCollectionResourceIdentifier
from tidal.models.offline_tasks_collection_resource_identifier_meta import OfflineTasksCollectionResourceIdentifierMeta as OfflineTasksCollectionResourceIdentifierMeta
from tidal.models.offline_tasks_collection_single_relationship_data_document import OfflineTasksCollectionSingleRelationshipDataDocument as OfflineTasksCollectionSingleRelationshipDataDocument
from tidal.models.offline_tasks_item_resource_identifier import OfflineTasksItemResourceIdentifier as OfflineTasksItemResourceIdentifier
from tidal.models.offline_tasks_item_resource_identifier_meta import OfflineTasksItemResourceIdentifierMeta as OfflineTasksItemResourceIdentifierMeta
from tidal.models.offline_tasks_item_single_relationship_data_document import OfflineTasksItemSingleRelationshipDataDocument as OfflineTasksItemSingleRelationshipDataDocument
from tidal.models.offline_tasks_multi_resource_data_document import OfflineTasksMultiResourceDataDocument as OfflineTasksMultiResourceDataDocument
from tidal.models.offline_tasks_owners_multi_relationship_data_document import OfflineTasksOwnersMultiRelationshipDataDocument as OfflineTasksOwnersMultiRelationshipDataDocument
from tidal.models.offline_tasks_relationships import OfflineTasksRelationships as OfflineTasksRelationships
from tidal.models.offline_tasks_resource_object import OfflineTasksResourceObject as OfflineTasksResourceObject
from tidal.models.offline_tasks_single_resource_data_document import OfflineTasksSingleResourceDataDocument as OfflineTasksSingleResourceDataDocument
from tidal.models.offline_tasks_update_operation_payload import OfflineTasksUpdateOperationPayload as OfflineTasksUpdateOperationPayload
from tidal.models.offline_tasks_update_operation_payload_data import OfflineTasksUpdateOperationPayloadData as OfflineTasksUpdateOperationPayloadData
from tidal.models.offline_tasks_update_operation_payload_data_attributes import OfflineTasksUpdateOperationPayloadDataAttributes as OfflineTasksUpdateOperationPayloadDataAttributes
from tidal.models.play_queues_attributes import PlayQueuesAttributes as PlayQueuesAttributes
from tidal.models.play_queues_change_event_stream_single_relationship_data_document import PlayQueuesChangeEventStreamSingleRelationshipDataDocument as PlayQueuesChangeEventStreamSingleRelationshipDataDocument
from tidal.models.play_queues_create_operation_payload import PlayQueuesCreateOperationPayload as PlayQueuesCreateOperationPayload
from tidal.models.play_queues_create_operation_payload_data import PlayQueuesCreateOperationPayloadData as PlayQueuesCreateOperationPayloadData
from tidal.models.play_queues_create_single_resource_data_document import PlayQueuesCreateSingleResourceDataDocument as PlayQueuesCreateSingleResourceDataDocument
from tidal.models.play_queues_create_single_resource_data_document_meta import PlayQueuesCreateSingleResourceDataDocumentMeta as PlayQueuesCreateSingleResourceDataDocumentMeta
from tidal.models.play_queues_current_relationship_update_operation_payload import PlayQueuesCurrentRelationshipUpdateOperationPayload as PlayQueuesCurrentRelationshipUpdateOperationPayload
from tidal.models.play_queues_current_relationship_update_operation_payload_data import PlayQueuesCurrentRelationshipUpdateOperationPayloadData as PlayQueuesCurrentRelationshipUpdateOperationPayloadData
from tidal.models.play_queues_current_relationship_update_operation_payload_data_meta import PlayQueuesCurrentRelationshipUpdateOperationPayloadDataMeta as PlayQueuesCurrentRelationshipUpdateOperationPayloadDataMeta
from tidal.models.play_queues_current_resource_identifier import PlayQueuesCurrentResourceIdentifier as PlayQueuesCurrentResourceIdentifier
from tidal.models.play_queues_current_resource_identifier_meta import PlayQueuesCurrentResourceIdentifierMeta as PlayQueuesCurrentResourceIdentifierMeta
from tidal.models.play_queues_current_single_relationship_data_document import PlayQueuesCurrentSingleRelationshipDataDocument as PlayQueuesCurrentSingleRelationshipDataDocument
from tidal.models.play_queues_current_update_resource_identifier import PlayQueuesCurrentUpdateResourceIdentifier as PlayQueuesCurrentUpdateResourceIdentifier
from tidal.models.play_queues_current_update_resource_identifier_meta import PlayQueuesCurrentUpdateResourceIdentifierMeta as PlayQueuesCurrentUpdateResourceIdentifierMeta
from tidal.models.play_queues_current_update_single_relationship_data_document import PlayQueuesCurrentUpdateSingleRelationshipDataDocument as PlayQueuesCurrentUpdateSingleRelationshipDataDocument
from tidal.models.play_queues_current_update_single_relationship_data_document_meta import PlayQueuesCurrentUpdateSingleRelationshipDataDocumentMeta as PlayQueuesCurrentUpdateSingleRelationshipDataDocumentMeta
from tidal.models.play_queues_future_add_multi_relationship_data_document import PlayQueuesFutureAddMultiRelationshipDataDocument as PlayQueuesFutureAddMultiRelationshipDataDocument
from tidal.models.play_queues_future_add_multi_relationship_data_document_meta import PlayQueuesFutureAddMultiRelationshipDataDocumentMeta as PlayQueuesFutureAddMultiRelationshipDataDocumentMeta
from tidal.models.play_queues_future_add_resource_identifier import PlayQueuesFutureAddResourceIdentifier as PlayQueuesFutureAddResourceIdentifier
from tidal.models.play_queues_future_multi_relationship_data_document import PlayQueuesFutureMultiRelationshipDataDocument as PlayQueuesFutureMultiRelationshipDataDocument
from tidal.models.play_queues_future_relationship_add_operation_payload import PlayQueuesFutureRelationshipAddOperationPayload as PlayQueuesFutureRelationshipAddOperationPayload
from tidal.models.play_queues_future_relationship_add_operation_payload_data import PlayQueuesFutureRelationshipAddOperationPayloadData as PlayQueuesFutureRelationshipAddOperationPayloadData
from tidal.models.play_queues_future_relationship_add_operation_payload_meta import PlayQueuesFutureRelationshipAddOperationPayloadMeta as PlayQueuesFutureRelationshipAddOperationPayloadMeta
from tidal.models.play_queues_future_relationship_remove_operation_payload import PlayQueuesFutureRelationshipRemoveOperationPayload as PlayQueuesFutureRelationshipRemoveOperationPayload
from tidal.models.play_queues_future_relationship_remove_operation_payload_data import PlayQueuesFutureRelationshipRemoveOperationPayloadData as PlayQueuesFutureRelationshipRemoveOperationPayloadData
from tidal.models.play_queues_future_relationship_remove_operation_payload_data_meta import PlayQueuesFutureRelationshipRemoveOperationPayloadDataMeta as PlayQueuesFutureRelationshipRemoveOperationPayloadDataMeta
from tidal.models.play_queues_future_relationship_source import PlayQueuesFutureRelationshipSource as PlayQueuesFutureRelationshipSource
from tidal.models.play_queues_future_relationship_update_operation_payload import PlayQueuesFutureRelationshipUpdateOperationPayload as PlayQueuesFutureRelationshipUpdateOperationPayload
from tidal.models.play_queues_future_relationship_update_operation_payload_data import PlayQueuesFutureRelationshipUpdateOperationPayloadData as PlayQueuesFutureRelationshipUpdateOperationPayloadData
from tidal.models.play_queues_future_relationship_update_operation_payload_data_meta import PlayQueuesFutureRelationshipUpdateOperationPayloadDataMeta as PlayQueuesFutureRelationshipUpdateOperationPayloadDataMeta
from tidal.models.play_queues_future_relationship_update_operation_payload_meta import PlayQueuesFutureRelationshipUpdateOperationPayloadMeta as PlayQueuesFutureRelationshipUpdateOperationPayloadMeta
from tidal.models.play_queues_future_resource_identifier import PlayQueuesFutureResourceIdentifier as PlayQueuesFutureResourceIdentifier
from tidal.models.play_queues_future_resource_identifier_meta import PlayQueuesFutureResourceIdentifierMeta as PlayQueuesFutureResourceIdentifierMeta
from tidal.models.play_queues_future_update_multi_relationship_data_document import PlayQueuesFutureUpdateMultiRelationshipDataDocument as PlayQueuesFutureUpdateMultiRelationshipDataDocument
from tidal.models.play_queues_future_update_multi_relationship_data_document_meta import PlayQueuesFutureUpdateMultiRelationshipDataDocumentMeta as PlayQueuesFutureUpdateMultiRelationshipDataDocumentMeta
from tidal.models.play_queues_future_update_resource_identifier import PlayQueuesFutureUpdateResourceIdentifier as PlayQueuesFutureUpdateResourceIdentifier
from tidal.models.play_queues_multi_resource_data_document import PlayQueuesMultiResourceDataDocument as PlayQueuesMultiResourceDataDocument
from tidal.models.play_queues_owners_multi_relationship_data_document import PlayQueuesOwnersMultiRelationshipDataDocument as PlayQueuesOwnersMultiRelationshipDataDocument
from tidal.models.play_queues_past_multi_relationship_data_document import PlayQueuesPastMultiRelationshipDataDocument as PlayQueuesPastMultiRelationshipDataDocument
from tidal.models.play_queues_past_resource_identifier import PlayQueuesPastResourceIdentifier as PlayQueuesPastResourceIdentifier
from tidal.models.play_queues_past_resource_identifier_meta import PlayQueuesPastResourceIdentifierMeta as PlayQueuesPastResourceIdentifierMeta
from tidal.models.play_queues_relationships import PlayQueuesRelationships as PlayQueuesRelationships
from tidal.models.play_queues_resource_object import PlayQueuesResourceObject as PlayQueuesResourceObject
from tidal.models.play_queues_single_resource_data_document import PlayQueuesSingleResourceDataDocument as PlayQueuesSingleResourceDataDocument
from tidal.models.play_queues_update_operation_current import PlayQueuesUpdateOperationCurrent as PlayQueuesUpdateOperationCurrent
from tidal.models.play_queues_update_operation_current_meta import PlayQueuesUpdateOperationCurrentMeta as PlayQueuesUpdateOperationCurrentMeta
from tidal.models.play_queues_update_operation_future import PlayQueuesUpdateOperationFuture as PlayQueuesUpdateOperationFuture
from tidal.models.play_queues_update_operation_future_data import PlayQueuesUpdateOperationFutureData as PlayQueuesUpdateOperationFutureData
from tidal.models.play_queues_update_operation_future_meta import PlayQueuesUpdateOperationFutureMeta as PlayQueuesUpdateOperationFutureMeta
from tidal.models.play_queues_update_operation_payload import PlayQueuesUpdateOperationPayload as PlayQueuesUpdateOperationPayload
from tidal.models.play_queues_update_operation_payload_data import PlayQueuesUpdateOperationPayloadData as PlayQueuesUpdateOperationPayloadData
from tidal.models.play_queues_update_operation_payload_data_attributes import PlayQueuesUpdateOperationPayloadDataAttributes as PlayQueuesUpdateOperationPayloadDataAttributes
from tidal.models.play_queues_update_operation_payload_data_relationships import PlayQueuesUpdateOperationPayloadDataRelationships as PlayQueuesUpdateOperationPayloadDataRelationships
from tidal.models.play_queues_update_single_resource_data_document import PlayQueuesUpdateSingleResourceDataDocument as PlayQueuesUpdateSingleResourceDataDocument
from tidal.models.play_queues_update_single_resource_data_document_meta import PlayQueuesUpdateSingleResourceDataDocumentMeta as PlayQueuesUpdateSingleResourceDataDocumentMeta
from tidal.models.playlist_generation_progress import PlaylistGenerationProgress as PlaylistGenerationProgress
from tidal.models.playlist_generation_schedules_attributes import PlaylistGenerationSchedulesAttributes as PlaylistGenerationSchedulesAttributes
from tidal.models.playlist_generation_schedules_create_operation_payload import PlaylistGenerationSchedulesCreateOperationPayload as PlaylistGenerationSchedulesCreateOperationPayload
from tidal.models.playlist_generation_schedules_create_operation_payload_data import PlaylistGenerationSchedulesCreateOperationPayloadData as PlaylistGenerationSchedulesCreateOperationPayloadData
from tidal.models.playlist_generation_schedules_create_operation_payload_data_attributes import PlaylistGenerationSchedulesCreateOperationPayloadDataAttributes as PlaylistGenerationSchedulesCreateOperationPayloadDataAttributes
from tidal.models.playlist_generation_schedules_create_operation_payload_data_relationships import PlaylistGenerationSchedulesCreateOperationPayloadDataRelationships as PlaylistGenerationSchedulesCreateOperationPayloadDataRelationships
from tidal.models.playlist_generation_schedules_create_operation_payload_data_relationships_playlist import PlaylistGenerationSchedulesCreateOperationPayloadDataRelationshipsPlaylist as PlaylistGenerationSchedulesCreateOperationPayloadDataRelationshipsPlaylist
from tidal.models.playlist_generation_schedules_create_operation_payload_data_relationships_playlist_data import PlaylistGenerationSchedulesCreateOperationPayloadDataRelationshipsPlaylistData as PlaylistGenerationSchedulesCreateOperationPayloadDataRelationshipsPlaylistData
from tidal.models.playlist_generation_schedules_create_resource403_response_body import PlaylistGenerationSchedulesCreateResource403ResponseBody as PlaylistGenerationSchedulesCreateResource403ResponseBody
from tidal.models.playlist_generation_schedules_create_resource403_response_body_errors_inner import PlaylistGenerationSchedulesCreateResource403ResponseBodyErrorsInner as PlaylistGenerationSchedulesCreateResource403ResponseBodyErrorsInner
from tidal.models.playlist_generation_schedules_create_single_resource_data_document import PlaylistGenerationSchedulesCreateSingleResourceDataDocument as PlaylistGenerationSchedulesCreateSingleResourceDataDocument
from tidal.models.playlist_generation_schedules_multi_resource_data_document import PlaylistGenerationSchedulesMultiResourceDataDocument as PlaylistGenerationSchedulesMultiResourceDataDocument
from tidal.models.playlist_generation_schedules_playlist_single_relationship_data_document import PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument as PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument
from tidal.models.playlist_generation_schedules_relationships import PlaylistGenerationSchedulesRelationships as PlaylistGenerationSchedulesRelationships
from tidal.models.playlist_generation_schedules_resource_object import PlaylistGenerationSchedulesResourceObject as PlaylistGenerationSchedulesResourceObject
from tidal.models.playlist_generation_schedules_single_resource_data_document import PlaylistGenerationSchedulesSingleResourceDataDocument as PlaylistGenerationSchedulesSingleResourceDataDocument
from tidal.models.playlist_generation_schedules_update_operation_payload import PlaylistGenerationSchedulesUpdateOperationPayload as PlaylistGenerationSchedulesUpdateOperationPayload
from tidal.models.playlist_generation_schedules_update_operation_payload_data import PlaylistGenerationSchedulesUpdateOperationPayloadData as PlaylistGenerationSchedulesUpdateOperationPayloadData
from tidal.models.playlist_generation_schedules_update_operation_payload_data_attributes import PlaylistGenerationSchedulesUpdateOperationPayloadDataAttributes as PlaylistGenerationSchedulesUpdateOperationPayloadDataAttributes
from tidal.models.playlist_generation_schedules_update_single_resource_data_document import PlaylistGenerationSchedulesUpdateSingleResourceDataDocument as PlaylistGenerationSchedulesUpdateSingleResourceDataDocument
from tidal.models.playlist_generations_attributes import PlaylistGenerationsAttributes as PlaylistGenerationsAttributes
from tidal.models.playlist_generations_base_generation_single_relationship_data_document import PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument as PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument
from tidal.models.playlist_generations_create_operation_payload import PlaylistGenerationsCreateOperationPayload as PlaylistGenerationsCreateOperationPayload
from tidal.models.playlist_generations_create_operation_payload_data import PlaylistGenerationsCreateOperationPayloadData as PlaylistGenerationsCreateOperationPayloadData
from tidal.models.playlist_generations_create_operation_payload_data_attributes import PlaylistGenerationsCreateOperationPayloadDataAttributes as PlaylistGenerationsCreateOperationPayloadDataAttributes
from tidal.models.playlist_generations_create_operation_payload_data_relationships import PlaylistGenerationsCreateOperationPayloadDataRelationships as PlaylistGenerationsCreateOperationPayloadDataRelationships
from tidal.models.playlist_generations_create_operation_payload_data_relationships_base_generation import PlaylistGenerationsCreateOperationPayloadDataRelationshipsBaseGeneration as PlaylistGenerationsCreateOperationPayloadDataRelationshipsBaseGeneration
from tidal.models.playlist_generations_create_operation_payload_data_relationships_base_generation_data import PlaylistGenerationsCreateOperationPayloadDataRelationshipsBaseGenerationData as PlaylistGenerationsCreateOperationPayloadDataRelationshipsBaseGenerationData
from tidal.models.playlist_generations_create_operation_payload_data_relationships_playlist import PlaylistGenerationsCreateOperationPayloadDataRelationshipsPlaylist as PlaylistGenerationsCreateOperationPayloadDataRelationshipsPlaylist
from tidal.models.playlist_generations_create_operation_payload_data_relationships_playlist_data import PlaylistGenerationsCreateOperationPayloadDataRelationshipsPlaylistData as PlaylistGenerationsCreateOperationPayloadDataRelationshipsPlaylistData
from tidal.models.playlist_generations_create_resource409_response_body import PlaylistGenerationsCreateResource409ResponseBody as PlaylistGenerationsCreateResource409ResponseBody
from tidal.models.playlist_generations_create_resource409_response_body_errors_inner import PlaylistGenerationsCreateResource409ResponseBodyErrorsInner as PlaylistGenerationsCreateResource409ResponseBodyErrorsInner
from tidal.models.playlist_generations_create_single_resource_data_document import PlaylistGenerationsCreateSingleResourceDataDocument as PlaylistGenerationsCreateSingleResourceDataDocument
from tidal.models.playlist_generations_multi_resource_data_document import PlaylistGenerationsMultiResourceDataDocument as PlaylistGenerationsMultiResourceDataDocument
from tidal.models.playlist_generations_playlist_single_relationship_data_document import PlaylistGenerationsPlaylistSingleRelationshipDataDocument as PlaylistGenerationsPlaylistSingleRelationshipDataDocument
from tidal.models.playlist_generations_relationships import PlaylistGenerationsRelationships as PlaylistGenerationsRelationships
from tidal.models.playlist_generations_resource_object import PlaylistGenerationsResourceObject as PlaylistGenerationsResourceObject
from tidal.models.playlist_generations_single_resource_data_document import PlaylistGenerationsSingleResourceDataDocument as PlaylistGenerationsSingleResourceDataDocument
from tidal.models.playlist_generations_track_preferences_add_multi_data_relationship_with_response409_response_body import PlaylistGenerationsTrackPreferencesAddMultiDataRelationshipWithResponse409ResponseBody as PlaylistGenerationsTrackPreferencesAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.playlist_generations_track_preferences_add_multi_relationship_data_document import PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocument as PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocument
from tidal.models.playlist_generations_track_preferences_add_multi_relationship_data_document_meta import PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocumentMeta as PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocumentMeta
from tidal.models.playlist_generations_track_preferences_add_resource_identifier import PlaylistGenerationsTrackPreferencesAddResourceIdentifier as PlaylistGenerationsTrackPreferencesAddResourceIdentifier
from tidal.models.playlist_generations_track_preferences_add_resource_identifier_meta import PlaylistGenerationsTrackPreferencesAddResourceIdentifierMeta as PlaylistGenerationsTrackPreferencesAddResourceIdentifierMeta
from tidal.models.playlist_generations_track_preferences_multi_relationship_data_document import PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument as PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument
from tidal.models.playlist_generations_track_preferences_multi_relationship_data_document_meta import PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocumentMeta as PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocumentMeta
from tidal.models.playlist_generations_track_preferences_relationship_add_operation_payload import PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload as PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload
from tidal.models.playlist_generations_track_preferences_relationship_payload_data import PlaylistGenerationsTrackPreferencesRelationshipPayloadData as PlaylistGenerationsTrackPreferencesRelationshipPayloadData
from tidal.models.playlist_generations_track_preferences_relationship_payload_data_meta import PlaylistGenerationsTrackPreferencesRelationshipPayloadDataMeta as PlaylistGenerationsTrackPreferencesRelationshipPayloadDataMeta
from tidal.models.playlist_generations_track_preferences_relationship_payload_meta import PlaylistGenerationsTrackPreferencesRelationshipPayloadMeta as PlaylistGenerationsTrackPreferencesRelationshipPayloadMeta
from tidal.models.playlist_generations_track_preferences_relationship_remove_operation_payload import PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload as PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload
from tidal.models.playlist_generations_track_preferences_relationship_remove_operation_payload_data import PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayloadData as PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayloadData
from tidal.models.playlist_generations_track_preferences_relationship_update_operation_payload import PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload as PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload
from tidal.models.playlist_generations_track_preferences_relationship_update_operation_payload_meta import PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayloadMeta as PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayloadMeta
from tidal.models.playlist_generations_track_preferences_remove_multi_data_relationship409_response_body import PlaylistGenerationsTrackPreferencesRemoveMultiDataRelationship409ResponseBody as PlaylistGenerationsTrackPreferencesRemoveMultiDataRelationship409ResponseBody
from tidal.models.playlist_generations_track_preferences_resource_identifier import PlaylistGenerationsTrackPreferencesResourceIdentifier as PlaylistGenerationsTrackPreferencesResourceIdentifier
from tidal.models.playlist_generations_track_preferences_resource_identifier_meta import PlaylistGenerationsTrackPreferencesResourceIdentifierMeta as PlaylistGenerationsTrackPreferencesResourceIdentifierMeta
from tidal.models.playlist_generations_track_preferences_update_multi_data_relationship409_response_body import PlaylistGenerationsTrackPreferencesUpdateMultiDataRelationship409ResponseBody as PlaylistGenerationsTrackPreferencesUpdateMultiDataRelationship409ResponseBody
from tidal.models.playlist_generations_track_preferences_update_multi_relationship_data_document import PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocument as PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocument
from tidal.models.playlist_generations_track_preferences_update_multi_relationship_data_document_meta import PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocumentMeta as PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocumentMeta
from tidal.models.playlist_generations_track_preferences_update_resource_identifier import PlaylistGenerationsTrackPreferencesUpdateResourceIdentifier as PlaylistGenerationsTrackPreferencesUpdateResourceIdentifier
from tidal.models.playlist_generations_track_preferences_update_resource_identifier_meta import PlaylistGenerationsTrackPreferencesUpdateResourceIdentifierMeta as PlaylistGenerationsTrackPreferencesUpdateResourceIdentifierMeta
from tidal.models.playlists_attributes import PlaylistsAttributes as PlaylistsAttributes
from tidal.models.playlists_collaborator_profiles_multi_relationship_data_document import PlaylistsCollaboratorProfilesMultiRelationshipDataDocument as PlaylistsCollaboratorProfilesMultiRelationshipDataDocument
from tidal.models.playlists_collaborator_profiles_relationship_remove_operation_payload import PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload as PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload
from tidal.models.playlists_collaborator_profiles_relationship_remove_operation_payload_data import PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayloadData as PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayloadData
from tidal.models.playlists_collaborators_multi_relationship_data_document import PlaylistsCollaboratorsMultiRelationshipDataDocument as PlaylistsCollaboratorsMultiRelationshipDataDocument
from tidal.models.playlists_cover_art_multi_relationship_data_document import PlaylistsCoverArtMultiRelationshipDataDocument as PlaylistsCoverArtMultiRelationshipDataDocument
from tidal.models.playlists_cover_art_relationship_update_operation_payload import PlaylistsCoverArtRelationshipUpdateOperationPayload as PlaylistsCoverArtRelationshipUpdateOperationPayload
from tidal.models.playlists_cover_art_relationship_update_operation_payload_data import PlaylistsCoverArtRelationshipUpdateOperationPayloadData as PlaylistsCoverArtRelationshipUpdateOperationPayloadData
from tidal.models.playlists_create_operation_payload import PlaylistsCreateOperationPayload as PlaylistsCreateOperationPayload
from tidal.models.playlists_create_operation_payload_data import PlaylistsCreateOperationPayloadData as PlaylistsCreateOperationPayloadData
from tidal.models.playlists_create_operation_payload_data_attributes import PlaylistsCreateOperationPayloadDataAttributes as PlaylistsCreateOperationPayloadDataAttributes
from tidal.models.playlists_create_single_resource_data_document import PlaylistsCreateSingleResourceDataDocument as PlaylistsCreateSingleResourceDataDocument
from tidal.models.playlists_curators_multi_relationship_data_document import PlaylistsCuratorsMultiRelationshipDataDocument as PlaylistsCuratorsMultiRelationshipDataDocument
from tidal.models.playlists_items_add_multi_data_relationship_with_response409_response_body import PlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBody as PlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.playlists_items_add_multi_data_relationship_with_response409_response_body_errors_inner import PlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner as PlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner
from tidal.models.playlists_items_add_multi_relationship_data_document import PlaylistsItemsAddMultiRelationshipDataDocument as PlaylistsItemsAddMultiRelationshipDataDocument
from tidal.models.playlists_items_add_multi_relationship_data_document_meta import PlaylistsItemsAddMultiRelationshipDataDocumentMeta as PlaylistsItemsAddMultiRelationshipDataDocumentMeta
from tidal.models.playlists_items_add_resource_identifier import PlaylistsItemsAddResourceIdentifier as PlaylistsItemsAddResourceIdentifier
from tidal.models.playlists_items_add_resource_identifier_meta import PlaylistsItemsAddResourceIdentifierMeta as PlaylistsItemsAddResourceIdentifierMeta
from tidal.models.playlists_items_multi_relationship_data_document import PlaylistsItemsMultiRelationshipDataDocument as PlaylistsItemsMultiRelationshipDataDocument
from tidal.models.playlists_items_relationship_add_operation_payload import PlaylistsItemsRelationshipAddOperationPayload as PlaylistsItemsRelationshipAddOperationPayload
from tidal.models.playlists_items_relationship_add_operation_payload_data import PlaylistsItemsRelationshipAddOperationPayloadData as PlaylistsItemsRelationshipAddOperationPayloadData
from tidal.models.playlists_items_relationship_add_operation_payload_data_meta import PlaylistsItemsRelationshipAddOperationPayloadDataMeta as PlaylistsItemsRelationshipAddOperationPayloadDataMeta
from tidal.models.playlists_items_relationship_add_operation_payload_meta import PlaylistsItemsRelationshipAddOperationPayloadMeta as PlaylistsItemsRelationshipAddOperationPayloadMeta
from tidal.models.playlists_items_relationship_add_operation_response_meta_skipped_item import PlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem as PlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem
from tidal.models.playlists_items_relationship_remove_operation_payload import PlaylistsItemsRelationshipRemoveOperationPayload as PlaylistsItemsRelationshipRemoveOperationPayload
from tidal.models.playlists_items_relationship_remove_operation_payload_data import PlaylistsItemsRelationshipRemoveOperationPayloadData as PlaylistsItemsRelationshipRemoveOperationPayloadData
from tidal.models.playlists_items_relationship_remove_operation_payload_data_meta import PlaylistsItemsRelationshipRemoveOperationPayloadDataMeta as PlaylistsItemsRelationshipRemoveOperationPayloadDataMeta
from tidal.models.playlists_items_relationship_update_operation_payload import PlaylistsItemsRelationshipUpdateOperationPayload as PlaylistsItemsRelationshipUpdateOperationPayload
from tidal.models.playlists_items_relationship_update_operation_payload_data import PlaylistsItemsRelationshipUpdateOperationPayloadData as PlaylistsItemsRelationshipUpdateOperationPayloadData
from tidal.models.playlists_items_relationship_update_operation_payload_data_meta import PlaylistsItemsRelationshipUpdateOperationPayloadDataMeta as PlaylistsItemsRelationshipUpdateOperationPayloadDataMeta
from tidal.models.playlists_items_relationship_update_operation_payload_meta import PlaylistsItemsRelationshipUpdateOperationPayloadMeta as PlaylistsItemsRelationshipUpdateOperationPayloadMeta
from tidal.models.playlists_items_relationship_update_operation_payload_meta_any_of import PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf as PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf
from tidal.models.playlists_items_relationship_update_operation_payload_meta_any_of1 import PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf1 as PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf1
from tidal.models.playlists_items_resource_identifier import PlaylistsItemsResourceIdentifier as PlaylistsItemsResourceIdentifier
from tidal.models.playlists_items_resource_identifier_meta import PlaylistsItemsResourceIdentifierMeta as PlaylistsItemsResourceIdentifierMeta
from tidal.models.playlists_multi_resource_data_document import PlaylistsMultiResourceDataDocument as PlaylistsMultiResourceDataDocument
from tidal.models.playlists_owner_profiles_multi_relationship_data_document import PlaylistsOwnerProfilesMultiRelationshipDataDocument as PlaylistsOwnerProfilesMultiRelationshipDataDocument
from tidal.models.playlists_owners_multi_relationship_data_document import PlaylistsOwnersMultiRelationshipDataDocument as PlaylistsOwnersMultiRelationshipDataDocument
from tidal.models.playlists_relationships import PlaylistsRelationships as PlaylistsRelationships
from tidal.models.playlists_resource_object import PlaylistsResourceObject as PlaylistsResourceObject
from tidal.models.playlists_single_resource_data_document import PlaylistsSingleResourceDataDocument as PlaylistsSingleResourceDataDocument
from tidal.models.playlists_suggested_cover_arts_multi_relationship_data_document import PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument as PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument
from tidal.models.playlists_suggested_cover_arts_resource_identifier import PlaylistsSuggestedCoverArtsResourceIdentifier as PlaylistsSuggestedCoverArtsResourceIdentifier
from tidal.models.playlists_suggested_cover_arts_resource_identifier_meta import PlaylistsSuggestedCoverArtsResourceIdentifierMeta as PlaylistsSuggestedCoverArtsResourceIdentifierMeta
from tidal.models.playlists_update_operation_payload import PlaylistsUpdateOperationPayload as PlaylistsUpdateOperationPayload
from tidal.models.playlists_update_operation_payload_data import PlaylistsUpdateOperationPayloadData as PlaylistsUpdateOperationPayloadData
from tidal.models.playlists_update_operation_payload_data_attributes import PlaylistsUpdateOperationPayloadDataAttributes as PlaylistsUpdateOperationPayloadDataAttributes
from tidal.models.playlists_update_single_resource_data_document import PlaylistsUpdateSingleResourceDataDocument as PlaylistsUpdateSingleResourceDataDocument
from tidal.models.price_configurations_attributes import PriceConfigurationsAttributes as PriceConfigurationsAttributes
from tidal.models.price_configurations_create_operation_payload import PriceConfigurationsCreateOperationPayload as PriceConfigurationsCreateOperationPayload
from tidal.models.price_configurations_create_operation_payload_data import PriceConfigurationsCreateOperationPayloadData as PriceConfigurationsCreateOperationPayloadData
from tidal.models.price_configurations_create_operation_payload_data_attributes import PriceConfigurationsCreateOperationPayloadDataAttributes as PriceConfigurationsCreateOperationPayloadDataAttributes
from tidal.models.price_configurations_create_operation_payload_data_relationships import PriceConfigurationsCreateOperationPayloadDataRelationships as PriceConfigurationsCreateOperationPayloadDataRelationships
from tidal.models.price_configurations_create_operation_payload_data_relationships_subjects import PriceConfigurationsCreateOperationPayloadDataRelationshipsSubjects as PriceConfigurationsCreateOperationPayloadDataRelationshipsSubjects
from tidal.models.price_configurations_create_operation_payload_subjects import PriceConfigurationsCreateOperationPayloadSubjects as PriceConfigurationsCreateOperationPayloadSubjects
from tidal.models.price_configurations_create_single_resource_data_document import PriceConfigurationsCreateSingleResourceDataDocument as PriceConfigurationsCreateSingleResourceDataDocument
from tidal.models.price_configurations_multi_resource_data_document import PriceConfigurationsMultiResourceDataDocument as PriceConfigurationsMultiResourceDataDocument
from tidal.models.price_configurations_resource_object import PriceConfigurationsResourceObject as PriceConfigurationsResourceObject
from tidal.models.price_configurations_single_resource_data_document import PriceConfigurationsSingleResourceDataDocument as PriceConfigurationsSingleResourceDataDocument
from tidal.models.provider_owners_attributes import ProviderOwnersAttributes as ProviderOwnersAttributes
from tidal.models.provider_owners_multi_resource_data_document import ProviderOwnersMultiResourceDataDocument as ProviderOwnersMultiResourceDataDocument
from tidal.models.provider_owners_owners_multi_relationship_data_document import ProviderOwnersOwnersMultiRelationshipDataDocument as ProviderOwnersOwnersMultiRelationshipDataDocument
from tidal.models.provider_owners_provider_single_relationship_data_document import ProviderOwnersProviderSingleRelationshipDataDocument as ProviderOwnersProviderSingleRelationshipDataDocument
from tidal.models.provider_owners_relationships import ProviderOwnersRelationships as ProviderOwnersRelationships
from tidal.models.provider_owners_resource_object import ProviderOwnersResourceObject as ProviderOwnersResourceObject
from tidal.models.provider_product_infos_attributes import ProviderProductInfosAttributes as ProviderProductInfosAttributes
from tidal.models.provider_product_infos_multi_resource_data_document import ProviderProductInfosMultiResourceDataDocument as ProviderProductInfosMultiResourceDataDocument
from tidal.models.provider_product_infos_provider_single_relationship_data_document import ProviderProductInfosProviderSingleRelationshipDataDocument as ProviderProductInfosProviderSingleRelationshipDataDocument
from tidal.models.provider_product_infos_relationships import ProviderProductInfosRelationships as ProviderProductInfosRelationships
from tidal.models.provider_product_infos_resource_object import ProviderProductInfosResourceObject as ProviderProductInfosResourceObject
from tidal.models.provider_product_infos_subject_resource_identifier import ProviderProductInfosSubjectResourceIdentifier as ProviderProductInfosSubjectResourceIdentifier
from tidal.models.provider_product_infos_subject_resource_identifier_meta import ProviderProductInfosSubjectResourceIdentifierMeta as ProviderProductInfosSubjectResourceIdentifierMeta
from tidal.models.provider_product_infos_subject_single_relationship_data_document import ProviderProductInfosSubjectSingleRelationshipDataDocument as ProviderProductInfosSubjectSingleRelationshipDataDocument
from tidal.models.providers_attributes import ProvidersAttributes as ProvidersAttributes
from tidal.models.providers_resource_object import ProvidersResourceObject as ProvidersResourceObject
from tidal.models.providers_single_resource_data_document import ProvidersSingleResourceDataDocument as ProvidersSingleResourceDataDocument
from tidal.models.purchases_attributes import PurchasesAttributes as PurchasesAttributes
from tidal.models.purchases_multi_resource_data_document import PurchasesMultiResourceDataDocument as PurchasesMultiResourceDataDocument
from tidal.models.purchases_owners_multi_relationship_data_document import PurchasesOwnersMultiRelationshipDataDocument as PurchasesOwnersMultiRelationshipDataDocument
from tidal.models.purchases_relationships import PurchasesRelationships as PurchasesRelationships
from tidal.models.purchases_resource_object import PurchasesResourceObject as PurchasesResourceObject
from tidal.models.purchases_subject_resource_identifier import PurchasesSubjectResourceIdentifier as PurchasesSubjectResourceIdentifier
from tidal.models.purchases_subject_resource_identifier_meta import PurchasesSubjectResourceIdentifierMeta as PurchasesSubjectResourceIdentifierMeta
from tidal.models.purchases_subject_single_relationship_data_document import PurchasesSubjectSingleRelationshipDataDocument as PurchasesSubjectSingleRelationshipDataDocument
from tidal.models.reaction_summaries_attributes import ReactionSummariesAttributes as ReactionSummariesAttributes
from tidal.models.reaction_summaries_multi_resource_data_document import ReactionSummariesMultiResourceDataDocument as ReactionSummariesMultiResourceDataDocument
from tidal.models.reaction_summaries_relationships import ReactionSummariesRelationships as ReactionSummariesRelationships
from tidal.models.reaction_summaries_resource_object import ReactionSummariesResourceObject as ReactionSummariesResourceObject
from tidal.models.reaction_summaries_subject_single_relationship_data_document import ReactionSummariesSubjectSingleRelationshipDataDocument as ReactionSummariesSubjectSingleRelationshipDataDocument
from tidal.models.reactions_attributes import ReactionsAttributes as ReactionsAttributes
from tidal.models.reactions_author_single_relationship_data_document import ReactionsAuthorSingleRelationshipDataDocument as ReactionsAuthorSingleRelationshipDataDocument
from tidal.models.reactions_create_operation_payload import ReactionsCreateOperationPayload as ReactionsCreateOperationPayload
from tidal.models.reactions_create_operation_payload_data import ReactionsCreateOperationPayloadData as ReactionsCreateOperationPayloadData
from tidal.models.reactions_create_operation_payload_data_attributes import ReactionsCreateOperationPayloadDataAttributes as ReactionsCreateOperationPayloadDataAttributes
from tidal.models.reactions_create_operation_payload_data_relationships import ReactionsCreateOperationPayloadDataRelationships as ReactionsCreateOperationPayloadDataRelationships
from tidal.models.reactions_create_operation_payload_data_relationships_subject import ReactionsCreateOperationPayloadDataRelationshipsSubject as ReactionsCreateOperationPayloadDataRelationshipsSubject
from tidal.models.reactions_create_operation_payload_data_relationships_subject_data import ReactionsCreateOperationPayloadDataRelationshipsSubjectData as ReactionsCreateOperationPayloadDataRelationshipsSubjectData
from tidal.models.reactions_create_single_resource_data_document import ReactionsCreateSingleResourceDataDocument as ReactionsCreateSingleResourceDataDocument
from tidal.models.reactions_multi_resource_data_document import ReactionsMultiResourceDataDocument as ReactionsMultiResourceDataDocument
from tidal.models.reactions_owners_multi_relationship_data_document import ReactionsOwnersMultiRelationshipDataDocument as ReactionsOwnersMultiRelationshipDataDocument
from tidal.models.reactions_relationships import ReactionsRelationships as ReactionsRelationships
from tidal.models.reactions_resource_object import ReactionsResourceObject as ReactionsResourceObject
from tidal.models.reactions_subject_single_relationship_data_document import ReactionsSubjectSingleRelationshipDataDocument as ReactionsSubjectSingleRelationshipDataDocument
from tidal.models.replacement_original_identifier import ReplacementOriginalIdentifier as ReplacementOriginalIdentifier
from tidal.models.replacement_provenance import ReplacementProvenance as ReplacementProvenance
from tidal.models.resource_grant_invitations_attributes import ResourceGrantInvitationsAttributes as ResourceGrantInvitationsAttributes
from tidal.models.resource_grant_invitations_create_operation_payload import ResourceGrantInvitationsCreateOperationPayload as ResourceGrantInvitationsCreateOperationPayload
from tidal.models.resource_grant_invitations_create_operation_payload_data import ResourceGrantInvitationsCreateOperationPayloadData as ResourceGrantInvitationsCreateOperationPayloadData
from tidal.models.resource_grant_invitations_create_operation_payload_data_attributes import ResourceGrantInvitationsCreateOperationPayloadDataAttributes as ResourceGrantInvitationsCreateOperationPayloadDataAttributes
from tidal.models.resource_grant_invitations_create_operation_payload_data_relationships import ResourceGrantInvitationsCreateOperationPayloadDataRelationships as ResourceGrantInvitationsCreateOperationPayloadDataRelationships
from tidal.models.resource_grant_invitations_create_operation_payload_data_relationships_subject import ResourceGrantInvitationsCreateOperationPayloadDataRelationshipsSubject as ResourceGrantInvitationsCreateOperationPayloadDataRelationshipsSubject
from tidal.models.resource_grant_invitations_create_operation_payload_data_relationships_subject_data import ResourceGrantInvitationsCreateOperationPayloadDataRelationshipsSubjectData as ResourceGrantInvitationsCreateOperationPayloadDataRelationshipsSubjectData
from tidal.models.resource_grant_invitations_create_single_resource_data_document import ResourceGrantInvitationsCreateSingleResourceDataDocument as ResourceGrantInvitationsCreateSingleResourceDataDocument
from tidal.models.resource_grant_invitations_multi_resource_data_document import ResourceGrantInvitationsMultiResourceDataDocument as ResourceGrantInvitationsMultiResourceDataDocument
from tidal.models.resource_grant_invitations_owners_multi_relationship_data_document import ResourceGrantInvitationsOwnersMultiRelationshipDataDocument as ResourceGrantInvitationsOwnersMultiRelationshipDataDocument
from tidal.models.resource_grant_invitations_preview_grant_single_relationship_data_document import ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument as ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument
from tidal.models.resource_grant_invitations_relationships import ResourceGrantInvitationsRelationships as ResourceGrantInvitationsRelationships
from tidal.models.resource_grant_invitations_resource_object import ResourceGrantInvitationsResourceObject as ResourceGrantInvitationsResourceObject
from tidal.models.resource_grant_invitations_single_resource_data_document import ResourceGrantInvitationsSingleResourceDataDocument as ResourceGrantInvitationsSingleResourceDataDocument
from tidal.models.resource_grant_invitations_subject_resource_identifier import ResourceGrantInvitationsSubjectResourceIdentifier as ResourceGrantInvitationsSubjectResourceIdentifier
from tidal.models.resource_grant_invitations_subject_resource_identifier_meta import ResourceGrantInvitationsSubjectResourceIdentifierMeta as ResourceGrantInvitationsSubjectResourceIdentifierMeta
from tidal.models.resource_grant_invitations_subject_single_relationship_data_document import ResourceGrantInvitationsSubjectSingleRelationshipDataDocument as ResourceGrantInvitationsSubjectSingleRelationshipDataDocument
from tidal.models.resource_grant_invitations_update_operation_payload import ResourceGrantInvitationsUpdateOperationPayload as ResourceGrantInvitationsUpdateOperationPayload
from tidal.models.resource_grant_invitations_update_operation_payload_data import ResourceGrantInvitationsUpdateOperationPayloadData as ResourceGrantInvitationsUpdateOperationPayloadData
from tidal.models.resource_grant_invitations_update_operation_payload_data_attributes import ResourceGrantInvitationsUpdateOperationPayloadDataAttributes as ResourceGrantInvitationsUpdateOperationPayloadDataAttributes
from tidal.models.resource_grant_invitations_update_single_resource_data_document import ResourceGrantInvitationsUpdateSingleResourceDataDocument as ResourceGrantInvitationsUpdateSingleResourceDataDocument
from tidal.models.resource_grants_attributes import ResourceGrantsAttributes as ResourceGrantsAttributes
from tidal.models.resource_grants_create_operation_payload import ResourceGrantsCreateOperationPayload as ResourceGrantsCreateOperationPayload
from tidal.models.resource_grants_create_operation_payload_data import ResourceGrantsCreateOperationPayloadData as ResourceGrantsCreateOperationPayloadData
from tidal.models.resource_grants_create_operation_payload_data_attributes import ResourceGrantsCreateOperationPayloadDataAttributes as ResourceGrantsCreateOperationPayloadDataAttributes
from tidal.models.resource_grants_create_operation_payload_data_relationships import ResourceGrantsCreateOperationPayloadDataRelationships as ResourceGrantsCreateOperationPayloadDataRelationships
from tidal.models.resource_grants_create_operation_payload_meta import ResourceGrantsCreateOperationPayloadMeta as ResourceGrantsCreateOperationPayloadMeta
from tidal.models.resource_grants_create_resource403_response_body import ResourceGrantsCreateResource403ResponseBody as ResourceGrantsCreateResource403ResponseBody
from tidal.models.resource_grants_create_resource403_response_body_errors_inner import ResourceGrantsCreateResource403ResponseBodyErrorsInner as ResourceGrantsCreateResource403ResponseBodyErrorsInner
from tidal.models.resource_grants_create_resource429_response_body import ResourceGrantsCreateResource429ResponseBody as ResourceGrantsCreateResource429ResponseBody
from tidal.models.resource_grants_create_resource429_response_body_errors_inner import ResourceGrantsCreateResource429ResponseBodyErrorsInner as ResourceGrantsCreateResource429ResponseBodyErrorsInner
from tidal.models.resource_grants_create_single_resource_data_document import ResourceGrantsCreateSingleResourceDataDocument as ResourceGrantsCreateSingleResourceDataDocument
from tidal.models.resource_grants_grantee import ResourceGrantsGrantee as ResourceGrantsGrantee
from tidal.models.resource_grants_grantee_linkage import ResourceGrantsGranteeLinkage as ResourceGrantsGranteeLinkage
from tidal.models.resource_grants_grantee_single_relationship_data_document import ResourceGrantsGranteeSingleRelationshipDataDocument as ResourceGrantsGranteeSingleRelationshipDataDocument
from tidal.models.resource_grants_invitation import ResourceGrantsInvitation as ResourceGrantsInvitation
from tidal.models.resource_grants_invitation_linkage import ResourceGrantsInvitationLinkage as ResourceGrantsInvitationLinkage
from tidal.models.resource_grants_invitation_single_relationship_data_document import ResourceGrantsInvitationSingleRelationshipDataDocument as ResourceGrantsInvitationSingleRelationshipDataDocument
from tidal.models.resource_grants_multi_resource_data_document import ResourceGrantsMultiResourceDataDocument as ResourceGrantsMultiResourceDataDocument
from tidal.models.resource_grants_relationships import ResourceGrantsRelationships as ResourceGrantsRelationships
from tidal.models.resource_grants_resource_object import ResourceGrantsResourceObject as ResourceGrantsResourceObject
from tidal.models.resource_grants_single_resource_data_document import ResourceGrantsSingleResourceDataDocument as ResourceGrantsSingleResourceDataDocument
from tidal.models.resource_grants_subject import ResourceGrantsSubject as ResourceGrantsSubject
from tidal.models.resource_grants_subject_linkage import ResourceGrantsSubjectLinkage as ResourceGrantsSubjectLinkage
from tidal.models.resource_grants_subject_resource_identifier import ResourceGrantsSubjectResourceIdentifier as ResourceGrantsSubjectResourceIdentifier
from tidal.models.resource_grants_subject_resource_identifier_meta import ResourceGrantsSubjectResourceIdentifierMeta as ResourceGrantsSubjectResourceIdentifierMeta
from tidal.models.resource_grants_subject_single_relationship_data_document import ResourceGrantsSubjectSingleRelationshipDataDocument as ResourceGrantsSubjectSingleRelationshipDataDocument
from tidal.models.resource_grants_update_operation_payload import ResourceGrantsUpdateOperationPayload as ResourceGrantsUpdateOperationPayload
from tidal.models.resource_grants_update_operation_payload_data import ResourceGrantsUpdateOperationPayloadData as ResourceGrantsUpdateOperationPayloadData
from tidal.models.resource_grants_update_operation_payload_data_attributes import ResourceGrantsUpdateOperationPayloadDataAttributes as ResourceGrantsUpdateOperationPayloadDataAttributes
from tidal.models.resource_grants_update_single_resource_data_document import ResourceGrantsUpdateSingleResourceDataDocument as ResourceGrantsUpdateSingleResourceDataDocument
from tidal.models.resource_identifier import ResourceIdentifier as ResourceIdentifier
from tidal.models.resource_object_object_object import ResourceObjectObjectObject as ResourceObjectObjectObject
from tidal.models.saved_shares_attributes import SavedSharesAttributes as SavedSharesAttributes
from tidal.models.saved_shares_create_operation_payload import SavedSharesCreateOperationPayload as SavedSharesCreateOperationPayload
from tidal.models.saved_shares_create_operation_payload_data import SavedSharesCreateOperationPayloadData as SavedSharesCreateOperationPayloadData
from tidal.models.saved_shares_create_operation_payload_data_relationships import SavedSharesCreateOperationPayloadDataRelationships as SavedSharesCreateOperationPayloadDataRelationships
from tidal.models.saved_shares_create_operation_payload_data_relationships_share import SavedSharesCreateOperationPayloadDataRelationshipsShare as SavedSharesCreateOperationPayloadDataRelationshipsShare
from tidal.models.saved_shares_create_operation_payload_data_relationships_share_data import SavedSharesCreateOperationPayloadDataRelationshipsShareData as SavedSharesCreateOperationPayloadDataRelationshipsShareData
from tidal.models.saved_shares_create_operation_payload_meta import SavedSharesCreateOperationPayloadMeta as SavedSharesCreateOperationPayloadMeta
from tidal.models.saved_shares_create_resource403_response_body import SavedSharesCreateResource403ResponseBody as SavedSharesCreateResource403ResponseBody
from tidal.models.saved_shares_create_resource403_response_body_errors_inner import SavedSharesCreateResource403ResponseBodyErrorsInner as SavedSharesCreateResource403ResponseBodyErrorsInner
from tidal.models.saved_shares_create_resource429_response_body import SavedSharesCreateResource429ResponseBody as SavedSharesCreateResource429ResponseBody
from tidal.models.saved_shares_create_resource429_response_body_errors_inner import SavedSharesCreateResource429ResponseBodyErrorsInner as SavedSharesCreateResource429ResponseBodyErrorsInner
from tidal.models.saved_shares_create_single_resource_data_document import SavedSharesCreateSingleResourceDataDocument as SavedSharesCreateSingleResourceDataDocument
from tidal.models.saved_shares_resource_object import SavedSharesResourceObject as SavedSharesResourceObject
from tidal.models.scopes_attributes import ScopesAttributes as ScopesAttributes
from tidal.models.scopes_multi_resource_data_document import ScopesMultiResourceDataDocument as ScopesMultiResourceDataDocument
from tidal.models.scopes_resource_object import ScopesResourceObject as ScopesResourceObject
from tidal.models.search_history_entries_attributes import SearchHistoryEntriesAttributes as SearchHistoryEntriesAttributes
from tidal.models.search_history_entries_resource_object import SearchHistoryEntriesResourceObject as SearchHistoryEntriesResourceObject
from tidal.models.search_results_albums_multi_relationship_data_document import SearchResultsAlbumsMultiRelationshipDataDocument as SearchResultsAlbumsMultiRelationshipDataDocument
from tidal.models.search_results_albums_resource_identifier import SearchResultsAlbumsResourceIdentifier as SearchResultsAlbumsResourceIdentifier
from tidal.models.search_results_albums_resource_identifier_meta import SearchResultsAlbumsResourceIdentifierMeta as SearchResultsAlbumsResourceIdentifierMeta
from tidal.models.search_results_artists_multi_relationship_data_document import SearchResultsArtistsMultiRelationshipDataDocument as SearchResultsArtistsMultiRelationshipDataDocument
from tidal.models.search_results_attributes import SearchResultsAttributes as SearchResultsAttributes
from tidal.models.search_results_multi_resource_data_document import SearchResultsMultiResourceDataDocument as SearchResultsMultiResourceDataDocument
from tidal.models.search_results_playlists_multi_relationship_data_document import SearchResultsPlaylistsMultiRelationshipDataDocument as SearchResultsPlaylistsMultiRelationshipDataDocument
from tidal.models.search_results_relationships import SearchResultsRelationships as SearchResultsRelationships
from tidal.models.search_results_resource_object import SearchResultsResourceObject as SearchResultsResourceObject
from tidal.models.search_results_top_hits_multi_relationship_data_document import SearchResultsTopHitsMultiRelationshipDataDocument as SearchResultsTopHitsMultiRelationshipDataDocument
from tidal.models.search_results_top_hits_resource_identifier import SearchResultsTopHitsResourceIdentifier as SearchResultsTopHitsResourceIdentifier
from tidal.models.search_results_top_hits_resource_identifier_meta import SearchResultsTopHitsResourceIdentifierMeta as SearchResultsTopHitsResourceIdentifierMeta
from tidal.models.search_results_tracks_multi_relationship_data_document import SearchResultsTracksMultiRelationshipDataDocument as SearchResultsTracksMultiRelationshipDataDocument
from tidal.models.search_results_tracks_resource_identifier import SearchResultsTracksResourceIdentifier as SearchResultsTracksResourceIdentifier
from tidal.models.search_results_tracks_resource_identifier_meta import SearchResultsTracksResourceIdentifierMeta as SearchResultsTracksResourceIdentifierMeta
from tidal.models.search_results_videos_multi_relationship_data_document import SearchResultsVideosMultiRelationshipDataDocument as SearchResultsVideosMultiRelationshipDataDocument
from tidal.models.search_results_videos_resource_identifier import SearchResultsVideosResourceIdentifier as SearchResultsVideosResourceIdentifier
from tidal.models.search_results_videos_resource_identifier_meta import SearchResultsVideosResourceIdentifierMeta as SearchResultsVideosResourceIdentifierMeta
from tidal.models.search_suggestions_attributes import SearchSuggestionsAttributes as SearchSuggestionsAttributes
from tidal.models.search_suggestions_direct_hits_multi_relationship_data_document import SearchSuggestionsDirectHitsMultiRelationshipDataDocument as SearchSuggestionsDirectHitsMultiRelationshipDataDocument
from tidal.models.search_suggestions_direct_hits_resource_identifier import SearchSuggestionsDirectHitsResourceIdentifier as SearchSuggestionsDirectHitsResourceIdentifier
from tidal.models.search_suggestions_direct_hits_resource_identifier_meta import SearchSuggestionsDirectHitsResourceIdentifierMeta as SearchSuggestionsDirectHitsResourceIdentifierMeta
from tidal.models.search_suggestions_highlights import SearchSuggestionsHighlights as SearchSuggestionsHighlights
from tidal.models.search_suggestions_history_multi_relationship_data_document import SearchSuggestionsHistoryMultiRelationshipDataDocument as SearchSuggestionsHistoryMultiRelationshipDataDocument
from tidal.models.search_suggestions_multi_resource_data_document import SearchSuggestionsMultiResourceDataDocument as SearchSuggestionsMultiResourceDataDocument
from tidal.models.search_suggestions_relationships import SearchSuggestionsRelationships as SearchSuggestionsRelationships
from tidal.models.search_suggestions_resource_object import SearchSuggestionsResourceObject as SearchSuggestionsResourceObject
from tidal.models.search_suggestions_suggestions import SearchSuggestionsSuggestions as SearchSuggestionsSuggestions
from tidal.models.shares_attributes import SharesAttributes as SharesAttributes
from tidal.models.shares_create_operation_payload import SharesCreateOperationPayload as SharesCreateOperationPayload
from tidal.models.shares_create_operation_payload_data import SharesCreateOperationPayloadData as SharesCreateOperationPayloadData
from tidal.models.shares_create_operation_payload_data_attributes import SharesCreateOperationPayloadDataAttributes as SharesCreateOperationPayloadDataAttributes
from tidal.models.shares_create_operation_payload_data_relationships import SharesCreateOperationPayloadDataRelationships as SharesCreateOperationPayloadDataRelationships
from tidal.models.shares_create_operation_payload_data_relationships_shared_resources import SharesCreateOperationPayloadDataRelationshipsSharedResources as SharesCreateOperationPayloadDataRelationshipsSharedResources
from tidal.models.shares_create_operation_payload_data_relationships_shared_resources_data import SharesCreateOperationPayloadDataRelationshipsSharedResourcesData as SharesCreateOperationPayloadDataRelationshipsSharedResourcesData
from tidal.models.shares_create_single_resource_data_document import SharesCreateSingleResourceDataDocument as SharesCreateSingleResourceDataDocument
from tidal.models.shares_multi_resource_data_document import SharesMultiResourceDataDocument as SharesMultiResourceDataDocument
from tidal.models.shares_owners_multi_relationship_data_document import SharesOwnersMultiRelationshipDataDocument as SharesOwnersMultiRelationshipDataDocument
from tidal.models.shares_relationships import SharesRelationships as SharesRelationships
from tidal.models.shares_resource_object import SharesResourceObject as SharesResourceObject
from tidal.models.shares_shared_resources_multi_relationship_data_document import SharesSharedResourcesMultiRelationshipDataDocument as SharesSharedResourcesMultiRelationshipDataDocument
from tidal.models.shares_shared_resources_resource_identifier import SharesSharedResourcesResourceIdentifier as SharesSharedResourcesResourceIdentifier
from tidal.models.shares_shared_resources_resource_identifier_meta import SharesSharedResourcesResourceIdentifierMeta as SharesSharedResourcesResourceIdentifierMeta
from tidal.models.shares_single_resource_data_document import SharesSingleResourceDataDocument as SharesSingleResourceDataDocument
from tidal.models.shares_update_operation_payload import SharesUpdateOperationPayload as SharesUpdateOperationPayload
from tidal.models.shares_update_operation_payload_data import SharesUpdateOperationPayloadData as SharesUpdateOperationPayloadData
from tidal.models.shares_update_operation_payload_data_attributes import SharesUpdateOperationPayloadDataAttributes as SharesUpdateOperationPayloadDataAttributes
from tidal.models.shares_update_single_resource_data_document import SharesUpdateSingleResourceDataDocument as SharesUpdateSingleResourceDataDocument
from tidal.models.sharing_summaries_attributes import SharingSummariesAttributes as SharingSummariesAttributes
from tidal.models.sharing_summaries_multi_resource_data_document import SharingSummariesMultiResourceDataDocument as SharingSummariesMultiResourceDataDocument
from tidal.models.sharing_summaries_relationships import SharingSummariesRelationships as SharingSummariesRelationships
from tidal.models.sharing_summaries_resource_object import SharingSummariesResourceObject as SharingSummariesResourceObject
from tidal.models.sharing_summaries_subject_resource_identifier import SharingSummariesSubjectResourceIdentifier as SharingSummariesSubjectResourceIdentifier
from tidal.models.sharing_summaries_subject_resource_identifier_meta import SharingSummariesSubjectResourceIdentifierMeta as SharingSummariesSubjectResourceIdentifierMeta
from tidal.models.sharing_summaries_subject_single_relationship_data_document import SharingSummariesSubjectSingleRelationshipDataDocument as SharingSummariesSubjectSingleRelationshipDataDocument
from tidal.models.site import Site as Site
from tidal.models.source_processing import SourceProcessing as SourceProcessing
from tidal.models.square_connections_attributes import SquareConnectionsAttributes as SquareConnectionsAttributes
from tidal.models.square_connections_capability import SquareConnectionsCapability as SquareConnectionsCapability
from tidal.models.square_connections_create_operation_payload import SquareConnectionsCreateOperationPayload as SquareConnectionsCreateOperationPayload
from tidal.models.square_connections_create_operation_payload_data import SquareConnectionsCreateOperationPayloadData as SquareConnectionsCreateOperationPayloadData
from tidal.models.square_connections_create_operation_payload_meta import SquareConnectionsCreateOperationPayloadMeta as SquareConnectionsCreateOperationPayloadMeta
from tidal.models.square_connections_create_single_resource_data_document import SquareConnectionsCreateSingleResourceDataDocument as SquareConnectionsCreateSingleResourceDataDocument
from tidal.models.square_connections_read_by_id403_response_body import SquareConnectionsReadById403ResponseBody as SquareConnectionsReadById403ResponseBody
from tidal.models.square_connections_relationships import SquareConnectionsRelationships as SquareConnectionsRelationships
from tidal.models.square_connections_resource_object import SquareConnectionsResourceObject as SquareConnectionsResourceObject
from tidal.models.square_connections_selected_site_read_single_data_relationship403_response_body import SquareConnectionsSelectedSiteReadSingleDataRelationship403ResponseBody as SquareConnectionsSelectedSiteReadSingleDataRelationship403ResponseBody
from tidal.models.square_connections_selected_site_relationship_update_operation_payload import SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload as SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload
from tidal.models.square_connections_selected_site_relationship_update_operation_payload_data import SquareConnectionsSelectedSiteRelationshipUpdateOperationPayloadData as SquareConnectionsSelectedSiteRelationshipUpdateOperationPayloadData
from tidal.models.square_connections_selected_site_single_relationship_data_document import SquareConnectionsSelectedSiteSingleRelationshipDataDocument as SquareConnectionsSelectedSiteSingleRelationshipDataDocument
from tidal.models.square_connections_selected_site_update_resource_identifier import SquareConnectionsSelectedSiteUpdateResourceIdentifier as SquareConnectionsSelectedSiteUpdateResourceIdentifier
from tidal.models.square_connections_selected_site_update_single_data_relationship403_response_body import SquareConnectionsSelectedSiteUpdateSingleDataRelationship403ResponseBody as SquareConnectionsSelectedSiteUpdateSingleDataRelationship403ResponseBody
from tidal.models.square_connections_selected_site_update_single_data_relationship409_response_body import SquareConnectionsSelectedSiteUpdateSingleDataRelationship409ResponseBody as SquareConnectionsSelectedSiteUpdateSingleDataRelationship409ResponseBody
from tidal.models.square_connections_selected_site_update_single_data_relationship409_response_body_errors_inner import SquareConnectionsSelectedSiteUpdateSingleDataRelationship409ResponseBodyErrorsInner as SquareConnectionsSelectedSiteUpdateSingleDataRelationship409ResponseBodyErrorsInner
from tidal.models.square_connections_selected_site_update_single_relationship_data_document import SquareConnectionsSelectedSiteUpdateSingleRelationshipDataDocument as SquareConnectionsSelectedSiteUpdateSingleRelationshipDataDocument
from tidal.models.square_connections_single_resource_data_document import SquareConnectionsSingleResourceDataDocument as SquareConnectionsSingleResourceDataDocument
from tidal.models.square_connections_sites_multi_relationship_data_document import SquareConnectionsSitesMultiRelationshipDataDocument as SquareConnectionsSitesMultiRelationshipDataDocument
from tidal.models.square_connections_sites_read_multi_data_relationship403_response_body import SquareConnectionsSitesReadMultiDataRelationship403ResponseBody as SquareConnectionsSitesReadMultiDataRelationship403ResponseBody
from tidal.models.square_item_variation_physical_counts_attributes import SquareItemVariationPhysicalCountsAttributes as SquareItemVariationPhysicalCountsAttributes
from tidal.models.square_item_variation_physical_counts_create_operation_payload import SquareItemVariationPhysicalCountsCreateOperationPayload as SquareItemVariationPhysicalCountsCreateOperationPayload
from tidal.models.square_item_variation_physical_counts_create_operation_payload_data import SquareItemVariationPhysicalCountsCreateOperationPayloadData as SquareItemVariationPhysicalCountsCreateOperationPayloadData
from tidal.models.square_item_variation_physical_counts_create_operation_payload_data_attributes import SquareItemVariationPhysicalCountsCreateOperationPayloadDataAttributes as SquareItemVariationPhysicalCountsCreateOperationPayloadDataAttributes
from tidal.models.square_item_variation_physical_counts_create_operation_payload_data_relationships import SquareItemVariationPhysicalCountsCreateOperationPayloadDataRelationships as SquareItemVariationPhysicalCountsCreateOperationPayloadDataRelationships
from tidal.models.square_item_variation_physical_counts_create_operation_payload_data_relationships_variations import SquareItemVariationPhysicalCountsCreateOperationPayloadDataRelationshipsVariations as SquareItemVariationPhysicalCountsCreateOperationPayloadDataRelationshipsVariations
from tidal.models.square_item_variation_physical_counts_create_resource403_response_body import SquareItemVariationPhysicalCountsCreateResource403ResponseBody as SquareItemVariationPhysicalCountsCreateResource403ResponseBody
from tidal.models.square_item_variation_physical_counts_create_resource409_response_body import SquareItemVariationPhysicalCountsCreateResource409ResponseBody as SquareItemVariationPhysicalCountsCreateResource409ResponseBody
from tidal.models.square_item_variation_physical_counts_create_resource409_response_body_errors_inner import SquareItemVariationPhysicalCountsCreateResource409ResponseBodyErrorsInner as SquareItemVariationPhysicalCountsCreateResource409ResponseBodyErrorsInner
from tidal.models.square_item_variation_physical_counts_create_single_resource_data_document import SquareItemVariationPhysicalCountsCreateSingleResourceDataDocument as SquareItemVariationPhysicalCountsCreateSingleResourceDataDocument
from tidal.models.square_item_variation_physical_counts_resource_object import SquareItemVariationPhysicalCountsResourceObject as SquareItemVariationPhysicalCountsResourceObject
from tidal.models.square_item_variations_artworks_multi_relationship_data_document import SquareItemVariationsArtworksMultiRelationshipDataDocument as SquareItemVariationsArtworksMultiRelationshipDataDocument
from tidal.models.square_item_variations_artworks_multi_relationship_data_document_meta import SquareItemVariationsArtworksMultiRelationshipDataDocumentMeta as SquareItemVariationsArtworksMultiRelationshipDataDocumentMeta
from tidal.models.square_item_variations_artworks_read_multi_data_relationship403_response_body import SquareItemVariationsArtworksReadMultiDataRelationship403ResponseBody as SquareItemVariationsArtworksReadMultiDataRelationship403ResponseBody
from tidal.models.square_item_variations_artworks_read_multi_data_relationship409_response_body import SquareItemVariationsArtworksReadMultiDataRelationship409ResponseBody as SquareItemVariationsArtworksReadMultiDataRelationship409ResponseBody
from tidal.models.square_item_variations_artworks_read_multi_data_relationship409_response_body_errors_inner import SquareItemVariationsArtworksReadMultiDataRelationship409ResponseBodyErrorsInner as SquareItemVariationsArtworksReadMultiDataRelationship409ResponseBodyErrorsInner
from tidal.models.square_item_variations_artworks_relationship_update_operation_payload import SquareItemVariationsArtworksRelationshipUpdateOperationPayload as SquareItemVariationsArtworksRelationshipUpdateOperationPayload
from tidal.models.square_item_variations_artworks_relationship_update_operation_payload_meta import SquareItemVariationsArtworksRelationshipUpdateOperationPayloadMeta as SquareItemVariationsArtworksRelationshipUpdateOperationPayloadMeta
from tidal.models.square_item_variations_artworks_update_multi_data_relationship403_response_body import SquareItemVariationsArtworksUpdateMultiDataRelationship403ResponseBody as SquareItemVariationsArtworksUpdateMultiDataRelationship403ResponseBody
from tidal.models.square_item_variations_artworks_update_multi_data_relationship409_response_body import SquareItemVariationsArtworksUpdateMultiDataRelationship409ResponseBody as SquareItemVariationsArtworksUpdateMultiDataRelationship409ResponseBody
from tidal.models.square_item_variations_artworks_update_multi_data_relationship409_response_body_errors_inner import SquareItemVariationsArtworksUpdateMultiDataRelationship409ResponseBodyErrorsInner as SquareItemVariationsArtworksUpdateMultiDataRelationship409ResponseBodyErrorsInner
from tidal.models.square_item_variations_artworks_update_multi_data_relationship413_response_body import SquareItemVariationsArtworksUpdateMultiDataRelationship413ResponseBody as SquareItemVariationsArtworksUpdateMultiDataRelationship413ResponseBody
from tidal.models.square_item_variations_artworks_update_multi_data_relationship413_response_body_errors_inner import SquareItemVariationsArtworksUpdateMultiDataRelationship413ResponseBodyErrorsInner as SquareItemVariationsArtworksUpdateMultiDataRelationship413ResponseBodyErrorsInner
from tidal.models.square_item_variations_artworks_update_multi_relationship_data_document import SquareItemVariationsArtworksUpdateMultiRelationshipDataDocument as SquareItemVariationsArtworksUpdateMultiRelationshipDataDocument
from tidal.models.square_item_variations_artworks_update_multi_relationship_data_document_meta import SquareItemVariationsArtworksUpdateMultiRelationshipDataDocumentMeta as SquareItemVariationsArtworksUpdateMultiRelationshipDataDocumentMeta
from tidal.models.square_item_variations_artworks_update_resource_identifier import SquareItemVariationsArtworksUpdateResourceIdentifier as SquareItemVariationsArtworksUpdateResourceIdentifier
from tidal.models.square_item_variations_attributes import SquareItemVariationsAttributes as SquareItemVariationsAttributes
from tidal.models.square_item_variations_create_operation_payload import SquareItemVariationsCreateOperationPayload as SquareItemVariationsCreateOperationPayload
from tidal.models.square_item_variations_create_operation_payload_data import SquareItemVariationsCreateOperationPayloadData as SquareItemVariationsCreateOperationPayloadData
from tidal.models.square_item_variations_create_operation_payload_data_attributes import SquareItemVariationsCreateOperationPayloadDataAttributes as SquareItemVariationsCreateOperationPayloadDataAttributes
from tidal.models.square_item_variations_create_operation_payload_data_relationships import SquareItemVariationsCreateOperationPayloadDataRelationships as SquareItemVariationsCreateOperationPayloadDataRelationships
from tidal.models.square_item_variations_create_operation_payload_data_relationships_items import SquareItemVariationsCreateOperationPayloadDataRelationshipsItems as SquareItemVariationsCreateOperationPayloadDataRelationshipsItems
from tidal.models.square_item_variations_create_operation_payload_local import SquareItemVariationsCreateOperationPayloadLocal as SquareItemVariationsCreateOperationPayloadLocal
from tidal.models.square_item_variations_create_operation_payload_local_data import SquareItemVariationsCreateOperationPayloadLocalData as SquareItemVariationsCreateOperationPayloadLocalData
from tidal.models.square_item_variations_create_operation_payload_local_data_relationships import SquareItemVariationsCreateOperationPayloadLocalDataRelationships as SquareItemVariationsCreateOperationPayloadLocalDataRelationships
from tidal.models.square_item_variations_create_operation_payload_local_data_relationships_items import SquareItemVariationsCreateOperationPayloadLocalDataRelationshipsItems as SquareItemVariationsCreateOperationPayloadLocalDataRelationshipsItems
from tidal.models.square_item_variations_create_operation_payload_local_item import SquareItemVariationsCreateOperationPayloadLocalItem as SquareItemVariationsCreateOperationPayloadLocalItem
from tidal.models.square_item_variations_create_resource403_response_body import SquareItemVariationsCreateResource403ResponseBody as SquareItemVariationsCreateResource403ResponseBody
from tidal.models.square_item_variations_create_resource409_response_body import SquareItemVariationsCreateResource409ResponseBody as SquareItemVariationsCreateResource409ResponseBody
from tidal.models.square_item_variations_create_resource409_response_body_errors_inner import SquareItemVariationsCreateResource409ResponseBodyErrorsInner as SquareItemVariationsCreateResource409ResponseBodyErrorsInner
from tidal.models.square_item_variations_create_single_resource_data_document import SquareItemVariationsCreateSingleResourceDataDocument as SquareItemVariationsCreateSingleResourceDataDocument
from tidal.models.square_item_variations_create_single_resource_data_document_meta import SquareItemVariationsCreateSingleResourceDataDocumentMeta as SquareItemVariationsCreateSingleResourceDataDocumentMeta
from tidal.models.square_item_variations_delete_resource403_response_body import SquareItemVariationsDeleteResource403ResponseBody as SquareItemVariationsDeleteResource403ResponseBody
from tidal.models.square_item_variations_delete_resource409_response_body import SquareItemVariationsDeleteResource409ResponseBody as SquareItemVariationsDeleteResource409ResponseBody
from tidal.models.square_item_variations_delete_resource409_response_body_errors_inner import SquareItemVariationsDeleteResource409ResponseBodyErrorsInner as SquareItemVariationsDeleteResource409ResponseBodyErrorsInner
from tidal.models.square_item_variations_expected_item_revision import SquareItemVariationsExpectedItemRevision as SquareItemVariationsExpectedItemRevision
from tidal.models.square_item_variations_owners_multi_relationship_data_document import SquareItemVariationsOwnersMultiRelationshipDataDocument as SquareItemVariationsOwnersMultiRelationshipDataDocument
from tidal.models.square_item_variations_read_by_id403_response_body import SquareItemVariationsReadById403ResponseBody as SquareItemVariationsReadById403ResponseBody
from tidal.models.square_item_variations_read_by_id409_response_body import SquareItemVariationsReadById409ResponseBody as SquareItemVariationsReadById409ResponseBody
from tidal.models.square_item_variations_read_by_id409_response_body_errors_inner import SquareItemVariationsReadById409ResponseBodyErrorsInner as SquareItemVariationsReadById409ResponseBodyErrorsInner
from tidal.models.square_item_variations_relationships import SquareItemVariationsRelationships as SquareItemVariationsRelationships
from tidal.models.square_item_variations_resource_object import SquareItemVariationsResourceObject as SquareItemVariationsResourceObject
from tidal.models.square_item_variations_single_resource_data_document import SquareItemVariationsSingleResourceDataDocument as SquareItemVariationsSingleResourceDataDocument
from tidal.models.square_item_variations_update_operation_payload import SquareItemVariationsUpdateOperationPayload as SquareItemVariationsUpdateOperationPayload
from tidal.models.square_item_variations_update_operation_payload_data import SquareItemVariationsUpdateOperationPayloadData as SquareItemVariationsUpdateOperationPayloadData
from tidal.models.square_item_variations_update_operation_payload_data_attributes import SquareItemVariationsUpdateOperationPayloadDataAttributes as SquareItemVariationsUpdateOperationPayloadDataAttributes
from tidal.models.square_item_variations_update_operation_payload_meta import SquareItemVariationsUpdateOperationPayloadMeta as SquareItemVariationsUpdateOperationPayloadMeta
from tidal.models.square_item_variations_update_resource403_response_body import SquareItemVariationsUpdateResource403ResponseBody as SquareItemVariationsUpdateResource403ResponseBody
from tidal.models.square_item_variations_update_resource409_response_body import SquareItemVariationsUpdateResource409ResponseBody as SquareItemVariationsUpdateResource409ResponseBody
from tidal.models.square_item_variations_update_resource409_response_body_errors_inner import SquareItemVariationsUpdateResource409ResponseBodyErrorsInner as SquareItemVariationsUpdateResource409ResponseBodyErrorsInner
from tidal.models.square_item_variations_update_single_resource_data_document import SquareItemVariationsUpdateSingleResourceDataDocument as SquareItemVariationsUpdateSingleResourceDataDocument
from tidal.models.square_items_artworks_multi_relationship_data_document import SquareItemsArtworksMultiRelationshipDataDocument as SquareItemsArtworksMultiRelationshipDataDocument
from tidal.models.square_items_artworks_read_multi_data_relationship409_response_body import SquareItemsArtworksReadMultiDataRelationship409ResponseBody as SquareItemsArtworksReadMultiDataRelationship409ResponseBody
from tidal.models.square_items_artworks_relationship_update_operation_payload import SquareItemsArtworksRelationshipUpdateOperationPayload as SquareItemsArtworksRelationshipUpdateOperationPayload
from tidal.models.square_items_artworks_relationship_update_operation_payload_meta import SquareItemsArtworksRelationshipUpdateOperationPayloadMeta as SquareItemsArtworksRelationshipUpdateOperationPayloadMeta
from tidal.models.square_items_artworks_update_multi_data_relationship403_response_body import SquareItemsArtworksUpdateMultiDataRelationship403ResponseBody as SquareItemsArtworksUpdateMultiDataRelationship403ResponseBody
from tidal.models.square_items_artworks_update_multi_data_relationship409_response_body import SquareItemsArtworksUpdateMultiDataRelationship409ResponseBody as SquareItemsArtworksUpdateMultiDataRelationship409ResponseBody
from tidal.models.square_items_artworks_update_multi_data_relationship409_response_body_errors_inner import SquareItemsArtworksUpdateMultiDataRelationship409ResponseBodyErrorsInner as SquareItemsArtworksUpdateMultiDataRelationship409ResponseBodyErrorsInner
from tidal.models.square_items_artworks_update_multi_data_relationship413_response_body import SquareItemsArtworksUpdateMultiDataRelationship413ResponseBody as SquareItemsArtworksUpdateMultiDataRelationship413ResponseBody
from tidal.models.square_items_artworks_update_multi_relationship_data_document import SquareItemsArtworksUpdateMultiRelationshipDataDocument as SquareItemsArtworksUpdateMultiRelationshipDataDocument
from tidal.models.square_items_artworks_update_multi_relationship_data_document_meta import SquareItemsArtworksUpdateMultiRelationshipDataDocumentMeta as SquareItemsArtworksUpdateMultiRelationshipDataDocumentMeta
from tidal.models.square_items_artworks_update_resource_identifier import SquareItemsArtworksUpdateResourceIdentifier as SquareItemsArtworksUpdateResourceIdentifier
from tidal.models.square_items_attributes import SquareItemsAttributes as SquareItemsAttributes
from tidal.models.square_items_create_operation_payload import SquareItemsCreateOperationPayload as SquareItemsCreateOperationPayload
from tidal.models.square_items_create_operation_payload_data import SquareItemsCreateOperationPayloadData as SquareItemsCreateOperationPayloadData
from tidal.models.square_items_create_operation_payload_data_attributes import SquareItemsCreateOperationPayloadDataAttributes as SquareItemsCreateOperationPayloadDataAttributes
from tidal.models.square_items_create_operation_payload_data_relationships import SquareItemsCreateOperationPayloadDataRelationships as SquareItemsCreateOperationPayloadDataRelationships
from tidal.models.square_items_create_operation_payload_data_relationships_sites import SquareItemsCreateOperationPayloadDataRelationshipsSites as SquareItemsCreateOperationPayloadDataRelationshipsSites
from tidal.models.square_items_delete_resource403_response_body import SquareItemsDeleteResource403ResponseBody as SquareItemsDeleteResource403ResponseBody
from tidal.models.square_items_delete_resource409_response_body import SquareItemsDeleteResource409ResponseBody as SquareItemsDeleteResource409ResponseBody
from tidal.models.square_items_delete_resource409_response_body_errors_inner import SquareItemsDeleteResource409ResponseBodyErrorsInner as SquareItemsDeleteResource409ResponseBodyErrorsInner
from tidal.models.square_items_multi_resource_data_document import SquareItemsMultiResourceDataDocument as SquareItemsMultiResourceDataDocument
from tidal.models.square_items_owners_multi_relationship_data_document import SquareItemsOwnersMultiRelationshipDataDocument as SquareItemsOwnersMultiRelationshipDataDocument
from tidal.models.square_items_read_by_filter403_response_body import SquareItemsReadByFilter403ResponseBody as SquareItemsReadByFilter403ResponseBody
from tidal.models.square_items_read_by_filter409_response_body import SquareItemsReadByFilter409ResponseBody as SquareItemsReadByFilter409ResponseBody
from tidal.models.square_items_read_by_id403_response_body import SquareItemsReadById403ResponseBody as SquareItemsReadById403ResponseBody
from tidal.models.square_items_read_by_id409_response_body import SquareItemsReadById409ResponseBody as SquareItemsReadById409ResponseBody
from tidal.models.square_items_relationships import SquareItemsRelationships as SquareItemsRelationships
from tidal.models.square_items_resource_object import SquareItemsResourceObject as SquareItemsResourceObject
from tidal.models.square_items_single_resource_data_document import SquareItemsSingleResourceDataDocument as SquareItemsSingleResourceDataDocument
from tidal.models.square_items_update_operation_payload import SquareItemsUpdateOperationPayload as SquareItemsUpdateOperationPayload
from tidal.models.square_items_update_operation_payload_data import SquareItemsUpdateOperationPayloadData as SquareItemsUpdateOperationPayloadData
from tidal.models.square_items_update_operation_payload_data_attributes import SquareItemsUpdateOperationPayloadDataAttributes as SquareItemsUpdateOperationPayloadDataAttributes
from tidal.models.square_items_update_operation_payload_meta import SquareItemsUpdateOperationPayloadMeta as SquareItemsUpdateOperationPayloadMeta
from tidal.models.square_items_update_resource403_response_body import SquareItemsUpdateResource403ResponseBody as SquareItemsUpdateResource403ResponseBody
from tidal.models.square_items_update_resource409_response_body import SquareItemsUpdateResource409ResponseBody as SquareItemsUpdateResource409ResponseBody
from tidal.models.square_items_update_single_resource_data_document import SquareItemsUpdateSingleResourceDataDocument as SquareItemsUpdateSingleResourceDataDocument
from tidal.models.square_items_variations_multi_relationship_data_document import SquareItemsVariationsMultiRelationshipDataDocument as SquareItemsVariationsMultiRelationshipDataDocument
from tidal.models.square_items_variations_read_multi_data_relationship403_response_body import SquareItemsVariationsReadMultiDataRelationship403ResponseBody as SquareItemsVariationsReadMultiDataRelationship403ResponseBody
from tidal.models.square_items_variations_read_multi_data_relationship409_response_body import SquareItemsVariationsReadMultiDataRelationship409ResponseBody as SquareItemsVariationsReadMultiDataRelationship409ResponseBody
from tidal.models.square_items_variations_relationship_update_operation_payload import SquareItemsVariationsRelationshipUpdateOperationPayload as SquareItemsVariationsRelationshipUpdateOperationPayload
from tidal.models.square_items_variations_relationship_update_operation_payload_meta import SquareItemsVariationsRelationshipUpdateOperationPayloadMeta as SquareItemsVariationsRelationshipUpdateOperationPayloadMeta
from tidal.models.square_items_variations_update_multi_data_relationship403_response_body import SquareItemsVariationsUpdateMultiDataRelationship403ResponseBody as SquareItemsVariationsUpdateMultiDataRelationship403ResponseBody
from tidal.models.square_items_variations_update_multi_data_relationship409_response_body import SquareItemsVariationsUpdateMultiDataRelationship409ResponseBody as SquareItemsVariationsUpdateMultiDataRelationship409ResponseBody
from tidal.models.square_items_variations_update_multi_relationship_data_document import SquareItemsVariationsUpdateMultiRelationshipDataDocument as SquareItemsVariationsUpdateMultiRelationshipDataDocument
from tidal.models.square_items_variations_update_multi_relationship_data_document_meta import SquareItemsVariationsUpdateMultiRelationshipDataDocumentMeta as SquareItemsVariationsUpdateMultiRelationshipDataDocumentMeta
from tidal.models.square_items_variations_update_resource_identifier import SquareItemsVariationsUpdateResourceIdentifier as SquareItemsVariationsUpdateResourceIdentifier
from tidal.models.square_sites_attributes import SquareSitesAttributes as SquareSitesAttributes
from tidal.models.square_sites_items_add_multi_data_relationship403_response_body import SquareSitesItemsAddMultiDataRelationship403ResponseBody as SquareSitesItemsAddMultiDataRelationship403ResponseBody
from tidal.models.square_sites_items_add_multi_data_relationship409_response_body import SquareSitesItemsAddMultiDataRelationship409ResponseBody as SquareSitesItemsAddMultiDataRelationship409ResponseBody
from tidal.models.square_sites_items_add_multi_data_relationship409_response_body_errors_inner import SquareSitesItemsAddMultiDataRelationship409ResponseBodyErrorsInner as SquareSitesItemsAddMultiDataRelationship409ResponseBodyErrorsInner
from tidal.models.square_sites_items_multi_relationship_data_document import SquareSitesItemsMultiRelationshipDataDocument as SquareSitesItemsMultiRelationshipDataDocument
from tidal.models.square_sites_items_read_multi_data_relationship403_response_body import SquareSitesItemsReadMultiDataRelationship403ResponseBody as SquareSitesItemsReadMultiDataRelationship403ResponseBody
from tidal.models.square_sites_items_read_multi_data_relationship409_response_body import SquareSitesItemsReadMultiDataRelationship409ResponseBody as SquareSitesItemsReadMultiDataRelationship409ResponseBody
from tidal.models.square_sites_items_read_multi_data_relationship409_response_body_errors_inner import SquareSitesItemsReadMultiDataRelationship409ResponseBodyErrorsInner as SquareSitesItemsReadMultiDataRelationship409ResponseBodyErrorsInner
from tidal.models.square_sites_items_relationship_add_operation_payload import SquareSitesItemsRelationshipAddOperationPayload as SquareSitesItemsRelationshipAddOperationPayload
from tidal.models.square_sites_items_relationship_add_operation_payload_data import SquareSitesItemsRelationshipAddOperationPayloadData as SquareSitesItemsRelationshipAddOperationPayloadData
from tidal.models.square_sites_items_relationship_remove_operation_payload import SquareSitesItemsRelationshipRemoveOperationPayload as SquareSitesItemsRelationshipRemoveOperationPayload
from tidal.models.square_sites_items_relationship_remove_operation_payload_data import SquareSitesItemsRelationshipRemoveOperationPayloadData as SquareSitesItemsRelationshipRemoveOperationPayloadData
from tidal.models.square_sites_items_remove_multi_data_relationship403_response_body import SquareSitesItemsRemoveMultiDataRelationship403ResponseBody as SquareSitesItemsRemoveMultiDataRelationship403ResponseBody
from tidal.models.square_sites_items_remove_multi_data_relationship409_response_body import SquareSitesItemsRemoveMultiDataRelationship409ResponseBody as SquareSitesItemsRemoveMultiDataRelationship409ResponseBody
from tidal.models.square_sites_relationships import SquareSitesRelationships as SquareSitesRelationships
from tidal.models.square_sites_resource_object import SquareSitesResourceObject as SquareSitesResourceObject
from tidal.models.stripe_connections_attributes import StripeConnectionsAttributes as StripeConnectionsAttributes
from tidal.models.stripe_connections_create_operation_payload import StripeConnectionsCreateOperationPayload as StripeConnectionsCreateOperationPayload
from tidal.models.stripe_connections_create_operation_payload_data import StripeConnectionsCreateOperationPayloadData as StripeConnectionsCreateOperationPayloadData
from tidal.models.stripe_connections_create_operation_payload_data_attributes import StripeConnectionsCreateOperationPayloadDataAttributes as StripeConnectionsCreateOperationPayloadDataAttributes
from tidal.models.stripe_connections_create_operation_payload_meta import StripeConnectionsCreateOperationPayloadMeta as StripeConnectionsCreateOperationPayloadMeta
from tidal.models.stripe_connections_create_single_resource_data_document import StripeConnectionsCreateSingleResourceDataDocument as StripeConnectionsCreateSingleResourceDataDocument
from tidal.models.stripe_connections_multi_resource_data_document import StripeConnectionsMultiResourceDataDocument as StripeConnectionsMultiResourceDataDocument
from tidal.models.stripe_connections_owners_multi_relationship_data_document import StripeConnectionsOwnersMultiRelationshipDataDocument as StripeConnectionsOwnersMultiRelationshipDataDocument
from tidal.models.stripe_connections_relationships import StripeConnectionsRelationships as StripeConnectionsRelationships
from tidal.models.stripe_connections_resource_object import StripeConnectionsResourceObject as StripeConnectionsResourceObject
from tidal.models.stripe_dashboard_links_attributes import StripeDashboardLinksAttributes as StripeDashboardLinksAttributes
from tidal.models.stripe_dashboard_links_multi_resource_data_document import StripeDashboardLinksMultiResourceDataDocument as StripeDashboardLinksMultiResourceDataDocument
from tidal.models.stripe_dashboard_links_owners_multi_relationship_data_document import StripeDashboardLinksOwnersMultiRelationshipDataDocument as StripeDashboardLinksOwnersMultiRelationshipDataDocument
from tidal.models.stripe_dashboard_links_relationships import StripeDashboardLinksRelationships as StripeDashboardLinksRelationships
from tidal.models.stripe_dashboard_links_resource_object import StripeDashboardLinksResourceObject as StripeDashboardLinksResourceObject
from tidal.models.studio_home_event_tiles_attributes import StudioHomeEventTilesAttributes as StudioHomeEventTilesAttributes
from tidal.models.studio_home_event_tiles_resource_object import StudioHomeEventTilesResourceObject as StudioHomeEventTilesResourceObject
from tidal.models.studio_home_event_tiles_single_resource_data_document import StudioHomeEventTilesSingleResourceDataDocument as StudioHomeEventTilesSingleResourceDataDocument
from tidal.models.studio_home_insight_tiles_attributes import StudioHomeInsightTilesAttributes as StudioHomeInsightTilesAttributes
from tidal.models.studio_home_insight_tiles_resource_object import StudioHomeInsightTilesResourceObject as StudioHomeInsightTilesResourceObject
from tidal.models.studio_home_insight_tiles_single_resource_data_document import StudioHomeInsightTilesSingleResourceDataDocument as StudioHomeInsightTilesSingleResourceDataDocument
from tidal.models.studio_home_merch_tiles_attributes import StudioHomeMerchTilesAttributes as StudioHomeMerchTilesAttributes
from tidal.models.studio_home_merch_tiles_items_multi_relationship_data_document import StudioHomeMerchTilesItemsMultiRelationshipDataDocument as StudioHomeMerchTilesItemsMultiRelationshipDataDocument
from tidal.models.studio_home_merch_tiles_relationships import StudioHomeMerchTilesRelationships as StudioHomeMerchTilesRelationships
from tidal.models.studio_home_merch_tiles_resource_object import StudioHomeMerchTilesResourceObject as StudioHomeMerchTilesResourceObject
from tidal.models.studio_home_merch_tiles_single_resource_data_document import StudioHomeMerchTilesSingleResourceDataDocument as StudioHomeMerchTilesSingleResourceDataDocument
from tidal.models.studio_home_music_tiles_attributes import StudioHomeMusicTilesAttributes as StudioHomeMusicTilesAttributes
from tidal.models.studio_home_music_tiles_resource_object import StudioHomeMusicTilesResourceObject as StudioHomeMusicTilesResourceObject
from tidal.models.studio_home_music_tiles_single_resource_data_document import StudioHomeMusicTilesSingleResourceDataDocument as StudioHomeMusicTilesSingleResourceDataDocument
from tidal.models.subscription_price_change_decisions_attributes import SubscriptionPriceChangeDecisionsAttributes as SubscriptionPriceChangeDecisionsAttributes
from tidal.models.subscription_price_change_decisions_create_operation_payload import SubscriptionPriceChangeDecisionsCreateOperationPayload as SubscriptionPriceChangeDecisionsCreateOperationPayload
from tidal.models.subscription_price_change_decisions_create_operation_payload_data import SubscriptionPriceChangeDecisionsCreateOperationPayloadData as SubscriptionPriceChangeDecisionsCreateOperationPayloadData
from tidal.models.subscription_price_change_decisions_create_operation_payload_data_attributes import SubscriptionPriceChangeDecisionsCreateOperationPayloadDataAttributes as SubscriptionPriceChangeDecisionsCreateOperationPayloadDataAttributes
from tidal.models.subscription_price_change_decisions_create_operation_payload_data_relationships import SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationships as SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationships
from tidal.models.subscription_price_change_decisions_create_operation_payload_data_relationships_price_change import SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationshipsPriceChange as SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationshipsPriceChange
from tidal.models.subscription_price_change_decisions_create_operation_payload_data_relationships_price_change_data import SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationshipsPriceChangeData as SubscriptionPriceChangeDecisionsCreateOperationPayloadDataRelationshipsPriceChangeData
from tidal.models.subscription_price_change_decisions_create_single_resource_data_document import SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument as SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument
from tidal.models.subscription_price_change_decisions_multi_resource_data_document import SubscriptionPriceChangeDecisionsMultiResourceDataDocument as SubscriptionPriceChangeDecisionsMultiResourceDataDocument
from tidal.models.subscription_price_change_decisions_price_change_single_relationship_data_document import SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument as SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument
from tidal.models.subscription_price_change_decisions_relationships import SubscriptionPriceChangeDecisionsRelationships as SubscriptionPriceChangeDecisionsRelationships
from tidal.models.subscription_price_change_decisions_resource_object import SubscriptionPriceChangeDecisionsResourceObject as SubscriptionPriceChangeDecisionsResourceObject
from tidal.models.subscription_price_change_decisions_update_operation_payload import SubscriptionPriceChangeDecisionsUpdateOperationPayload as SubscriptionPriceChangeDecisionsUpdateOperationPayload
from tidal.models.subscription_price_change_decisions_update_operation_payload_data import SubscriptionPriceChangeDecisionsUpdateOperationPayloadData as SubscriptionPriceChangeDecisionsUpdateOperationPayloadData
from tidal.models.subscription_price_change_decisions_update_operation_payload_data_attributes import SubscriptionPriceChangeDecisionsUpdateOperationPayloadDataAttributes as SubscriptionPriceChangeDecisionsUpdateOperationPayloadDataAttributes
from tidal.models.subscription_price_change_decisions_update_single_resource_data_document import SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument as SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument
from tidal.models.temporary_user_tokens_create_operation_payload import TemporaryUserTokensCreateOperationPayload as TemporaryUserTokensCreateOperationPayload
from tidal.models.temporary_user_tokens_create_operation_payload_data import TemporaryUserTokensCreateOperationPayloadData as TemporaryUserTokensCreateOperationPayloadData
from tidal.models.temporary_user_tokens_create_single_resource_data_document import TemporaryUserTokensCreateSingleResourceDataDocument as TemporaryUserTokensCreateSingleResourceDataDocument
from tidal.models.temporary_user_tokens_owners_multi_relationship_data_document import TemporaryUserTokensOwnersMultiRelationshipDataDocument as TemporaryUserTokensOwnersMultiRelationshipDataDocument
from tidal.models.temporary_user_tokens_relationships import TemporaryUserTokensRelationships as TemporaryUserTokensRelationships
from tidal.models.temporary_user_tokens_resource_object import TemporaryUserTokensResourceObject as TemporaryUserTokensResourceObject
from tidal.models.temporary_user_tokens_single_resource_data_document import TemporaryUserTokensSingleResourceDataDocument as TemporaryUserTokensSingleResourceDataDocument
from tidal.models.terms_attributes import TermsAttributes as TermsAttributes
from tidal.models.terms_multi_resource_data_document import TermsMultiResourceDataDocument as TermsMultiResourceDataDocument
from tidal.models.terms_resource_object import TermsResourceObject as TermsResourceObject
from tidal.models.terms_resource_object_meta import TermsResourceObjectMeta as TermsResourceObjectMeta
from tidal.models.terms_single_resource_data_document import TermsSingleResourceDataDocument as TermsSingleResourceDataDocument
from tidal.models.third_party_lyrics_provider import ThirdPartyLyricsProvider as ThirdPartyLyricsProvider
from tidal.models.tidal_lyrics_provider import TidalLyricsProvider as TidalLyricsProvider
from tidal.models.track_files_attributes import TrackFilesAttributes as TrackFilesAttributes
from tidal.models.track_files_read_by_id403_response_body import TrackFilesReadById403ResponseBody as TrackFilesReadById403ResponseBody
from tidal.models.track_files_read_by_id403_response_body_errors_inner import TrackFilesReadById403ResponseBodyErrorsInner as TrackFilesReadById403ResponseBodyErrorsInner
from tidal.models.track_files_read_by_id404_response_body import TrackFilesReadById404ResponseBody as TrackFilesReadById404ResponseBody
from tidal.models.track_files_read_by_id404_response_body_errors_inner import TrackFilesReadById404ResponseBodyErrorsInner as TrackFilesReadById404ResponseBodyErrorsInner
from tidal.models.track_files_resource_object import TrackFilesResourceObject as TrackFilesResourceObject
from tidal.models.track_files_single_resource_data_document import TrackFilesSingleResourceDataDocument as TrackFilesSingleResourceDataDocument
from tidal.models.track_info import TrackInfo as TrackInfo
from tidal.models.track_manifests_attributes import TrackManifestsAttributes as TrackManifestsAttributes
from tidal.models.track_manifests_read_by_id403_response_body import TrackManifestsReadById403ResponseBody as TrackManifestsReadById403ResponseBody
from tidal.models.track_manifests_read_by_id404_response_body import TrackManifestsReadById404ResponseBody as TrackManifestsReadById404ResponseBody
from tidal.models.track_manifests_resource_object import TrackManifestsResourceObject as TrackManifestsResourceObject
from tidal.models.track_manifests_single_resource_data_document import TrackManifestsSingleResourceDataDocument as TrackManifestsSingleResourceDataDocument
from tidal.models.track_source_files_attributes import TrackSourceFilesAttributes as TrackSourceFilesAttributes
from tidal.models.track_source_files_comment_summary_single_relationship_data_document import TrackSourceFilesCommentSummarySingleRelationshipDataDocument as TrackSourceFilesCommentSummarySingleRelationshipDataDocument
from tidal.models.track_source_files_create_operation_payload import TrackSourceFilesCreateOperationPayload as TrackSourceFilesCreateOperationPayload
from tidal.models.track_source_files_create_operation_payload_data import TrackSourceFilesCreateOperationPayloadData as TrackSourceFilesCreateOperationPayloadData
from tidal.models.track_source_files_create_operation_payload_data_attributes import TrackSourceFilesCreateOperationPayloadDataAttributes as TrackSourceFilesCreateOperationPayloadDataAttributes
from tidal.models.track_source_files_create_operation_payload_data_relationships import TrackSourceFilesCreateOperationPayloadDataRelationships as TrackSourceFilesCreateOperationPayloadDataRelationships
from tidal.models.track_source_files_create_operation_payload_data_relationships_track import TrackSourceFilesCreateOperationPayloadDataRelationshipsTrack as TrackSourceFilesCreateOperationPayloadDataRelationshipsTrack
from tidal.models.track_source_files_create_operation_payload_data_relationships_track_data import TrackSourceFilesCreateOperationPayloadDataRelationshipsTrackData as TrackSourceFilesCreateOperationPayloadDataRelationshipsTrackData
from tidal.models.track_source_files_create_single_resource_data_document import TrackSourceFilesCreateSingleResourceDataDocument as TrackSourceFilesCreateSingleResourceDataDocument
from tidal.models.track_source_files_owners_multi_relationship_data_document import TrackSourceFilesOwnersMultiRelationshipDataDocument as TrackSourceFilesOwnersMultiRelationshipDataDocument
from tidal.models.track_source_files_reaction_summary_single_relationship_data_document import TrackSourceFilesReactionSummarySingleRelationshipDataDocument as TrackSourceFilesReactionSummarySingleRelationshipDataDocument
from tidal.models.track_source_files_relationships import TrackSourceFilesRelationships as TrackSourceFilesRelationships
from tidal.models.track_source_files_resource_object import TrackSourceFilesResourceObject as TrackSourceFilesResourceObject
from tidal.models.track_source_files_single_resource_data_document import TrackSourceFilesSingleResourceDataDocument as TrackSourceFilesSingleResourceDataDocument
from tidal.models.track_statistics_attributes import TrackStatisticsAttributes as TrackStatisticsAttributes
from tidal.models.track_statistics_owners_multi_relationship_data_document import TrackStatisticsOwnersMultiRelationshipDataDocument as TrackStatisticsOwnersMultiRelationshipDataDocument
from tidal.models.track_statistics_relationships import TrackStatisticsRelationships as TrackStatisticsRelationships
from tidal.models.track_statistics_resource_object import TrackStatisticsResourceObject as TrackStatisticsResourceObject
from tidal.models.track_statistics_single_resource_data_document import TrackStatisticsSingleResourceDataDocument as TrackStatisticsSingleResourceDataDocument
from tidal.models.tracks_albums_multi_relationship_data_document import TracksAlbumsMultiRelationshipDataDocument as TracksAlbumsMultiRelationshipDataDocument
from tidal.models.tracks_albums_relationship_update_operation_payload import TracksAlbumsRelationshipUpdateOperationPayload as TracksAlbumsRelationshipUpdateOperationPayload
from tidal.models.tracks_albums_relationship_update_operation_payload_data import TracksAlbumsRelationshipUpdateOperationPayloadData as TracksAlbumsRelationshipUpdateOperationPayloadData
from tidal.models.tracks_albums_resource_identifier import TracksAlbumsResourceIdentifier as TracksAlbumsResourceIdentifier
from tidal.models.tracks_albums_resource_identifier_meta import TracksAlbumsResourceIdentifierMeta as TracksAlbumsResourceIdentifierMeta
from tidal.models.tracks_artists_multi_relationship_data_document import TracksArtistsMultiRelationshipDataDocument as TracksArtistsMultiRelationshipDataDocument
from tidal.models.tracks_artists_relationship_update_operation_payload import TracksArtistsRelationshipUpdateOperationPayload as TracksArtistsRelationshipUpdateOperationPayload
from tidal.models.tracks_artists_relationship_update_operation_payload_data import TracksArtistsRelationshipUpdateOperationPayloadData as TracksArtistsRelationshipUpdateOperationPayloadData
from tidal.models.tracks_attributes import TracksAttributes as TracksAttributes
from tidal.models.tracks_create_operation_payload import TracksCreateOperationPayload as TracksCreateOperationPayload
from tidal.models.tracks_create_operation_payload_data import TracksCreateOperationPayloadData as TracksCreateOperationPayloadData
from tidal.models.tracks_create_operation_payload_data_attributes import TracksCreateOperationPayloadDataAttributes as TracksCreateOperationPayloadDataAttributes
from tidal.models.tracks_create_operation_payload_data_relationships import TracksCreateOperationPayloadDataRelationships as TracksCreateOperationPayloadDataRelationships
from tidal.models.tracks_create_operation_payload_data_relationships_albums import TracksCreateOperationPayloadDataRelationshipsAlbums as TracksCreateOperationPayloadDataRelationshipsAlbums
from tidal.models.tracks_create_operation_payload_data_relationships_albums_data import TracksCreateOperationPayloadDataRelationshipsAlbumsData as TracksCreateOperationPayloadDataRelationshipsAlbumsData
from tidal.models.tracks_create_operation_payload_data_relationships_artists import TracksCreateOperationPayloadDataRelationshipsArtists as TracksCreateOperationPayloadDataRelationshipsArtists
from tidal.models.tracks_create_operation_payload_data_relationships_artists_data import TracksCreateOperationPayloadDataRelationshipsArtistsData as TracksCreateOperationPayloadDataRelationshipsArtistsData
from tidal.models.tracks_create_operation_payload_data_relationships_genres import TracksCreateOperationPayloadDataRelationshipsGenres as TracksCreateOperationPayloadDataRelationshipsGenres
from tidal.models.tracks_create_operation_payload_data_relationships_genres_data import TracksCreateOperationPayloadDataRelationshipsGenresData as TracksCreateOperationPayloadDataRelationshipsGenresData
from tidal.models.tracks_create_single_resource_data_document import TracksCreateSingleResourceDataDocument as TracksCreateSingleResourceDataDocument
from tidal.models.tracks_credits_multi_relationship_data_document import TracksCreditsMultiRelationshipDataDocument as TracksCreditsMultiRelationshipDataDocument
from tidal.models.tracks_download_single_relationship_data_document import TracksDownloadSingleRelationshipDataDocument as TracksDownloadSingleRelationshipDataDocument
from tidal.models.tracks_genres_multi_relationship_data_document import TracksGenresMultiRelationshipDataDocument as TracksGenresMultiRelationshipDataDocument
from tidal.models.tracks_lyrics_multi_relationship_data_document import TracksLyricsMultiRelationshipDataDocument as TracksLyricsMultiRelationshipDataDocument
from tidal.models.tracks_metadata_status_attributes import TracksMetadataStatusAttributes as TracksMetadataStatusAttributes
from tidal.models.tracks_metadata_status_resource_object import TracksMetadataStatusResourceObject as TracksMetadataStatusResourceObject
from tidal.models.tracks_metadata_status_single_relationship_data_document import TracksMetadataStatusSingleRelationshipDataDocument as TracksMetadataStatusSingleRelationshipDataDocument
from tidal.models.tracks_metadata_status_single_resource_data_document import TracksMetadataStatusSingleResourceDataDocument as TracksMetadataStatusSingleResourceDataDocument
from tidal.models.tracks_multi_resource_data_document import TracksMultiResourceDataDocument as TracksMultiResourceDataDocument
from tidal.models.tracks_owners_multi_relationship_data_document import TracksOwnersMultiRelationshipDataDocument as TracksOwnersMultiRelationshipDataDocument
from tidal.models.tracks_price_config_single_relationship_data_document import TracksPriceConfigSingleRelationshipDataDocument as TracksPriceConfigSingleRelationshipDataDocument
from tidal.models.tracks_providers_multi_relationship_data_document import TracksProvidersMultiRelationshipDataDocument as TracksProvidersMultiRelationshipDataDocument
from tidal.models.tracks_radio_multi_relationship_data_document import TracksRadioMultiRelationshipDataDocument as TracksRadioMultiRelationshipDataDocument
from tidal.models.tracks_relationships import TracksRelationships as TracksRelationships
from tidal.models.tracks_replacement_resource_identifier import TracksReplacementResourceIdentifier as TracksReplacementResourceIdentifier
from tidal.models.tracks_replacement_resource_identifier_meta import TracksReplacementResourceIdentifierMeta as TracksReplacementResourceIdentifierMeta
from tidal.models.tracks_replacement_single_relationship_data_document import TracksReplacementSingleRelationshipDataDocument as TracksReplacementSingleRelationshipDataDocument
from tidal.models.tracks_resource_object import TracksResourceObject as TracksResourceObject
from tidal.models.tracks_shares_multi_relationship_data_document import TracksSharesMultiRelationshipDataDocument as TracksSharesMultiRelationshipDataDocument
from tidal.models.tracks_similar_tracks_multi_relationship_data_document import TracksSimilarTracksMultiRelationshipDataDocument as TracksSimilarTracksMultiRelationshipDataDocument
from tidal.models.tracks_similar_tracks_resource_identifier import TracksSimilarTracksResourceIdentifier as TracksSimilarTracksResourceIdentifier
from tidal.models.tracks_similar_tracks_resource_identifier_meta import TracksSimilarTracksResourceIdentifierMeta as TracksSimilarTracksResourceIdentifierMeta
from tidal.models.tracks_single_resource_data_document import TracksSingleResourceDataDocument as TracksSingleResourceDataDocument
from tidal.models.tracks_source_file_single_relationship_data_document import TracksSourceFileSingleRelationshipDataDocument as TracksSourceFileSingleRelationshipDataDocument
from tidal.models.tracks_suggested_tracks_multi_relationship_data_document import TracksSuggestedTracksMultiRelationshipDataDocument as TracksSuggestedTracksMultiRelationshipDataDocument
from tidal.models.tracks_suggested_tracks_resource_identifier import TracksSuggestedTracksResourceIdentifier as TracksSuggestedTracksResourceIdentifier
from tidal.models.tracks_suggested_tracks_resource_identifier_meta import TracksSuggestedTracksResourceIdentifierMeta as TracksSuggestedTracksResourceIdentifierMeta
from tidal.models.tracks_track_statistics_single_relationship_data_document import TracksTrackStatisticsSingleRelationshipDataDocument as TracksTrackStatisticsSingleRelationshipDataDocument
from tidal.models.tracks_update_operation_payload import TracksUpdateOperationPayload as TracksUpdateOperationPayload
from tidal.models.tracks_update_operation_payload_data import TracksUpdateOperationPayloadData as TracksUpdateOperationPayloadData
from tidal.models.tracks_update_operation_payload_data_attributes import TracksUpdateOperationPayloadDataAttributes as TracksUpdateOperationPayloadDataAttributes
from tidal.models.tracks_update_operation_payload_data_relationships import TracksUpdateOperationPayloadDataRelationships as TracksUpdateOperationPayloadDataRelationships
from tidal.models.tracks_update_operation_payload_data_relationships_genres import TracksUpdateOperationPayloadDataRelationshipsGenres as TracksUpdateOperationPayloadDataRelationshipsGenres
from tidal.models.tracks_update_operation_payload_data_relationships_genres_data import TracksUpdateOperationPayloadDataRelationshipsGenresData as TracksUpdateOperationPayloadDataRelationshipsGenresData
from tidal.models.tracks_usage_rules_single_relationship_data_document import TracksUsageRulesSingleRelationshipDataDocument as TracksUsageRulesSingleRelationshipDataDocument
from tidal.models.usage_rules_attributes import UsageRulesAttributes as UsageRulesAttributes
from tidal.models.usage_rules_create_operation_payload import UsageRulesCreateOperationPayload as UsageRulesCreateOperationPayload
from tidal.models.usage_rules_create_operation_payload_data import UsageRulesCreateOperationPayloadData as UsageRulesCreateOperationPayloadData
from tidal.models.usage_rules_create_operation_payload_data_attributes import UsageRulesCreateOperationPayloadDataAttributes as UsageRulesCreateOperationPayloadDataAttributes
from tidal.models.usage_rules_create_operation_payload_data_relationships import UsageRulesCreateOperationPayloadDataRelationships as UsageRulesCreateOperationPayloadDataRelationships
from tidal.models.usage_rules_create_operation_payload_data_relationships_subject import UsageRulesCreateOperationPayloadDataRelationshipsSubject as UsageRulesCreateOperationPayloadDataRelationshipsSubject
from tidal.models.usage_rules_create_operation_payload_subject import UsageRulesCreateOperationPayloadSubject as UsageRulesCreateOperationPayloadSubject
from tidal.models.usage_rules_create_resource403_response_body import UsageRulesCreateResource403ResponseBody as UsageRulesCreateResource403ResponseBody
from tidal.models.usage_rules_create_resource403_response_body_errors_inner import UsageRulesCreateResource403ResponseBodyErrorsInner as UsageRulesCreateResource403ResponseBodyErrorsInner
from tidal.models.usage_rules_create_single_resource_data_document import UsageRulesCreateSingleResourceDataDocument as UsageRulesCreateSingleResourceDataDocument
from tidal.models.usage_rules_resource_object import UsageRulesResourceObject as UsageRulesResourceObject
from tidal.models.usage_rules_single_resource_data_document import UsageRulesSingleResourceDataDocument as UsageRulesSingleResourceDataDocument
from tidal.models.user_collection import UserCollection as UserCollection
from tidal.models.user_collection_albums_attributes import UserCollectionAlbumsAttributes as UserCollectionAlbumsAttributes
from tidal.models.user_collection_albums_items_add_multi_data_relationship_with_response409_response_body import UserCollectionAlbumsItemsAddMultiDataRelationshipWithResponse409ResponseBody as UserCollectionAlbumsItemsAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_collection_albums_items_add_multi_data_relationship_with_response409_response_body_errors_inner import UserCollectionAlbumsItemsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner as UserCollectionAlbumsItemsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner
from tidal.models.user_collection_albums_items_add_multi_relationship_data_document import UserCollectionAlbumsItemsAddMultiRelationshipDataDocument as UserCollectionAlbumsItemsAddMultiRelationshipDataDocument
from tidal.models.user_collection_albums_items_add_multi_relationship_data_document_meta import UserCollectionAlbumsItemsAddMultiRelationshipDataDocumentMeta as UserCollectionAlbumsItemsAddMultiRelationshipDataDocumentMeta
from tidal.models.user_collection_albums_items_add_resource_identifier import UserCollectionAlbumsItemsAddResourceIdentifier as UserCollectionAlbumsItemsAddResourceIdentifier
from tidal.models.user_collection_albums_items_add_resource_identifier_meta import UserCollectionAlbumsItemsAddResourceIdentifierMeta as UserCollectionAlbumsItemsAddResourceIdentifierMeta
from tidal.models.user_collection_albums_items_multi_relationship_data_document import UserCollectionAlbumsItemsMultiRelationshipDataDocument as UserCollectionAlbumsItemsMultiRelationshipDataDocument
from tidal.models.user_collection_albums_items_read_multi_data_relationship403_response_body import UserCollectionAlbumsItemsReadMultiDataRelationship403ResponseBody as UserCollectionAlbumsItemsReadMultiDataRelationship403ResponseBody
from tidal.models.user_collection_albums_items_read_multi_data_relationship403_response_body_errors_inner import UserCollectionAlbumsItemsReadMultiDataRelationship403ResponseBodyErrorsInner as UserCollectionAlbumsItemsReadMultiDataRelationship403ResponseBodyErrorsInner
from tidal.models.user_collection_albums_items_relationship_add_operation_payload import UserCollectionAlbumsItemsRelationshipAddOperationPayload as UserCollectionAlbumsItemsRelationshipAddOperationPayload
from tidal.models.user_collection_albums_items_relationship_add_operation_payload_data import UserCollectionAlbumsItemsRelationshipAddOperationPayloadData as UserCollectionAlbumsItemsRelationshipAddOperationPayloadData
from tidal.models.user_collection_albums_items_relationship_add_operation_payload_data_meta import UserCollectionAlbumsItemsRelationshipAddOperationPayloadDataMeta as UserCollectionAlbumsItemsRelationshipAddOperationPayloadDataMeta
from tidal.models.user_collection_albums_items_relationship_add_operation_response_meta_skipped_item import UserCollectionAlbumsItemsRelationshipAddOperationResponseMetaSkippedItem as UserCollectionAlbumsItemsRelationshipAddOperationResponseMetaSkippedItem
from tidal.models.user_collection_albums_items_relationship_remove_operation_payload import UserCollectionAlbumsItemsRelationshipRemoveOperationPayload as UserCollectionAlbumsItemsRelationshipRemoveOperationPayload
from tidal.models.user_collection_albums_items_relationship_remove_operation_payload_data import UserCollectionAlbumsItemsRelationshipRemoveOperationPayloadData as UserCollectionAlbumsItemsRelationshipRemoveOperationPayloadData
from tidal.models.user_collection_albums_items_resource_identifier import UserCollectionAlbumsItemsResourceIdentifier as UserCollectionAlbumsItemsResourceIdentifier
from tidal.models.user_collection_albums_items_resource_identifier_meta import UserCollectionAlbumsItemsResourceIdentifierMeta as UserCollectionAlbumsItemsResourceIdentifierMeta
from tidal.models.user_collection_albums_owners_multi_relationship_data_document import UserCollectionAlbumsOwnersMultiRelationshipDataDocument as UserCollectionAlbumsOwnersMultiRelationshipDataDocument
from tidal.models.user_collection_albums_relationships import UserCollectionAlbumsRelationships as UserCollectionAlbumsRelationships
from tidal.models.user_collection_albums_resource_object import UserCollectionAlbumsResourceObject as UserCollectionAlbumsResourceObject
from tidal.models.user_collection_albums_single_resource_data_document import UserCollectionAlbumsSingleResourceDataDocument as UserCollectionAlbumsSingleResourceDataDocument
from tidal.models.user_collection_artists_attributes import UserCollectionArtistsAttributes as UserCollectionArtistsAttributes
from tidal.models.user_collection_artists_items_add_multi_data_relationship_with_response409_response_body import UserCollectionArtistsItemsAddMultiDataRelationshipWithResponse409ResponseBody as UserCollectionArtistsItemsAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_collection_artists_items_add_multi_relationship_data_document import UserCollectionArtistsItemsAddMultiRelationshipDataDocument as UserCollectionArtistsItemsAddMultiRelationshipDataDocument
from tidal.models.user_collection_artists_items_add_multi_relationship_data_document_meta import UserCollectionArtistsItemsAddMultiRelationshipDataDocumentMeta as UserCollectionArtistsItemsAddMultiRelationshipDataDocumentMeta
from tidal.models.user_collection_artists_items_add_resource_identifier import UserCollectionArtistsItemsAddResourceIdentifier as UserCollectionArtistsItemsAddResourceIdentifier
from tidal.models.user_collection_artists_items_add_resource_identifier_meta import UserCollectionArtistsItemsAddResourceIdentifierMeta as UserCollectionArtistsItemsAddResourceIdentifierMeta
from tidal.models.user_collection_artists_items_multi_relationship_data_document import UserCollectionArtistsItemsMultiRelationshipDataDocument as UserCollectionArtistsItemsMultiRelationshipDataDocument
from tidal.models.user_collection_artists_items_read_multi_data_relationship403_response_body import UserCollectionArtistsItemsReadMultiDataRelationship403ResponseBody as UserCollectionArtistsItemsReadMultiDataRelationship403ResponseBody
from tidal.models.user_collection_artists_items_relationship_add_operation_payload import UserCollectionArtistsItemsRelationshipAddOperationPayload as UserCollectionArtistsItemsRelationshipAddOperationPayload
from tidal.models.user_collection_artists_items_relationship_add_operation_payload_data import UserCollectionArtistsItemsRelationshipAddOperationPayloadData as UserCollectionArtistsItemsRelationshipAddOperationPayloadData
from tidal.models.user_collection_artists_items_relationship_add_operation_payload_data_meta import UserCollectionArtistsItemsRelationshipAddOperationPayloadDataMeta as UserCollectionArtistsItemsRelationshipAddOperationPayloadDataMeta
from tidal.models.user_collection_artists_items_relationship_add_operation_response_meta_skipped_item import UserCollectionArtistsItemsRelationshipAddOperationResponseMetaSkippedItem as UserCollectionArtistsItemsRelationshipAddOperationResponseMetaSkippedItem
from tidal.models.user_collection_artists_items_relationship_remove_operation_payload import UserCollectionArtistsItemsRelationshipRemoveOperationPayload as UserCollectionArtistsItemsRelationshipRemoveOperationPayload
from tidal.models.user_collection_artists_items_relationship_remove_operation_payload_data import UserCollectionArtistsItemsRelationshipRemoveOperationPayloadData as UserCollectionArtistsItemsRelationshipRemoveOperationPayloadData
from tidal.models.user_collection_artists_items_resource_identifier import UserCollectionArtistsItemsResourceIdentifier as UserCollectionArtistsItemsResourceIdentifier
from tidal.models.user_collection_artists_items_resource_identifier_meta import UserCollectionArtistsItemsResourceIdentifierMeta as UserCollectionArtistsItemsResourceIdentifierMeta
from tidal.models.user_collection_artists_owners_multi_relationship_data_document import UserCollectionArtistsOwnersMultiRelationshipDataDocument as UserCollectionArtistsOwnersMultiRelationshipDataDocument
from tidal.models.user_collection_artists_relationships import UserCollectionArtistsRelationships as UserCollectionArtistsRelationships
from tidal.models.user_collection_artists_resource_object import UserCollectionArtistsResourceObject as UserCollectionArtistsResourceObject
from tidal.models.user_collection_artists_single_resource_data_document import UserCollectionArtistsSingleResourceDataDocument as UserCollectionArtistsSingleResourceDataDocument
from tidal.models.user_collection_folders_attributes import UserCollectionFoldersAttributes as UserCollectionFoldersAttributes
from tidal.models.user_collection_folders_create_operation_payload import UserCollectionFoldersCreateOperationPayload as UserCollectionFoldersCreateOperationPayload
from tidal.models.user_collection_folders_create_operation_payload_data import UserCollectionFoldersCreateOperationPayloadData as UserCollectionFoldersCreateOperationPayloadData
from tidal.models.user_collection_folders_create_operation_payload_data_attributes import UserCollectionFoldersCreateOperationPayloadDataAttributes as UserCollectionFoldersCreateOperationPayloadDataAttributes
from tidal.models.user_collection_folders_create_operation_payload_data_relationships import UserCollectionFoldersCreateOperationPayloadDataRelationships as UserCollectionFoldersCreateOperationPayloadDataRelationships
from tidal.models.user_collection_folders_create_operation_payload_data_relationships_user_collection import UserCollectionFoldersCreateOperationPayloadDataRelationshipsUserCollection as UserCollectionFoldersCreateOperationPayloadDataRelationshipsUserCollection
from tidal.models.user_collection_folders_create_single_resource_data_document import UserCollectionFoldersCreateSingleResourceDataDocument as UserCollectionFoldersCreateSingleResourceDataDocument
from tidal.models.user_collection_folders_delete_resource400_response_body import UserCollectionFoldersDeleteResource400ResponseBody as UserCollectionFoldersDeleteResource400ResponseBody
from tidal.models.user_collection_folders_delete_resource400_response_body_errors_inner import UserCollectionFoldersDeleteResource400ResponseBodyErrorsInner as UserCollectionFoldersDeleteResource400ResponseBodyErrorsInner
from tidal.models.user_collection_folders_items_multi_relationship_data_document import UserCollectionFoldersItemsMultiRelationshipDataDocument as UserCollectionFoldersItemsMultiRelationshipDataDocument
from tidal.models.user_collection_folders_items_relationship_add_operation_payload import UserCollectionFoldersItemsRelationshipAddOperationPayload as UserCollectionFoldersItemsRelationshipAddOperationPayload
from tidal.models.user_collection_folders_items_relationship_add_operation_payload_data import UserCollectionFoldersItemsRelationshipAddOperationPayloadData as UserCollectionFoldersItemsRelationshipAddOperationPayloadData
from tidal.models.user_collection_folders_items_relationship_remove_operation_payload import UserCollectionFoldersItemsRelationshipRemoveOperationPayload as UserCollectionFoldersItemsRelationshipRemoveOperationPayload
from tidal.models.user_collection_folders_items_relationship_remove_operation_payload_data import UserCollectionFoldersItemsRelationshipRemoveOperationPayloadData as UserCollectionFoldersItemsRelationshipRemoveOperationPayloadData
from tidal.models.user_collection_folders_items_resource_identifier import UserCollectionFoldersItemsResourceIdentifier as UserCollectionFoldersItemsResourceIdentifier
from tidal.models.user_collection_folders_items_resource_identifier_meta import UserCollectionFoldersItemsResourceIdentifierMeta as UserCollectionFoldersItemsResourceIdentifierMeta
from tidal.models.user_collection_folders_multi_resource_data_document import UserCollectionFoldersMultiResourceDataDocument as UserCollectionFoldersMultiResourceDataDocument
from tidal.models.user_collection_folders_owners_multi_relationship_data_document import UserCollectionFoldersOwnersMultiRelationshipDataDocument as UserCollectionFoldersOwnersMultiRelationshipDataDocument
from tidal.models.user_collection_folders_relationships import UserCollectionFoldersRelationships as UserCollectionFoldersRelationships
from tidal.models.user_collection_folders_resource_object import UserCollectionFoldersResourceObject as UserCollectionFoldersResourceObject
from tidal.models.user_collection_folders_single_resource_data_document import UserCollectionFoldersSingleResourceDataDocument as UserCollectionFoldersSingleResourceDataDocument
from tidal.models.user_collection_folders_update_operation_payload import UserCollectionFoldersUpdateOperationPayload as UserCollectionFoldersUpdateOperationPayload
from tidal.models.user_collection_folders_update_operation_payload_data import UserCollectionFoldersUpdateOperationPayloadData as UserCollectionFoldersUpdateOperationPayloadData
from tidal.models.user_collection_folders_update_operation_payload_data_attributes import UserCollectionFoldersUpdateOperationPayloadDataAttributes as UserCollectionFoldersUpdateOperationPayloadDataAttributes
from tidal.models.user_collection_folders_user_collection_single_relationship_data_document import UserCollectionFoldersUserCollectionSingleRelationshipDataDocument as UserCollectionFoldersUserCollectionSingleRelationshipDataDocument
from tidal.models.user_collection_playlists_attributes import UserCollectionPlaylistsAttributes as UserCollectionPlaylistsAttributes
from tidal.models.user_collection_playlists_items_add_multi_data_relationship_with_response409_response_body import UserCollectionPlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBody as UserCollectionPlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_collection_playlists_items_add_multi_relationship_data_document import UserCollectionPlaylistsItemsAddMultiRelationshipDataDocument as UserCollectionPlaylistsItemsAddMultiRelationshipDataDocument
from tidal.models.user_collection_playlists_items_add_multi_relationship_data_document_meta import UserCollectionPlaylistsItemsAddMultiRelationshipDataDocumentMeta as UserCollectionPlaylistsItemsAddMultiRelationshipDataDocumentMeta
from tidal.models.user_collection_playlists_items_add_resource_identifier import UserCollectionPlaylistsItemsAddResourceIdentifier as UserCollectionPlaylistsItemsAddResourceIdentifier
from tidal.models.user_collection_playlists_items_add_resource_identifier_meta import UserCollectionPlaylistsItemsAddResourceIdentifierMeta as UserCollectionPlaylistsItemsAddResourceIdentifierMeta
from tidal.models.user_collection_playlists_items_multi_relationship_data_document import UserCollectionPlaylistsItemsMultiRelationshipDataDocument as UserCollectionPlaylistsItemsMultiRelationshipDataDocument
from tidal.models.user_collection_playlists_items_read_multi_data_relationship403_response_body import UserCollectionPlaylistsItemsReadMultiDataRelationship403ResponseBody as UserCollectionPlaylistsItemsReadMultiDataRelationship403ResponseBody
from tidal.models.user_collection_playlists_items_relationship_add_operation_payload import UserCollectionPlaylistsItemsRelationshipAddOperationPayload as UserCollectionPlaylistsItemsRelationshipAddOperationPayload
from tidal.models.user_collection_playlists_items_relationship_add_operation_payload_data import UserCollectionPlaylistsItemsRelationshipAddOperationPayloadData as UserCollectionPlaylistsItemsRelationshipAddOperationPayloadData
from tidal.models.user_collection_playlists_items_relationship_add_operation_payload_data_meta import UserCollectionPlaylistsItemsRelationshipAddOperationPayloadDataMeta as UserCollectionPlaylistsItemsRelationshipAddOperationPayloadDataMeta
from tidal.models.user_collection_playlists_items_relationship_add_operation_response_meta_skipped_item import UserCollectionPlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem as UserCollectionPlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem
from tidal.models.user_collection_playlists_items_relationship_remove_operation_payload import UserCollectionPlaylistsItemsRelationshipRemoveOperationPayload as UserCollectionPlaylistsItemsRelationshipRemoveOperationPayload
from tidal.models.user_collection_playlists_items_relationship_remove_operation_payload_data import UserCollectionPlaylistsItemsRelationshipRemoveOperationPayloadData as UserCollectionPlaylistsItemsRelationshipRemoveOperationPayloadData
from tidal.models.user_collection_playlists_items_resource_identifier import UserCollectionPlaylistsItemsResourceIdentifier as UserCollectionPlaylistsItemsResourceIdentifier
from tidal.models.user_collection_playlists_items_resource_identifier_meta import UserCollectionPlaylistsItemsResourceIdentifierMeta as UserCollectionPlaylistsItemsResourceIdentifierMeta
from tidal.models.user_collection_playlists_owners_multi_relationship_data_document import UserCollectionPlaylistsOwnersMultiRelationshipDataDocument as UserCollectionPlaylistsOwnersMultiRelationshipDataDocument
from tidal.models.user_collection_playlists_relationships import UserCollectionPlaylistsRelationships as UserCollectionPlaylistsRelationships
from tidal.models.user_collection_playlists_resource_object import UserCollectionPlaylistsResourceObject as UserCollectionPlaylistsResourceObject
from tidal.models.user_collection_playlists_single_resource_data_document import UserCollectionPlaylistsSingleResourceDataDocument as UserCollectionPlaylistsSingleResourceDataDocument
from tidal.models.user_collection_save_for_laters_attributes import UserCollectionSaveForLatersAttributes as UserCollectionSaveForLatersAttributes
from tidal.models.user_collection_save_for_laters_items_add_multi_data_relationship_with_response409_response_body import UserCollectionSaveForLatersItemsAddMultiDataRelationshipWithResponse409ResponseBody as UserCollectionSaveForLatersItemsAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_collection_save_for_laters_items_add_multi_relationship_data_document import UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocument as UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocument
from tidal.models.user_collection_save_for_laters_items_add_multi_relationship_data_document_meta import UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocumentMeta as UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocumentMeta
from tidal.models.user_collection_save_for_laters_items_add_resource_identifier import UserCollectionSaveForLatersItemsAddResourceIdentifier as UserCollectionSaveForLatersItemsAddResourceIdentifier
from tidal.models.user_collection_save_for_laters_items_add_resource_identifier_meta import UserCollectionSaveForLatersItemsAddResourceIdentifierMeta as UserCollectionSaveForLatersItemsAddResourceIdentifierMeta
from tidal.models.user_collection_save_for_laters_items_multi_relationship_data_document import UserCollectionSaveForLatersItemsMultiRelationshipDataDocument as UserCollectionSaveForLatersItemsMultiRelationshipDataDocument
from tidal.models.user_collection_save_for_laters_items_relationship_add_operation_payload import UserCollectionSaveForLatersItemsRelationshipAddOperationPayload as UserCollectionSaveForLatersItemsRelationshipAddOperationPayload
from tidal.models.user_collection_save_for_laters_items_relationship_add_operation_payload_data import UserCollectionSaveForLatersItemsRelationshipAddOperationPayloadData as UserCollectionSaveForLatersItemsRelationshipAddOperationPayloadData
from tidal.models.user_collection_save_for_laters_items_relationship_add_operation_response_meta_skipped_item import UserCollectionSaveForLatersItemsRelationshipAddOperationResponseMetaSkippedItem as UserCollectionSaveForLatersItemsRelationshipAddOperationResponseMetaSkippedItem
from tidal.models.user_collection_save_for_laters_items_relationship_remove_operation_payload import UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayload as UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayload
from tidal.models.user_collection_save_for_laters_items_relationship_remove_operation_payload_data import UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayloadData as UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayloadData
from tidal.models.user_collection_save_for_laters_items_resource_identifier import UserCollectionSaveForLatersItemsResourceIdentifier as UserCollectionSaveForLatersItemsResourceIdentifier
from tidal.models.user_collection_save_for_laters_items_resource_identifier_meta import UserCollectionSaveForLatersItemsResourceIdentifierMeta as UserCollectionSaveForLatersItemsResourceIdentifierMeta
from tidal.models.user_collection_save_for_laters_owners_multi_relationship_data_document import UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument as UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument
from tidal.models.user_collection_save_for_laters_relationships import UserCollectionSaveForLatersRelationships as UserCollectionSaveForLatersRelationships
from tidal.models.user_collection_save_for_laters_resource_object import UserCollectionSaveForLatersResourceObject as UserCollectionSaveForLatersResourceObject
from tidal.models.user_collection_save_for_laters_single_resource_data_document import UserCollectionSaveForLatersSingleResourceDataDocument as UserCollectionSaveForLatersSingleResourceDataDocument
from tidal.models.user_collection_tracks_attributes import UserCollectionTracksAttributes as UserCollectionTracksAttributes
from tidal.models.user_collection_tracks_items_add_multi_data_relationship_with_response409_response_body import UserCollectionTracksItemsAddMultiDataRelationshipWithResponse409ResponseBody as UserCollectionTracksItemsAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_collection_tracks_items_add_multi_relationship_data_document import UserCollectionTracksItemsAddMultiRelationshipDataDocument as UserCollectionTracksItemsAddMultiRelationshipDataDocument
from tidal.models.user_collection_tracks_items_add_multi_relationship_data_document_meta import UserCollectionTracksItemsAddMultiRelationshipDataDocumentMeta as UserCollectionTracksItemsAddMultiRelationshipDataDocumentMeta
from tidal.models.user_collection_tracks_items_add_resource_identifier import UserCollectionTracksItemsAddResourceIdentifier as UserCollectionTracksItemsAddResourceIdentifier
from tidal.models.user_collection_tracks_items_add_resource_identifier_meta import UserCollectionTracksItemsAddResourceIdentifierMeta as UserCollectionTracksItemsAddResourceIdentifierMeta
from tidal.models.user_collection_tracks_items_multi_relationship_data_document import UserCollectionTracksItemsMultiRelationshipDataDocument as UserCollectionTracksItemsMultiRelationshipDataDocument
from tidal.models.user_collection_tracks_items_read_multi_data_relationship403_response_body import UserCollectionTracksItemsReadMultiDataRelationship403ResponseBody as UserCollectionTracksItemsReadMultiDataRelationship403ResponseBody
from tidal.models.user_collection_tracks_items_relationship_add_operation_payload import UserCollectionTracksItemsRelationshipAddOperationPayload as UserCollectionTracksItemsRelationshipAddOperationPayload
from tidal.models.user_collection_tracks_items_relationship_add_operation_payload_data import UserCollectionTracksItemsRelationshipAddOperationPayloadData as UserCollectionTracksItemsRelationshipAddOperationPayloadData
from tidal.models.user_collection_tracks_items_relationship_add_operation_payload_data_meta import UserCollectionTracksItemsRelationshipAddOperationPayloadDataMeta as UserCollectionTracksItemsRelationshipAddOperationPayloadDataMeta
from tidal.models.user_collection_tracks_items_relationship_add_operation_response_meta_skipped_item import UserCollectionTracksItemsRelationshipAddOperationResponseMetaSkippedItem as UserCollectionTracksItemsRelationshipAddOperationResponseMetaSkippedItem
from tidal.models.user_collection_tracks_items_relationship_remove_operation_payload import UserCollectionTracksItemsRelationshipRemoveOperationPayload as UserCollectionTracksItemsRelationshipRemoveOperationPayload
from tidal.models.user_collection_tracks_items_relationship_remove_operation_payload_data import UserCollectionTracksItemsRelationshipRemoveOperationPayloadData as UserCollectionTracksItemsRelationshipRemoveOperationPayloadData
from tidal.models.user_collection_tracks_items_resource_identifier import UserCollectionTracksItemsResourceIdentifier as UserCollectionTracksItemsResourceIdentifier
from tidal.models.user_collection_tracks_items_resource_identifier_meta import UserCollectionTracksItemsResourceIdentifierMeta as UserCollectionTracksItemsResourceIdentifierMeta
from tidal.models.user_collection_tracks_owners_multi_relationship_data_document import UserCollectionTracksOwnersMultiRelationshipDataDocument as UserCollectionTracksOwnersMultiRelationshipDataDocument
from tidal.models.user_collection_tracks_relationships import UserCollectionTracksRelationships as UserCollectionTracksRelationships
from tidal.models.user_collection_tracks_resource_object import UserCollectionTracksResourceObject as UserCollectionTracksResourceObject
from tidal.models.user_collection_tracks_single_resource_data_document import UserCollectionTracksSingleResourceDataDocument as UserCollectionTracksSingleResourceDataDocument
from tidal.models.user_collection_videos_attributes import UserCollectionVideosAttributes as UserCollectionVideosAttributes
from tidal.models.user_collection_videos_items_add_multi_data_relationship_with_response409_response_body import UserCollectionVideosItemsAddMultiDataRelationshipWithResponse409ResponseBody as UserCollectionVideosItemsAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_collection_videos_items_add_multi_relationship_data_document import UserCollectionVideosItemsAddMultiRelationshipDataDocument as UserCollectionVideosItemsAddMultiRelationshipDataDocument
from tidal.models.user_collection_videos_items_add_multi_relationship_data_document_meta import UserCollectionVideosItemsAddMultiRelationshipDataDocumentMeta as UserCollectionVideosItemsAddMultiRelationshipDataDocumentMeta
from tidal.models.user_collection_videos_items_add_resource_identifier import UserCollectionVideosItemsAddResourceIdentifier as UserCollectionVideosItemsAddResourceIdentifier
from tidal.models.user_collection_videos_items_add_resource_identifier_meta import UserCollectionVideosItemsAddResourceIdentifierMeta as UserCollectionVideosItemsAddResourceIdentifierMeta
from tidal.models.user_collection_videos_items_multi_relationship_data_document import UserCollectionVideosItemsMultiRelationshipDataDocument as UserCollectionVideosItemsMultiRelationshipDataDocument
from tidal.models.user_collection_videos_items_read_multi_data_relationship403_response_body import UserCollectionVideosItemsReadMultiDataRelationship403ResponseBody as UserCollectionVideosItemsReadMultiDataRelationship403ResponseBody
from tidal.models.user_collection_videos_items_relationship_add_operation_payload import UserCollectionVideosItemsRelationshipAddOperationPayload as UserCollectionVideosItemsRelationshipAddOperationPayload
from tidal.models.user_collection_videos_items_relationship_add_operation_payload_data import UserCollectionVideosItemsRelationshipAddOperationPayloadData as UserCollectionVideosItemsRelationshipAddOperationPayloadData
from tidal.models.user_collection_videos_items_relationship_add_operation_payload_data_meta import UserCollectionVideosItemsRelationshipAddOperationPayloadDataMeta as UserCollectionVideosItemsRelationshipAddOperationPayloadDataMeta
from tidal.models.user_collection_videos_items_relationship_add_operation_response_meta_skipped_item import UserCollectionVideosItemsRelationshipAddOperationResponseMetaSkippedItem as UserCollectionVideosItemsRelationshipAddOperationResponseMetaSkippedItem
from tidal.models.user_collection_videos_items_relationship_remove_operation_payload import UserCollectionVideosItemsRelationshipRemoveOperationPayload as UserCollectionVideosItemsRelationshipRemoveOperationPayload
from tidal.models.user_collection_videos_items_relationship_remove_operation_payload_data import UserCollectionVideosItemsRelationshipRemoveOperationPayloadData as UserCollectionVideosItemsRelationshipRemoveOperationPayloadData
from tidal.models.user_collection_videos_items_resource_identifier import UserCollectionVideosItemsResourceIdentifier as UserCollectionVideosItemsResourceIdentifier
from tidal.models.user_collection_videos_items_resource_identifier_meta import UserCollectionVideosItemsResourceIdentifierMeta as UserCollectionVideosItemsResourceIdentifierMeta
from tidal.models.user_collection_videos_owners_multi_relationship_data_document import UserCollectionVideosOwnersMultiRelationshipDataDocument as UserCollectionVideosOwnersMultiRelationshipDataDocument
from tidal.models.user_collection_videos_relationships import UserCollectionVideosRelationships as UserCollectionVideosRelationships
from tidal.models.user_collection_videos_resource_object import UserCollectionVideosResourceObject as UserCollectionVideosResourceObject
from tidal.models.user_collection_videos_single_resource_data_document import UserCollectionVideosSingleResourceDataDocument as UserCollectionVideosSingleResourceDataDocument
from tidal.models.user_daily_mixes_items_multi_relationship_data_document import UserDailyMixesItemsMultiRelationshipDataDocument as UserDailyMixesItemsMultiRelationshipDataDocument
from tidal.models.user_daily_mixes_relationships import UserDailyMixesRelationships as UserDailyMixesRelationships
from tidal.models.user_daily_mixes_resource_object import UserDailyMixesResourceObject as UserDailyMixesResourceObject
from tidal.models.user_daily_mixes_single_resource_data_document import UserDailyMixesSingleResourceDataDocument as UserDailyMixesSingleResourceDataDocument
from tidal.models.user_data_export_requests_attributes import UserDataExportRequestsAttributes as UserDataExportRequestsAttributes
from tidal.models.user_data_export_requests_create_operation_payload import UserDataExportRequestsCreateOperationPayload as UserDataExportRequestsCreateOperationPayload
from tidal.models.user_data_export_requests_create_operation_payload_data import UserDataExportRequestsCreateOperationPayloadData as UserDataExportRequestsCreateOperationPayloadData
from tidal.models.user_data_export_requests_create_operation_payload_data_attributes import UserDataExportRequestsCreateOperationPayloadDataAttributes as UserDataExportRequestsCreateOperationPayloadDataAttributes
from tidal.models.user_data_export_requests_create_single_resource_data_document import UserDataExportRequestsCreateSingleResourceDataDocument as UserDataExportRequestsCreateSingleResourceDataDocument
from tidal.models.user_data_export_requests_resource_object import UserDataExportRequestsResourceObject as UserDataExportRequestsResourceObject
from tidal.models.user_data_exports_attributes import UserDataExportsAttributes as UserDataExportsAttributes
from tidal.models.user_data_exports_create_operation_payload import UserDataExportsCreateOperationPayload as UserDataExportsCreateOperationPayload
from tidal.models.user_data_exports_create_operation_payload_data import UserDataExportsCreateOperationPayloadData as UserDataExportsCreateOperationPayloadData
from tidal.models.user_data_exports_create_operation_payload_data_attributes import UserDataExportsCreateOperationPayloadDataAttributes as UserDataExportsCreateOperationPayloadDataAttributes
from tidal.models.user_data_exports_create_operation_payload_meta import UserDataExportsCreateOperationPayloadMeta as UserDataExportsCreateOperationPayloadMeta
from tidal.models.user_data_exports_create_resource400_response_body import UserDataExportsCreateResource400ResponseBody as UserDataExportsCreateResource400ResponseBody
from tidal.models.user_data_exports_create_resource400_response_body_errors_inner import UserDataExportsCreateResource400ResponseBodyErrorsInner as UserDataExportsCreateResource400ResponseBodyErrorsInner
from tidal.models.user_data_exports_create_resource409_response_body import UserDataExportsCreateResource409ResponseBody as UserDataExportsCreateResource409ResponseBody
from tidal.models.user_data_exports_create_resource409_response_body_errors_inner import UserDataExportsCreateResource409ResponseBodyErrorsInner as UserDataExportsCreateResource409ResponseBodyErrorsInner
from tidal.models.user_data_exports_create_single_resource_data_document import UserDataExportsCreateSingleResourceDataDocument as UserDataExportsCreateSingleResourceDataDocument
from tidal.models.user_data_exports_multi_resource_data_document import UserDataExportsMultiResourceDataDocument as UserDataExportsMultiResourceDataDocument
from tidal.models.user_data_exports_owners_multi_relationship_data_document import UserDataExportsOwnersMultiRelationshipDataDocument as UserDataExportsOwnersMultiRelationshipDataDocument
from tidal.models.user_data_exports_relationships import UserDataExportsRelationships as UserDataExportsRelationships
from tidal.models.user_data_exports_resource_object import UserDataExportsResourceObject as UserDataExportsResourceObject
from tidal.models.user_data_exports_single_resource_data_document import UserDataExportsSingleResourceDataDocument as UserDataExportsSingleResourceDataDocument
from tidal.models.user_discovery_mixes_items_multi_relationship_data_document import UserDiscoveryMixesItemsMultiRelationshipDataDocument as UserDiscoveryMixesItemsMultiRelationshipDataDocument
from tidal.models.user_discovery_mixes_relationships import UserDiscoveryMixesRelationships as UserDiscoveryMixesRelationships
from tidal.models.user_discovery_mixes_resource_object import UserDiscoveryMixesResourceObject as UserDiscoveryMixesResourceObject
from tidal.models.user_discovery_mixes_single_resource_data_document import UserDiscoveryMixesSingleResourceDataDocument as UserDiscoveryMixesSingleResourceDataDocument
from tidal.models.user_feed_item_activity_details import UserFeedItemActivityDetails as UserFeedItemActivityDetails
from tidal.models.user_feed_item_album_favourited_details import UserFeedItemAlbumFavouritedDetails as UserFeedItemAlbumFavouritedDetails
from tidal.models.user_feed_item_album_released_details import UserFeedItemAlbumReleasedDetails as UserFeedItemAlbumReleasedDetails
from tidal.models.user_feed_item_album_shared_details import UserFeedItemAlbumSharedDetails as UserFeedItemAlbumSharedDetails
from tidal.models.user_feed_item_artist_followed_details import UserFeedItemArtistFollowedDetails as UserFeedItemArtistFollowedDetails
from tidal.models.user_feed_item_comment_replied_details import UserFeedItemCommentRepliedDetails as UserFeedItemCommentRepliedDetails
from tidal.models.user_feed_item_copyright_flagged_details import UserFeedItemCopyrightFlaggedDetails as UserFeedItemCopyrightFlaggedDetails
from tidal.models.user_feed_item_history_mix_ready_details import UserFeedItemHistoryMixReadyDetails as UserFeedItemHistoryMixReadyDetails
from tidal.models.user_feed_item_playlist_updated_details import UserFeedItemPlaylistUpdatedDetails as UserFeedItemPlaylistUpdatedDetails
from tidal.models.user_feed_item_track_favourited_details import UserFeedItemTrackFavouritedDetails as UserFeedItemTrackFavouritedDetails
from tidal.models.user_feed_item_track_play_milestone_details import UserFeedItemTrackPlayMilestoneDetails as UserFeedItemTrackPlayMilestoneDetails
from tidal.models.user_feed_item_track_playlisted_details import UserFeedItemTrackPlaylistedDetails as UserFeedItemTrackPlaylistedDetails
from tidal.models.user_feed_item_track_source_file_commented_details import UserFeedItemTrackSourceFileCommentedDetails as UserFeedItemTrackSourceFileCommentedDetails
from tidal.models.user_feed_items_actors_multi_relationship_data_document import UserFeedItemsActorsMultiRelationshipDataDocument as UserFeedItemsActorsMultiRelationshipDataDocument
from tidal.models.user_feed_items_attributes import UserFeedItemsAttributes as UserFeedItemsAttributes
from tidal.models.user_feed_items_multi_resource_data_document import UserFeedItemsMultiResourceDataDocument as UserFeedItemsMultiResourceDataDocument
from tidal.models.user_feed_items_multi_resource_data_document_meta import UserFeedItemsMultiResourceDataDocumentMeta as UserFeedItemsMultiResourceDataDocumentMeta
from tidal.models.user_feed_items_relationships import UserFeedItemsRelationships as UserFeedItemsRelationships
from tidal.models.user_feed_items_resource_object import UserFeedItemsResourceObject as UserFeedItemsResourceObject
from tidal.models.user_feed_items_subject_resource_identifier import UserFeedItemsSubjectResourceIdentifier as UserFeedItemsSubjectResourceIdentifier
from tidal.models.user_feed_items_subject_resource_identifier_meta import UserFeedItemsSubjectResourceIdentifierMeta as UserFeedItemsSubjectResourceIdentifierMeta
from tidal.models.user_feed_items_subject_single_relationship_data_document import UserFeedItemsSubjectSingleRelationshipDataDocument as UserFeedItemsSubjectSingleRelationshipDataDocument
from tidal.models.user_feeds_attributes import UserFeedsAttributes as UserFeedsAttributes
from tidal.models.user_feeds_attributes_feed import UserFeedsAttributesFeed as UserFeedsAttributesFeed
from tidal.models.user_feeds_attributes_inbox import UserFeedsAttributesInbox as UserFeedsAttributesInbox
from tidal.models.user_feeds_resource_object import UserFeedsResourceObject as UserFeedsResourceObject
from tidal.models.user_feeds_single_resource_data_document import UserFeedsSingleResourceDataDocument as UserFeedsSingleResourceDataDocument
from tidal.models.user_feeds_update_operation_payload import UserFeedsUpdateOperationPayload as UserFeedsUpdateOperationPayload
from tidal.models.user_feeds_update_operation_payload_data import UserFeedsUpdateOperationPayloadData as UserFeedsUpdateOperationPayloadData
from tidal.models.user_feeds_update_operation_payload_data_attributes import UserFeedsUpdateOperationPayloadDataAttributes as UserFeedsUpdateOperationPayloadDataAttributes
from tidal.models.user_feeds_update_operation_payload_data_attributes_feed import UserFeedsUpdateOperationPayloadDataAttributesFeed as UserFeedsUpdateOperationPayloadDataAttributesFeed
from tidal.models.user_feeds_update_operation_payload_data_attributes_inbox import UserFeedsUpdateOperationPayloadDataAttributesInbox as UserFeedsUpdateOperationPayloadDataAttributesInbox
from tidal.models.user_feeds_update_single_resource_data_document import UserFeedsUpdateSingleResourceDataDocument as UserFeedsUpdateSingleResourceDataDocument
from tidal.models.user_new_release_mixes_items_multi_relationship_data_document import UserNewReleaseMixesItemsMultiRelationshipDataDocument as UserNewReleaseMixesItemsMultiRelationshipDataDocument
from tidal.models.user_new_release_mixes_relationships import UserNewReleaseMixesRelationships as UserNewReleaseMixesRelationships
from tidal.models.user_new_release_mixes_resource_object import UserNewReleaseMixesResourceObject as UserNewReleaseMixesResourceObject
from tidal.models.user_new_release_mixes_single_resource_data_document import UserNewReleaseMixesSingleResourceDataDocument as UserNewReleaseMixesSingleResourceDataDocument
from tidal.models.user_offline_mixes_items_multi_relationship_data_document import UserOfflineMixesItemsMultiRelationshipDataDocument as UserOfflineMixesItemsMultiRelationshipDataDocument
from tidal.models.user_offline_mixes_relationships import UserOfflineMixesRelationships as UserOfflineMixesRelationships
from tidal.models.user_offline_mixes_resource_object import UserOfflineMixesResourceObject as UserOfflineMixesResourceObject
from tidal.models.user_offline_mixes_single_resource_data_document import UserOfflineMixesSingleResourceDataDocument as UserOfflineMixesSingleResourceDataDocument
from tidal.models.user_playback_states_active_player_relationship_update_operation_payload import UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload as UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload
from tidal.models.user_playback_states_active_player_relationship_update_operation_payload_data import UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayloadData as UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayloadData
from tidal.models.user_playback_states_active_player_single_relationship_data_document import UserPlaybackStatesActivePlayerSingleRelationshipDataDocument as UserPlaybackStatesActivePlayerSingleRelationshipDataDocument
from tidal.models.user_playback_states_active_player_update_resource_identifier import UserPlaybackStatesActivePlayerUpdateResourceIdentifier as UserPlaybackStatesActivePlayerUpdateResourceIdentifier
from tidal.models.user_playback_states_active_player_update_single_relationship_data_document import UserPlaybackStatesActivePlayerUpdateSingleRelationshipDataDocument as UserPlaybackStatesActivePlayerUpdateSingleRelationshipDataDocument
from tidal.models.user_playback_states_attributes import UserPlaybackStatesAttributes as UserPlaybackStatesAttributes
from tidal.models.user_playback_states_available_players_add_multi_relationship_data_document import UserPlaybackStatesAvailablePlayersAddMultiRelationshipDataDocument as UserPlaybackStatesAvailablePlayersAddMultiRelationshipDataDocument
from tidal.models.user_playback_states_available_players_add_resource_identifier import UserPlaybackStatesAvailablePlayersAddResourceIdentifier as UserPlaybackStatesAvailablePlayersAddResourceIdentifier
from tidal.models.user_playback_states_available_players_multi_relationship_data_document import UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument as UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument
from tidal.models.user_playback_states_available_players_relationship_add_operation_payload import UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload as UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload
from tidal.models.user_playback_states_available_players_relationship_operation_payload_data import UserPlaybackStatesAvailablePlayersRelationshipOperationPayloadData as UserPlaybackStatesAvailablePlayersRelationshipOperationPayloadData
from tidal.models.user_playback_states_available_players_relationship_remove_operation_payload import UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload as UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload
from tidal.models.user_playback_states_change_event_stream_single_relationship_data_document import UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument as UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument
from tidal.models.user_playback_states_play_queue_relationship_update_operation_payload import UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload as UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload
from tidal.models.user_playback_states_play_queue_relationship_update_operation_payload_data import UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayloadData as UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayloadData
from tidal.models.user_playback_states_play_queue_single_relationship_data_document import UserPlaybackStatesPlayQueueSingleRelationshipDataDocument as UserPlaybackStatesPlayQueueSingleRelationshipDataDocument
from tidal.models.user_playback_states_play_queue_update_resource_identifier import UserPlaybackStatesPlayQueueUpdateResourceIdentifier as UserPlaybackStatesPlayQueueUpdateResourceIdentifier
from tidal.models.user_playback_states_play_queue_update_single_relationship_data_document import UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument as UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument
from tidal.models.user_playback_states_relationships import UserPlaybackStatesRelationships as UserPlaybackStatesRelationships
from tidal.models.user_playback_states_resource_object import UserPlaybackStatesResourceObject as UserPlaybackStatesResourceObject
from tidal.models.user_playback_states_single_resource_data_document import UserPlaybackStatesSingleResourceDataDocument as UserPlaybackStatesSingleResourceDataDocument
from tidal.models.user_playback_states_update_operation_payload import UserPlaybackStatesUpdateOperationPayload as UserPlaybackStatesUpdateOperationPayload
from tidal.models.user_playback_states_update_operation_payload_data import UserPlaybackStatesUpdateOperationPayloadData as UserPlaybackStatesUpdateOperationPayloadData
from tidal.models.user_playback_states_update_operation_payload_data_attributes import UserPlaybackStatesUpdateOperationPayloadDataAttributes as UserPlaybackStatesUpdateOperationPayloadDataAttributes
from tidal.models.user_playback_states_update_single_resource_data_document import UserPlaybackStatesUpdateSingleResourceDataDocument as UserPlaybackStatesUpdateSingleResourceDataDocument
from tidal.models.user_recommendation_blocks_artists_add_multi_data_relationship_with_response409_response_body import UserRecommendationBlocksArtistsAddMultiDataRelationshipWithResponse409ResponseBody as UserRecommendationBlocksArtistsAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_recommendation_blocks_artists_add_multi_data_relationship_with_response409_response_body_errors_inner import UserRecommendationBlocksArtistsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner as UserRecommendationBlocksArtistsAddMultiDataRelationshipWithResponse409ResponseBodyErrorsInner
from tidal.models.user_recommendation_blocks_artists_add_multi_relationship_data_document import UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument as UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_artists_add_resource_identifier import UserRecommendationBlocksArtistsAddResourceIdentifier as UserRecommendationBlocksArtistsAddResourceIdentifier
from tidal.models.user_recommendation_blocks_artists_multi_relationship_data_document import UserRecommendationBlocksArtistsMultiRelationshipDataDocument as UserRecommendationBlocksArtistsMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_artists_relationship_add_operation_payload import UserRecommendationBlocksArtistsRelationshipAddOperationPayload as UserRecommendationBlocksArtistsRelationshipAddOperationPayload
from tidal.models.user_recommendation_blocks_artists_relationship_add_operation_payload_data import UserRecommendationBlocksArtistsRelationshipAddOperationPayloadData as UserRecommendationBlocksArtistsRelationshipAddOperationPayloadData
from tidal.models.user_recommendation_blocks_artists_relationship_remove_operation_payload import UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload as UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload
from tidal.models.user_recommendation_blocks_artists_relationship_remove_operation_payload_data import UserRecommendationBlocksArtistsRelationshipRemoveOperationPayloadData as UserRecommendationBlocksArtistsRelationshipRemoveOperationPayloadData
from tidal.models.user_recommendation_blocks_artists_resource_identifier import UserRecommendationBlocksArtistsResourceIdentifier as UserRecommendationBlocksArtistsResourceIdentifier
from tidal.models.user_recommendation_blocks_artists_resource_identifier_meta import UserRecommendationBlocksArtistsResourceIdentifierMeta as UserRecommendationBlocksArtistsResourceIdentifierMeta
from tidal.models.user_recommendation_blocks_owners_multi_relationship_data_document import UserRecommendationBlocksOwnersMultiRelationshipDataDocument as UserRecommendationBlocksOwnersMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_relationships import UserRecommendationBlocksRelationships as UserRecommendationBlocksRelationships
from tidal.models.user_recommendation_blocks_resource_object import UserRecommendationBlocksResourceObject as UserRecommendationBlocksResourceObject
from tidal.models.user_recommendation_blocks_single_resource_data_document import UserRecommendationBlocksSingleResourceDataDocument as UserRecommendationBlocksSingleResourceDataDocument
from tidal.models.user_recommendation_blocks_tracks_add_multi_data_relationship_with_response409_response_body import UserRecommendationBlocksTracksAddMultiDataRelationshipWithResponse409ResponseBody as UserRecommendationBlocksTracksAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_recommendation_blocks_tracks_add_multi_relationship_data_document import UserRecommendationBlocksTracksAddMultiRelationshipDataDocument as UserRecommendationBlocksTracksAddMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_tracks_add_resource_identifier import UserRecommendationBlocksTracksAddResourceIdentifier as UserRecommendationBlocksTracksAddResourceIdentifier
from tidal.models.user_recommendation_blocks_tracks_multi_relationship_data_document import UserRecommendationBlocksTracksMultiRelationshipDataDocument as UserRecommendationBlocksTracksMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_tracks_relationship_add_operation_payload import UserRecommendationBlocksTracksRelationshipAddOperationPayload as UserRecommendationBlocksTracksRelationshipAddOperationPayload
from tidal.models.user_recommendation_blocks_tracks_relationship_add_operation_payload_data import UserRecommendationBlocksTracksRelationshipAddOperationPayloadData as UserRecommendationBlocksTracksRelationshipAddOperationPayloadData
from tidal.models.user_recommendation_blocks_tracks_relationship_remove_operation_payload import UserRecommendationBlocksTracksRelationshipRemoveOperationPayload as UserRecommendationBlocksTracksRelationshipRemoveOperationPayload
from tidal.models.user_recommendation_blocks_tracks_relationship_remove_operation_payload_data import UserRecommendationBlocksTracksRelationshipRemoveOperationPayloadData as UserRecommendationBlocksTracksRelationshipRemoveOperationPayloadData
from tidal.models.user_recommendation_blocks_tracks_resource_identifier import UserRecommendationBlocksTracksResourceIdentifier as UserRecommendationBlocksTracksResourceIdentifier
from tidal.models.user_recommendation_blocks_tracks_resource_identifier_meta import UserRecommendationBlocksTracksResourceIdentifierMeta as UserRecommendationBlocksTracksResourceIdentifierMeta
from tidal.models.user_recommendation_blocks_videos_add_multi_data_relationship_with_response409_response_body import UserRecommendationBlocksVideosAddMultiDataRelationshipWithResponse409ResponseBody as UserRecommendationBlocksVideosAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_recommendation_blocks_videos_add_multi_relationship_data_document import UserRecommendationBlocksVideosAddMultiRelationshipDataDocument as UserRecommendationBlocksVideosAddMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_videos_add_resource_identifier import UserRecommendationBlocksVideosAddResourceIdentifier as UserRecommendationBlocksVideosAddResourceIdentifier
from tidal.models.user_recommendation_blocks_videos_multi_relationship_data_document import UserRecommendationBlocksVideosMultiRelationshipDataDocument as UserRecommendationBlocksVideosMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_videos_relationship_add_operation_payload import UserRecommendationBlocksVideosRelationshipAddOperationPayload as UserRecommendationBlocksVideosRelationshipAddOperationPayload
from tidal.models.user_recommendation_blocks_videos_relationship_add_operation_payload_data import UserRecommendationBlocksVideosRelationshipAddOperationPayloadData as UserRecommendationBlocksVideosRelationshipAddOperationPayloadData
from tidal.models.user_recommendation_blocks_videos_relationship_remove_operation_payload import UserRecommendationBlocksVideosRelationshipRemoveOperationPayload as UserRecommendationBlocksVideosRelationshipRemoveOperationPayload
from tidal.models.user_recommendation_blocks_videos_relationship_remove_operation_payload_data import UserRecommendationBlocksVideosRelationshipRemoveOperationPayloadData as UserRecommendationBlocksVideosRelationshipRemoveOperationPayloadData
from tidal.models.user_recommendation_blocks_videos_resource_identifier import UserRecommendationBlocksVideosResourceIdentifier as UserRecommendationBlocksVideosResourceIdentifier
from tidal.models.user_recommendation_blocks_videos_resource_identifier_meta import UserRecommendationBlocksVideosResourceIdentifierMeta as UserRecommendationBlocksVideosResourceIdentifierMeta
from tidal.models.user_reports_attributes import UserReportsAttributes as UserReportsAttributes
from tidal.models.user_reports_create_operation_payload import UserReportsCreateOperationPayload as UserReportsCreateOperationPayload
from tidal.models.user_reports_create_operation_payload_data import UserReportsCreateOperationPayloadData as UserReportsCreateOperationPayloadData
from tidal.models.user_reports_create_operation_payload_data_attributes import UserReportsCreateOperationPayloadDataAttributes as UserReportsCreateOperationPayloadDataAttributes
from tidal.models.user_reports_create_operation_payload_data_relationships import UserReportsCreateOperationPayloadDataRelationships as UserReportsCreateOperationPayloadDataRelationships
from tidal.models.user_reports_create_operation_payload_data_relationships_reported_resources import UserReportsCreateOperationPayloadDataRelationshipsReportedResources as UserReportsCreateOperationPayloadDataRelationshipsReportedResources
from tidal.models.user_reports_create_operation_payload_data_relationships_reported_resources_data import UserReportsCreateOperationPayloadDataRelationshipsReportedResourcesData as UserReportsCreateOperationPayloadDataRelationshipsReportedResourcesData
from tidal.models.user_reports_create_resource403_response_body import UserReportsCreateResource403ResponseBody as UserReportsCreateResource403ResponseBody
from tidal.models.user_reports_create_resource403_response_body_errors_inner import UserReportsCreateResource403ResponseBodyErrorsInner as UserReportsCreateResource403ResponseBodyErrorsInner
from tidal.models.user_reports_create_single_resource_data_document import UserReportsCreateSingleResourceDataDocument as UserReportsCreateSingleResourceDataDocument
from tidal.models.user_reports_resource_object import UserReportsResourceObject as UserReportsResourceObject
from tidal.models.user_subscription_price_changes_attributes import UserSubscriptionPriceChangesAttributes as UserSubscriptionPriceChangesAttributes
from tidal.models.user_subscription_price_changes_decision_single_relationship_data_document import UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument as UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument
from tidal.models.user_subscription_price_changes_multi_resource_data_document import UserSubscriptionPriceChangesMultiResourceDataDocument as UserSubscriptionPriceChangesMultiResourceDataDocument
from tidal.models.user_subscription_price_changes_relationships import UserSubscriptionPriceChangesRelationships as UserSubscriptionPriceChangesRelationships
from tidal.models.user_subscription_price_changes_resource_object import UserSubscriptionPriceChangesResourceObject as UserSubscriptionPriceChangesResourceObject
from tidal.models.users_artist_single_relationship_data_document import UsersArtistSingleRelationshipDataDocument as UsersArtistSingleRelationshipDataDocument
from tidal.models.users_attributes import UsersAttributes as UsersAttributes
from tidal.models.users_relationships import UsersRelationships as UsersRelationships
from tidal.models.users_resource_object import UsersResourceObject as UsersResourceObject
from tidal.models.users_single_resource_data_document import UsersSingleResourceDataDocument as UsersSingleResourceDataDocument
from tidal.models.variation import Variation as Variation
from tidal.models.video_manifests_attributes import VideoManifestsAttributes as VideoManifestsAttributes
from tidal.models.video_manifests_read_by_id403_response_body import VideoManifestsReadById403ResponseBody as VideoManifestsReadById403ResponseBody
from tidal.models.video_manifests_read_by_id404_response_body import VideoManifestsReadById404ResponseBody as VideoManifestsReadById404ResponseBody
from tidal.models.video_manifests_resource_object import VideoManifestsResourceObject as VideoManifestsResourceObject
from tidal.models.video_manifests_single_resource_data_document import VideoManifestsSingleResourceDataDocument as VideoManifestsSingleResourceDataDocument
from tidal.models.videos_albums_multi_relationship_data_document import VideosAlbumsMultiRelationshipDataDocument as VideosAlbumsMultiRelationshipDataDocument
from tidal.models.videos_albums_resource_identifier import VideosAlbumsResourceIdentifier as VideosAlbumsResourceIdentifier
from tidal.models.videos_albums_resource_identifier_meta import VideosAlbumsResourceIdentifierMeta as VideosAlbumsResourceIdentifierMeta
from tidal.models.videos_artists_multi_relationship_data_document import VideosArtistsMultiRelationshipDataDocument as VideosArtistsMultiRelationshipDataDocument
from tidal.models.videos_attributes import VideosAttributes as VideosAttributes
from tidal.models.videos_credits_multi_relationship_data_document import VideosCreditsMultiRelationshipDataDocument as VideosCreditsMultiRelationshipDataDocument
from tidal.models.videos_multi_resource_data_document import VideosMultiResourceDataDocument as VideosMultiResourceDataDocument
from tidal.models.videos_providers_multi_relationship_data_document import VideosProvidersMultiRelationshipDataDocument as VideosProvidersMultiRelationshipDataDocument
from tidal.models.videos_relationships import VideosRelationships as VideosRelationships
from tidal.models.videos_replacement_resource_identifier import VideosReplacementResourceIdentifier as VideosReplacementResourceIdentifier
from tidal.models.videos_replacement_resource_identifier_meta import VideosReplacementResourceIdentifierMeta as VideosReplacementResourceIdentifierMeta
from tidal.models.videos_replacement_single_relationship_data_document import VideosReplacementSingleRelationshipDataDocument as VideosReplacementSingleRelationshipDataDocument
from tidal.models.videos_resource_object import VideosResourceObject as VideosResourceObject
from tidal.models.videos_similar_videos_multi_relationship_data_document import VideosSimilarVideosMultiRelationshipDataDocument as VideosSimilarVideosMultiRelationshipDataDocument
from tidal.models.videos_similar_videos_resource_identifier import VideosSimilarVideosResourceIdentifier as VideosSimilarVideosResourceIdentifier
from tidal.models.videos_similar_videos_resource_identifier_meta import VideosSimilarVideosResourceIdentifierMeta as VideosSimilarVideosResourceIdentifierMeta
from tidal.models.videos_single_resource_data_document import VideosSingleResourceDataDocument as VideosSingleResourceDataDocument
from tidal.models.videos_suggested_videos_multi_relationship_data_document import VideosSuggestedVideosMultiRelationshipDataDocument as VideosSuggestedVideosMultiRelationshipDataDocument
from tidal.models.videos_suggested_videos_resource_identifier import VideosSuggestedVideosResourceIdentifier as VideosSuggestedVideosResourceIdentifier
from tidal.models.videos_suggested_videos_resource_identifier_meta import VideosSuggestedVideosResourceIdentifierMeta as VideosSuggestedVideosResourceIdentifierMeta
from tidal.models.videos_thumbnail_art_multi_relationship_data_document import VideosThumbnailArtMultiRelationshipDataDocument as VideosThumbnailArtMultiRelationshipDataDocument
from tidal.models.videos_usage_rules_single_relationship_data_document import VideosUsageRulesSingleRelationshipDataDocument as VideosUsageRulesSingleRelationshipDataDocument
from tidal.models.viewer_contexts_attributes import ViewerContextsAttributes as ViewerContextsAttributes
from tidal.models.viewer_contexts_comments_multi_relationship_data_document import ViewerContextsCommentsMultiRelationshipDataDocument as ViewerContextsCommentsMultiRelationshipDataDocument
from tidal.models.viewer_contexts_multi_resource_data_document import ViewerContextsMultiResourceDataDocument as ViewerContextsMultiResourceDataDocument
from tidal.models.viewer_contexts_reactions_multi_relationship_data_document import ViewerContextsReactionsMultiRelationshipDataDocument as ViewerContextsReactionsMultiRelationshipDataDocument
from tidal.models.viewer_contexts_relationships import ViewerContextsRelationships as ViewerContextsRelationships
from tidal.models.viewer_contexts_resource_object import ViewerContextsResourceObject as ViewerContextsResourceObject
from tidal.models.viewer_contexts_single_resource_data_document import ViewerContextsSingleResourceDataDocument as ViewerContextsSingleResourceDataDocument
from tidal.models.viewer_contexts_subject_resource_identifier import ViewerContextsSubjectResourceIdentifier as ViewerContextsSubjectResourceIdentifier
from tidal.models.viewer_contexts_subject_resource_identifier_meta import ViewerContextsSubjectResourceIdentifierMeta as ViewerContextsSubjectResourceIdentifierMeta
from tidal.models.viewer_contexts_subject_single_relationship_data_document import ViewerContextsSubjectSingleRelationshipDataDocument as ViewerContextsSubjectSingleRelationshipDataDocument
from tidal.models.viewer_contexts_viewer_single_relationship_data_document import ViewerContextsViewerSingleRelationshipDataDocument as ViewerContextsViewerSingleRelationshipDataDocument
from tidal.models.waveform import Waveform as Waveform

