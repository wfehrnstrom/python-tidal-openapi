# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.user_data_exports_api_base import BaseUserDataExportsApi
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
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.user_data_exports_create_operation_payload import UserDataExportsCreateOperationPayload
from tidal.models.user_data_exports_create_resource400_response_body import UserDataExportsCreateResource400ResponseBody
from tidal.models.user_data_exports_create_resource409_response_body import UserDataExportsCreateResource409ResponseBody
from tidal.models.user_data_exports_create_single_resource_data_document import UserDataExportsCreateSingleResourceDataDocument
from tidal.models.user_data_exports_multi_resource_data_document import UserDataExportsMultiResourceDataDocument
from tidal.models.user_data_exports_owners_multi_relationship_data_document import UserDataExportsOwnersMultiRelationshipDataDocument
from tidal.models.user_data_exports_single_resource_data_document import UserDataExportsSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/userDataExports",
    responses={
        200: {"model": UserDataExportsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userDataExports"],
    summary="Get multiple userDataExports.",
    response_model_by_alias=True,
)
async def user_data_exports_get(
    filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="The authenticated user; exports of other users are never listed. Also accepts `me`.")] = Query(..., description="The authenticated user; exports of other users are never listed. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include"),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> UserDataExportsMultiResourceDataDocument:
    """Lists the authenticated user&#39;s exports, newest first."""
    if not BaseUserDataExportsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserDataExportsApi.subclasses[0]().user_data_exports_get(filter_owners_id, include, include_linkage, page_cursor)


@router.post(
    "/userDataExports",
    responses={
        201: {"model": UserDataExportsCreateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": UserDataExportsCreateResource400ResponseBody, "description": "One or more of the selected data types are not available"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": UserDataExportsCreateResource409ResponseBody, "description": "Another data export request is being handled; try again shortly; A data export was prepared recently; wait before requesting another; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userDataExports"],
    summary="Create single userDataExport.",
    response_model_by_alias=True,
)
async def user_data_exports_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_data_exports_create_operation_payload: Optional[UserDataExportsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> UserDataExportsCreateSingleResourceDataDocument:
    """Requests an export of the selected data types of the authenticated user&#39;s data, or returns the export already in progress as it was requested."""
    if not BaseUserDataExportsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserDataExportsApi.subclasses[0]().user_data_exports_post(idempotency_key, user_data_exports_create_operation_payload)


@router.get(
    "/userDataExports/{id}",
    responses={
        200: {"model": UserDataExportsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userDataExports"],
    summary="Get single userDataExport.",
    response_model_by_alias=True,
)
async def user_data_exports_id_get(
    id: Annotated[str, Field(max_length=64)] = Path(..., description="", max_length=64),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include"),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> UserDataExportsSingleResourceDataDocument:
    """Retrieves single userDataExport by id."""
    if not BaseUserDataExportsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserDataExportsApi.subclasses[0]().user_data_exports_id_get(id, include, include_linkage)


@router.get(
    "/userDataExports/{id}/relationships/owners",
    responses={
        200: {"model": UserDataExportsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userDataExports"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_data_exports_id_relationships_owners_get(
    id: Annotated[str, Field(max_length=64)] = Path(..., description="", max_length=64),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> UserDataExportsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseUserDataExportsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserDataExportsApi.subclasses[0]().user_data_exports_id_relationships_owners_get(id, include, page_cursor)
