# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.shares_api_base import BaseSharesApi
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
from tidal.models.shares_create_operation_payload import SharesCreateOperationPayload
from tidal.models.shares_create_single_resource_data_document import SharesCreateSingleResourceDataDocument
from tidal.models.shares_multi_resource_data_document import SharesMultiResourceDataDocument
from tidal.models.shares_owners_multi_relationship_data_document import SharesOwnersMultiRelationshipDataDocument
from tidal.models.shares_shared_resources_multi_relationship_data_document import SharesSharedResourcesMultiRelationshipDataDocument
from tidal.models.shares_single_resource_data_document import SharesSingleResourceDataDocument
from tidal.models.shares_update_operation_payload import SharesUpdateOperationPayload
from tidal.models.shares_update_single_resource_data_document import SharesUpdateSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/shares",
    responses={
        200: {"model": SharesMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["shares"],
    summary="Get multiple shares.",
    response_model_by_alias=True,
)
async def shares_get(
    filter_code: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="A share code (e.g. `xyz`)")] = Query(None, description="A share code (e.g. &#x60;xyz&#x60;)", alias="filter[code]"),
    filter_self_applies_to: Annotated[Optional[str], Field(description="Album or track owned by the caller. Selects undeleted, unexpired links on the resource or its album. Exhausted links are included. Each link keeps its own sharedResources. Cannot be combined with other filters. Missing or non-owned resources and subjects without a live access node return no records. Ordered by expiry then share ID; at most 20 links per page.")] = Query(None, description="Album or track owned by the caller. Selects undeleted, unexpired links on the resource or its album. Exhausted links are included. Each link keeps its own sharedResources. Cannot be combined with other filters. Missing or non-owned resources and subjects without a live access node return no records. Ordered by expiry then share ID; at most 20 links per page.", alias="filter[self][appliesTo]", regex=r"^(?:tracks|albums):[^,]+$"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, sharedResources")] = Query(None, description="Include related resources. Available relationships: owners, sharedResources", alias="include", examples=["sharedResources"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: sharedResources")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: sharedResources", alias="replaceMedia", examples=["sharedResources"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> SharesMultiResourceDataDocument:
    """Retrieves multiple shares by available filters, or without if applicable."""
    if not BaseSharesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSharesApi.subclasses[0]().shares_get(filter_code, filter_self_applies_to, include, include_linkage, page_cursor, replace_media)


@router.post(
    "/shares",
    responses={
        201: {"model": SharesCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["shares"],
    summary="Create single share.",
    response_model_by_alias=True,
)
async def shares_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    shares_create_operation_payload: Optional[SharesCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> SharesCreateSingleResourceDataDocument:
    """Creates a new share. Deprecated for playlists: use &#x60;resourceGrantInvitations&#x60; instead."""
    if not BaseSharesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSharesApi.subclasses[0]().shares_post(idempotency_key, shares_create_operation_payload)


@router.get(
    "/shares/{id}",
    responses={
        200: {"model": SharesSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["shares"],
    summary="Get single share.",
    response_model_by_alias=True,
)
async def shares_id_get(
    id: Annotated[str, Field(description="Share id")] = Path(..., description="Share id", examples=["a468bee88def"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, sharedResources")] = Query(None, description="Include related resources. Available relationships: owners, sharedResources", alias="include", examples=["sharedResources"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: sharedResources")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: sharedResources", alias="replaceMedia", examples=["sharedResources"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> SharesSingleResourceDataDocument:
    """Retrieves single share by id."""
    if not BaseSharesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSharesApi.subclasses[0]().shares_id_get(id, include, include_linkage, replace_media)


@router.delete(
    "/shares/{id}",
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
    tags=["shares"],
    summary="Delete single share.",
    response_model_by_alias=True,
)
async def shares_id_delete(
    id: Annotated[str, Field(description="Share id")] = Path(..., description="Share id", examples=["a468bee88def"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    revoke_grants: Annotated[Optional[bool], Field(description="Also revoke the access granted to everyone who saved this share; access from other sources stays. Defaults to false. Not supported for playlist shares or for owners not yet on the access store; there true is rejected with 400.")] = Query(None, description="Also revoke the access granted to everyone who saved this share; access from other sources stays. Defaults to false. Not supported for playlist shares or for owners not yet on the access store; there true is rejected with 400.", alias="revokeGrants"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Delete share. Effectively revokes bearer access and acceptance."""
    if not BaseSharesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSharesApi.subclasses[0]().shares_id_delete(id, idempotency_key, revoke_grants)


@router.patch(
    "/shares/{id}",
    responses={
        200: {"model": SharesUpdateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["shares"],
    summary="Update single share.",
    response_model_by_alias=True,
)
async def shares_id_patch(
    id: Annotated[str, Field(description="Share id")] = Path(..., description="Share id", examples=["a468bee88def"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    shares_update_operation_payload: Optional[SharesUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> SharesUpdateSingleResourceDataDocument:
    """Set, change or remove the share&#39;s password. Setting one also removes BEARER access; removing one leaves the access modes unchanged. Existing savers keep their access."""
    if not BaseSharesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSharesApi.subclasses[0]().shares_id_patch(id, idempotency_key, shares_update_operation_payload)


@router.get(
    "/shares/{id}/relationships/owners",
    responses={
        200: {"model": SharesOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["shares"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def shares_id_relationships_owners_get(
    id: Annotated[str, Field(description="Share id")] = Path(..., description="Share id", examples=["a468bee88def"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> SharesOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseSharesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSharesApi.subclasses[0]().shares_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/shares/{id}/relationships/sharedResources",
    responses={
        200: {"model": SharesSharedResourcesMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["shares"],
    summary="Get sharedResources relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def shares_id_relationships_shared_resources_get(
    id: Annotated[str, Field(description="Share id")] = Path(..., description="Share id", examples=["a468bee88def"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: sharedResources")] = Query(None, description="Include related resources. Available relationships: sharedResources", alias="include", examples=["sharedResources"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: sharedResources")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: sharedResources", alias="replaceMedia", examples=["sharedResources"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> SharesSharedResourcesMultiRelationshipDataDocument:
    """Retrieves sharedResources relationship."""
    if not BaseSharesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSharesApi.subclasses[0]().shares_id_relationships_shared_resources_get(id, include, page_cursor, replace_media)
