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
from tidal.models.folders_children_multi_relationship_data_document import FoldersChildrenMultiRelationshipDataDocument
from tidal.models.folders_create_operation_payload import FoldersCreateOperationPayload
from tidal.models.folders_create_single_resource_data_document import FoldersCreateSingleResourceDataDocument
from tidal.models.folders_delete_resource400_response_body import FoldersDeleteResource400ResponseBody
from tidal.models.folders_multi_resource_data_document import FoldersMultiResourceDataDocument
from tidal.models.folders_owners_multi_relationship_data_document import FoldersOwnersMultiRelationshipDataDocument
from tidal.models.folders_parent_single_relationship_data_document import FoldersParentSingleRelationshipDataDocument
from tidal.models.folders_preview_multi_relationship_data_document import FoldersPreviewMultiRelationshipDataDocument
from tidal.models.folders_single_resource_data_document import FoldersSingleResourceDataDocument
from tidal.models.folders_update_operation_payload import FoldersUpdateOperationPayload
from tidal.models.folders_update_resource400_response_body import FoldersUpdateResource400ResponseBody
from tidal.models.folders_update_single_resource_data_document import FoldersUpdateSingleResourceDataDocument
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseFoldersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseFoldersApi.subclasses = BaseFoldersApi.subclasses + (cls,)
    async def folders_get(
        self,
        filter_id: Annotated[List[str], Field(min_length=1, max_length=20, description="Folder id (e.g. `e3226624-355b-48f8-aa93-db42532caa66`). Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: children, owners, parent, preview")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: children.subject")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> FoldersMultiResourceDataDocument:
        """Retrieves multiple folders by available filters, or without if applicable."""
        ...


    async def folders_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        folders_create_operation_payload: Optional[FoldersCreateOperationPayload],
    ) -> FoldersCreateSingleResourceDataDocument:
        """Creates a new folder."""
        ...


    async def folders_id_get(
        self,
        id: Annotated[str, Field(description="Folder id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: children, owners, parent, preview")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: children.subject")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> FoldersSingleResourceDataDocument:
        """Retrieves single folder by id."""
        ...


    async def folders_id_delete(
        self,
        id: Annotated[str, Field(description="Folder id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> MutationResponseDocument:
        """Deletes existing folder."""
        ...


    async def folders_id_patch(
        self,
        id: Annotated[str, Field(description="Folder id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
        folders_update_operation_payload: Optional[FoldersUpdateOperationPayload],
    ) -> FoldersUpdateSingleResourceDataDocument:
        """Updates existing folder."""
        ...


    async def folders_id_relationships_children_get(
        self,
        id: Annotated[str, Field(description="Folder id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: children")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: children.subject")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> FoldersChildrenMultiRelationshipDataDocument:
        """Lists folder items newest first by placement timestamp, with ID as a stable tie-breaker. Moving to another parent resets the timestamp; renaming preserves it."""
        ...


    async def folders_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Folder id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> FoldersOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def folders_id_relationships_parent_get(
        self,
        id: Annotated[str, Field(description="Folder id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: parent")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: parent.children.subject")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> FoldersParentSingleRelationshipDataDocument:
        """Retrieves parent relationship."""
        ...


    async def folders_id_relationships_preview_get(
        self,
        id: Annotated[str, Field(description="Folder id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: preview")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: preview.subject")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> FoldersPreviewMultiRelationshipDataDocument:
        """The first four items of this folder, as &#x60;children&#x60; lists them."""
        ...
