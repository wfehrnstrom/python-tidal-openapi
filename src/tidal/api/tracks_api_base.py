# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.tracks_albums_multi_relationship_data_document import TracksAlbumsMultiRelationshipDataDocument
from tidal.models.tracks_albums_relationship_update_operation_payload import TracksAlbumsRelationshipUpdateOperationPayload
from tidal.models.tracks_artists_multi_relationship_data_document import TracksArtistsMultiRelationshipDataDocument
from tidal.models.tracks_artists_relationship_update_operation_payload import TracksArtistsRelationshipUpdateOperationPayload
from tidal.models.tracks_create_operation_payload import TracksCreateOperationPayload
from tidal.models.tracks_create_single_resource_data_document import TracksCreateSingleResourceDataDocument
from tidal.models.tracks_credits_multi_relationship_data_document import TracksCreditsMultiRelationshipDataDocument
from tidal.models.tracks_download_single_relationship_data_document import TracksDownloadSingleRelationshipDataDocument
from tidal.models.tracks_genres_multi_relationship_data_document import TracksGenresMultiRelationshipDataDocument
from tidal.models.tracks_lyrics_multi_relationship_data_document import TracksLyricsMultiRelationshipDataDocument
from tidal.models.tracks_metadata_status_single_relationship_data_document import TracksMetadataStatusSingleRelationshipDataDocument
from tidal.models.tracks_multi_resource_data_document import TracksMultiResourceDataDocument
from tidal.models.tracks_owners_multi_relationship_data_document import TracksOwnersMultiRelationshipDataDocument
from tidal.models.tracks_price_config_single_relationship_data_document import TracksPriceConfigSingleRelationshipDataDocument
from tidal.models.tracks_providers_multi_relationship_data_document import TracksProvidersMultiRelationshipDataDocument
from tidal.models.tracks_radio_multi_relationship_data_document import TracksRadioMultiRelationshipDataDocument
from tidal.models.tracks_replacement_single_relationship_data_document import TracksReplacementSingleRelationshipDataDocument
from tidal.models.tracks_shares_multi_relationship_data_document import TracksSharesMultiRelationshipDataDocument
from tidal.models.tracks_similar_tracks_multi_relationship_data_document import TracksSimilarTracksMultiRelationshipDataDocument
from tidal.models.tracks_single_resource_data_document import TracksSingleResourceDataDocument
from tidal.models.tracks_source_file_single_relationship_data_document import TracksSourceFileSingleRelationshipDataDocument
from tidal.models.tracks_suggested_tracks_multi_relationship_data_document import TracksSuggestedTracksMultiRelationshipDataDocument
from tidal.models.tracks_track_statistics_single_relationship_data_document import TracksTrackStatisticsSingleRelationshipDataDocument
from tidal.models.tracks_update_operation_payload import TracksUpdateOperationPayload
from tidal.models.tracks_usage_rules_single_relationship_data_document import TracksUsageRulesSingleRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseTracksApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTracksApi.subclasses = BaseTracksApi.subclasses + (cls,)
    async def tracks_get(
        self,
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of track IDs (e.g. `75413016`)")],
        filter_isrc: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of ISRCs. When a single ISRC is provided, pagination is supported and multiple tracks may be returned. When multiple ISRCs are provided, one track per ISRC is returned without pagination. (e.g. `QMJMT1701237`)")],
        filter_owners_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1)]], Field(description="User id. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums, artists, credits, download, genres, lyrics, metadataStatus, owners, priceConfig, providers, radio, replacement, shares, similarTracks, sourceFile, suggestedTracks, trackStatistics, usageRules")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
        sort: Annotated[Optional[List[str]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")],
    ) -> TracksMultiResourceDataDocument:
        """Retrieves multiple tracks by available filters, or without if applicable."""
        ...


    async def tracks_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        tracks_create_operation_payload: Optional[TracksCreateOperationPayload],
    ) -> TracksCreateSingleResourceDataDocument:
        """Creates a new track."""
        ...


    async def tracks_id_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums, artists, credits, download, genres, lyrics, metadataStatus, owners, priceConfig, providers, radio, replacement, shares, similarTracks, sourceFile, suggestedTracks, trackStatistics, usageRules")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksSingleResourceDataDocument:
        """Retrieves single track by id."""
        ...


    async def tracks_id_delete(
        self,
        id: Annotated[str, Field(description="Track id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> MutationResponseDocument:
        """Deletes existing track."""
        ...


    async def tracks_id_patch(
        self,
        id: Annotated[str, Field(description="Track id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
        tracks_update_operation_payload: Optional[TracksUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Updates existing track. A COLLABORATOR on the track may update it; changing accessType or isrc needs OWNER."""
        ...


    async def tracks_id_relationships_albums_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksAlbumsMultiRelationshipDataDocument:
        """Retrieves albums relationship."""
        ...


    async def tracks_id_relationships_albums_patch(
        self,
        id: Annotated[str, Field(description="Track id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
        tracks_albums_relationship_update_operation_payload: Optional[TracksAlbumsRelationshipUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Moves the uploaded track to the supplied album, replacing its previous album association. Exactly one album is required; empty data cannot clear it. The caller needs COLLABORATOR on the track and the album. The album must be in the same user&#39;s folders as the track (409 otherwise). Returns an acknowledgement."""
        ...


    async def tracks_id_relationships_artists_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artists")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksArtistsMultiRelationshipDataDocument:
        """Retrieves artists relationship."""
        ...


    async def tracks_id_relationships_artists_patch(
        self,
        id: Annotated[str, Field(description="Track id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
        tracks_artists_relationship_update_operation_payload: Optional[TracksArtistsRelationshipUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Sets the track&#39;s artists, replacing the current list. Artists are listed in the order given. Provide 1 to 10 distinct artists. You can add your own artist profile and the profiles of users who have owner or collaborator access to the track or its album. Owners and collaborators can change its artists. Returns an acknowledgement."""
        ...


    async def tracks_id_relationships_credits_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: credits")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: credits.artist.albums")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksCreditsMultiRelationshipDataDocument:
        """Retrieves credits relationship."""
        ...


    async def tracks_id_relationships_download_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: download")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksDownloadSingleRelationshipDataDocument:
        """Retrieves download relationship."""
        ...


    async def tracks_id_relationships_genres_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: genres")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksGenresMultiRelationshipDataDocument:
        """Retrieves genres relationship."""
        ...


    async def tracks_id_relationships_lyrics_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: lyrics")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: lyrics.track")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksLyricsMultiRelationshipDataDocument:
        """Retrieves lyrics relationship."""
        ...


    async def tracks_id_relationships_metadata_status_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: metadataStatus")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksMetadataStatusSingleRelationshipDataDocument:
        """Retrieves metadataStatus relationship."""
        ...


    async def tracks_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def tracks_id_relationships_price_config_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: priceConfig")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksPriceConfigSingleRelationshipDataDocument:
        """Retrieves priceConfig relationship."""
        ...


    async def tracks_id_relationships_providers_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: providers")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksProvidersMultiRelationshipDataDocument:
        """Retrieves providers relationship."""
        ...


    async def tracks_id_relationships_radio_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: radio")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: radio.items")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksRadioMultiRelationshipDataDocument:
        """Retrieves radio relationship."""
        ...


    async def tracks_id_relationships_replacement_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: replacement")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: replacement")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksReplacementSingleRelationshipDataDocument:
        """Retrieves replacement relationship."""
        ...


    async def tracks_id_relationships_shares_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: shares")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: shares.sharedResources")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksSharesMultiRelationshipDataDocument:
        """The track&#39;s share links, active and expired, newest first."""
        ...


    async def tracks_id_relationships_similar_tracks_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: similarTracks")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarTracks")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksSimilarTracksMultiRelationshipDataDocument:
        """Retrieves similarTracks relationship."""
        ...


    async def tracks_id_relationships_source_file_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: sourceFile")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksSourceFileSingleRelationshipDataDocument:
        """Retrieves sourceFile relationship."""
        ...


    async def tracks_id_relationships_suggested_tracks_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: suggestedTracks")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: suggestedTracks")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksSuggestedTracksMultiRelationshipDataDocument:
        """Retrieves suggestedTracks relationship."""
        ...


    async def tracks_id_relationships_track_statistics_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: trackStatistics")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksTrackStatisticsSingleRelationshipDataDocument:
        """Retrieves trackStatistics relationship."""
        ...


    async def tracks_id_relationships_usage_rules_get(
        self,
        id: Annotated[str, Field(description="Track id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: usageRules")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TracksUsageRulesSingleRelationshipDataDocument:
        """Retrieves usageRules relationship."""
        ...
