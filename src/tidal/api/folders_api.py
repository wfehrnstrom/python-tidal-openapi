# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.folders_api_base import BaseFoldersApi
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
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/folders",
    responses={
        200: {"model": FoldersMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folders"],
    summary="Get multiple folders.",
    response_model_by_alias=True,
)
async def folders_get(
    filter_id: Annotated[List[str], Field(min_length=1, max_length=20, description="Folder id (e.g. `e3226624-355b-48f8-aa93-db42532caa66`). Also accepts `me`.")] = Query(..., description="Folder id (e.g. &#x60;e3226624-355b-48f8-aa93-db42532caa66&#x60;). Also accepts &#x60;me&#x60;.", alias="filter[id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: children, owners, parent, preview")] = Query(None, description="Include related resources. Available relationships: children, owners, parent, preview", alias="include", examples=["children.subject"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: children.subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: children.subject", alias="replaceMedia", examples=["children.subject"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> FoldersMultiResourceDataDocument:
    """Retrieves multiple folders by available filters, or without if applicable."""
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folders_get(filter_id, include, include_linkage, replace_media, share_code)


@router.post(
    "/folders",
    responses={
        201: {"model": FoldersCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["folders"],
    summary="Create single folder.",
    response_model_by_alias=True,
)
async def folders_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    folders_create_operation_payload: Optional[FoldersCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.write", "w_usr"]
    ),
) -> FoldersCreateSingleResourceDataDocument:
    """Creates a new folder."""
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folders_post(idempotency_key, folders_create_operation_payload)


@router.get(
    "/folders/{id}",
    responses={
        200: {"model": FoldersSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folders"],
    summary="Get single folder.",
    response_model_by_alias=True,
)
async def folders_id_get(
    id: Annotated[str, Field(description="Folder id. Use `me` for the authenticated user's resource")] = Path(..., description="Folder id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: children, owners, parent, preview")] = Query(None, description="Include related resources. Available relationships: children, owners, parent, preview", alias="include", examples=["children.subject"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: children.subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: children.subject", alias="replaceMedia", examples=["children.subject"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> FoldersSingleResourceDataDocument:
    """Retrieves single folder by id."""
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folders_id_get(id, include, include_linkage, replace_media, share_code)


@router.delete(
    "/folders/{id}",
    responses={
        200: {"model": MutationResponseDocument, "description": "Successful response"},
        400: {"model": FoldersDeleteResource400ResponseBody, "description": "The root folder cannot be renamed or deleted"},
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
    tags=["folders"],
    summary="Delete single folder.",
    response_model_by_alias=True,
)
async def folders_id_delete(
    id: Annotated[str, Field(description="Folder id. Use `me` for the authenticated user's resource")] = Path(..., description="Folder id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing folder."""
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folders_id_delete(id, idempotency_key, share_code)


@router.patch(
    "/folders/{id}",
    responses={
        200: {"model": FoldersUpdateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": FoldersUpdateResource400ResponseBody, "description": "The root folder cannot be renamed or deleted"},
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
    tags=["folders"],
    summary="Update single folder.",
    response_model_by_alias=True,
)
async def folders_id_patch(
    id: Annotated[str, Field(description="Folder id. Use `me` for the authenticated user's resource")] = Path(..., description="Folder id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    folders_update_operation_payload: Optional[FoldersUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.write", "w_usr"]
    ),
) -> FoldersUpdateSingleResourceDataDocument:
    """Updates existing folder."""
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folders_id_patch(id, idempotency_key, share_code, folders_update_operation_payload)


@router.get(
    "/folders/{id}/relationships/children",
    responses={
        200: {"model": FoldersChildrenMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folders"],
    summary="Get children relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def folders_id_relationships_children_get(
    id: Annotated[str, Field(description="Folder id. Use `me` for the authenticated user's resource")] = Path(..., description="Folder id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: children")] = Query(None, description="Include related resources. Available relationships: children", alias="include", examples=["children.subject"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: children.subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: children.subject", alias="replaceMedia", examples=["children.subject"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
) -> FoldersChildrenMultiRelationshipDataDocument:
    """Lists folder items newest first by placement timestamp, with ID as a stable tie-breaker. Moving to another parent resets the timestamp; renaming preserves it."""
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folders_id_relationships_children_get(id, include, page_cursor, replace_media, share_code)


@router.get(
    "/folders/{id}/relationships/owners",
    responses={
        200: {"model": FoldersOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folders"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def folders_id_relationships_owners_get(
    id: Annotated[str, Field(description="Folder id. Use `me` for the authenticated user's resource")] = Path(..., description="Folder id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> FoldersOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folders_id_relationships_owners_get(id, include, page_cursor, share_code)


@router.get(
    "/folders/{id}/relationships/parent",
    responses={
        200: {"model": FoldersParentSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folders"],
    summary="Get parent relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def folders_id_relationships_parent_get(
    id: Annotated[str, Field(description="Folder id. Use `me` for the authenticated user's resource")] = Path(..., description="Folder id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: parent")] = Query(None, description="Include related resources. Available relationships: parent", alias="include", examples=["parent.children.subject"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: parent.children.subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: parent.children.subject", alias="replaceMedia", examples=["parent.children.subject"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
) -> FoldersParentSingleRelationshipDataDocument:
    """Retrieves parent relationship."""
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folders_id_relationships_parent_get(id, include, replace_media, share_code)


@router.get(
    "/folders/{id}/relationships/preview",
    responses={
        200: {"model": FoldersPreviewMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["folders"],
    summary="Get preview relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def folders_id_relationships_preview_get(
    id: Annotated[str, Field(description="Folder id. Use `me` for the authenticated user's resource")] = Path(..., description="Folder id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: preview")] = Query(None, description="Include related resources. Available relationships: preview", alias="include", examples=["preview.subject"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: preview.subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: preview.subject", alias="replaceMedia", examples=["preview.subject"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> FoldersPreviewMultiRelationshipDataDocument:
    """The first four items of this folder, as &#x60;children&#x60; lists them."""
    if not BaseFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseFoldersApi.subclasses[0]().folders_id_relationships_preview_get(id, include, page_cursor, replace_media, share_code)
