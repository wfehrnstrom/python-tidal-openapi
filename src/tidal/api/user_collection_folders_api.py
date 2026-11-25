# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.user_collection_folders_api_base import BaseUserCollectionFoldersApi
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
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/userCollectionFolders",
    responses={
        200: {"model": UserCollectionFoldersMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userCollectionFolders"],
    summary="Get multiple userCollectionFolders.",
    response_model_by_alias=True,
)
async def user_collection_folders_get(
    filter_id: Annotated[List[str], Field(min_length=1, max_length=20, description="Folder Id (e.g. `CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX`)")] = Query(..., description="Folder Id (e.g. &#x60;CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX&#x60;)", alias="filter[id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items, owners, userCollection")] = Query(None, description="Include related resources. Available relationships: items, owners, userCollection", alias="include", examples=["items.items"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items.items", alias="replaceMedia", examples=["items.items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
) -> UserCollectionFoldersMultiResourceDataDocument:
    """Retrieves multiple userCollectionFolders by available filters, or without if applicable."""
    if not BaseUserCollectionFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionFoldersApi.subclasses[0]().user_collection_folders_get(filter_id, include, include_linkage, replace_media)


@router.post(
    "/userCollectionFolders",
    responses={
        201: {"model": UserCollectionFoldersCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["userCollectionFolders"],
    summary="Create single userCollectionFolder.",
    response_model_by_alias=True,
)
async def user_collection_folders_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_collection_folders_create_operation_payload: Optional[UserCollectionFoldersCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.write", "w_usr"]
    ),
) -> UserCollectionFoldersCreateSingleResourceDataDocument:
    """Creates a new userCollectionFolder."""
    if not BaseUserCollectionFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionFoldersApi.subclasses[0]().user_collection_folders_post(idempotency_key, user_collection_folders_create_operation_payload)


@router.get(
    "/userCollectionFolders/{id}",
    responses={
        200: {"model": UserCollectionFoldersSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userCollectionFolders"],
    summary="Get single userCollectionFolder.",
    response_model_by_alias=True,
)
async def user_collection_folders_id_get(
    id: Annotated[str, Field(description="Folder Id")] = Path(..., description="Folder Id", examples=["CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items, owners, userCollection")] = Query(None, description="Include related resources. Available relationships: items, owners, userCollection", alias="include", examples=["items.items"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items.items", alias="replaceMedia", examples=["items.items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
) -> UserCollectionFoldersSingleResourceDataDocument:
    """Retrieves single userCollectionFolder by id."""
    if not BaseUserCollectionFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionFoldersApi.subclasses[0]().user_collection_folders_id_get(id, include, include_linkage, replace_media)


@router.delete(
    "/userCollectionFolders/{id}",
    responses={
        200: {"model": MutationResponseDocument, "description": "Successful response"},
        400: {"model": UserCollectionFoldersDeleteResource400ResponseBody, "description": "Folder must be empty and owned by you"},
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
    tags=["userCollectionFolders"],
    summary="Delete single userCollectionFolder.",
    response_model_by_alias=True,
)
async def user_collection_folders_id_delete(
    id: Annotated[str, Field(description="Folder Id")] = Path(..., description="Folder Id", examples=["CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing userCollectionFolder."""
    if not BaseUserCollectionFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionFoldersApi.subclasses[0]().user_collection_folders_id_delete(id, idempotency_key)


@router.patch(
    "/userCollectionFolders/{id}",
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
    tags=["userCollectionFolders"],
    summary="Update single userCollectionFolder.",
    response_model_by_alias=True,
)
async def user_collection_folders_id_patch(
    id: Annotated[str, Field(description="Folder Id")] = Path(..., description="Folder Id", examples=["CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_collection_folders_update_operation_payload: Optional[UserCollectionFoldersUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Updates existing userCollectionFolder."""
    if not BaseUserCollectionFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionFoldersApi.subclasses[0]().user_collection_folders_id_patch(id, idempotency_key, user_collection_folders_update_operation_payload)


@router.get(
    "/userCollectionFolders/{id}/relationships/items",
    responses={
        200: {"model": UserCollectionFoldersItemsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userCollectionFolders"],
    summary="Get items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_collection_folders_id_relationships_items_get(
    id: Annotated[str, Field(description="Folder Id")] = Path(..., description="Folder Id", examples=["CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")] = Query(None, description="Include related resources. Available relationships: items", alias="include", examples=["items.items"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items.items", alias="replaceMedia", examples=["items.items"]),
    sort: Annotated[Optional[List[str]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")] = Query(None, description="Values prefixed with \&quot;-\&quot; are sorted descending; values without it are sorted ascending.", alias="sort"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
) -> UserCollectionFoldersItemsMultiRelationshipDataDocument:
    """Retrieves items relationship."""
    if not BaseUserCollectionFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionFoldersApi.subclasses[0]().user_collection_folders_id_relationships_items_get(id, include, page_cursor, replace_media, sort)


@router.post(
    "/userCollectionFolders/{id}/relationships/items",
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
    tags=["userCollectionFolders"],
    summary="Add to items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_collection_folders_id_relationships_items_post(
    id: Annotated[str, Field(description="Folder Id")] = Path(..., description="Folder Id", examples=["CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_collection_folders_items_relationship_add_operation_payload: Optional[UserCollectionFoldersItemsRelationshipAddOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Adds item(s) to items relationship."""
    if not BaseUserCollectionFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionFoldersApi.subclasses[0]().user_collection_folders_id_relationships_items_post(id, idempotency_key, user_collection_folders_items_relationship_add_operation_payload)


@router.delete(
    "/userCollectionFolders/{id}/relationships/items",
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
    tags=["userCollectionFolders"],
    summary="Delete from items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_collection_folders_id_relationships_items_delete(
    id: Annotated[str, Field(description="Folder Id")] = Path(..., description="Folder Id", examples=["CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_collection_folders_items_relationship_remove_operation_payload: Optional[UserCollectionFoldersItemsRelationshipRemoveOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes item(s) from items relationship."""
    if not BaseUserCollectionFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionFoldersApi.subclasses[0]().user_collection_folders_id_relationships_items_delete(id, idempotency_key, user_collection_folders_items_relationship_remove_operation_payload)


@router.get(
    "/userCollectionFolders/{id}/relationships/owners",
    responses={
        200: {"model": UserCollectionFoldersOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userCollectionFolders"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_collection_folders_id_relationships_owners_get(
    id: Annotated[str, Field(description="Folder Id")] = Path(..., description="Folder Id", examples=["CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
) -> UserCollectionFoldersOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseUserCollectionFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionFoldersApi.subclasses[0]().user_collection_folders_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/userCollectionFolders/{id}/relationships/userCollection",
    responses={
        200: {"model": UserCollectionFoldersUserCollectionSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userCollectionFolders"],
    summary="Get userCollection relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def user_collection_folders_id_relationships_user_collection_get(
    id: Annotated[str, Field(description="Folder Id")] = Path(..., description="Folder Id", examples=["CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: userCollection")] = Query(None, description="Include related resources. Available relationships: userCollection", alias="include", examples=["userCollection.items.items"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: userCollection.items.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: userCollection.items.items", alias="replaceMedia", examples=["userCollection.items.items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
) -> UserCollectionFoldersUserCollectionSingleRelationshipDataDocument:
    """Retrieves userCollection relationship."""
    if not BaseUserCollectionFoldersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionFoldersApi.subclasses[0]().user_collection_folders_id_relationships_user_collection_get(id, include, replace_media)
