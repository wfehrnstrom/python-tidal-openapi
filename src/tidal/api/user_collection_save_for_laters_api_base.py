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
from tidal.models.user_collection_save_for_laters_items_add_multi_data_relationship_with_response409_response_body import UserCollectionSaveForLatersItemsAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_collection_save_for_laters_items_add_multi_relationship_data_document import UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocument
from tidal.models.user_collection_save_for_laters_items_multi_relationship_data_document import UserCollectionSaveForLatersItemsMultiRelationshipDataDocument
from tidal.models.user_collection_save_for_laters_items_relationship_add_operation_payload import UserCollectionSaveForLatersItemsRelationshipAddOperationPayload
from tidal.models.user_collection_save_for_laters_items_relationship_remove_operation_payload import UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayload
from tidal.models.user_collection_save_for_laters_owners_multi_relationship_data_document import UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument
from tidal.models.user_collection_save_for_laters_single_resource_data_document import UserCollectionSaveForLatersSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseUserCollectionSaveForLatersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUserCollectionSaveForLatersApi.subclasses = BaseUserCollectionSaveForLatersApi.subclasses + (cls,)
    async def user_collection_save_for_laters_id_get(
        self,
        id: Annotated[str, Field(description="User collection save for later id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items, owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")],
    ) -> UserCollectionSaveForLatersSingleResourceDataDocument:
        """Retrieves single userCollectionSaveForLater by id."""
        ...


    async def user_collection_save_for_laters_id_relationships_items_get(
        self,
        id: Annotated[str, Field(description="User collection save for later id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")],
    ) -> UserCollectionSaveForLatersItemsMultiRelationshipDataDocument:
        """Retrieves items relationship."""
        ...


    async def user_collection_save_for_laters_id_relationships_items_post(
        self,
        id: Annotated[str, Field(description="User collection save for later id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_collection_save_for_laters_items_relationship_add_operation_payload: Optional[UserCollectionSaveForLatersItemsRelationshipAddOperationPayload],
    ) -> UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocument:
        """Adds item(s) to items relationship."""
        ...


    async def user_collection_save_for_laters_id_relationships_items_delete(
        self,
        id: Annotated[str, Field(description="User collection save for later id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_collection_save_for_laters_items_relationship_remove_operation_payload: Optional[UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayload],
    ) -> MutationResponseDocument:
        """Deletes item(s) from items relationship."""
        ...


    async def user_collection_save_for_laters_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="User collection save for later id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...
