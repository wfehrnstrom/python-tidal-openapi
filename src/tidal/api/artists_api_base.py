# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.artists_albums_multi_relationship_data_document import ArtistsAlbumsMultiRelationshipDataDocument
from tidal.models.artists_banner_art_multi_relationship_data_document import ArtistsBannerArtMultiRelationshipDataDocument
from tidal.models.artists_banner_art_relationship_update_operation_payload import ArtistsBannerArtRelationshipUpdateOperationPayload
from tidal.models.artists_biography_single_relationship_data_document import ArtistsBiographySingleRelationshipDataDocument
from tidal.models.artists_claim_status_single_relationship_data_document import ArtistsClaimStatusSingleRelationshipDataDocument
from tidal.models.artists_create_operation_payload import ArtistsCreateOperationPayload
from tidal.models.artists_create_single_resource_data_document import ArtistsCreateSingleResourceDataDocument
from tidal.models.artists_followers_multi_relationship_data_document import ArtistsFollowersMultiRelationshipDataDocument
from tidal.models.artists_following_multi_relationship_data_document import ArtistsFollowingMultiRelationshipDataDocument
from tidal.models.artists_following_relationship_add_operation_payload import ArtistsFollowingRelationshipAddOperationPayload
from tidal.models.artists_following_relationship_remove_operation_payload import ArtistsFollowingRelationshipRemoveOperationPayload
from tidal.models.artists_logo_art_multi_relationship_data_document import ArtistsLogoArtMultiRelationshipDataDocument
from tidal.models.artists_logo_art_relationship_update_operation_payload import ArtistsLogoArtRelationshipUpdateOperationPayload
from tidal.models.artists_multi_resource_data_document import ArtistsMultiResourceDataDocument
from tidal.models.artists_owners_multi_relationship_data_document import ArtistsOwnersMultiRelationshipDataDocument
from tidal.models.artists_profile_art_multi_relationship_data_document import ArtistsProfileArtMultiRelationshipDataDocument
from tidal.models.artists_profile_art_relationship_update_operation_payload import ArtistsProfileArtRelationshipUpdateOperationPayload
from tidal.models.artists_radio_multi_relationship_data_document import ArtistsRadioMultiRelationshipDataDocument
from tidal.models.artists_roles_multi_relationship_data_document import ArtistsRolesMultiRelationshipDataDocument
from tidal.models.artists_similar_artists_multi_relationship_data_document import ArtistsSimilarArtistsMultiRelationshipDataDocument
from tidal.models.artists_single_resource_data_document import ArtistsSingleResourceDataDocument
from tidal.models.artists_track_providers_multi_relationship_data_document import ArtistsTrackProvidersMultiRelationshipDataDocument
from tidal.models.artists_tracks_multi_relationship_data_document import ArtistsTracksMultiRelationshipDataDocument
from tidal.models.artists_update_operation_payload import ArtistsUpdateOperationPayload
from tidal.models.artists_videos_multi_relationship_data_document import ArtistsVideosMultiRelationshipDataDocument
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
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseArtistsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseArtistsApi.subclasses = BaseArtistsApi.subclasses + (cls,)
    async def artists_get(
        self,
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        filter_handle: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="Artist handle (e.g. `jayz`)")],
        filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of artist IDs (e.g. `1566`)")],
        filter_owners_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1)]], Field(description="User id. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")],
    ) -> ArtistsMultiResourceDataDocument:
        """Retrieves multiple artists by available filters, or without if applicable."""
        ...


    async def artists_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        artists_create_operation_payload: Optional[ArtistsCreateOperationPayload],
    ) -> MutationResponseDocument:
        """Creates a new artist."""
        ...


    async def artists_id_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")],
    ) -> ArtistsSingleResourceDataDocument:
        """Retrieves single artist by id."""
        ...


    async def artists_id_patch(
        self,
        id: Annotated[str, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        artists_update_operation_payload: Optional[ArtistsUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """When both profile colours are available, they must have at least 3:1 contrast."""
        ...


    async def artists_id_relationships_albums_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")],
    ) -> ArtistsAlbumsMultiRelationshipDataDocument:
        """Retrieves albums relationship."""
        ...


    async def artists_id_relationships_banner_art_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: bannerArt")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ArtistsBannerArtMultiRelationshipDataDocument:
        """Reads the selected header banner artwork."""
        ...


    async def artists_id_relationships_banner_art_patch(
        self,
        id: Annotated[str, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        artists_banner_art_relationship_update_operation_payload: Optional[ArtistsBannerArtRelationshipUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Selects one owned, attachable IMAGE artwork by ID, replacing the selection. Empty data clears the selection; null data and more than one entry are rejected. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement."""
        ...


    async def artists_id_relationships_biography_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: biography")],
    ) -> ArtistsBiographySingleRelationshipDataDocument:
        """Retrieves biography relationship."""
        ...


    async def artists_id_relationships_claim_status_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: claimStatus")],
    ) -> ArtistsClaimStatusSingleRelationshipDataDocument:
        """Retrieves claimStatus relationship."""
        ...


    async def artists_id_relationships_followers_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: followers")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: followers.albums")],
        viewer_context: Optional[str],
    ) -> ArtistsFollowersMultiRelationshipDataDocument:
        """Retrieves followers relationship."""
        ...


    async def artists_id_relationships_following_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: following")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: following.albums")],
        viewer_context: Optional[str],
    ) -> ArtistsFollowingMultiRelationshipDataDocument:
        """Retrieves following relationship."""
        ...


    async def artists_id_relationships_following_post(
        self,
        id: Annotated[str, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        artists_following_relationship_add_operation_payload: Optional[ArtistsFollowingRelationshipAddOperationPayload],
    ) -> MutationResponseDocument:
        """Adds item(s) to following relationship."""
        ...


    async def artists_id_relationships_following_delete(
        self,
        id: Annotated[str, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        artists_following_relationship_remove_operation_payload: Optional[ArtistsFollowingRelationshipRemoveOperationPayload],
    ) -> MutationResponseDocument:
        """Deletes item(s) from following relationship."""
        ...


    async def artists_id_relationships_logo_art_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: logoArt")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ArtistsLogoArtMultiRelationshipDataDocument:
        """Reads the selected logo artwork."""
        ...


    async def artists_id_relationships_logo_art_patch(
        self,
        id: Annotated[str, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        artists_logo_art_relationship_update_operation_payload: Optional[ArtistsLogoArtRelationshipUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Selects one owned, attachable IMAGE artwork by ID, replacing the selection. Empty data clears the selection; null data and more than one entry are rejected. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement."""
        ...


    async def artists_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ArtistsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def artists_id_relationships_profile_art_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: profileArt")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ArtistsProfileArtMultiRelationshipDataDocument:
        """Reads the artist&#39;s avatar artwork."""
        ...


    async def artists_id_relationships_profile_art_patch(
        self,
        id: Annotated[str, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        artists_profile_art_relationship_update_operation_payload: Optional[ArtistsProfileArtRelationshipUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Replaces the artist&#39;s uploaded avatar selection with one owned, attachable artwork. Empty data clears the uploaded selection; legacy pictures or album fallback artwork may still appear in profileArt. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement."""
        ...


    async def artists_id_relationships_radio_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: radio")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: radio.items")],
    ) -> ArtistsRadioMultiRelationshipDataDocument:
        """Retrieves radio relationship."""
        ...


    async def artists_id_relationships_roles_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: roles")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ArtistsRolesMultiRelationshipDataDocument:
        """Retrieves roles relationship."""
        ...


    async def artists_id_relationships_similar_artists_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: similarArtists")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarArtists.albums")],
    ) -> ArtistsSimilarArtistsMultiRelationshipDataDocument:
        """Retrieves similarArtists relationship."""
        ...


    async def artists_id_relationships_track_providers_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: trackProviders")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ArtistsTrackProvidersMultiRelationshipDataDocument:
        """Retrieves trackProviders relationship."""
        ...


    async def artists_id_relationships_tracks_get(
        self,
        collapse_by: Annotated[str, Field(description="Collapse by options for getting artist tracks. Available options: FINGERPRINT, ID. FINGERPRINT option might collapse similar tracks based entry fingerprints while collapsing by ID always returns all available items.")],
        id: Annotated[str, Field(description="Artist id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: tracks")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks")],
    ) -> ArtistsTracksMultiRelationshipDataDocument:
        """Retrieves tracks relationship."""
        ...


    async def artists_id_relationships_videos_get(
        self,
        id: Annotated[str, Field(description="Artist id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: videos")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos")],
    ) -> ArtistsVideosMultiRelationshipDataDocument:
        """Retrieves videos relationship."""
        ...
