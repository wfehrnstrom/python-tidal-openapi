# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.temporary_user_tokens_api_base import BaseTemporaryUserTokensApi
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
from tidal.models.temporary_user_tokens_create_operation_payload import TemporaryUserTokensCreateOperationPayload
from tidal.models.temporary_user_tokens_create_single_resource_data_document import TemporaryUserTokensCreateSingleResourceDataDocument
from tidal.models.temporary_user_tokens_owners_multi_relationship_data_document import TemporaryUserTokensOwnersMultiRelationshipDataDocument
from tidal.models.temporary_user_tokens_single_resource_data_document import TemporaryUserTokensSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/temporaryUserTokens",
    responses={
        201: {"model": TemporaryUserTokensCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["temporaryUserTokens"],
    summary="Create single temporaryUserToken.",
    response_model_by_alias=True,
)
async def temporary_user_tokens_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    temporary_user_tokens_create_operation_payload: Optional[TemporaryUserTokensCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> TemporaryUserTokensCreateSingleResourceDataDocument:
    """Creates a new temporaryUserToken."""
    if not BaseTemporaryUserTokensApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTemporaryUserTokensApi.subclasses[0]().temporary_user_tokens_post(idempotency_key, temporary_user_tokens_create_operation_payload)


@router.get(
    "/temporaryUserTokens/{id}",
    responses={
        200: {"model": TemporaryUserTokensSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["temporaryUserTokens"],
    summary="Get single temporaryUserToken.",
    response_model_by_alias=True,
)
async def temporary_user_tokens_id_get(
    id: Annotated[str, Field(description="Temporary user token id")] = Path(..., description="Temporary user token id", examples=["abc123"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include"),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> TemporaryUserTokensSingleResourceDataDocument:
    """Retrieves single temporaryUserToken by id."""
    if not BaseTemporaryUserTokensApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTemporaryUserTokensApi.subclasses[0]().temporary_user_tokens_id_get(id, include, include_linkage)


@router.get(
    "/temporaryUserTokens/{id}/relationships/owners",
    responses={
        200: {"model": TemporaryUserTokensOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["temporaryUserTokens"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def temporary_user_tokens_id_relationships_owners_get(
    id: Annotated[str, Field(description="Temporary user token id")] = Path(..., description="Temporary user token id", examples=["abc123"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> TemporaryUserTokensOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseTemporaryUserTokensApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTemporaryUserTokensApi.subclasses[0]().temporary_user_tokens_id_relationships_owners_get(id, include, page_cursor)
