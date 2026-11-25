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
from tidal.models.folder_items_breadcrumb_multi_relationship_data_document import FolderItemsBreadcrumbMultiRelationshipDataDocument
from tidal.models.folder_items_create_operation_payload import FolderItemsCreateOperationPayload
from tidal.models.folder_items_create_resource400_response_body import FolderItemsCreateResource400ResponseBody
from tidal.models.folder_items_create_single_resource_data_document import FolderItemsCreateSingleResourceDataDocument
from tidal.models.folder_items_multi_resource_data_document import FolderItemsMultiResourceDataDocument
from tidal.models.folder_items_owners_multi_relationship_data_document import FolderItemsOwnersMultiRelationshipDataDocument
from tidal.models.folder_items_parent_relationship_update_operation_payload import FolderItemsParentRelationshipUpdateOperationPayload
from tidal.models.folder_items_parent_single_relationship_data_document import FolderItemsParentSingleRelationshipDataDocument
from tidal.models.folder_items_parent_update_single_data_relationship400_response_body import FolderItemsParentUpdateSingleDataRelationship400ResponseBody
from tidal.models.folder_items_parent_update_single_relationship_data_document import FolderItemsParentUpdateSingleRelationshipDataDocument
from tidal.models.folder_items_sharing_summary_single_relationship_data_document import FolderItemsSharingSummarySingleRelationshipDataDocument
from tidal.models.folder_items_single_resource_data_document import FolderItemsSingleResourceDataDocument
from tidal.models.folder_items_subject_single_relationship_data_document import FolderItemsSubjectSingleRelationshipDataDocument
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseFolderItemsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseFolderItemsApi.subclasses = BaseFolderItemsApi.subclasses + (cls,)
    async def folder_items_get(
        self,
        filter_parent_id: Annotated[Optional[str], Field(description="Folder id (e.g. `e3226624-355b-48f8-aa93-db42532caa66`). Also accepts `me`.")],
        filter_parent_is_root: Annotated[Optional[str], Field(description="Filter by parent.isRoot")],
        filter_parent_owners_id: Annotated[Optional[Annotated[str, Field(min_length=1)]], Field(description="Owner of the folder an item is in; must be the authenticated user. With parent.isRoot=true it selects your root, and with query or subject.albums:published your whole tree. Also accepts `me`.")],
        filter_self_matches_query: Annotated[Optional[Annotated[str, Field(min_length=1, max_length=200)]], Field(description="Searches every folder in your tree, selected with parent.owners.id=me, and lists the matching items in one flat list. An item matches when each word given starts a word in its folder's name, its album's title or the title of one of the album's tracks, ignoring case. An item shared with you matches by its subject, and only while you can open it. (e.g. `demo`)")],
        filter_subject_albums_published: Annotated[Optional[str], Field(description="Searches every folder in your tree, selected with parent.owners.id=me, for albums that are (true) or are not (false) published, and lists them in one flat list. Other items never match. Combines with filter[self][matchesQuery]. (e.g. `true`)")],
        filter_subject_owners_id: Annotated[Optional[Annotated[str, Field(min_length=1)]], Field(description="In your folders, `=me` selects owned placements and `[ne]=me` selects shared placements. In someone else's folder, `=me` returns no items and `[ne]=me` returns all items. Accepts only `me` or your own user ID.")],
        filter_subject_owners_id_ne: Annotated[Optional[Annotated[str, Field(min_length=1)]], Field(description="In your folders, `=me` selects owned placements and `[ne]=me` selects shared placements. In someone else's folder, `=me` returns no items and `[ne]=me` returns all items. Accepts only `me` or your own user ID.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: breadcrumb, owners, parent, sharingSummary, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: breadcrumb.children.subject")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> FolderItemsMultiResourceDataDocument:
        """Lists items in a folder, newest placement first. Select a folder with parent.id, or select your root with parent.isRoot&#x3D;true and parent.owners.id&#x3D;me. These forms cannot be combined; no other parent-filter combinations are supported. To search every folder in your tree instead, use query, subject.albums:published or both with parent.owners.id&#x3D;me alone."""
        ...


    async def folder_items_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        folder_items_create_operation_payload: Optional[FolderItemsCreateOperationPayload],
    ) -> FolderItemsCreateSingleResourceDataDocument:
        """Creates a new folderItem."""
        ...


    async def folder_items_id_get(
        self,
        id: Annotated[str, Field(description="Folder item id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: breadcrumb, owners, parent, sharingSummary, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: breadcrumb.children.subject")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> FolderItemsSingleResourceDataDocument:
        """Retrieves single folderItem by id."""
        ...


    async def folder_items_id_delete(
        self,
        id: Annotated[str, Field(description="Folder item id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> MutationResponseDocument:
        """Deletes existing folderItem."""
        ...


    async def folder_items_id_relationships_breadcrumb_get(
        self,
        id: Annotated[str, Field(description="Folder item id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: breadcrumb")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: breadcrumb.children.subject")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> FolderItemsBreadcrumbMultiRelationshipDataDocument:
        """The folders from the root to this item&#39;s parent; only for the tree&#39;s owner, empty otherwise."""
        ...


    async def folder_items_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Folder item id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> FolderItemsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def folder_items_id_relationships_parent_get(
        self,
        id: Annotated[str, Field(description="Folder item id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: parent")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: parent.children.subject")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> FolderItemsParentSingleRelationshipDataDocument:
        """Retrieves parent relationship."""
        ...


    async def folder_items_id_relationships_parent_patch(
        self,
        id: Annotated[str, Field(description="Folder item id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
        folder_items_parent_relationship_update_operation_payload: Optional[FolderItemsParentRelationshipUpdateOperationPayload],
    ) -> FolderItemsParentUpdateSingleRelationshipDataDocument:
        """Moves the item to the supplied parent folder, replacing its previous parent. To move to the top level, supply the root folder explicitly; null data is rejected. The caller needs at least COLLABORATOR on the new parent. Within the item&#39;s tree they need OWNER on the item or COLLABORATOR on the folder holding it; only its creator moves it into another user&#39;s tree. Returns the new parent linkage."""
        ...


    async def folder_items_id_relationships_sharing_summary_get(
        self,
        id: Annotated[str, Field(description="Folder item id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: sharingSummary")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: sharingSummary.subject")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> FolderItemsSharingSummarySingleRelationshipDataDocument:
        """Retrieves sharingSummary relationship."""
        ...


    async def folder_items_id_relationships_subject_get(
        self,
        id: Annotated[str, Field(description="Folder item id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> FolderItemsSubjectSingleRelationshipDataDocument:
        """Retrieves subject relationship."""
        ...
