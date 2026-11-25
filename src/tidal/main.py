# coding: utf-8

"""
    TIDAL API

    The TIDAL API is a [JSON:API](https://jsonapi.org/)-compliant web API exposing TIDAL's music catalogue, metadata, and user functionality. Guides, authorization documentation, and API key management live at [developer.tidal.com](https://developer.tidal.com).  All endpoints exchange `application/vnd.api+json` documents per the [JSON:API specification](https://jsonapi.org/format/): [resource objects](https://jsonapi.org/format/#document-resource-objects) with `attributes` and `relationships`, [compound documents](https://jsonapi.org/format/#document-compound-documents) via `include`, and standard [error objects](https://jsonapi.org/format/#error-objects).  ### Authentication and authorization  Every request requires an OAuth 2.0 access token in the `Authorization: Bearer` header. Tokens are issued at `https://auth.tidal.com/v1/oauth2/token` via the client-credentials flow (server-to-server) or the authorization-code + PKCE flow (user context; authorize at `https://login.tidal.com/authorize`). Each endpoint documents which flows it accepts, the access tier it requires, and the scopes that apply. Scopes protect private user data: fields you are not authorized to read are redacted from the response rather than causing an error, and resources you cannot access at all behave as if they do not exist. See the [authorization guide](https://developer.tidal.com/documentation/api-sdk/api-sdk-authorization) for details.  ### Common wire types and compatibility  Each property's schema is authoritative for its allowed values, format, requiredness, nullability, and constraints. A standard defines how a value is represented; an individual schema may support only a documented subset.  - **Enums** use `UPPER_CASE_UNDERSCORE`, except JSON:API resource types, which use plural camelCase names such as `playlistGenerationSchedules`. New values can be added to any enum at any time, so treat unknown values as forward-compatible rather than errors. - **Resource IDs** are opaque strings. A few resources document well-known IDs for permanent system singleton instances; compare those IDs by exact value. Never parse, construct, or infer meaning from any other `id`, even when its current representation resembles an integer, UUID, or another recognizable value. Other properties explicitly marked with OpenAPI `format: uuid` are UUIDs. - **Dates and times** use ISO 8601. Date-times use the OpenAPI `date-time` format (`2024-05-01T12:00:00Z`), dates use `YYYY-MM-DD`, and durations use values such as `PT3M5S`. - **Recurrence frequencies** use RFC 5545 `FREQ` names such as `DAILY`, `WEEKLY`, and `MONTHLY`. The property's enum lists the frequencies that field currently supports. - **Weekdays** use `MONDAY` through `SUNDAY`. - **Time zones** use IANA Time Zone Database identifiers such as `Europe/Stockholm`, not abbreviations or raw UTC offsets for recurring civil-time schedules. - **Country codes** use ISO 3166-1 alpha-2; the shared country type also accepts `WW` for worldwide. **Locales** use IETF BCP 47 language tags such as `en-US`. - **Currencies** use ISO 4217 codes. Monetary amounts are decimal strings; each field defines its sign and precision constraints. - **Colors** use three- or six-digit hexadecimal strings (`#RGB` or `#RRGGBB`). Resource links to external URLs use JSON:API link objects with an `href` member.  ### Resource identifiers  Where supported, `filter[subject]=tracks:123` matches a related resource by type and ID; `filter[subject.id]=123` and `filter[subject.type]=tracks` match either component. Where multiple identifiers are accepted, comma-separated values match any complete pair. When a member path names a to-many relationship, at least one related resource must match; filtering does not trim that relationship. On collection and to-many relationship reads, the reserved root `self` (`filter[self]=tracks:123`) filters primary data itself. Each endpoint lists its supported filters and types.  Where supported, `me` aliases the authenticated user's dedicated resource ID for the referenced resource type. It works in paths, resource-ID filters, compact identifiers (`type:me`), resource PATCH primary IDs and standalone relationship mutation identifiers, with the same meaning as the resolved ID. Reads using the alias are `no-store`.  ### Relationships and includes  [Relationships](https://jsonapi.org/format/#document-resource-object-relationships) are returned only on request: [`include`](https://jsonapi.org/format/#fetching-includes) selects linkage and related content, while `includeLinkage` selects authorized linkage only. A relationship that was not requested is absent from the response, not empty. The full set of relationships a resource supports is documented in its schema.  For INTERNAL clients on resource GET endpoints, `includeLinkage` accepts comma-separated direct relationship names, for example `includeLinkage=subject,viewer`. It does not load related resources or add an `included` section. Nested paths and type qualifiers are unsupported. To-many linkage retains its normal pagination and relationship `next` links. Selecting the same relationship with both parameters applies full include behavior and reads the relationship once.  Request related resources in one round trip with `?include=`, a comma-separated list of dot-separated relationship paths — e.g. `include=coverArt,artists.profileArt` on an album. A nested path automatically embeds its intermediate resources: `artists.profileArt` includes the artists as well as their profile art. Include paths are always relative to the request's root resource, also on relationship endpoints. Including a relationship never changes the primary data; the related resources are added to `included`.  Include paths are validated: a path that cannot be resolved against the resources' documented relationships is rejected with `400`. Include trees are also bounded in path depth (default 3 levels) and in the total number of distinct resources they name (default 10); individual endpoints may apply different limits. Both selectors share the include-node limit, counting overlapping roots once. A request exceeding either limit is rejected with `400`, with the effective limit stated in the error.  ### Filtering, sorting, pagination  - [`filter[<memberPath>]=value`](https://jsonapi.org/format/#fetching-filtering) filters primary data by equality. Each endpoint lists its available filters; most collections require at least one. - Where explicitly documented, `filter[<memberPath>][ne]=value` negates the complete equality predicate. When the member path names a to-many relationship, no related ID may match any supplied value; a known-empty relationship matches. Operators are separate from values. Supplied comparisons combine with AND. For a required filter with multiple supported comparisons, at least one must be supplied; the parameter descriptions identify these alternatives. Unsupported operators and groups return `400`. - Where documented, `filter[<path>][<operator>]=value` applies an endpoint-defined operator, such as `filter[self][matchesQuery]`. Its meaning is described per endpoint, and it combines with other filters by AND. - [`sort=<memberPath>`](https://jsonapi.org/format/#fetching-sorting) sorts ascending, `-<memberPath>` descending (`sort=-addedAt`). Filter and sort member paths are relative to primary data. - Parameters an endpoint cannot honor are rejected with `400`: a `filter[...]` parameter the endpoint does not document (the error lists the available filters), or `sort` on an endpoint that documents no sort values. - [Pagination](https://jsonapi.org/format/#fetching-pagination) is cursor-based: responses carry `links.self` and, while more pages exist, `links.next` with an opaque `page[cursor]`. Follow `next` until absent — there are no offset or total-page parameters. Collection sizes, when available, appear as `meta.total` and may be approximate.  ### Type qualifiers  Where a relationship can contain several resource types, a path segment may be prefixed with a concrete type to scope which type's member is accessed. A playlist's `items` are `tracks` or `videos`: `GET /playlists/{id}?include=items.tracks:albums` resolves `albums` only for the items that are tracks. Qualifiers scope member access — they never filter which resources appear in a relationship — and can be chained.  The same syntax applies to `filter` and `sort` member paths on endpoints that support it; where supported, the qualified member is listed among the endpoint's documented filters and sort values. The syntax follows JSON:API proposal [json-api#1695](https://github.com/json-api/json-api/issues/1695).  ### Mutations  - [Partial updates](https://jsonapi.org/format/#crud-updating-resource-attributes) distinguish three wire states for nullable attributes: omission leaves the current value unchanged, an explicit `null` clears it, and a concrete value updates it. - Every mutation accepts an [`Idempotency-Key`](https://www.ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-07.html) header. Keys are scoped to the client and the authenticated user. Once the original request has completed, retrying it with the same key, method, path, query and payload within one hour replays its response; a retry while it is still processing is rejected with `409`, and the same key with a different method, path, query or payload with `422`. - After a successful write, your own subsequent reads reflect the change; other clients may observe it with a delay.  ### Revisions and concurrent editing  Where supported, `attributes.revision` identifies the resource's documented aggregate state; a separately versioned relationship collection uses document `meta.revision`. Revisions are nonnegative integers that increase when covered state changes. Compare them only within the same identity and scope, preserve the exact value, and never calculate the next revision. Related content, viewer projections and independent sources are not automatically covered. Domain fields named `version`, such as a music edition, are distinct; existing endpoints retain their documented contracts.  Guarded mutations accept the observed value as top-level `meta.expectedRevision`. Each operation declares its scope and whether the precondition is required. A mismatch returns `409`; missing required input returns `400`. Refresh and reconcile after a conflict, then submit a new operation with a new idempotency key. An identical retry with the original key replays a recorded success under the idempotency contract. These revisions are not HTTP ETags.  Returned revisions describe observed snapshots, not reservations for later writes. Background changes can advance them immediately after a successful response.  ### Media resource replacements - BETA Internal only  Media resources (`tracks`, `videos`, and `albums`) can become unavailable in a country when licensing rights change. By default, TIDAL API returns the resource identifiers originally stored in a collection. This keeps ordinary reads predictable and consistent.  If a stored media resource is unavailable for the effective country, TIDAL may identify a contextually applicable alternative that is available there. Replacement is best effort, so an alternative is not always available. Replacement never changes the stored collection.  TIDAL API provides two ways to work with replacements:  1. **Inspect the `replacement` relationship.** A media resource can expose its applicable alternative through the `replacement` relationship. Include this relationship when a client needs both the original and replacement identifiers or wants to decide whether to use the replacement.  2. **Apply replacements with `replaceMedia`.** Clients can use `replaceMedia` to substitute applicable replacements directly into selected relationship data. The parameter accepts relationship paths using the same syntax as `include`. Projection affects only the response and preserves relationship order and metadata. Each identifier includes `meta.replacement` describing whether it was `ORIGINAL`, `REPLACED`, or `NOT_REPLACED`.  For example, `GET /playlists/{id}?include=items&replaceMedia=items` applies replacements to media identifiers in the playlist's `items` relationship.  ### Compression  Responses are gzip-compressed when the request includes `Accept-Encoding: gzip` (bodies over 2 KB).  ### Deprecation  Deprecated endpoints, parameters, and fields are marked `deprecated` in this specification, with the replacement noted in their description. Deprecated functionality keeps working for at least six months after being marked, and is only removed once a replacement is generally available.

    The version of the OpenAPI document: 1.10.263
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from fastapi import FastAPI

from api.accepted_terms_api import router as AcceptedTermsApiRouter
from api.album_statistics_api import router as AlbumStatisticsApiRouter
from api.albums_api import router as AlbumsApiRouter
from api.appreciations_api import router as AppreciationsApiRouter
from api.artist_biographies_api import router as ArtistBiographiesApiRouter
from api.artist_claim_statuses_api import router as ArtistClaimStatusesApiRouter
from api.artist_claims_api import router as ArtistClaimsApiRouter
from api.artist_roles_api import router as ArtistRolesApiRouter
from api.artist_sales_statistics_api import router as ArtistSalesStatisticsApiRouter
from api.artist_streams_statistics_api import router as ArtistStreamsStatisticsApiRouter
from api.artists_api import router as ArtistsApiRouter
from api.artwork_libraries_api import router as ArtworkLibrariesApiRouter
from api.artworks_api import router as ArtworksApiRouter
from api.client_certificates_api import router as ClientCertificatesApiRouter
from api.clients_api import router as ClientsApiRouter
from api.collaboration_invite_redemptions_api import router as CollaborationInviteRedemptionsApiRouter
from api.collaboration_invites_api import router as CollaborationInvitesApiRouter
from api.comment_summaries_api import router as CommentSummariesApiRouter
from api.comments_api import router as CommentsApiRouter
from api.content_claims_api import router as ContentClaimsApiRouter
from api.credits_api import router as CreditsApiRouter
from api.downloads_api import router as DownloadsApiRouter
from api.dsp_sharing_links_api import router as DspSharingLinksApiRouter
from api.dynamic_modules_api import router as DynamicModulesApiRouter
from api.dynamic_pages_api import router as DynamicPagesApiRouter
from api.folder_items_api import router as FolderItemsApiRouter
from api.folders_api import router as FoldersApiRouter
from api.genres_api import router as GenresApiRouter
from api.groups_api import router as GroupsApiRouter
from api.installations_api import router as InstallationsApiRouter
from api.lyrics_api import router as LyricsApiRouter
from api.manual_artist_claims_api import router as ManualArtistClaimsApiRouter
from api.offline_tasks_api import router as OfflineTasksApiRouter
from api.play_queues_api import router as PlayQueuesApiRouter
from api.playlist_generation_schedules_api import router as PlaylistGenerationSchedulesApiRouter
from api.playlist_generations_api import router as PlaylistGenerationsApiRouter
from api.playlists_api import router as PlaylistsApiRouter
from api.price_configurations_api import router as PriceConfigurationsApiRouter
from api.provider_owners_api import router as ProviderOwnersApiRouter
from api.provider_product_infos_api import router as ProviderProductInfosApiRouter
from api.providers_api import router as ProvidersApiRouter
from api.purchases_api import router as PurchasesApiRouter
from api.reaction_summaries_api import router as ReactionSummariesApiRouter
from api.reactions_api import router as ReactionsApiRouter
from api.resource_grant_invitations_api import router as ResourceGrantInvitationsApiRouter
from api.resource_grants_api import router as ResourceGrantsApiRouter
from api.saved_shares_api import router as SavedSharesApiRouter
from api.scopes_api import router as ScopesApiRouter
from api.search_history_entries_api import router as SearchHistoryEntriesApiRouter
from api.search_results_api import router as SearchResultsApiRouter
from api.search_suggestions_api import router as SearchSuggestionsApiRouter
from api.shares_api import router as SharesApiRouter
from api.sharing_summaries_api import router as SharingSummariesApiRouter
from api.square_connections_api import router as SquareConnectionsApiRouter
from api.square_item_variation_physical_counts_api import router as SquareItemVariationPhysicalCountsApiRouter
from api.square_item_variations_api import router as SquareItemVariationsApiRouter
from api.square_items_api import router as SquareItemsApiRouter
from api.square_sites_api import router as SquareSitesApiRouter
from api.stripe_connections_api import router as StripeConnectionsApiRouter
from api.stripe_dashboard_links_api import router as StripeDashboardLinksApiRouter
from api.studio_home_event_tiles_api import router as StudioHomeEventTilesApiRouter
from api.studio_home_insight_tiles_api import router as StudioHomeInsightTilesApiRouter
from api.studio_home_merch_tiles_api import router as StudioHomeMerchTilesApiRouter
from api.studio_home_music_tiles_api import router as StudioHomeMusicTilesApiRouter
from api.subscription_price_change_decisions_api import router as SubscriptionPriceChangeDecisionsApiRouter
from api.temporary_user_tokens_api import router as TemporaryUserTokensApiRouter
from api.terms_api import router as TermsApiRouter
from api.track_files_api import router as TrackFilesApiRouter
from api.track_manifests_api import router as TrackManifestsApiRouter
from api.track_source_files_api import router as TrackSourceFilesApiRouter
from api.track_statistics_api import router as TrackStatisticsApiRouter
from api.tracks_api import router as TracksApiRouter
from api.tracks_metadata_status_api import router as TracksMetadataStatusApiRouter
from api.usage_rules_api import router as UsageRulesApiRouter
from api.user_collection_albums_api import router as UserCollectionAlbumsApiRouter
from api.user_collection_artists_api import router as UserCollectionArtistsApiRouter
from api.user_collection_folders_api import router as UserCollectionFoldersApiRouter
from api.user_collection_playlists_api import router as UserCollectionPlaylistsApiRouter
from api.user_collection_save_for_laters_api import router as UserCollectionSaveForLatersApiRouter
from api.user_collection_tracks_api import router as UserCollectionTracksApiRouter
from api.user_collection_videos_api import router as UserCollectionVideosApiRouter
from api.user_daily_mixes_api import router as UserDailyMixesApiRouter
from api.user_data_export_requests_api import router as UserDataExportRequestsApiRouter
from api.user_data_exports_api import router as UserDataExportsApiRouter
from api.user_discovery_mixes_api import router as UserDiscoveryMixesApiRouter
from api.user_feed_items_api import router as UserFeedItemsApiRouter
from api.user_feeds_api import router as UserFeedsApiRouter
from api.user_new_release_mixes_api import router as UserNewReleaseMixesApiRouter
from api.user_offline_mixes_api import router as UserOfflineMixesApiRouter
from api.user_playback_states_api import router as UserPlaybackStatesApiRouter
from api.user_recommendation_blocks_api import router as UserRecommendationBlocksApiRouter
from api.user_reports_api import router as UserReportsApiRouter
from api.user_subscription_price_changes_api import router as UserSubscriptionPriceChangesApiRouter
from api.users_api import router as UsersApiRouter
from api.video_manifests_api import router as VideoManifestsApiRouter
from api.videos_api import router as VideosApiRouter
from api.viewer_contexts_api import router as ViewerContextsApiRouter

app = FastAPI(
    title="TIDAL API",
    description="The TIDAL API is a [JSON:API](https://jsonapi.org/)-compliant web API exposing TIDAL&#39;s music catalogue, metadata, and user functionality. Guides, authorization documentation, and API key management live at [developer.tidal.com](https://developer.tidal.com).  All endpoints exchange &#x60;application/vnd.api+json&#x60; documents per the [JSON:API specification](https://jsonapi.org/format/): [resource objects](https://jsonapi.org/format/#document-resource-objects) with &#x60;attributes&#x60; and &#x60;relationships&#x60;, [compound documents](https://jsonapi.org/format/#document-compound-documents) via &#x60;include&#x60;, and standard [error objects](https://jsonapi.org/format/#error-objects).  ### Authentication and authorization  Every request requires an OAuth 2.0 access token in the &#x60;Authorization: Bearer&#x60; header. Tokens are issued at &#x60;https://auth.tidal.com/v1/oauth2/token&#x60; via the client-credentials flow (server-to-server) or the authorization-code + PKCE flow (user context; authorize at &#x60;https://login.tidal.com/authorize&#x60;). Each endpoint documents which flows it accepts, the access tier it requires, and the scopes that apply. Scopes protect private user data: fields you are not authorized to read are redacted from the response rather than causing an error, and resources you cannot access at all behave as if they do not exist. See the [authorization guide](https://developer.tidal.com/documentation/api-sdk/api-sdk-authorization) for details.  ### Common wire types and compatibility  Each property&#39;s schema is authoritative for its allowed values, format, requiredness, nullability, and constraints. A standard defines how a value is represented; an individual schema may support only a documented subset.  - **Enums** use &#x60;UPPER_CASE_UNDERSCORE&#x60;, except JSON:API resource types, which use plural camelCase names such as &#x60;playlistGenerationSchedules&#x60;. New values can be added to any enum at any time, so treat unknown values as forward-compatible rather than errors. - **Resource IDs** are opaque strings. A few resources document well-known IDs for permanent system singleton instances; compare those IDs by exact value. Never parse, construct, or infer meaning from any other &#x60;id&#x60;, even when its current representation resembles an integer, UUID, or another recognizable value. Other properties explicitly marked with OpenAPI &#x60;format: uuid&#x60; are UUIDs. - **Dates and times** use ISO 8601. Date-times use the OpenAPI &#x60;date-time&#x60; format (&#x60;2024-05-01T12:00:00Z&#x60;), dates use &#x60;YYYY-MM-DD&#x60;, and durations use values such as &#x60;PT3M5S&#x60;. - **Recurrence frequencies** use RFC 5545 &#x60;FREQ&#x60; names such as &#x60;DAILY&#x60;, &#x60;WEEKLY&#x60;, and &#x60;MONTHLY&#x60;. The property&#39;s enum lists the frequencies that field currently supports. - **Weekdays** use &#x60;MONDAY&#x60; through &#x60;SUNDAY&#x60;. - **Time zones** use IANA Time Zone Database identifiers such as &#x60;Europe/Stockholm&#x60;, not abbreviations or raw UTC offsets for recurring civil-time schedules. - **Country codes** use ISO 3166-1 alpha-2; the shared country type also accepts &#x60;WW&#x60; for worldwide. **Locales** use IETF BCP 47 language tags such as &#x60;en-US&#x60;. - **Currencies** use ISO 4217 codes. Monetary amounts are decimal strings; each field defines its sign and precision constraints. - **Colors** use three- or six-digit hexadecimal strings (&#x60;#RGB&#x60; or &#x60;#RRGGBB&#x60;). Resource links to external URLs use JSON:API link objects with an &#x60;href&#x60; member.  ### Resource identifiers  Where supported, &#x60;filter[subject]&#x3D;tracks:123&#x60; matches a related resource by type and ID; &#x60;filter[subject.id]&#x3D;123&#x60; and &#x60;filter[subject.type]&#x3D;tracks&#x60; match either component. Where multiple identifiers are accepted, comma-separated values match any complete pair. When a member path names a to-many relationship, at least one related resource must match; filtering does not trim that relationship. On collection and to-many relationship reads, the reserved root &#x60;self&#x60; (&#x60;filter[self]&#x3D;tracks:123&#x60;) filters primary data itself. Each endpoint lists its supported filters and types.  Where supported, &#x60;me&#x60; aliases the authenticated user&#39;s dedicated resource ID for the referenced resource type. It works in paths, resource-ID filters, compact identifiers (&#x60;type:me&#x60;), resource PATCH primary IDs and standalone relationship mutation identifiers, with the same meaning as the resolved ID. Reads using the alias are &#x60;no-store&#x60;.  ### Relationships and includes  [Relationships](https://jsonapi.org/format/#document-resource-object-relationships) are returned only on request: [&#x60;include&#x60;](https://jsonapi.org/format/#fetching-includes) selects linkage and related content, while &#x60;includeLinkage&#x60; selects authorized linkage only. A relationship that was not requested is absent from the response, not empty. The full set of relationships a resource supports is documented in its schema.  For INTERNAL clients on resource GET endpoints, &#x60;includeLinkage&#x60; accepts comma-separated direct relationship names, for example &#x60;includeLinkage&#x3D;subject,viewer&#x60;. It does not load related resources or add an &#x60;included&#x60; section. Nested paths and type qualifiers are unsupported. To-many linkage retains its normal pagination and relationship &#x60;next&#x60; links. Selecting the same relationship with both parameters applies full include behavior and reads the relationship once.  Request related resources in one round trip with &#x60;?include&#x3D;&#x60;, a comma-separated list of dot-separated relationship paths — e.g. &#x60;include&#x3D;coverArt,artists.profileArt&#x60; on an album. A nested path automatically embeds its intermediate resources: &#x60;artists.profileArt&#x60; includes the artists as well as their profile art. Include paths are always relative to the request&#39;s root resource, also on relationship endpoints. Including a relationship never changes the primary data; the related resources are added to &#x60;included&#x60;.  Include paths are validated: a path that cannot be resolved against the resources&#39; documented relationships is rejected with &#x60;400&#x60;. Include trees are also bounded in path depth (default 3 levels) and in the total number of distinct resources they name (default 10); individual endpoints may apply different limits. Both selectors share the include-node limit, counting overlapping roots once. A request exceeding either limit is rejected with &#x60;400&#x60;, with the effective limit stated in the error.  ### Filtering, sorting, pagination  - [&#x60;filter[&lt;memberPath&gt;]&#x3D;value&#x60;](https://jsonapi.org/format/#fetching-filtering) filters primary data by equality. Each endpoint lists its available filters; most collections require at least one. - Where explicitly documented, &#x60;filter[&lt;memberPath&gt;][ne]&#x3D;value&#x60; negates the complete equality predicate. When the member path names a to-many relationship, no related ID may match any supplied value; a known-empty relationship matches. Operators are separate from values. Supplied comparisons combine with AND. For a required filter with multiple supported comparisons, at least one must be supplied; the parameter descriptions identify these alternatives. Unsupported operators and groups return &#x60;400&#x60;. - Where documented, &#x60;filter[&lt;path&gt;][&lt;operator&gt;]&#x3D;value&#x60; applies an endpoint-defined operator, such as &#x60;filter[self][matchesQuery]&#x60;. Its meaning is described per endpoint, and it combines with other filters by AND. - [&#x60;sort&#x3D;&lt;memberPath&gt;&#x60;](https://jsonapi.org/format/#fetching-sorting) sorts ascending, &#x60;-&lt;memberPath&gt;&#x60; descending (&#x60;sort&#x3D;-addedAt&#x60;). Filter and sort member paths are relative to primary data. - Parameters an endpoint cannot honor are rejected with &#x60;400&#x60;: a &#x60;filter[...]&#x60; parameter the endpoint does not document (the error lists the available filters), or &#x60;sort&#x60; on an endpoint that documents no sort values. - [Pagination](https://jsonapi.org/format/#fetching-pagination) is cursor-based: responses carry &#x60;links.self&#x60; and, while more pages exist, &#x60;links.next&#x60; with an opaque &#x60;page[cursor]&#x60;. Follow &#x60;next&#x60; until absent — there are no offset or total-page parameters. Collection sizes, when available, appear as &#x60;meta.total&#x60; and may be approximate.  ### Type qualifiers  Where a relationship can contain several resource types, a path segment may be prefixed with a concrete type to scope which type&#39;s member is accessed. A playlist&#39;s &#x60;items&#x60; are &#x60;tracks&#x60; or &#x60;videos&#x60;: &#x60;GET /playlists/{id}?include&#x3D;items.tracks:albums&#x60; resolves &#x60;albums&#x60; only for the items that are tracks. Qualifiers scope member access — they never filter which resources appear in a relationship — and can be chained.  The same syntax applies to &#x60;filter&#x60; and &#x60;sort&#x60; member paths on endpoints that support it; where supported, the qualified member is listed among the endpoint&#39;s documented filters and sort values. The syntax follows JSON:API proposal [json-api#1695](https://github.com/json-api/json-api/issues/1695).  ### Mutations  - [Partial updates](https://jsonapi.org/format/#crud-updating-resource-attributes) distinguish three wire states for nullable attributes: omission leaves the current value unchanged, an explicit &#x60;null&#x60; clears it, and a concrete value updates it. - Every mutation accepts an [&#x60;Idempotency-Key&#x60;](https://www.ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-07.html) header. Keys are scoped to the client and the authenticated user. Once the original request has completed, retrying it with the same key, method, path, query and payload within one hour replays its response; a retry while it is still processing is rejected with &#x60;409&#x60;, and the same key with a different method, path, query or payload with &#x60;422&#x60;. - After a successful write, your own subsequent reads reflect the change; other clients may observe it with a delay.  ### Revisions and concurrent editing  Where supported, &#x60;attributes.revision&#x60; identifies the resource&#39;s documented aggregate state; a separately versioned relationship collection uses document &#x60;meta.revision&#x60;. Revisions are nonnegative integers that increase when covered state changes. Compare them only within the same identity and scope, preserve the exact value, and never calculate the next revision. Related content, viewer projections and independent sources are not automatically covered. Domain fields named &#x60;version&#x60;, such as a music edition, are distinct; existing endpoints retain their documented contracts.  Guarded mutations accept the observed value as top-level &#x60;meta.expectedRevision&#x60;. Each operation declares its scope and whether the precondition is required. A mismatch returns &#x60;409&#x60;; missing required input returns &#x60;400&#x60;. Refresh and reconcile after a conflict, then submit a new operation with a new idempotency key. An identical retry with the original key replays a recorded success under the idempotency contract. These revisions are not HTTP ETags.  Returned revisions describe observed snapshots, not reservations for later writes. Background changes can advance them immediately after a successful response.  ### Media resource replacements - BETA Internal only  Media resources (&#x60;tracks&#x60;, &#x60;videos&#x60;, and &#x60;albums&#x60;) can become unavailable in a country when licensing rights change. By default, TIDAL API returns the resource identifiers originally stored in a collection. This keeps ordinary reads predictable and consistent.  If a stored media resource is unavailable for the effective country, TIDAL may identify a contextually applicable alternative that is available there. Replacement is best effort, so an alternative is not always available. Replacement never changes the stored collection.  TIDAL API provides two ways to work with replacements:  1. **Inspect the &#x60;replacement&#x60; relationship.** A media resource can expose its applicable alternative through the &#x60;replacement&#x60; relationship. Include this relationship when a client needs both the original and replacement identifiers or wants to decide whether to use the replacement.  2. **Apply replacements with &#x60;replaceMedia&#x60;.** Clients can use &#x60;replaceMedia&#x60; to substitute applicable replacements directly into selected relationship data. The parameter accepts relationship paths using the same syntax as &#x60;include&#x60;. Projection affects only the response and preserves relationship order and metadata. Each identifier includes &#x60;meta.replacement&#x60; describing whether it was &#x60;ORIGINAL&#x60;, &#x60;REPLACED&#x60;, or &#x60;NOT_REPLACED&#x60;.  For example, &#x60;GET /playlists/{id}?include&#x3D;items&amp;replaceMedia&#x3D;items&#x60; applies replacements to media identifiers in the playlist&#39;s &#x60;items&#x60; relationship.  ### Compression  Responses are gzip-compressed when the request includes &#x60;Accept-Encoding: gzip&#x60; (bodies over 2 KB).  ### Deprecation  Deprecated endpoints, parameters, and fields are marked &#x60;deprecated&#x60; in this specification, with the replacement noted in their description. Deprecated functionality keeps working for at least six months after being marked, and is only removed once a replacement is generally available.",
    version="1.10.263",
)

app.include_router(AcceptedTermsApiRouter)
app.include_router(AlbumStatisticsApiRouter)
app.include_router(AlbumsApiRouter)
app.include_router(AppreciationsApiRouter)
app.include_router(ArtistBiographiesApiRouter)
app.include_router(ArtistClaimStatusesApiRouter)
app.include_router(ArtistClaimsApiRouter)
app.include_router(ArtistRolesApiRouter)
app.include_router(ArtistSalesStatisticsApiRouter)
app.include_router(ArtistStreamsStatisticsApiRouter)
app.include_router(ArtistsApiRouter)
app.include_router(ArtworkLibrariesApiRouter)
app.include_router(ArtworksApiRouter)
app.include_router(ClientCertificatesApiRouter)
app.include_router(ClientsApiRouter)
app.include_router(CollaborationInviteRedemptionsApiRouter)
app.include_router(CollaborationInvitesApiRouter)
app.include_router(CommentSummariesApiRouter)
app.include_router(CommentsApiRouter)
app.include_router(ContentClaimsApiRouter)
app.include_router(CreditsApiRouter)
app.include_router(DownloadsApiRouter)
app.include_router(DspSharingLinksApiRouter)
app.include_router(DynamicModulesApiRouter)
app.include_router(DynamicPagesApiRouter)
app.include_router(FolderItemsApiRouter)
app.include_router(FoldersApiRouter)
app.include_router(GenresApiRouter)
app.include_router(GroupsApiRouter)
app.include_router(InstallationsApiRouter)
app.include_router(LyricsApiRouter)
app.include_router(ManualArtistClaimsApiRouter)
app.include_router(OfflineTasksApiRouter)
app.include_router(PlayQueuesApiRouter)
app.include_router(PlaylistGenerationSchedulesApiRouter)
app.include_router(PlaylistGenerationsApiRouter)
app.include_router(PlaylistsApiRouter)
app.include_router(PriceConfigurationsApiRouter)
app.include_router(ProviderOwnersApiRouter)
app.include_router(ProviderProductInfosApiRouter)
app.include_router(ProvidersApiRouter)
app.include_router(PurchasesApiRouter)
app.include_router(ReactionSummariesApiRouter)
app.include_router(ReactionsApiRouter)
app.include_router(ResourceGrantInvitationsApiRouter)
app.include_router(ResourceGrantsApiRouter)
app.include_router(SavedSharesApiRouter)
app.include_router(ScopesApiRouter)
app.include_router(SearchHistoryEntriesApiRouter)
app.include_router(SearchResultsApiRouter)
app.include_router(SearchSuggestionsApiRouter)
app.include_router(SharesApiRouter)
app.include_router(SharingSummariesApiRouter)
app.include_router(SquareConnectionsApiRouter)
app.include_router(SquareItemVariationPhysicalCountsApiRouter)
app.include_router(SquareItemVariationsApiRouter)
app.include_router(SquareItemsApiRouter)
app.include_router(SquareSitesApiRouter)
app.include_router(StripeConnectionsApiRouter)
app.include_router(StripeDashboardLinksApiRouter)
app.include_router(StudioHomeEventTilesApiRouter)
app.include_router(StudioHomeInsightTilesApiRouter)
app.include_router(StudioHomeMerchTilesApiRouter)
app.include_router(StudioHomeMusicTilesApiRouter)
app.include_router(SubscriptionPriceChangeDecisionsApiRouter)
app.include_router(TemporaryUserTokensApiRouter)
app.include_router(TermsApiRouter)
app.include_router(TrackFilesApiRouter)
app.include_router(TrackManifestsApiRouter)
app.include_router(TrackSourceFilesApiRouter)
app.include_router(TrackStatisticsApiRouter)
app.include_router(TracksApiRouter)
app.include_router(TracksMetadataStatusApiRouter)
app.include_router(UsageRulesApiRouter)
app.include_router(UserCollectionAlbumsApiRouter)
app.include_router(UserCollectionArtistsApiRouter)
app.include_router(UserCollectionFoldersApiRouter)
app.include_router(UserCollectionPlaylistsApiRouter)
app.include_router(UserCollectionSaveForLatersApiRouter)
app.include_router(UserCollectionTracksApiRouter)
app.include_router(UserCollectionVideosApiRouter)
app.include_router(UserDailyMixesApiRouter)
app.include_router(UserDataExportRequestsApiRouter)
app.include_router(UserDataExportsApiRouter)
app.include_router(UserDiscoveryMixesApiRouter)
app.include_router(UserFeedItemsApiRouter)
app.include_router(UserFeedsApiRouter)
app.include_router(UserNewReleaseMixesApiRouter)
app.include_router(UserOfflineMixesApiRouter)
app.include_router(UserPlaybackStatesApiRouter)
app.include_router(UserRecommendationBlocksApiRouter)
app.include_router(UserReportsApiRouter)
app.include_router(UserSubscriptionPriceChangesApiRouter)
app.include_router(UsersApiRouter)
app.include_router(VideoManifestsApiRouter)
app.include_router(VideosApiRouter)
app.include_router(ViewerContextsApiRouter)
