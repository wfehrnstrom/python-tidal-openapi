# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.provider_owners_api_base import BaseProviderOwnersApi
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
from tidal.models.provider_owners_multi_resource_data_document import ProviderOwnersMultiResourceDataDocument
from tidal.models.provider_owners_owners_multi_relationship_data_document import ProviderOwnersOwnersMultiRelationshipDataDocument
from tidal.models.provider_owners_provider_single_relationship_data_document import ProviderOwnersProviderSingleRelationshipDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/providerOwners",
    responses={
        200: {"model": ProviderOwnersMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["providerOwners"],
    summary="Get multiple providerOwners.",
    response_model_by_alias=True,
)
async def provider_owners_get(
    filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="User id. Also accepts `me`.")] = Query(..., description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, provider")] = Query(None, description="Include related resources. Available relationships: owners, provider", alias="include", examples=["provider"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ProviderOwnersMultiResourceDataDocument:
    """Retrieves multiple providerOwners by available filters, or without if applicable."""
    if not BaseProviderOwnersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProviderOwnersApi.subclasses[0]().provider_owners_get(filter_owners_id, include, include_linkage)


@router.get(
    "/providerOwners/{id}/relationships/owners",
    responses={
        200: {"model": ProviderOwnersOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["providerOwners"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def provider_owners_id_relationships_owners_get(
    id: Annotated[str, Field(description="Provider owner id")] = Path(..., description="Provider owner id"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ProviderOwnersOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseProviderOwnersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProviderOwnersApi.subclasses[0]().provider_owners_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/providerOwners/{id}/relationships/provider",
    responses={
        200: {"model": ProviderOwnersProviderSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["providerOwners"],
    summary="Get provider relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def provider_owners_id_relationships_provider_get(
    id: Annotated[str, Field(description="Provider owner id")] = Path(..., description="Provider owner id"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: provider")] = Query(None, description="Include related resources. Available relationships: provider", alias="include", examples=["provider"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ProviderOwnersProviderSingleRelationshipDataDocument:
    """Retrieves provider relationship."""
    if not BaseProviderOwnersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProviderOwnersApi.subclasses[0]().provider_owners_id_relationships_provider_get(id, include)
