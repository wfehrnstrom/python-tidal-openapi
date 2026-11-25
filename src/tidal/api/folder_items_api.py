# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.folder_items_api_base import BaseFolderItemsApi
import tidal.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

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
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/folderItems",
    responses={
        200: {"model": FolderItemsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folderItems"],
    summary="Get multiple folderItems.",
    response_model_by_alias=True,
)
async def folder_items_get(
    filter_parent_id: Annotated[Optional[str], Field(description="Folder id (e.g. `e3226624-355b-48f8-aa93-db42532caa66`). Also accepts `me`.")] = Query(None, description="Folder id (e.g. &#x60;e3226624-355b-48f8-aa93-db42532caa66&#x60;). Also accepts &#x60;me&#x60;.", alias="filter[parent.id]"),
    filter_parent_is_root: Annotated[Optional[str], Field(description="Filter by parent.isRoot")] = Query(None, description="Filter by parent.isRoot", alias="filter[parent.isRoot]"),
    filter_parent_owners_id: Annotated[Optional[Annotated[str, Field(min_length=1)]], Field(description="Owner of the folder an item is in; must be the authenticated user. With parent.isRoot=true it selects your root, and with query or subject.albums:published your whole tree. Also accepts `me`.")] = Query(None, description="Owner of the folder an item is in; must be the authenticated user. With parent.isRoot&#x3D;true it selects your root, and with query or subject.albums:published your whole tree. Also accepts &#x60;me&#x60;.", alias="filter[parent.owners.id]", min_length=1),
    filter_self_matches_query: Annotated[Optional[Annotated[str, Field(min_length=1, max_length=200)]], Field(description="Searches every folder in your tree, selected with parent.owners.id=me, and lists the matching items in one flat list. An item matches when each word given starts a word in its folder's name, its album's title or the title of one of the album's tracks, ignoring case. An item shared with you matches by its subject, and only while you can open it. (e.g. `demo`)")] = Query(None, description="Searches every folder in your tree, selected with parent.owners.id&#x3D;me, and lists the matching items in one flat list. An item matches when each word given starts a word in its folder&#39;s name, its album&#39;s title or the title of one of the album&#39;s tracks, ignoring case. An item shared with you matches by its subject, and only while you can open it. (e.g. &#x60;demo&#x60;)", alias="filter[self][matchesQuery]", min_length=1, max_length=200),
    filter_subject_albums_published: Annotated[Optional[str], Field(description="Searches every folder in your tree, selected with parent.owners.id=me, for albums that are (true) or are not (false) published, and lists them in one flat list. Other items never match. Combines with filter[self][matchesQuery]. (e.g. `true`)")] = Query(None, description="Searches every folder in your tree, selected with parent.owners.id&#x3D;me, for albums that are (true) or are not (false) published, and lists them in one flat list. Other items never match. Combines with filter[self][matchesQuery]. (e.g. &#x60;true&#x60;)", alias="filter[subject.albums:published]"),
    filter_subject_owners_id: Annotated[Optional[Annotated[str, Field(min_length=1)]], Field(description="In your folders, `=me` selects owned placements and `[ne]=me` selects shared placements. In someone else's folder, `=me` returns no items and `[ne]=me` returns all items. Accepts only `me` or your own user ID.")] = Query(None, description="In your folders, &#x60;&#x3D;me&#x60; selects owned placements and &#x60;[ne]&#x3D;me&#x60; selects shared placements. In someone else&#39;s folder, &#x60;&#x3D;me&#x60; returns no items and &#x60;[ne]&#x3D;me&#x60; returns all items. Accepts only &#x60;me&#x60; or your own user ID.", alias="filter[subject.owners.id]", min_length=1),
    filter_subject_owners_id_ne: Annotated[Optional[Annotated[str, Field(min_length=1)]], Field(description="In your folders, `=me` selects owned placements and `[ne]=me` selects shared placements. In someone else's folder, `=me` returns no items and `[ne]=me` returns all items. Accepts only `me` or your own user ID.")] = Query(None, description="In your folders, &#x60;&#x3D;me&#x60; selects owned placements and &#x60;[ne]&#x3D;me&#x60; selects shared placements. In someone else&#39;s folder, &#x60;&#x3D;me&#x60; returns no items and &#x60;[ne]&#x3D;me&#x60; returns all items. Accepts only &#x60;me&#x60; or your own user ID.", alias="filter[subject.owners.id][ne]", min_length=1),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: breadcrumb, owners, parent, sharingSummary, subject")] = Query(None, description="Include related resources. Available relationships: breadcrumb, owners, parent, sharingSummary, subject", alias="include", examples=["breadcrumb.children.subject"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: breadcrumb.children.subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: breadcrumb.children.subject", alias="replaceMedia", examples=["breadcrumb.children.subject"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
) -> FolderItemsMultiResourceDataDocument:
    """Lists items in a folder, newest placement first. Select a folder with parent.id, or select your root with parent.isRoot&#x3D;true and parent.owners.id&#x3D;me. These forms cannot be combined; no other parent-filter combinations are supported. To search every folder in your tree instead, use query, subject.albums:published or both with parent.owners.id&#x3D;me alone."""
    if not BaseFolderItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFolderItemsApi.subclasses[0]().folder_items_get(filter_parent_id, filter_parent_is_root, filter_parent_owners_id, filter_self_matches_query, filter_subject_albums_published, filter_subject_owners_id, filter_subject_owners_id_ne, include, include_linkage, page_cursor, replace_media, share_code)


@router.post(
    "/folderItems",
    responses={
        201: {"model": FolderItemsCreateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": FolderItemsCreateResource400ResponseBody, "description": "A folder cannot be placed inside itself or one of its descendants"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": Idempotency409ResponseBody, "description": "Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folderItems"],
    summary="Create single folderItem.",
    response_model_by_alias=True,
)
async def folder_items_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    folder_items_create_operation_payload: Optional[FolderItemsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.write", "w_usr"]
    ),
) -> FolderItemsCreateSingleResourceDataDocument:
    """Creates a new folderItem."""
    if not BaseFolderItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFolderItemsApi.subclasses[0]().folder_items_post(idempotency_key, folder_items_create_operation_payload)


@router.get(
    "/folderItems/{id}",
    responses={
        200: {"model": FolderItemsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folderItems"],
    summary="Get single folderItem.",
    response_model_by_alias=True,
)
async def folder_items_id_get(
    id: Annotated[str, Field(description="Folder item id")] = Path(..., description="Folder item id", examples=["e3226624-355b-48f8-aa93-db42532caa66"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: breadcrumb, owners, parent, sharingSummary, subject")] = Query(None, description="Include related resources. Available relationships: breadcrumb, owners, parent, sharingSummary, subject", alias="include", examples=["breadcrumb.children.subject"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: breadcrumb.children.subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: breadcrumb.children.subject", alias="replaceMedia", examples=["breadcrumb.children.subject"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> FolderItemsSingleResourceDataDocument:
    """Retrieves single folderItem by id."""
    if not BaseFolderItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFolderItemsApi.subclasses[0]().folder_items_id_get(id, include, include_linkage, replace_media, share_code)


@router.delete(
    "/folderItems/{id}",
    responses={
        200: {"model": MutationResponseDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": Idempotency409ResponseBody, "description": "Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folderItems"],
    summary="Delete single folderItem.",
    response_model_by_alias=True,
)
async def folder_items_id_delete(
    id: Annotated[str, Field(description="Folder item id")] = Path(..., description="Folder item id", examples=["e3226624-355b-48f8-aa93-db42532caa66"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing folderItem."""
    if not BaseFolderItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFolderItemsApi.subclasses[0]().folder_items_id_delete(id, idempotency_key, share_code)


@router.get(
    "/folderItems/{id}/relationships/breadcrumb",
    responses={
        200: {"model": FolderItemsBreadcrumbMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folderItems"],
    summary="Get breadcrumb relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def folder_items_id_relationships_breadcrumb_get(
    id: Annotated[str, Field(description="Folder item id")] = Path(..., description="Folder item id", examples=["e3226624-355b-48f8-aa93-db42532caa66"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: breadcrumb")] = Query(None, description="Include related resources. Available relationships: breadcrumb", alias="include", examples=["breadcrumb.children.subject"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: breadcrumb.children.subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: breadcrumb.children.subject", alias="replaceMedia", examples=["breadcrumb.children.subject"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
) -> FolderItemsBreadcrumbMultiRelationshipDataDocument:
    """The folders from the root to this item&#39;s parent; only for the tree&#39;s owner, empty otherwise."""
    if not BaseFolderItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFolderItemsApi.subclasses[0]().folder_items_id_relationships_breadcrumb_get(id, include, page_cursor, replace_media, share_code)


@router.get(
    "/folderItems/{id}/relationships/owners",
    responses={
        200: {"model": FolderItemsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folderItems"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def folder_items_id_relationships_owners_get(
    id: Annotated[str, Field(description="Folder item id")] = Path(..., description="Folder item id", examples=["e3226624-355b-48f8-aa93-db42532caa66"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> FolderItemsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseFolderItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFolderItemsApi.subclasses[0]().folder_items_id_relationships_owners_get(id, include, page_cursor, share_code)


@router.get(
    "/folderItems/{id}/relationships/parent",
    responses={
        200: {"model": FolderItemsParentSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folderItems"],
    summary="Get parent relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def folder_items_id_relationships_parent_get(
    id: Annotated[str, Field(description="Folder item id")] = Path(..., description="Folder item id", examples=["e3226624-355b-48f8-aa93-db42532caa66"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: parent")] = Query(None, description="Include related resources. Available relationships: parent", alias="include", examples=["parent.children.subject"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: parent.children.subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: parent.children.subject", alias="replaceMedia", examples=["parent.children.subject"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
) -> FolderItemsParentSingleRelationshipDataDocument:
    """Retrieves parent relationship."""
    if not BaseFolderItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFolderItemsApi.subclasses[0]().folder_items_id_relationships_parent_get(id, include, replace_media, share_code)


@router.patch(
    "/folderItems/{id}/relationships/parent",
    responses={
        200: {"model": FolderItemsParentUpdateSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": FolderItemsParentUpdateSingleDataRelationship400ResponseBody, "description": "A folder cannot be placed inside itself or one of its descendants"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": Idempotency409ResponseBody, "description": "Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folderItems"],
    summary="Update parent relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def folder_items_id_relationships_parent_patch(
    id: Annotated[str, Field(description="Folder item id")] = Path(..., description="Folder item id", examples=["e3226624-355b-48f8-aa93-db42532caa66"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    folder_items_parent_relationship_update_operation_payload: Optional[FolderItemsParentRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.write", "w_usr"]
    ),
) -> FolderItemsParentUpdateSingleRelationshipDataDocument:
    """Moves the item to the supplied parent folder, replacing its previous parent. To move to the top level, supply the root folder explicitly; null data is rejected. The caller needs at least COLLABORATOR on the new parent. Within the item&#39;s tree they need OWNER on the item or COLLABORATOR on the folder holding it; only its creator moves it into another user&#39;s tree. Returns the new parent linkage."""
    if not BaseFolderItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFolderItemsApi.subclasses[0]().folder_items_id_relationships_parent_patch(id, idempotency_key, share_code, folder_items_parent_relationship_update_operation_payload)


@router.get(
    "/folderItems/{id}/relationships/sharingSummary",
    responses={
        200: {"model": FolderItemsSharingSummarySingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folderItems"],
    summary="Get sharingSummary relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def folder_items_id_relationships_sharing_summary_get(
    id: Annotated[str, Field(description="Folder item id")] = Path(..., description="Folder item id", examples=["e3226624-355b-48f8-aa93-db42532caa66"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: sharingSummary")] = Query(None, description="Include related resources. Available relationships: sharingSummary", alias="include", examples=["sharingSummary.subject"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: sharingSummary.subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: sharingSummary.subject", alias="replaceMedia", examples=["sharingSummary.subject"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
) -> FolderItemsSharingSummarySingleRelationshipDataDocument:
    """Retrieves sharingSummary relationship."""
    if not BaseFolderItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFolderItemsApi.subclasses[0]().folder_items_id_relationships_sharing_summary_get(id, include, replace_media, share_code)


@router.get(
    "/folderItems/{id}/relationships/subject",
    responses={
        200: {"model": FolderItemsSubjectSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folderItems"],
    summary="Get subject relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def folder_items_id_relationships_subject_get(
    id: Annotated[str, Field(description="Folder item id")] = Path(..., description="Folder item id", examples=["e3226624-355b-48f8-aa93-db42532caa66"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject", alias="replaceMedia", examples=["subject"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> FolderItemsSubjectSingleRelationshipDataDocument:
    """Retrieves subject relationship."""
    if not BaseFolderItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFolderItemsApi.subclasses[0]().folder_items_id_relationships_subject_get(id, include, replace_media, share_code)
