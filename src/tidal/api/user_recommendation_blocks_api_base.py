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
from tidal.models.user_recommendation_blocks_artists_add_multi_data_relationship_with_response409_response_body import UserRecommendationBlocksArtistsAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_recommendation_blocks_artists_add_multi_relationship_data_document import UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_artists_multi_relationship_data_document import UserRecommendationBlocksArtistsMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_artists_relationship_add_operation_payload import UserRecommendationBlocksArtistsRelationshipAddOperationPayload
from tidal.models.user_recommendation_blocks_artists_relationship_remove_operation_payload import UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload
from tidal.models.user_recommendation_blocks_owners_multi_relationship_data_document import UserRecommendationBlocksOwnersMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_single_resource_data_document import UserRecommendationBlocksSingleResourceDataDocument
from tidal.models.user_recommendation_blocks_tracks_add_multi_data_relationship_with_response409_response_body import UserRecommendationBlocksTracksAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_recommendation_blocks_tracks_add_multi_relationship_data_document import UserRecommendationBlocksTracksAddMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_tracks_multi_relationship_data_document import UserRecommendationBlocksTracksMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_tracks_relationship_add_operation_payload import UserRecommendationBlocksTracksRelationshipAddOperationPayload
from tidal.models.user_recommendation_blocks_tracks_relationship_remove_operation_payload import UserRecommendationBlocksTracksRelationshipRemoveOperationPayload
from tidal.models.user_recommendation_blocks_videos_add_multi_data_relationship_with_response409_response_body import UserRecommendationBlocksVideosAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_recommendation_blocks_videos_add_multi_relationship_data_document import UserRecommendationBlocksVideosAddMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_videos_multi_relationship_data_document import UserRecommendationBlocksVideosMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_videos_relationship_add_operation_payload import UserRecommendationBlocksVideosRelationshipAddOperationPayload
from tidal.models.user_recommendation_blocks_videos_relationship_remove_operation_payload import UserRecommendationBlocksVideosRelationshipRemoveOperationPayload
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseUserRecommendationBlocksApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUserRecommendationBlocksApi.subclasses = BaseUserRecommendationBlocksApi.subclasses + (cls,)
    async def user_recommendation_blocks_id_get(
        self,
        id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artists, owners, tracks, videos")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")],
    ) -> UserRecommendationBlocksSingleResourceDataDocument:
        """Retrieves single userRecommendationBlock by id."""
        ...


    async def user_recommendation_blocks_id_relationships_artists_get(
        self,
        id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artists")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")],
    ) -> UserRecommendationBlocksArtistsMultiRelationshipDataDocument:
        """Retrieves artists relationship."""
        ...


    async def user_recommendation_blocks_id_relationships_artists_post(
        self,
        id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_recommendation_blocks_artists_relationship_add_operation_payload: Optional[UserRecommendationBlocksArtistsRelationshipAddOperationPayload],
    ) -> UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument:
        """Adds item(s) to artists relationship."""
        ...


    async def user_recommendation_blocks_id_relationships_artists_delete(
        self,
        id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_recommendation_blocks_artists_relationship_remove_operation_payload: Optional[UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload],
    ) -> MutationResponseDocument:
        """Deletes item(s) from artists relationship."""
        ...


    async def user_recommendation_blocks_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> UserRecommendationBlocksOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def user_recommendation_blocks_id_relationships_tracks_get(
        self,
        id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: tracks")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks")],
    ) -> UserRecommendationBlocksTracksMultiRelationshipDataDocument:
        """Retrieves tracks relationship."""
        ...


    async def user_recommendation_blocks_id_relationships_tracks_post(
        self,
        id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_recommendation_blocks_tracks_relationship_add_operation_payload: Optional[UserRecommendationBlocksTracksRelationshipAddOperationPayload],
    ) -> UserRecommendationBlocksTracksAddMultiRelationshipDataDocument:
        """Adds item(s) to tracks relationship."""
        ...


    async def user_recommendation_blocks_id_relationships_tracks_delete(
        self,
        id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_recommendation_blocks_tracks_relationship_remove_operation_payload: Optional[UserRecommendationBlocksTracksRelationshipRemoveOperationPayload],
    ) -> MutationResponseDocument:
        """Deletes item(s) from tracks relationship."""
        ...


    async def user_recommendation_blocks_id_relationships_videos_get(
        self,
        id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: videos")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos")],
    ) -> UserRecommendationBlocksVideosMultiRelationshipDataDocument:
        """Retrieves videos relationship."""
        ...


    async def user_recommendation_blocks_id_relationships_videos_post(
        self,
        id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_recommendation_blocks_videos_relationship_add_operation_payload: Optional[UserRecommendationBlocksVideosRelationshipAddOperationPayload],
    ) -> UserRecommendationBlocksVideosAddMultiRelationshipDataDocument:
        """Adds item(s) to videos relationship."""
        ...


    async def user_recommendation_blocks_id_relationships_videos_delete(
        self,
        id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_recommendation_blocks_videos_relationship_remove_operation_payload: Optional[UserRecommendationBlocksVideosRelationshipRemoveOperationPayload],
    ) -> MutationResponseDocument:
        """Deletes item(s) from videos relationship."""
        ...
