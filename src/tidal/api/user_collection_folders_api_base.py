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
from tidal.models.user_collection_folders_create_operation_payload import UserCollectionFoldersCreateOperationPayload
from tidal.models.user_collection_folders_create_single_resource_data_document import UserCollectionFoldersCreateSingleResourceDataDocument
from tidal.models.user_collection_folders_delete_resource400_response_body import UserCollectionFoldersDeleteResource400ResponseBody
from tidal.models.user_collection_folders_items_multi_relationship_data_document import UserCollectionFoldersItemsMultiRelationshipDataDocument
from tidal.models.user_collection_folders_items_relationship_add_operation_payload import UserCollectionFoldersItemsRelationshipAddOperationPayload
from tidal.models.user_collection_folders_items_relationship_remove_operation_payload import UserCollectionFoldersItemsRelationshipRemoveOperationPayload
from tidal.models.user_collection_folders_multi_resource_data_document import UserCollectionFoldersMultiResourceDataDocument
from tidal.models.user_collection_folders_owners_multi_relationship_data_document import UserCollectionFoldersOwnersMultiRelationshipDataDocument
from tidal.models.user_collection_folders_single_resource_data_document import UserCollectionFoldersSingleResourceDataDocument
from tidal.models.user_collection_folders_update_operation_payload import UserCollectionFoldersUpdateOperationPayload
from tidal.models.user_collection_folders_user_collection_single_relationship_data_document import UserCollectionFoldersUserCollectionSingleRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseUserCollectionFoldersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUserCollectionFoldersApi.subclasses = BaseUserCollectionFoldersApi.subclasses + (cls,)
    async def user_collection_folders_get(
        self,
        filter_id: Annotated[List[str], Field(min_length=1, max_length=20, description="Folder Id (e.g. `CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items, owners, userCollection")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items")],
    ) -> UserCollectionFoldersMultiResourceDataDocument:
        """Retrieves multiple userCollectionFolders by available filters, or without if applicable."""
        ...


    async def user_collection_folders_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_collection_folders_create_operation_payload: Optional[UserCollectionFoldersCreateOperationPayload],
    ) -> UserCollectionFoldersCreateSingleResourceDataDocument:
        """Creates a new userCollectionFolder."""
        ...


    async def user_collection_folders_id_get(
        self,
        id: Annotated[str, Field(description="Folder Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items, owners, userCollection")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items")],
    ) -> UserCollectionFoldersSingleResourceDataDocument:
        """Retrieves single userCollectionFolder by id."""
        ...


    async def user_collection_folders_id_delete(
        self,
        id: Annotated[str, Field(description="Folder Id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
    ) -> MutationResponseDocument:
        """Deletes existing userCollectionFolder."""
        ...


    async def user_collection_folders_id_patch(
        self,
        id: Annotated[str, Field(description="Folder Id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_collection_folders_update_operation_payload: Optional[UserCollectionFoldersUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Updates existing userCollectionFolder."""
        ...


    async def user_collection_folders_id_relationships_items_get(
        self,
        id: Annotated[str, Field(description="Folder Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items")],
        sort: Annotated[Optional[List[str]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")],
    ) -> UserCollectionFoldersItemsMultiRelationshipDataDocument:
        """Retrieves items relationship."""
        ...


    async def user_collection_folders_id_relationships_items_post(
        self,
        id: Annotated[str, Field(description="Folder Id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_collection_folders_items_relationship_add_operation_payload: Optional[UserCollectionFoldersItemsRelationshipAddOperationPayload],
    ) -> MutationResponseDocument:
        """Adds item(s) to items relationship."""
        ...


    async def user_collection_folders_id_relationships_items_delete(
        self,
        id: Annotated[str, Field(description="Folder Id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_collection_folders_items_relationship_remove_operation_payload: Optional[UserCollectionFoldersItemsRelationshipRemoveOperationPayload],
    ) -> MutationResponseDocument:
        """Deletes item(s) from items relationship."""
        ...


    async def user_collection_folders_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Folder Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> UserCollectionFoldersOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def user_collection_folders_id_relationships_user_collection_get(
        self,
        id: Annotated[str, Field(description="Folder Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: userCollection")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: userCollection.items.items")],
    ) -> UserCollectionFoldersUserCollectionSingleRelationshipDataDocument:
        """Retrieves userCollection relationship."""
        ...
