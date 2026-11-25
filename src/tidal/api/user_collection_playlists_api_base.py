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
from tidal.models.user_collection_playlists_items_add_multi_data_relationship_with_response409_response_body import UserCollectionPlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_collection_playlists_items_add_multi_relationship_data_document import UserCollectionPlaylistsItemsAddMultiRelationshipDataDocument
from tidal.models.user_collection_playlists_items_multi_relationship_data_document import UserCollectionPlaylistsItemsMultiRelationshipDataDocument
from tidal.models.user_collection_playlists_items_read_multi_data_relationship403_response_body import UserCollectionPlaylistsItemsReadMultiDataRelationship403ResponseBody
from tidal.models.user_collection_playlists_items_relationship_add_operation_payload import UserCollectionPlaylistsItemsRelationshipAddOperationPayload
from tidal.models.user_collection_playlists_items_relationship_remove_operation_payload import UserCollectionPlaylistsItemsRelationshipRemoveOperationPayload
from tidal.models.user_collection_playlists_owners_multi_relationship_data_document import UserCollectionPlaylistsOwnersMultiRelationshipDataDocument
from tidal.models.user_collection_playlists_single_resource_data_document import UserCollectionPlaylistsSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseUserCollectionPlaylistsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUserCollectionPlaylistsApi.subclasses = BaseUserCollectionPlaylistsApi.subclasses + (cls,)
    async def user_collection_playlists_id_get(
        self,
        id: Annotated[str, Field(description="User collection playlists id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items, owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items")],
    ) -> UserCollectionPlaylistsSingleResourceDataDocument:
        """Retrieves single userCollectionPlaylist by id."""
        ...


    async def user_collection_playlists_id_relationships_items_get(
        self,
        id: Annotated[str, Field(description="User collection playlists id. Use `me` for the authenticated user's resource")],
        collection_view: Optional[str],
        filter_self_matches_query: Annotated[Optional[Annotated[str, Field(max_length=100)]], Field(description="Filter playlists by a free-text query. Returns matching playlists only (no mixes or folders), including playlists inside folders. Cannot be combined with collectionView=FOLDERS. Internal clients only (e.g. `summer`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items")],
        sort: Annotated[Optional[List[str]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")],
    ) -> UserCollectionPlaylistsItemsMultiRelationshipDataDocument:
        """Retrieves items relationship."""
        ...


    async def user_collection_playlists_id_relationships_items_post(
        self,
        id: Annotated[str, Field(description="User collection playlists id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_collection_playlists_items_relationship_add_operation_payload: Optional[UserCollectionPlaylistsItemsRelationshipAddOperationPayload],
    ) -> UserCollectionPlaylistsItemsAddMultiRelationshipDataDocument:
        """Adds item(s) to items relationship."""
        ...


    async def user_collection_playlists_id_relationships_items_delete(
        self,
        id: Annotated[str, Field(description="User collection playlists id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_collection_playlists_items_relationship_remove_operation_payload: Optional[UserCollectionPlaylistsItemsRelationshipRemoveOperationPayload],
    ) -> MutationResponseDocument:
        """Deletes item(s) from items relationship."""
        ...


    async def user_collection_playlists_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="User collection playlists id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> UserCollectionPlaylistsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...
