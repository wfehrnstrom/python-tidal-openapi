# coding: utf-8

"""
    TIDAL API

    The TIDAL API is a [JSON:API](https://jsonapi.org/)-compliant web API exposing TIDAL's music catalogue, metadata, and user functionality. Guides, authorization documentation, and API key management live at [developer.tidal.com](https://developer.tidal.com).  All endpoints exchange `application/vnd.api+json` documents per the [JSON:API specification](https://jsonapi.org/format/): [resource objects](https://jsonapi.org/format/#document-resource-objects) with `attributes` and `relationships`, [compound documents](https://jsonapi.org/format/#document-compound-documents) via `include`, and standard [error objects](https://jsonapi.org/format/#error-objects).  ### Authentication and authorization  Every request requires an OAuth 2.0 access token in the `Authorization: Bearer` header. Tokens are issued at `https://auth.tidal.com/v1/oauth2/token` via the client-credentials flow (server-to-server) or the authorization-code + PKCE flow (user context; authorize at `https://login.tidal.com/authorize`). Each endpoint documents which flows it accepts, the access tier it requires, and the scopes that apply. Scopes protect private user data: fields you are not authorized to read are redacted from the response rather than causing an error, and resources you cannot access at all behave as if they do not exist. See the [authorization guide](https://developer.tidal.com/documentation/api-sdk/api-sdk-authorization) for details.  ### Common wire types and compatibility  Each property's schema is authoritative for its allowed values, format, requiredness, nullability, and constraints. A standard defines how a value is represented; an individual schema may support only a documented subset.  - **Enums** use `UPPER_CASE_UNDERSCORE`, except JSON:API resource types, which use plural camelCase names such as `playlistGenerationSchedules`. New values can be added to any enum at any time, so treat unknown values as forward-compatible rather than errors. - **Resource IDs** are opaque strings. A few resources document well-known IDs for permanent system singleton instances; compare those IDs by exact value. Never parse, construct, or infer meaning from any other `id`, even when its current representation resembles an integer, UUID, or another recognizable value. Other properties explicitly marked with OpenAPI `format: uuid` are UUIDs. - **Dates and times** use ISO 8601. Date-times use the OpenAPI `date-time` format (`2024-05-01T12:00:00Z`), dates use `YYYY-MM-DD`, and durations use values such as `PT3M5S`. - **Recurrence frequencies** use RFC 5545 `FREQ` names such as `DAILY`, `WEEKLY`, and `MONTHLY`. The property's enum lists the frequencies that field currently supports. - **Weekdays** use `MONDAY` through `SUNDAY`. - **Time zones** use IANA Time Zone Database identifiers such as `Europe/Stockholm`, not abbreviations or raw UTC offsets for recurring civil-time schedules. - **Country codes** use ISO 3166-1 alpha-2; the shared country type also accepts `WW` for worldwide. **Locales** use IETF BCP 47 language tags such as `en-US`. - **Currencies** use ISO 4217 codes. Monetary amounts are decimal strings; each field defines its sign and precision constraints. - **Colors** use three- or six-digit hexadecimal strings (`#RGB` or `#RRGGBB`). Resource links to external URLs use JSON:API link objects with an `href` member.  ### Resource identifiers  Where supported, `filter[subject]=tracks:123` matches a related resource by type and ID; `filter[subject.id]=123` and `filter[subject.type]=tracks` match either component. Where multiple identifiers are accepted, comma-separated values match any complete pair. When a member path names a to-many relationship, at least one related resource must match; filtering does not trim that relationship. On collection and to-many relationship reads, the reserved root `self` (`filter[self]=tracks:123`) filters primary data itself. Each endpoint lists its supported filters and types.  Where supported, `me` aliases the authenticated user's dedicated resource ID for the referenced resource type. It works in paths, resource-ID filters, compact identifiers (`type:me`), resource PATCH primary IDs and standalone relationship mutation identifiers, with the same meaning as the resolved ID. Reads using the alias are `no-store`.  ### Relationships and includes  [Relationships](https://jsonapi.org/format/#document-resource-object-relationships) are returned only on request: [`include`](https://jsonapi.org/format/#fetching-includes) selects linkage and related content, while `includeLinkage` selects authorized linkage only. A relationship that was not requested is absent from the response, not empty. The full set of relationships a resource supports is documented in its schema.  For INTERNAL clients on resource GET endpoints, `includeLinkage` accepts comma-separated direct relationship names, for example `includeLinkage=subject,viewer`. It does not load related resources or add an `included` section. Nested paths and type qualifiers are unsupported. To-many linkage retains its normal pagination and relationship `next` links. Selecting the same relationship with both parameters applies full include behavior and reads the relationship once.  Request related resources in one round trip with `?include=`, a comma-separated list of dot-separated relationship paths — e.g. `include=coverArt,artists.profileArt` on an album. A nested path automatically embeds its intermediate resources: `artists.profileArt` includes the artists as well as their profile art. Include paths are always relative to the request's root resource, also on relationship endpoints. Including a relationship never changes the primary data; the related resources are added to `included`.  Include paths are validated: a path that cannot be resolved against the resources' documented relationships is rejected with `400`. Include trees are also bounded in path depth (default 3 levels) and in the total number of distinct resources they name (default 10); individual endpoints may apply different limits. Both selectors share the include-node limit, counting overlapping roots once. A request exceeding either limit is rejected with `400`, with the effective limit stated in the error.  ### Filtering, sorting, pagination  - [`filter[<memberPath>]=value`](https://jsonapi.org/format/#fetching-filtering) filters primary data by equality. Each endpoint lists its available filters; most collections require at least one. - Where explicitly documented, `filter[<memberPath>][ne]=value` negates the complete equality predicate. When the member path names a to-many relationship, no related ID may match any supplied value; a known-empty relationship matches. Operators are separate from values. Supplied comparisons combine with AND. For a required filter with multiple supported comparisons, at least one must be supplied; the parameter descriptions identify these alternatives. Unsupported operators and groups return `400`. - Where documented, `filter[<path>][<operator>]=value` applies an endpoint-defined operator, such as `filter[self][matchesQuery]`. Its meaning is described per endpoint, and it combines with other filters by AND. - [`sort=<memberPath>`](https://jsonapi.org/format/#fetching-sorting) sorts ascending, `-<memberPath>` descending (`sort=-addedAt`). Filter and sort member paths are relative to primary data. - Parameters an endpoint cannot honor are rejected with `400`: a `filter[...]` parameter the endpoint does not document (the error lists the available filters), or `sort` on an endpoint that documents no sort values. - [Pagination](https://jsonapi.org/format/#fetching-pagination) is cursor-based: responses carry `links.self` and, while more pages exist, `links.next` with an opaque `page[cursor]`. Follow `next` until absent — there are no offset or total-page parameters. Collection sizes, when available, appear as `meta.total` and may be approximate.  ### Type qualifiers  Where a relationship can contain several resource types, a path segment may be prefixed with a concrete type to scope which type's member is accessed. A playlist's `items` are `tracks` or `videos`: `GET /playlists/{id}?include=items.tracks:albums` resolves `albums` only for the items that are tracks. Qualifiers scope member access — they never filter which resources appear in a relationship — and can be chained.  The same syntax applies to `filter` and `sort` member paths on endpoints that support it; where supported, the qualified member is listed among the endpoint's documented filters and sort values. The syntax follows JSON:API proposal [json-api#1695](https://github.com/json-api/json-api/issues/1695).  ### Mutations  - [Partial updates](https://jsonapi.org/format/#crud-updating-resource-attributes) distinguish three wire states for nullable attributes: omission leaves the current value unchanged, an explicit `null` clears it, and a concrete value updates it. - Every mutation accepts an [`Idempotency-Key`](https://www.ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-07.html) header. Keys are scoped to the client and the authenticated user. Once the original request has completed, retrying it with the same key, method, path, query and payload within one hour replays its response; a retry while it is still processing is rejected with `409`, and the same key with a different method, path, query or payload with `422`. - After a successful write, your own subsequent reads reflect the change; other clients may observe it with a delay.  ### Revisions and concurrent editing  Where supported, `attributes.revision` identifies the resource's documented aggregate state; a separately versioned relationship collection uses document `meta.revision`. Revisions are nonnegative integers that increase when covered state changes. Compare them only within the same identity and scope, preserve the exact value, and never calculate the next revision. Related content, viewer projections and independent sources are not automatically covered. Domain fields named `version`, such as a music edition, are distinct; existing endpoints retain their documented contracts.  Guarded mutations accept the observed value as top-level `meta.expectedRevision`. Each operation declares its scope and whether the precondition is required. A mismatch returns `409`; missing required input returns `400`. Refresh and reconcile after a conflict, then submit a new operation with a new idempotency key. An identical retry with the original key replays a recorded success under the idempotency contract. These revisions are not HTTP ETags.  Returned revisions describe observed snapshots, not reservations for later writes. Background changes can advance them immediately after a successful response.  ### Media resource replacements - BETA Internal only  Media resources (`tracks`, `videos`, and `albums`) can become unavailable in a country when licensing rights change. By default, TIDAL API returns the resource identifiers originally stored in a collection. This keeps ordinary reads predictable and consistent.  If a stored media resource is unavailable for the effective country, TIDAL may identify a contextually applicable alternative that is available there. Replacement is best effort, so an alternative is not always available. Replacement never changes the stored collection.  TIDAL API provides two ways to work with replacements:  1. **Inspect the `replacement` relationship.** A media resource can expose its applicable alternative through the `replacement` relationship. Include this relationship when a client needs both the original and replacement identifiers or wants to decide whether to use the replacement.  2. **Apply replacements with `replaceMedia`.** Clients can use `replaceMedia` to substitute applicable replacements directly into selected relationship data. The parameter accepts relationship paths using the same syntax as `include`. Projection affects only the response and preserves relationship order and metadata. Each identifier includes `meta.replacement` describing whether it was `ORIGINAL`, `REPLACED`, or `NOT_REPLACED`.  For example, `GET /playlists/{id}?include=items&replaceMedia=items` applies replacements to media identifiers in the playlist's `items` relationship.  ### Compression  Responses are gzip-compressed when the request includes `Accept-Encoding: gzip` (bodies over 2 KB).  ### Deprecation  Deprecated endpoints, parameters, and fields are marked `deprecated` in this specification, with the replacement noted in their description. Deprecated functionality keeps working for at least six months after being marked, and is only removed once a replacement is generally available.

    The version of the OpenAPI document: 1.10.263
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401



from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from tidal.models.appreciations_resource_object import AppreciationsResourceObject
from tidal.models.artist_claim_statuses_resource_object import ArtistClaimStatusesResourceObject
from tidal.models.artist_roles_resource_object import ArtistRolesResourceObject
from tidal.models.change_event_streams_resource_object import ChangeEventStreamsResourceObject
from tidal.models.collaboration_invite_redemptions_resource_object import CollaborationInviteRedemptionsResourceObject
from tidal.models.genres_resource_object import GenresResourceObject
from tidal.models.groups_resource_object import GroupsResourceObject
from tidal.models.manual_artist_claims_resource_object import ManualArtistClaimsResourceObject
from tidal.models.price_configurations_resource_object import PriceConfigurationsResourceObject
from tidal.models.providers_resource_object import ProvidersResourceObject
from tidal.models.saved_shares_resource_object import SavedSharesResourceObject
from tidal.models.scopes_resource_object import ScopesResourceObject
from tidal.models.search_history_entries_resource_object import SearchHistoryEntriesResourceObject
from tidal.models.square_item_variation_physical_counts_resource_object import SquareItemVariationPhysicalCountsResourceObject
from tidal.models.studio_home_event_tiles_resource_object import StudioHomeEventTilesResourceObject
from tidal.models.terms_resource_object import TermsResourceObject
from tidal.models.track_files_resource_object import TrackFilesResourceObject
from tidal.models.track_manifests_resource_object import TrackManifestsResourceObject
from tidal.models.tracks_metadata_status_resource_object import TracksMetadataStatusResourceObject
from tidal.models.usage_rules_resource_object import UsageRulesResourceObject
from tidal.models.user_data_export_requests_resource_object import UserDataExportRequestsResourceObject
from tidal.models.user_feeds_resource_object import UserFeedsResourceObject
from tidal.models.user_reports_resource_object import UserReportsResourceObject
from tidal.models.video_manifests_resource_object import VideoManifestsResourceObject
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

INCLUDEDINNER_ONE_OF_SCHEMAS = ["AcceptedTermsResourceObject", "AlbumStatisticsResourceObject", "AlbumsResourceObject", "AppreciationsResourceObject", "ArtistBiographiesResourceObject", "ArtistClaimStatusesResourceObject", "ArtistClaimsResourceObject", "ArtistRolesResourceObject", "ArtistSalesStatisticsResourceObject", "ArtistStreamsStatisticsResourceObject", "ArtistsResourceObject", "ArtworkLibrariesResourceObject", "ArtworksResourceObject", "ChangeEventStreamsResourceObject", "ClientCertificatesResourceObject", "ClientsResourceObject", "CollaborationInviteRedemptionsResourceObject", "CollaborationInvitesResourceObject", "CommentSummariesResourceObject", "CommentsResourceObject", "ContentClaimsResourceObject", "CreditsResourceObject", "DownloadsResourceObject", "DspSharingLinksResourceObject", "DynamicModulesResourceObject", "DynamicPagesResourceObject", "FolderItemsResourceObject", "FoldersResourceObject", "GenresResourceObject", "GroupsResourceObject", "InstallationsResourceObject", "LyricsResourceObject", "ManualArtistClaimsResourceObject", "OfflineTasksResourceObject", "PlayQueuesResourceObject", "PlaylistGenerationSchedulesResourceObject", "PlaylistGenerationsResourceObject", "PlaylistsResourceObject", "PriceConfigurationsResourceObject", "ProviderOwnersResourceObject", "ProviderProductInfosResourceObject", "ProvidersResourceObject", "PurchasesResourceObject", "ReactionSummariesResourceObject", "ReactionsResourceObject", "ResourceGrantInvitationsResourceObject", "ResourceGrantsResourceObject", "SavedSharesResourceObject", "ScopesResourceObject", "SearchHistoryEntriesResourceObject", "SearchResultsResourceObject", "SearchSuggestionsResourceObject", "SharesResourceObject", "SharingSummariesResourceObject", "SquareConnectionsResourceObject", "SquareItemVariationPhysicalCountsResourceObject", "SquareItemVariationsResourceObject", "SquareItemsResourceObject", "SquareSitesResourceObject", "StripeConnectionsResourceObject", "StripeDashboardLinksResourceObject", "StudioHomeEventTilesResourceObject", "StudioHomeInsightTilesResourceObject", "StudioHomeMerchTilesResourceObject", "StudioHomeMusicTilesResourceObject", "SubscriptionPriceChangeDecisionsResourceObject", "TemporaryUserTokensResourceObject", "TermsResourceObject", "TrackFilesResourceObject", "TrackManifestsResourceObject", "TrackSourceFilesResourceObject", "TrackStatisticsResourceObject", "TracksMetadataStatusResourceObject", "TracksResourceObject", "UsageRulesResourceObject", "UserCollectionAlbumsResourceObject", "UserCollectionArtistsResourceObject", "UserCollectionFoldersResourceObject", "UserCollectionPlaylistsResourceObject", "UserCollectionSaveForLatersResourceObject", "UserCollectionTracksResourceObject", "UserCollectionVideosResourceObject", "UserDailyMixesResourceObject", "UserDataExportRequestsResourceObject", "UserDataExportsResourceObject", "UserDiscoveryMixesResourceObject", "UserFeedItemsResourceObject", "UserFeedsResourceObject", "UserNewReleaseMixesResourceObject", "UserOfflineMixesResourceObject", "UserPlaybackStatesResourceObject", "UserRecommendationBlocksResourceObject", "UserReportsResourceObject", "UserSubscriptionPriceChangesResourceObject", "UsersResourceObject", "VideoManifestsResourceObject", "VideosResourceObject", "ViewerContextsResourceObject"]

class IncludedInner(BaseModel):
    """
    IncludedInner
    """
    # data type: AcceptedTermsResourceObject
    oneof_schema_1_validator: Optional[AcceptedTermsResourceObject] = None
    # data type: AlbumStatisticsResourceObject
    oneof_schema_2_validator: Optional[AlbumStatisticsResourceObject] = None
    # data type: AlbumsResourceObject
    oneof_schema_3_validator: Optional[AlbumsResourceObject] = None
    # data type: AppreciationsResourceObject
    oneof_schema_4_validator: Optional[AppreciationsResourceObject] = None
    # data type: ArtistBiographiesResourceObject
    oneof_schema_5_validator: Optional[ArtistBiographiesResourceObject] = None
    # data type: ArtistClaimStatusesResourceObject
    oneof_schema_6_validator: Optional[ArtistClaimStatusesResourceObject] = None
    # data type: ArtistClaimsResourceObject
    oneof_schema_7_validator: Optional[ArtistClaimsResourceObject] = None
    # data type: ArtistRolesResourceObject
    oneof_schema_8_validator: Optional[ArtistRolesResourceObject] = None
    # data type: ArtistSalesStatisticsResourceObject
    oneof_schema_9_validator: Optional[ArtistSalesStatisticsResourceObject] = None
    # data type: ArtistStreamsStatisticsResourceObject
    oneof_schema_10_validator: Optional[ArtistStreamsStatisticsResourceObject] = None
    # data type: ArtistsResourceObject
    oneof_schema_11_validator: Optional[ArtistsResourceObject] = None
    # data type: ArtworkLibrariesResourceObject
    oneof_schema_12_validator: Optional[ArtworkLibrariesResourceObject] = None
    # data type: ArtworksResourceObject
    oneof_schema_13_validator: Optional[ArtworksResourceObject] = None
    # data type: ChangeEventStreamsResourceObject
    oneof_schema_14_validator: Optional[ChangeEventStreamsResourceObject] = None
    # data type: ClientCertificatesResourceObject
    oneof_schema_15_validator: Optional[ClientCertificatesResourceObject] = None
    # data type: ClientsResourceObject
    oneof_schema_16_validator: Optional[ClientsResourceObject] = None
    # data type: CollaborationInviteRedemptionsResourceObject
    oneof_schema_17_validator: Optional[CollaborationInviteRedemptionsResourceObject] = None
    # data type: CollaborationInvitesResourceObject
    oneof_schema_18_validator: Optional[CollaborationInvitesResourceObject] = None
    # data type: CommentSummariesResourceObject
    oneof_schema_19_validator: Optional[CommentSummariesResourceObject] = None
    # data type: CommentsResourceObject
    oneof_schema_20_validator: Optional[CommentsResourceObject] = None
    # data type: ContentClaimsResourceObject
    oneof_schema_21_validator: Optional[ContentClaimsResourceObject] = None
    # data type: CreditsResourceObject
    oneof_schema_22_validator: Optional[CreditsResourceObject] = None
    # data type: DownloadsResourceObject
    oneof_schema_23_validator: Optional[DownloadsResourceObject] = None
    # data type: DspSharingLinksResourceObject
    oneof_schema_24_validator: Optional[DspSharingLinksResourceObject] = None
    # data type: DynamicModulesResourceObject
    oneof_schema_25_validator: Optional[DynamicModulesResourceObject] = None
    # data type: DynamicPagesResourceObject
    oneof_schema_26_validator: Optional[DynamicPagesResourceObject] = None
    # data type: FolderItemsResourceObject
    oneof_schema_27_validator: Optional[FolderItemsResourceObject] = None
    # data type: FoldersResourceObject
    oneof_schema_28_validator: Optional[FoldersResourceObject] = None
    # data type: GenresResourceObject
    oneof_schema_29_validator: Optional[GenresResourceObject] = None
    # data type: GroupsResourceObject
    oneof_schema_30_validator: Optional[GroupsResourceObject] = None
    # data type: InstallationsResourceObject
    oneof_schema_31_validator: Optional[InstallationsResourceObject] = None
    # data type: LyricsResourceObject
    oneof_schema_32_validator: Optional[LyricsResourceObject] = None
    # data type: ManualArtistClaimsResourceObject
    oneof_schema_33_validator: Optional[ManualArtistClaimsResourceObject] = None
    # data type: OfflineTasksResourceObject
    oneof_schema_34_validator: Optional[OfflineTasksResourceObject] = None
    # data type: PlayQueuesResourceObject
    oneof_schema_35_validator: Optional[PlayQueuesResourceObject] = None
    # data type: PlaylistGenerationSchedulesResourceObject
    oneof_schema_36_validator: Optional[PlaylistGenerationSchedulesResourceObject] = None
    # data type: PlaylistGenerationsResourceObject
    oneof_schema_37_validator: Optional[PlaylistGenerationsResourceObject] = None
    # data type: PlaylistsResourceObject
    oneof_schema_38_validator: Optional[PlaylistsResourceObject] = None
    # data type: PriceConfigurationsResourceObject
    oneof_schema_39_validator: Optional[PriceConfigurationsResourceObject] = None
    # data type: ProviderOwnersResourceObject
    oneof_schema_40_validator: Optional[ProviderOwnersResourceObject] = None
    # data type: ProviderProductInfosResourceObject
    oneof_schema_41_validator: Optional[ProviderProductInfosResourceObject] = None
    # data type: ProvidersResourceObject
    oneof_schema_42_validator: Optional[ProvidersResourceObject] = None
    # data type: PurchasesResourceObject
    oneof_schema_43_validator: Optional[PurchasesResourceObject] = None
    # data type: ReactionSummariesResourceObject
    oneof_schema_44_validator: Optional[ReactionSummariesResourceObject] = None
    # data type: ReactionsResourceObject
    oneof_schema_45_validator: Optional[ReactionsResourceObject] = None
    # data type: ResourceGrantInvitationsResourceObject
    oneof_schema_46_validator: Optional[ResourceGrantInvitationsResourceObject] = None
    # data type: ResourceGrantsResourceObject
    oneof_schema_47_validator: Optional[ResourceGrantsResourceObject] = None
    # data type: SavedSharesResourceObject
    oneof_schema_48_validator: Optional[SavedSharesResourceObject] = None
    # data type: ScopesResourceObject
    oneof_schema_49_validator: Optional[ScopesResourceObject] = None
    # data type: SearchHistoryEntriesResourceObject
    oneof_schema_50_validator: Optional[SearchHistoryEntriesResourceObject] = None
    # data type: SearchResultsResourceObject
    oneof_schema_51_validator: Optional[SearchResultsResourceObject] = None
    # data type: SearchSuggestionsResourceObject
    oneof_schema_52_validator: Optional[SearchSuggestionsResourceObject] = None
    # data type: SharesResourceObject
    oneof_schema_53_validator: Optional[SharesResourceObject] = None
    # data type: SharingSummariesResourceObject
    oneof_schema_54_validator: Optional[SharingSummariesResourceObject] = None
    # data type: SquareConnectionsResourceObject
    oneof_schema_55_validator: Optional[SquareConnectionsResourceObject] = None
    # data type: SquareItemVariationPhysicalCountsResourceObject
    oneof_schema_56_validator: Optional[SquareItemVariationPhysicalCountsResourceObject] = None
    # data type: SquareItemVariationsResourceObject
    oneof_schema_57_validator: Optional[SquareItemVariationsResourceObject] = None
    # data type: SquareItemsResourceObject
    oneof_schema_58_validator: Optional[SquareItemsResourceObject] = None
    # data type: SquareSitesResourceObject
    oneof_schema_59_validator: Optional[SquareSitesResourceObject] = None
    # data type: StripeConnectionsResourceObject
    oneof_schema_60_validator: Optional[StripeConnectionsResourceObject] = None
    # data type: StripeDashboardLinksResourceObject
    oneof_schema_61_validator: Optional[StripeDashboardLinksResourceObject] = None
    # data type: StudioHomeEventTilesResourceObject
    oneof_schema_62_validator: Optional[StudioHomeEventTilesResourceObject] = None
    # data type: StudioHomeInsightTilesResourceObject
    oneof_schema_63_validator: Optional[StudioHomeInsightTilesResourceObject] = None
    # data type: StudioHomeMerchTilesResourceObject
    oneof_schema_64_validator: Optional[StudioHomeMerchTilesResourceObject] = None
    # data type: StudioHomeMusicTilesResourceObject
    oneof_schema_65_validator: Optional[StudioHomeMusicTilesResourceObject] = None
    # data type: SubscriptionPriceChangeDecisionsResourceObject
    oneof_schema_66_validator: Optional[SubscriptionPriceChangeDecisionsResourceObject] = None
    # data type: TemporaryUserTokensResourceObject
    oneof_schema_67_validator: Optional[TemporaryUserTokensResourceObject] = None
    # data type: TermsResourceObject
    oneof_schema_68_validator: Optional[TermsResourceObject] = None
    # data type: TrackFilesResourceObject
    oneof_schema_69_validator: Optional[TrackFilesResourceObject] = None
    # data type: TrackManifestsResourceObject
    oneof_schema_70_validator: Optional[TrackManifestsResourceObject] = None
    # data type: TrackSourceFilesResourceObject
    oneof_schema_71_validator: Optional[TrackSourceFilesResourceObject] = None
    # data type: TrackStatisticsResourceObject
    oneof_schema_72_validator: Optional[TrackStatisticsResourceObject] = None
    # data type: TracksResourceObject
    oneof_schema_73_validator: Optional[TracksResourceObject] = None
    # data type: TracksMetadataStatusResourceObject
    oneof_schema_74_validator: Optional[TracksMetadataStatusResourceObject] = None
    # data type: UsageRulesResourceObject
    oneof_schema_75_validator: Optional[UsageRulesResourceObject] = None
    # data type: UserCollectionAlbumsResourceObject
    oneof_schema_76_validator: Optional[UserCollectionAlbumsResourceObject] = None
    # data type: UserCollectionArtistsResourceObject
    oneof_schema_77_validator: Optional[UserCollectionArtistsResourceObject] = None
    # data type: UserCollectionFoldersResourceObject
    oneof_schema_78_validator: Optional[UserCollectionFoldersResourceObject] = None
    # data type: UserCollectionPlaylistsResourceObject
    oneof_schema_79_validator: Optional[UserCollectionPlaylistsResourceObject] = None
    # data type: UserCollectionSaveForLatersResourceObject
    oneof_schema_80_validator: Optional[UserCollectionSaveForLatersResourceObject] = None
    # data type: UserCollectionTracksResourceObject
    oneof_schema_81_validator: Optional[UserCollectionTracksResourceObject] = None
    # data type: UserCollectionVideosResourceObject
    oneof_schema_82_validator: Optional[UserCollectionVideosResourceObject] = None
    # data type: UserDailyMixesResourceObject
    oneof_schema_83_validator: Optional[UserDailyMixesResourceObject] = None
    # data type: UserDataExportRequestsResourceObject
    oneof_schema_84_validator: Optional[UserDataExportRequestsResourceObject] = None
    # data type: UserDataExportsResourceObject
    oneof_schema_85_validator: Optional[UserDataExportsResourceObject] = None
    # data type: UserDiscoveryMixesResourceObject
    oneof_schema_86_validator: Optional[UserDiscoveryMixesResourceObject] = None
    # data type: UserFeedItemsResourceObject
    oneof_schema_87_validator: Optional[UserFeedItemsResourceObject] = None
    # data type: UserFeedsResourceObject
    oneof_schema_88_validator: Optional[UserFeedsResourceObject] = None
    # data type: UserNewReleaseMixesResourceObject
    oneof_schema_89_validator: Optional[UserNewReleaseMixesResourceObject] = None
    # data type: UserOfflineMixesResourceObject
    oneof_schema_90_validator: Optional[UserOfflineMixesResourceObject] = None
    # data type: UserPlaybackStatesResourceObject
    oneof_schema_91_validator: Optional[UserPlaybackStatesResourceObject] = None
    # data type: UserRecommendationBlocksResourceObject
    oneof_schema_92_validator: Optional[UserRecommendationBlocksResourceObject] = None
    # data type: UserReportsResourceObject
    oneof_schema_93_validator: Optional[UserReportsResourceObject] = None
    # data type: UserSubscriptionPriceChangesResourceObject
    oneof_schema_94_validator: Optional[UserSubscriptionPriceChangesResourceObject] = None
    # data type: UsersResourceObject
    oneof_schema_95_validator: Optional[UsersResourceObject] = None
    # data type: VideoManifestsResourceObject
    oneof_schema_96_validator: Optional[VideoManifestsResourceObject] = None
    # data type: VideosResourceObject
    oneof_schema_97_validator: Optional[VideosResourceObject] = None
    # data type: ViewerContextsResourceObject
    oneof_schema_98_validator: Optional[ViewerContextsResourceObject] = None
    actual_instance: Optional[Union[AcceptedTermsResourceObject, AlbumStatisticsResourceObject, AlbumsResourceObject, AppreciationsResourceObject, ArtistBiographiesResourceObject, ArtistClaimStatusesResourceObject, ArtistClaimsResourceObject, ArtistRolesResourceObject, ArtistSalesStatisticsResourceObject, ArtistStreamsStatisticsResourceObject, ArtistsResourceObject, ArtworkLibrariesResourceObject, ArtworksResourceObject, ChangeEventStreamsResourceObject, ClientCertificatesResourceObject, ClientsResourceObject, CollaborationInviteRedemptionsResourceObject, CollaborationInvitesResourceObject, CommentSummariesResourceObject, CommentsResourceObject, ContentClaimsResourceObject, CreditsResourceObject, DownloadsResourceObject, DspSharingLinksResourceObject, DynamicModulesResourceObject, DynamicPagesResourceObject, FolderItemsResourceObject, FoldersResourceObject, GenresResourceObject, GroupsResourceObject, InstallationsResourceObject, LyricsResourceObject, ManualArtistClaimsResourceObject, OfflineTasksResourceObject, PlayQueuesResourceObject, PlaylistGenerationSchedulesResourceObject, PlaylistGenerationsResourceObject, PlaylistsResourceObject, PriceConfigurationsResourceObject, ProviderOwnersResourceObject, ProviderProductInfosResourceObject, ProvidersResourceObject, PurchasesResourceObject, ReactionSummariesResourceObject, ReactionsResourceObject, ResourceGrantInvitationsResourceObject, ResourceGrantsResourceObject, SavedSharesResourceObject, ScopesResourceObject, SearchHistoryEntriesResourceObject, SearchResultsResourceObject, SearchSuggestionsResourceObject, SharesResourceObject, SharingSummariesResourceObject, SquareConnectionsResourceObject, SquareItemVariationPhysicalCountsResourceObject, SquareItemVariationsResourceObject, SquareItemsResourceObject, SquareSitesResourceObject, StripeConnectionsResourceObject, StripeDashboardLinksResourceObject, StudioHomeEventTilesResourceObject, StudioHomeInsightTilesResourceObject, StudioHomeMerchTilesResourceObject, StudioHomeMusicTilesResourceObject, SubscriptionPriceChangeDecisionsResourceObject, TemporaryUserTokensResourceObject, TermsResourceObject, TrackFilesResourceObject, TrackManifestsResourceObject, TrackSourceFilesResourceObject, TrackStatisticsResourceObject, TracksMetadataStatusResourceObject, TracksResourceObject, UsageRulesResourceObject, UserCollectionAlbumsResourceObject, UserCollectionArtistsResourceObject, UserCollectionFoldersResourceObject, UserCollectionPlaylistsResourceObject, UserCollectionSaveForLatersResourceObject, UserCollectionTracksResourceObject, UserCollectionVideosResourceObject, UserDailyMixesResourceObject, UserDataExportRequestsResourceObject, UserDataExportsResourceObject, UserDiscoveryMixesResourceObject, UserFeedItemsResourceObject, UserFeedsResourceObject, UserNewReleaseMixesResourceObject, UserOfflineMixesResourceObject, UserPlaybackStatesResourceObject, UserRecommendationBlocksResourceObject, UserReportsResourceObject, UserSubscriptionPriceChangesResourceObject, UsersResourceObject, VideoManifestsResourceObject, VideosResourceObject, ViewerContextsResourceObject]] = None
    one_of_schemas: List[str] = Literal["AcceptedTermsResourceObject", "AlbumStatisticsResourceObject", "AlbumsResourceObject", "AppreciationsResourceObject", "ArtistBiographiesResourceObject", "ArtistClaimStatusesResourceObject", "ArtistClaimsResourceObject", "ArtistRolesResourceObject", "ArtistSalesStatisticsResourceObject", "ArtistStreamsStatisticsResourceObject", "ArtistsResourceObject", "ArtworkLibrariesResourceObject", "ArtworksResourceObject", "ChangeEventStreamsResourceObject", "ClientCertificatesResourceObject", "ClientsResourceObject", "CollaborationInviteRedemptionsResourceObject", "CollaborationInvitesResourceObject", "CommentSummariesResourceObject", "CommentsResourceObject", "ContentClaimsResourceObject", "CreditsResourceObject", "DownloadsResourceObject", "DspSharingLinksResourceObject", "DynamicModulesResourceObject", "DynamicPagesResourceObject", "FolderItemsResourceObject", "FoldersResourceObject", "GenresResourceObject", "GroupsResourceObject", "InstallationsResourceObject", "LyricsResourceObject", "ManualArtistClaimsResourceObject", "OfflineTasksResourceObject", "PlayQueuesResourceObject", "PlaylistGenerationSchedulesResourceObject", "PlaylistGenerationsResourceObject", "PlaylistsResourceObject", "PriceConfigurationsResourceObject", "ProviderOwnersResourceObject", "ProviderProductInfosResourceObject", "ProvidersResourceObject", "PurchasesResourceObject", "ReactionSummariesResourceObject", "ReactionsResourceObject", "ResourceGrantInvitationsResourceObject", "ResourceGrantsResourceObject", "SavedSharesResourceObject", "ScopesResourceObject", "SearchHistoryEntriesResourceObject", "SearchResultsResourceObject", "SearchSuggestionsResourceObject", "SharesResourceObject", "SharingSummariesResourceObject", "SquareConnectionsResourceObject", "SquareItemVariationPhysicalCountsResourceObject", "SquareItemVariationsResourceObject", "SquareItemsResourceObject", "SquareSitesResourceObject", "StripeConnectionsResourceObject", "StripeDashboardLinksResourceObject", "StudioHomeEventTilesResourceObject", "StudioHomeInsightTilesResourceObject", "StudioHomeMerchTilesResourceObject", "StudioHomeMusicTilesResourceObject", "SubscriptionPriceChangeDecisionsResourceObject", "TemporaryUserTokensResourceObject", "TermsResourceObject", "TrackFilesResourceObject", "TrackManifestsResourceObject", "TrackSourceFilesResourceObject", "TrackStatisticsResourceObject", "TracksMetadataStatusResourceObject", "TracksResourceObject", "UsageRulesResourceObject", "UserCollectionAlbumsResourceObject", "UserCollectionArtistsResourceObject", "UserCollectionFoldersResourceObject", "UserCollectionPlaylistsResourceObject", "UserCollectionSaveForLatersResourceObject", "UserCollectionTracksResourceObject", "UserCollectionVideosResourceObject", "UserDailyMixesResourceObject", "UserDataExportRequestsResourceObject", "UserDataExportsResourceObject", "UserDiscoveryMixesResourceObject", "UserFeedItemsResourceObject", "UserFeedsResourceObject", "UserNewReleaseMixesResourceObject", "UserOfflineMixesResourceObject", "UserPlaybackStatesResourceObject", "UserRecommendationBlocksResourceObject", "UserReportsResourceObject", "UserSubscriptionPriceChangesResourceObject", "UsersResourceObject", "VideoManifestsResourceObject", "VideosResourceObject", "ViewerContextsResourceObject"]

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = IncludedInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: AcceptedTermsResourceObject
        if not isinstance(v, AcceptedTermsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AcceptedTermsResourceObject`")
        else:
            match += 1
        # validate data type: AlbumStatisticsResourceObject
        if not isinstance(v, AlbumStatisticsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AlbumStatisticsResourceObject`")
        else:
            match += 1
        # validate data type: AlbumsResourceObject
        if not isinstance(v, AlbumsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AlbumsResourceObject`")
        else:
            match += 1
        # validate data type: AppreciationsResourceObject
        if not isinstance(v, AppreciationsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AppreciationsResourceObject`")
        else:
            match += 1
        # validate data type: ArtistBiographiesResourceObject
        if not isinstance(v, ArtistBiographiesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ArtistBiographiesResourceObject`")
        else:
            match += 1
        # validate data type: ArtistClaimStatusesResourceObject
        if not isinstance(v, ArtistClaimStatusesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ArtistClaimStatusesResourceObject`")
        else:
            match += 1
        # validate data type: ArtistClaimsResourceObject
        if not isinstance(v, ArtistClaimsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ArtistClaimsResourceObject`")
        else:
            match += 1
        # validate data type: ArtistRolesResourceObject
        if not isinstance(v, ArtistRolesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ArtistRolesResourceObject`")
        else:
            match += 1
        # validate data type: ArtistSalesStatisticsResourceObject
        if not isinstance(v, ArtistSalesStatisticsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ArtistSalesStatisticsResourceObject`")
        else:
            match += 1
        # validate data type: ArtistStreamsStatisticsResourceObject
        if not isinstance(v, ArtistStreamsStatisticsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ArtistStreamsStatisticsResourceObject`")
        else:
            match += 1
        # validate data type: ArtistsResourceObject
        if not isinstance(v, ArtistsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ArtistsResourceObject`")
        else:
            match += 1
        # validate data type: ArtworkLibrariesResourceObject
        if not isinstance(v, ArtworkLibrariesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ArtworkLibrariesResourceObject`")
        else:
            match += 1
        # validate data type: ArtworksResourceObject
        if not isinstance(v, ArtworksResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ArtworksResourceObject`")
        else:
            match += 1
        # validate data type: ChangeEventStreamsResourceObject
        if not isinstance(v, ChangeEventStreamsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ChangeEventStreamsResourceObject`")
        else:
            match += 1
        # validate data type: ClientCertificatesResourceObject
        if not isinstance(v, ClientCertificatesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ClientCertificatesResourceObject`")
        else:
            match += 1
        # validate data type: ClientsResourceObject
        if not isinstance(v, ClientsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ClientsResourceObject`")
        else:
            match += 1
        # validate data type: CollaborationInviteRedemptionsResourceObject
        if not isinstance(v, CollaborationInviteRedemptionsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CollaborationInviteRedemptionsResourceObject`")
        else:
            match += 1
        # validate data type: CollaborationInvitesResourceObject
        if not isinstance(v, CollaborationInvitesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CollaborationInvitesResourceObject`")
        else:
            match += 1
        # validate data type: CommentSummariesResourceObject
        if not isinstance(v, CommentSummariesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CommentSummariesResourceObject`")
        else:
            match += 1
        # validate data type: CommentsResourceObject
        if not isinstance(v, CommentsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CommentsResourceObject`")
        else:
            match += 1
        # validate data type: ContentClaimsResourceObject
        if not isinstance(v, ContentClaimsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ContentClaimsResourceObject`")
        else:
            match += 1
        # validate data type: CreditsResourceObject
        if not isinstance(v, CreditsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CreditsResourceObject`")
        else:
            match += 1
        # validate data type: DownloadsResourceObject
        if not isinstance(v, DownloadsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DownloadsResourceObject`")
        else:
            match += 1
        # validate data type: DspSharingLinksResourceObject
        if not isinstance(v, DspSharingLinksResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DspSharingLinksResourceObject`")
        else:
            match += 1
        # validate data type: DynamicModulesResourceObject
        if not isinstance(v, DynamicModulesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DynamicModulesResourceObject`")
        else:
            match += 1
        # validate data type: DynamicPagesResourceObject
        if not isinstance(v, DynamicPagesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DynamicPagesResourceObject`")
        else:
            match += 1
        # validate data type: FolderItemsResourceObject
        if not isinstance(v, FolderItemsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FolderItemsResourceObject`")
        else:
            match += 1
        # validate data type: FoldersResourceObject
        if not isinstance(v, FoldersResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoldersResourceObject`")
        else:
            match += 1
        # validate data type: GenresResourceObject
        if not isinstance(v, GenresResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GenresResourceObject`")
        else:
            match += 1
        # validate data type: GroupsResourceObject
        if not isinstance(v, GroupsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GroupsResourceObject`")
        else:
            match += 1
        # validate data type: InstallationsResourceObject
        if not isinstance(v, InstallationsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InstallationsResourceObject`")
        else:
            match += 1
        # validate data type: LyricsResourceObject
        if not isinstance(v, LyricsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LyricsResourceObject`")
        else:
            match += 1
        # validate data type: ManualArtistClaimsResourceObject
        if not isinstance(v, ManualArtistClaimsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ManualArtistClaimsResourceObject`")
        else:
            match += 1
        # validate data type: OfflineTasksResourceObject
        if not isinstance(v, OfflineTasksResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OfflineTasksResourceObject`")
        else:
            match += 1
        # validate data type: PlayQueuesResourceObject
        if not isinstance(v, PlayQueuesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PlayQueuesResourceObject`")
        else:
            match += 1
        # validate data type: PlaylistGenerationSchedulesResourceObject
        if not isinstance(v, PlaylistGenerationSchedulesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PlaylistGenerationSchedulesResourceObject`")
        else:
            match += 1
        # validate data type: PlaylistGenerationsResourceObject
        if not isinstance(v, PlaylistGenerationsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PlaylistGenerationsResourceObject`")
        else:
            match += 1
        # validate data type: PlaylistsResourceObject
        if not isinstance(v, PlaylistsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PlaylistsResourceObject`")
        else:
            match += 1
        # validate data type: PriceConfigurationsResourceObject
        if not isinstance(v, PriceConfigurationsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PriceConfigurationsResourceObject`")
        else:
            match += 1
        # validate data type: ProviderOwnersResourceObject
        if not isinstance(v, ProviderOwnersResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ProviderOwnersResourceObject`")
        else:
            match += 1
        # validate data type: ProviderProductInfosResourceObject
        if not isinstance(v, ProviderProductInfosResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ProviderProductInfosResourceObject`")
        else:
            match += 1
        # validate data type: ProvidersResourceObject
        if not isinstance(v, ProvidersResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ProvidersResourceObject`")
        else:
            match += 1
        # validate data type: PurchasesResourceObject
        if not isinstance(v, PurchasesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PurchasesResourceObject`")
        else:
            match += 1
        # validate data type: ReactionSummariesResourceObject
        if not isinstance(v, ReactionSummariesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReactionSummariesResourceObject`")
        else:
            match += 1
        # validate data type: ReactionsResourceObject
        if not isinstance(v, ReactionsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReactionsResourceObject`")
        else:
            match += 1
        # validate data type: ResourceGrantInvitationsResourceObject
        if not isinstance(v, ResourceGrantInvitationsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResourceGrantInvitationsResourceObject`")
        else:
            match += 1
        # validate data type: ResourceGrantsResourceObject
        if not isinstance(v, ResourceGrantsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResourceGrantsResourceObject`")
        else:
            match += 1
        # validate data type: SavedSharesResourceObject
        if not isinstance(v, SavedSharesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SavedSharesResourceObject`")
        else:
            match += 1
        # validate data type: ScopesResourceObject
        if not isinstance(v, ScopesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ScopesResourceObject`")
        else:
            match += 1
        # validate data type: SearchHistoryEntriesResourceObject
        if not isinstance(v, SearchHistoryEntriesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SearchHistoryEntriesResourceObject`")
        else:
            match += 1
        # validate data type: SearchResultsResourceObject
        if not isinstance(v, SearchResultsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SearchResultsResourceObject`")
        else:
            match += 1
        # validate data type: SearchSuggestionsResourceObject
        if not isinstance(v, SearchSuggestionsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SearchSuggestionsResourceObject`")
        else:
            match += 1
        # validate data type: SharesResourceObject
        if not isinstance(v, SharesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SharesResourceObject`")
        else:
            match += 1
        # validate data type: SharingSummariesResourceObject
        if not isinstance(v, SharingSummariesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SharingSummariesResourceObject`")
        else:
            match += 1
        # validate data type: SquareConnectionsResourceObject
        if not isinstance(v, SquareConnectionsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SquareConnectionsResourceObject`")
        else:
            match += 1
        # validate data type: SquareItemVariationPhysicalCountsResourceObject
        if not isinstance(v, SquareItemVariationPhysicalCountsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SquareItemVariationPhysicalCountsResourceObject`")
        else:
            match += 1
        # validate data type: SquareItemVariationsResourceObject
        if not isinstance(v, SquareItemVariationsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SquareItemVariationsResourceObject`")
        else:
            match += 1
        # validate data type: SquareItemsResourceObject
        if not isinstance(v, SquareItemsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SquareItemsResourceObject`")
        else:
            match += 1
        # validate data type: SquareSitesResourceObject
        if not isinstance(v, SquareSitesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SquareSitesResourceObject`")
        else:
            match += 1
        # validate data type: StripeConnectionsResourceObject
        if not isinstance(v, StripeConnectionsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StripeConnectionsResourceObject`")
        else:
            match += 1
        # validate data type: StripeDashboardLinksResourceObject
        if not isinstance(v, StripeDashboardLinksResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StripeDashboardLinksResourceObject`")
        else:
            match += 1
        # validate data type: StudioHomeEventTilesResourceObject
        if not isinstance(v, StudioHomeEventTilesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StudioHomeEventTilesResourceObject`")
        else:
            match += 1
        # validate data type: StudioHomeInsightTilesResourceObject
        if not isinstance(v, StudioHomeInsightTilesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StudioHomeInsightTilesResourceObject`")
        else:
            match += 1
        # validate data type: StudioHomeMerchTilesResourceObject
        if not isinstance(v, StudioHomeMerchTilesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StudioHomeMerchTilesResourceObject`")
        else:
            match += 1
        # validate data type: StudioHomeMusicTilesResourceObject
        if not isinstance(v, StudioHomeMusicTilesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StudioHomeMusicTilesResourceObject`")
        else:
            match += 1
        # validate data type: SubscriptionPriceChangeDecisionsResourceObject
        if not isinstance(v, SubscriptionPriceChangeDecisionsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SubscriptionPriceChangeDecisionsResourceObject`")
        else:
            match += 1
        # validate data type: TemporaryUserTokensResourceObject
        if not isinstance(v, TemporaryUserTokensResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TemporaryUserTokensResourceObject`")
        else:
            match += 1
        # validate data type: TermsResourceObject
        if not isinstance(v, TermsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TermsResourceObject`")
        else:
            match += 1
        # validate data type: TrackFilesResourceObject
        if not isinstance(v, TrackFilesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TrackFilesResourceObject`")
        else:
            match += 1
        # validate data type: TrackManifestsResourceObject
        if not isinstance(v, TrackManifestsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TrackManifestsResourceObject`")
        else:
            match += 1
        # validate data type: TrackSourceFilesResourceObject
        if not isinstance(v, TrackSourceFilesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TrackSourceFilesResourceObject`")
        else:
            match += 1
        # validate data type: TrackStatisticsResourceObject
        if not isinstance(v, TrackStatisticsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TrackStatisticsResourceObject`")
        else:
            match += 1
        # validate data type: TracksResourceObject
        if not isinstance(v, TracksResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TracksResourceObject`")
        else:
            match += 1
        # validate data type: TracksMetadataStatusResourceObject
        if not isinstance(v, TracksMetadataStatusResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TracksMetadataStatusResourceObject`")
        else:
            match += 1
        # validate data type: UsageRulesResourceObject
        if not isinstance(v, UsageRulesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UsageRulesResourceObject`")
        else:
            match += 1
        # validate data type: UserCollectionAlbumsResourceObject
        if not isinstance(v, UserCollectionAlbumsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserCollectionAlbumsResourceObject`")
        else:
            match += 1
        # validate data type: UserCollectionArtistsResourceObject
        if not isinstance(v, UserCollectionArtistsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserCollectionArtistsResourceObject`")
        else:
            match += 1
        # validate data type: UserCollectionFoldersResourceObject
        if not isinstance(v, UserCollectionFoldersResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserCollectionFoldersResourceObject`")
        else:
            match += 1
        # validate data type: UserCollectionPlaylistsResourceObject
        if not isinstance(v, UserCollectionPlaylistsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserCollectionPlaylistsResourceObject`")
        else:
            match += 1
        # validate data type: UserCollectionSaveForLatersResourceObject
        if not isinstance(v, UserCollectionSaveForLatersResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserCollectionSaveForLatersResourceObject`")
        else:
            match += 1
        # validate data type: UserCollectionTracksResourceObject
        if not isinstance(v, UserCollectionTracksResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserCollectionTracksResourceObject`")
        else:
            match += 1
        # validate data type: UserCollectionVideosResourceObject
        if not isinstance(v, UserCollectionVideosResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserCollectionVideosResourceObject`")
        else:
            match += 1
        # validate data type: UserDailyMixesResourceObject
        if not isinstance(v, UserDailyMixesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserDailyMixesResourceObject`")
        else:
            match += 1
        # validate data type: UserDataExportRequestsResourceObject
        if not isinstance(v, UserDataExportRequestsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserDataExportRequestsResourceObject`")
        else:
            match += 1
        # validate data type: UserDataExportsResourceObject
        if not isinstance(v, UserDataExportsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserDataExportsResourceObject`")
        else:
            match += 1
        # validate data type: UserDiscoveryMixesResourceObject
        if not isinstance(v, UserDiscoveryMixesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserDiscoveryMixesResourceObject`")
        else:
            match += 1
        # validate data type: UserFeedItemsResourceObject
        if not isinstance(v, UserFeedItemsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserFeedItemsResourceObject`")
        else:
            match += 1
        # validate data type: UserFeedsResourceObject
        if not isinstance(v, UserFeedsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserFeedsResourceObject`")
        else:
            match += 1
        # validate data type: UserNewReleaseMixesResourceObject
        if not isinstance(v, UserNewReleaseMixesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserNewReleaseMixesResourceObject`")
        else:
            match += 1
        # validate data type: UserOfflineMixesResourceObject
        if not isinstance(v, UserOfflineMixesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserOfflineMixesResourceObject`")
        else:
            match += 1
        # validate data type: UserPlaybackStatesResourceObject
        if not isinstance(v, UserPlaybackStatesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserPlaybackStatesResourceObject`")
        else:
            match += 1
        # validate data type: UserRecommendationBlocksResourceObject
        if not isinstance(v, UserRecommendationBlocksResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserRecommendationBlocksResourceObject`")
        else:
            match += 1
        # validate data type: UserReportsResourceObject
        if not isinstance(v, UserReportsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserReportsResourceObject`")
        else:
            match += 1
        # validate data type: UserSubscriptionPriceChangesResourceObject
        if not isinstance(v, UserSubscriptionPriceChangesResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserSubscriptionPriceChangesResourceObject`")
        else:
            match += 1
        # validate data type: UsersResourceObject
        if not isinstance(v, UsersResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UsersResourceObject`")
        else:
            match += 1
        # validate data type: VideoManifestsResourceObject
        if not isinstance(v, VideoManifestsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `VideoManifestsResourceObject`")
        else:
            match += 1
        # validate data type: VideosResourceObject
        if not isinstance(v, VideosResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `VideosResourceObject`")
        else:
            match += 1
        # validate data type: ViewerContextsResourceObject
        if not isinstance(v, ViewerContextsResourceObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ViewerContextsResourceObject`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in IncludedInner with oneOf schemas: AcceptedTermsResourceObject, AlbumStatisticsResourceObject, AlbumsResourceObject, AppreciationsResourceObject, ArtistBiographiesResourceObject, ArtistClaimStatusesResourceObject, ArtistClaimsResourceObject, ArtistRolesResourceObject, ArtistSalesStatisticsResourceObject, ArtistStreamsStatisticsResourceObject, ArtistsResourceObject, ArtworkLibrariesResourceObject, ArtworksResourceObject, ChangeEventStreamsResourceObject, ClientCertificatesResourceObject, ClientsResourceObject, CollaborationInviteRedemptionsResourceObject, CollaborationInvitesResourceObject, CommentSummariesResourceObject, CommentsResourceObject, ContentClaimsResourceObject, CreditsResourceObject, DownloadsResourceObject, DspSharingLinksResourceObject, DynamicModulesResourceObject, DynamicPagesResourceObject, FolderItemsResourceObject, FoldersResourceObject, GenresResourceObject, GroupsResourceObject, InstallationsResourceObject, LyricsResourceObject, ManualArtistClaimsResourceObject, OfflineTasksResourceObject, PlayQueuesResourceObject, PlaylistGenerationSchedulesResourceObject, PlaylistGenerationsResourceObject, PlaylistsResourceObject, PriceConfigurationsResourceObject, ProviderOwnersResourceObject, ProviderProductInfosResourceObject, ProvidersResourceObject, PurchasesResourceObject, ReactionSummariesResourceObject, ReactionsResourceObject, ResourceGrantInvitationsResourceObject, ResourceGrantsResourceObject, SavedSharesResourceObject, ScopesResourceObject, SearchHistoryEntriesResourceObject, SearchResultsResourceObject, SearchSuggestionsResourceObject, SharesResourceObject, SharingSummariesResourceObject, SquareConnectionsResourceObject, SquareItemVariationPhysicalCountsResourceObject, SquareItemVariationsResourceObject, SquareItemsResourceObject, SquareSitesResourceObject, StripeConnectionsResourceObject, StripeDashboardLinksResourceObject, StudioHomeEventTilesResourceObject, StudioHomeInsightTilesResourceObject, StudioHomeMerchTilesResourceObject, StudioHomeMusicTilesResourceObject, SubscriptionPriceChangeDecisionsResourceObject, TemporaryUserTokensResourceObject, TermsResourceObject, TrackFilesResourceObject, TrackManifestsResourceObject, TrackSourceFilesResourceObject, TrackStatisticsResourceObject, TracksMetadataStatusResourceObject, TracksResourceObject, UsageRulesResourceObject, UserCollectionAlbumsResourceObject, UserCollectionArtistsResourceObject, UserCollectionFoldersResourceObject, UserCollectionPlaylistsResourceObject, UserCollectionSaveForLatersResourceObject, UserCollectionTracksResourceObject, UserCollectionVideosResourceObject, UserDailyMixesResourceObject, UserDataExportRequestsResourceObject, UserDataExportsResourceObject, UserDiscoveryMixesResourceObject, UserFeedItemsResourceObject, UserFeedsResourceObject, UserNewReleaseMixesResourceObject, UserOfflineMixesResourceObject, UserPlaybackStatesResourceObject, UserRecommendationBlocksResourceObject, UserReportsResourceObject, UserSubscriptionPriceChangesResourceObject, UsersResourceObject, VideoManifestsResourceObject, VideosResourceObject, ViewerContextsResourceObject. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in IncludedInner with oneOf schemas: AcceptedTermsResourceObject, AlbumStatisticsResourceObject, AlbumsResourceObject, AppreciationsResourceObject, ArtistBiographiesResourceObject, ArtistClaimStatusesResourceObject, ArtistClaimsResourceObject, ArtistRolesResourceObject, ArtistSalesStatisticsResourceObject, ArtistStreamsStatisticsResourceObject, ArtistsResourceObject, ArtworkLibrariesResourceObject, ArtworksResourceObject, ChangeEventStreamsResourceObject, ClientCertificatesResourceObject, ClientsResourceObject, CollaborationInviteRedemptionsResourceObject, CollaborationInvitesResourceObject, CommentSummariesResourceObject, CommentsResourceObject, ContentClaimsResourceObject, CreditsResourceObject, DownloadsResourceObject, DspSharingLinksResourceObject, DynamicModulesResourceObject, DynamicPagesResourceObject, FolderItemsResourceObject, FoldersResourceObject, GenresResourceObject, GroupsResourceObject, InstallationsResourceObject, LyricsResourceObject, ManualArtistClaimsResourceObject, OfflineTasksResourceObject, PlayQueuesResourceObject, PlaylistGenerationSchedulesResourceObject, PlaylistGenerationsResourceObject, PlaylistsResourceObject, PriceConfigurationsResourceObject, ProviderOwnersResourceObject, ProviderProductInfosResourceObject, ProvidersResourceObject, PurchasesResourceObject, ReactionSummariesResourceObject, ReactionsResourceObject, ResourceGrantInvitationsResourceObject, ResourceGrantsResourceObject, SavedSharesResourceObject, ScopesResourceObject, SearchHistoryEntriesResourceObject, SearchResultsResourceObject, SearchSuggestionsResourceObject, SharesResourceObject, SharingSummariesResourceObject, SquareConnectionsResourceObject, SquareItemVariationPhysicalCountsResourceObject, SquareItemVariationsResourceObject, SquareItemsResourceObject, SquareSitesResourceObject, StripeConnectionsResourceObject, StripeDashboardLinksResourceObject, StudioHomeEventTilesResourceObject, StudioHomeInsightTilesResourceObject, StudioHomeMerchTilesResourceObject, StudioHomeMusicTilesResourceObject, SubscriptionPriceChangeDecisionsResourceObject, TemporaryUserTokensResourceObject, TermsResourceObject, TrackFilesResourceObject, TrackManifestsResourceObject, TrackSourceFilesResourceObject, TrackStatisticsResourceObject, TracksMetadataStatusResourceObject, TracksResourceObject, UsageRulesResourceObject, UserCollectionAlbumsResourceObject, UserCollectionArtistsResourceObject, UserCollectionFoldersResourceObject, UserCollectionPlaylistsResourceObject, UserCollectionSaveForLatersResourceObject, UserCollectionTracksResourceObject, UserCollectionVideosResourceObject, UserDailyMixesResourceObject, UserDataExportRequestsResourceObject, UserDataExportsResourceObject, UserDiscoveryMixesResourceObject, UserFeedItemsResourceObject, UserFeedsResourceObject, UserNewReleaseMixesResourceObject, UserOfflineMixesResourceObject, UserPlaybackStatesResourceObject, UserRecommendationBlocksResourceObject, UserReportsResourceObject, UserSubscriptionPriceChangesResourceObject, UsersResourceObject, VideoManifestsResourceObject, VideosResourceObject, ViewerContextsResourceObject. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into AcceptedTermsResourceObject
        try:
            instance.actual_instance = AcceptedTermsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AlbumStatisticsResourceObject
        try:
            instance.actual_instance = AlbumStatisticsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AlbumsResourceObject
        try:
            instance.actual_instance = AlbumsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AppreciationsResourceObject
        try:
            instance.actual_instance = AppreciationsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ArtistBiographiesResourceObject
        try:
            instance.actual_instance = ArtistBiographiesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ArtistClaimStatusesResourceObject
        try:
            instance.actual_instance = ArtistClaimStatusesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ArtistClaimsResourceObject
        try:
            instance.actual_instance = ArtistClaimsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ArtistRolesResourceObject
        try:
            instance.actual_instance = ArtistRolesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ArtistSalesStatisticsResourceObject
        try:
            instance.actual_instance = ArtistSalesStatisticsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ArtistStreamsStatisticsResourceObject
        try:
            instance.actual_instance = ArtistStreamsStatisticsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ArtistsResourceObject
        try:
            instance.actual_instance = ArtistsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ArtworkLibrariesResourceObject
        try:
            instance.actual_instance = ArtworkLibrariesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ArtworksResourceObject
        try:
            instance.actual_instance = ArtworksResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ChangeEventStreamsResourceObject
        try:
            instance.actual_instance = ChangeEventStreamsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ClientCertificatesResourceObject
        try:
            instance.actual_instance = ClientCertificatesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ClientsResourceObject
        try:
            instance.actual_instance = ClientsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CollaborationInviteRedemptionsResourceObject
        try:
            instance.actual_instance = CollaborationInviteRedemptionsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CollaborationInvitesResourceObject
        try:
            instance.actual_instance = CollaborationInvitesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CommentSummariesResourceObject
        try:
            instance.actual_instance = CommentSummariesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CommentsResourceObject
        try:
            instance.actual_instance = CommentsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ContentClaimsResourceObject
        try:
            instance.actual_instance = ContentClaimsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CreditsResourceObject
        try:
            instance.actual_instance = CreditsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DownloadsResourceObject
        try:
            instance.actual_instance = DownloadsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DspSharingLinksResourceObject
        try:
            instance.actual_instance = DspSharingLinksResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DynamicModulesResourceObject
        try:
            instance.actual_instance = DynamicModulesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DynamicPagesResourceObject
        try:
            instance.actual_instance = DynamicPagesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FolderItemsResourceObject
        try:
            instance.actual_instance = FolderItemsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FoldersResourceObject
        try:
            instance.actual_instance = FoldersResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GenresResourceObject
        try:
            instance.actual_instance = GenresResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GroupsResourceObject
        try:
            instance.actual_instance = GroupsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InstallationsResourceObject
        try:
            instance.actual_instance = InstallationsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LyricsResourceObject
        try:
            instance.actual_instance = LyricsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ManualArtistClaimsResourceObject
        try:
            instance.actual_instance = ManualArtistClaimsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OfflineTasksResourceObject
        try:
            instance.actual_instance = OfflineTasksResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PlayQueuesResourceObject
        try:
            instance.actual_instance = PlayQueuesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PlaylistGenerationSchedulesResourceObject
        try:
            instance.actual_instance = PlaylistGenerationSchedulesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PlaylistGenerationsResourceObject
        try:
            instance.actual_instance = PlaylistGenerationsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PlaylistsResourceObject
        try:
            instance.actual_instance = PlaylistsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PriceConfigurationsResourceObject
        try:
            instance.actual_instance = PriceConfigurationsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ProviderOwnersResourceObject
        try:
            instance.actual_instance = ProviderOwnersResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ProviderProductInfosResourceObject
        try:
            instance.actual_instance = ProviderProductInfosResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ProvidersResourceObject
        try:
            instance.actual_instance = ProvidersResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PurchasesResourceObject
        try:
            instance.actual_instance = PurchasesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ReactionSummariesResourceObject
        try:
            instance.actual_instance = ReactionSummariesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ReactionsResourceObject
        try:
            instance.actual_instance = ReactionsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ResourceGrantInvitationsResourceObject
        try:
            instance.actual_instance = ResourceGrantInvitationsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ResourceGrantsResourceObject
        try:
            instance.actual_instance = ResourceGrantsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SavedSharesResourceObject
        try:
            instance.actual_instance = SavedSharesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ScopesResourceObject
        try:
            instance.actual_instance = ScopesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SearchHistoryEntriesResourceObject
        try:
            instance.actual_instance = SearchHistoryEntriesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SearchResultsResourceObject
        try:
            instance.actual_instance = SearchResultsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SearchSuggestionsResourceObject
        try:
            instance.actual_instance = SearchSuggestionsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SharesResourceObject
        try:
            instance.actual_instance = SharesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SharingSummariesResourceObject
        try:
            instance.actual_instance = SharingSummariesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SquareConnectionsResourceObject
        try:
            instance.actual_instance = SquareConnectionsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SquareItemVariationPhysicalCountsResourceObject
        try:
            instance.actual_instance = SquareItemVariationPhysicalCountsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SquareItemVariationsResourceObject
        try:
            instance.actual_instance = SquareItemVariationsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SquareItemsResourceObject
        try:
            instance.actual_instance = SquareItemsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SquareSitesResourceObject
        try:
            instance.actual_instance = SquareSitesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into StripeConnectionsResourceObject
        try:
            instance.actual_instance = StripeConnectionsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into StripeDashboardLinksResourceObject
        try:
            instance.actual_instance = StripeDashboardLinksResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into StudioHomeEventTilesResourceObject
        try:
            instance.actual_instance = StudioHomeEventTilesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into StudioHomeInsightTilesResourceObject
        try:
            instance.actual_instance = StudioHomeInsightTilesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into StudioHomeMerchTilesResourceObject
        try:
            instance.actual_instance = StudioHomeMerchTilesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into StudioHomeMusicTilesResourceObject
        try:
            instance.actual_instance = StudioHomeMusicTilesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SubscriptionPriceChangeDecisionsResourceObject
        try:
            instance.actual_instance = SubscriptionPriceChangeDecisionsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TemporaryUserTokensResourceObject
        try:
            instance.actual_instance = TemporaryUserTokensResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TermsResourceObject
        try:
            instance.actual_instance = TermsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TrackFilesResourceObject
        try:
            instance.actual_instance = TrackFilesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TrackManifestsResourceObject
        try:
            instance.actual_instance = TrackManifestsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TrackSourceFilesResourceObject
        try:
            instance.actual_instance = TrackSourceFilesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TrackStatisticsResourceObject
        try:
            instance.actual_instance = TrackStatisticsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TracksResourceObject
        try:
            instance.actual_instance = TracksResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TracksMetadataStatusResourceObject
        try:
            instance.actual_instance = TracksMetadataStatusResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UsageRulesResourceObject
        try:
            instance.actual_instance = UsageRulesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserCollectionAlbumsResourceObject
        try:
            instance.actual_instance = UserCollectionAlbumsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserCollectionArtistsResourceObject
        try:
            instance.actual_instance = UserCollectionArtistsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserCollectionFoldersResourceObject
        try:
            instance.actual_instance = UserCollectionFoldersResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserCollectionPlaylistsResourceObject
        try:
            instance.actual_instance = UserCollectionPlaylistsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserCollectionSaveForLatersResourceObject
        try:
            instance.actual_instance = UserCollectionSaveForLatersResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserCollectionTracksResourceObject
        try:
            instance.actual_instance = UserCollectionTracksResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserCollectionVideosResourceObject
        try:
            instance.actual_instance = UserCollectionVideosResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserDailyMixesResourceObject
        try:
            instance.actual_instance = UserDailyMixesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserDataExportRequestsResourceObject
        try:
            instance.actual_instance = UserDataExportRequestsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserDataExportsResourceObject
        try:
            instance.actual_instance = UserDataExportsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserDiscoveryMixesResourceObject
        try:
            instance.actual_instance = UserDiscoveryMixesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserFeedItemsResourceObject
        try:
            instance.actual_instance = UserFeedItemsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserFeedsResourceObject
        try:
            instance.actual_instance = UserFeedsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserNewReleaseMixesResourceObject
        try:
            instance.actual_instance = UserNewReleaseMixesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserOfflineMixesResourceObject
        try:
            instance.actual_instance = UserOfflineMixesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserPlaybackStatesResourceObject
        try:
            instance.actual_instance = UserPlaybackStatesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserRecommendationBlocksResourceObject
        try:
            instance.actual_instance = UserRecommendationBlocksResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserReportsResourceObject
        try:
            instance.actual_instance = UserReportsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserSubscriptionPriceChangesResourceObject
        try:
            instance.actual_instance = UserSubscriptionPriceChangesResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UsersResourceObject
        try:
            instance.actual_instance = UsersResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into VideoManifestsResourceObject
        try:
            instance.actual_instance = VideoManifestsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into VideosResourceObject
        try:
            instance.actual_instance = VideosResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ViewerContextsResourceObject
        try:
            instance.actual_instance = ViewerContextsResourceObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into IncludedInner with oneOf schemas: AcceptedTermsResourceObject, AlbumStatisticsResourceObject, AlbumsResourceObject, AppreciationsResourceObject, ArtistBiographiesResourceObject, ArtistClaimStatusesResourceObject, ArtistClaimsResourceObject, ArtistRolesResourceObject, ArtistSalesStatisticsResourceObject, ArtistStreamsStatisticsResourceObject, ArtistsResourceObject, ArtworkLibrariesResourceObject, ArtworksResourceObject, ChangeEventStreamsResourceObject, ClientCertificatesResourceObject, ClientsResourceObject, CollaborationInviteRedemptionsResourceObject, CollaborationInvitesResourceObject, CommentSummariesResourceObject, CommentsResourceObject, ContentClaimsResourceObject, CreditsResourceObject, DownloadsResourceObject, DspSharingLinksResourceObject, DynamicModulesResourceObject, DynamicPagesResourceObject, FolderItemsResourceObject, FoldersResourceObject, GenresResourceObject, GroupsResourceObject, InstallationsResourceObject, LyricsResourceObject, ManualArtistClaimsResourceObject, OfflineTasksResourceObject, PlayQueuesResourceObject, PlaylistGenerationSchedulesResourceObject, PlaylistGenerationsResourceObject, PlaylistsResourceObject, PriceConfigurationsResourceObject, ProviderOwnersResourceObject, ProviderProductInfosResourceObject, ProvidersResourceObject, PurchasesResourceObject, ReactionSummariesResourceObject, ReactionsResourceObject, ResourceGrantInvitationsResourceObject, ResourceGrantsResourceObject, SavedSharesResourceObject, ScopesResourceObject, SearchHistoryEntriesResourceObject, SearchResultsResourceObject, SearchSuggestionsResourceObject, SharesResourceObject, SharingSummariesResourceObject, SquareConnectionsResourceObject, SquareItemVariationPhysicalCountsResourceObject, SquareItemVariationsResourceObject, SquareItemsResourceObject, SquareSitesResourceObject, StripeConnectionsResourceObject, StripeDashboardLinksResourceObject, StudioHomeEventTilesResourceObject, StudioHomeInsightTilesResourceObject, StudioHomeMerchTilesResourceObject, StudioHomeMusicTilesResourceObject, SubscriptionPriceChangeDecisionsResourceObject, TemporaryUserTokensResourceObject, TermsResourceObject, TrackFilesResourceObject, TrackManifestsResourceObject, TrackSourceFilesResourceObject, TrackStatisticsResourceObject, TracksMetadataStatusResourceObject, TracksResourceObject, UsageRulesResourceObject, UserCollectionAlbumsResourceObject, UserCollectionArtistsResourceObject, UserCollectionFoldersResourceObject, UserCollectionPlaylistsResourceObject, UserCollectionSaveForLatersResourceObject, UserCollectionTracksResourceObject, UserCollectionVideosResourceObject, UserDailyMixesResourceObject, UserDataExportRequestsResourceObject, UserDataExportsResourceObject, UserDiscoveryMixesResourceObject, UserFeedItemsResourceObject, UserFeedsResourceObject, UserNewReleaseMixesResourceObject, UserOfflineMixesResourceObject, UserPlaybackStatesResourceObject, UserRecommendationBlocksResourceObject, UserReportsResourceObject, UserSubscriptionPriceChangesResourceObject, UsersResourceObject, VideoManifestsResourceObject, VideosResourceObject, ViewerContextsResourceObject. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into IncludedInner with oneOf schemas: AcceptedTermsResourceObject, AlbumStatisticsResourceObject, AlbumsResourceObject, AppreciationsResourceObject, ArtistBiographiesResourceObject, ArtistClaimStatusesResourceObject, ArtistClaimsResourceObject, ArtistRolesResourceObject, ArtistSalesStatisticsResourceObject, ArtistStreamsStatisticsResourceObject, ArtistsResourceObject, ArtworkLibrariesResourceObject, ArtworksResourceObject, ChangeEventStreamsResourceObject, ClientCertificatesResourceObject, ClientsResourceObject, CollaborationInviteRedemptionsResourceObject, CollaborationInvitesResourceObject, CommentSummariesResourceObject, CommentsResourceObject, ContentClaimsResourceObject, CreditsResourceObject, DownloadsResourceObject, DspSharingLinksResourceObject, DynamicModulesResourceObject, DynamicPagesResourceObject, FolderItemsResourceObject, FoldersResourceObject, GenresResourceObject, GroupsResourceObject, InstallationsResourceObject, LyricsResourceObject, ManualArtistClaimsResourceObject, OfflineTasksResourceObject, PlayQueuesResourceObject, PlaylistGenerationSchedulesResourceObject, PlaylistGenerationsResourceObject, PlaylistsResourceObject, PriceConfigurationsResourceObject, ProviderOwnersResourceObject, ProviderProductInfosResourceObject, ProvidersResourceObject, PurchasesResourceObject, ReactionSummariesResourceObject, ReactionsResourceObject, ResourceGrantInvitationsResourceObject, ResourceGrantsResourceObject, SavedSharesResourceObject, ScopesResourceObject, SearchHistoryEntriesResourceObject, SearchResultsResourceObject, SearchSuggestionsResourceObject, SharesResourceObject, SharingSummariesResourceObject, SquareConnectionsResourceObject, SquareItemVariationPhysicalCountsResourceObject, SquareItemVariationsResourceObject, SquareItemsResourceObject, SquareSitesResourceObject, StripeConnectionsResourceObject, StripeDashboardLinksResourceObject, StudioHomeEventTilesResourceObject, StudioHomeInsightTilesResourceObject, StudioHomeMerchTilesResourceObject, StudioHomeMusicTilesResourceObject, SubscriptionPriceChangeDecisionsResourceObject, TemporaryUserTokensResourceObject, TermsResourceObject, TrackFilesResourceObject, TrackManifestsResourceObject, TrackSourceFilesResourceObject, TrackStatisticsResourceObject, TracksMetadataStatusResourceObject, TracksResourceObject, UsageRulesResourceObject, UserCollectionAlbumsResourceObject, UserCollectionArtistsResourceObject, UserCollectionFoldersResourceObject, UserCollectionPlaylistsResourceObject, UserCollectionSaveForLatersResourceObject, UserCollectionTracksResourceObject, UserCollectionVideosResourceObject, UserDailyMixesResourceObject, UserDataExportRequestsResourceObject, UserDataExportsResourceObject, UserDiscoveryMixesResourceObject, UserFeedItemsResourceObject, UserFeedsResourceObject, UserNewReleaseMixesResourceObject, UserOfflineMixesResourceObject, UserPlaybackStatesResourceObject, UserRecommendationBlocksResourceObject, UserReportsResourceObject, UserSubscriptionPriceChangesResourceObject, UsersResourceObject, VideoManifestsResourceObject, VideosResourceObject, ViewerContextsResourceObject. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

from tidal.models.accepted_terms_resource_object import AcceptedTermsResourceObject
from tidal.models.album_statistics_resource_object import AlbumStatisticsResourceObject
from tidal.models.albums_resource_object import AlbumsResourceObject
from tidal.models.artist_biographies_resource_object import ArtistBiographiesResourceObject
from tidal.models.artist_claims_resource_object import ArtistClaimsResourceObject
from tidal.models.artist_sales_statistics_resource_object import ArtistSalesStatisticsResourceObject
from tidal.models.artist_streams_statistics_resource_object import ArtistStreamsStatisticsResourceObject
from tidal.models.artists_resource_object import ArtistsResourceObject
from tidal.models.artwork_libraries_resource_object import ArtworkLibrariesResourceObject
from tidal.models.artworks_resource_object import ArtworksResourceObject
from tidal.models.client_certificates_resource_object import ClientCertificatesResourceObject
from tidal.models.clients_resource_object import ClientsResourceObject
from tidal.models.collaboration_invites_resource_object import CollaborationInvitesResourceObject
from tidal.models.comment_summaries_resource_object import CommentSummariesResourceObject
from tidal.models.comments_resource_object import CommentsResourceObject
from tidal.models.content_claims_resource_object import ContentClaimsResourceObject
from tidal.models.credits_resource_object import CreditsResourceObject
from tidal.models.downloads_resource_object import DownloadsResourceObject
from tidal.models.dsp_sharing_links_resource_object import DspSharingLinksResourceObject
from tidal.models.dynamic_modules_resource_object import DynamicModulesResourceObject
from tidal.models.dynamic_pages_resource_object import DynamicPagesResourceObject
from tidal.models.folder_items_resource_object import FolderItemsResourceObject
from tidal.models.folders_resource_object import FoldersResourceObject
from tidal.models.installations_resource_object import InstallationsResourceObject
from tidal.models.lyrics_resource_object import LyricsResourceObject
from tidal.models.offline_tasks_resource_object import OfflineTasksResourceObject
from tidal.models.play_queues_resource_object import PlayQueuesResourceObject
from tidal.models.playlist_generation_schedules_resource_object import PlaylistGenerationSchedulesResourceObject
from tidal.models.playlist_generations_resource_object import PlaylistGenerationsResourceObject
from tidal.models.playlists_resource_object import PlaylistsResourceObject
from tidal.models.provider_owners_resource_object import ProviderOwnersResourceObject
from tidal.models.provider_product_infos_resource_object import ProviderProductInfosResourceObject
from tidal.models.purchases_resource_object import PurchasesResourceObject
from tidal.models.reaction_summaries_resource_object import ReactionSummariesResourceObject
from tidal.models.reactions_resource_object import ReactionsResourceObject
from tidal.models.resource_grant_invitations_resource_object import ResourceGrantInvitationsResourceObject
from tidal.models.resource_grants_resource_object import ResourceGrantsResourceObject
from tidal.models.search_results_resource_object import SearchResultsResourceObject
from tidal.models.search_suggestions_resource_object import SearchSuggestionsResourceObject
from tidal.models.shares_resource_object import SharesResourceObject
from tidal.models.sharing_summaries_resource_object import SharingSummariesResourceObject
from tidal.models.square_connections_resource_object import SquareConnectionsResourceObject
from tidal.models.square_item_variations_resource_object import SquareItemVariationsResourceObject
from tidal.models.square_items_resource_object import SquareItemsResourceObject
from tidal.models.square_sites_resource_object import SquareSitesResourceObject
from tidal.models.stripe_connections_resource_object import StripeConnectionsResourceObject
from tidal.models.stripe_dashboard_links_resource_object import StripeDashboardLinksResourceObject
from tidal.models.studio_home_insight_tiles_resource_object import StudioHomeInsightTilesResourceObject
from tidal.models.studio_home_merch_tiles_resource_object import StudioHomeMerchTilesResourceObject
from tidal.models.studio_home_music_tiles_resource_object import StudioHomeMusicTilesResourceObject
from tidal.models.subscription_price_change_decisions_resource_object import SubscriptionPriceChangeDecisionsResourceObject
from tidal.models.temporary_user_tokens_resource_object import TemporaryUserTokensResourceObject
from tidal.models.track_source_files_resource_object import TrackSourceFilesResourceObject
from tidal.models.track_statistics_resource_object import TrackStatisticsResourceObject
from tidal.models.tracks_resource_object import TracksResourceObject
from tidal.models.user_collection_albums_resource_object import UserCollectionAlbumsResourceObject
from tidal.models.user_collection_artists_resource_object import UserCollectionArtistsResourceObject
from tidal.models.user_collection_folders_resource_object import UserCollectionFoldersResourceObject
from tidal.models.user_collection_playlists_resource_object import UserCollectionPlaylistsResourceObject
from tidal.models.user_collection_save_for_laters_resource_object import UserCollectionSaveForLatersResourceObject
from tidal.models.user_collection_tracks_resource_object import UserCollectionTracksResourceObject
from tidal.models.user_collection_videos_resource_object import UserCollectionVideosResourceObject
from tidal.models.user_daily_mixes_resource_object import UserDailyMixesResourceObject
from tidal.models.user_data_exports_resource_object import UserDataExportsResourceObject
from tidal.models.user_discovery_mixes_resource_object import UserDiscoveryMixesResourceObject
from tidal.models.user_feed_items_resource_object import UserFeedItemsResourceObject
from tidal.models.user_new_release_mixes_resource_object import UserNewReleaseMixesResourceObject
from tidal.models.user_offline_mixes_resource_object import UserOfflineMixesResourceObject
from tidal.models.user_playback_states_resource_object import UserPlaybackStatesResourceObject
from tidal.models.user_recommendation_blocks_resource_object import UserRecommendationBlocksResourceObject
from tidal.models.user_subscription_price_changes_resource_object import UserSubscriptionPriceChangesResourceObject
from tidal.models.users_resource_object import UsersResourceObject
from tidal.models.videos_resource_object import VideosResourceObject
from tidal.models.viewer_contexts_resource_object import ViewerContextsResourceObject
# TODO: Rewrite to not use raise_errors
IncludedInner.model_rebuild(raise_errors=False)

