# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.provider_product_infos_api_base import BaseProviderProductInfosApi
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
from tidal.models.provider_product_infos_multi_resource_data_document import ProviderProductInfosMultiResourceDataDocument
from tidal.models.provider_product_infos_provider_single_relationship_data_document import ProviderProductInfosProviderSingleRelationshipDataDocument
from tidal.models.provider_product_infos_subject_single_relationship_data_document import ProviderProductInfosSubjectSingleRelationshipDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/providerProductInfos",
    responses={
        200: {"model": ProviderProductInfosMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["providerProductInfos"],
    summary="Get multiple providerProductInfos.",
    response_model_by_alias=True,
)
async def provider_product_infos_get(
    filter_provider_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="Content provider ID (e.g. `50`)")] = Query(..., description="Content provider ID (e.g. &#x60;50&#x60;)", alias="filter[provider.id]"),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    filter_barcode_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of barcode IDs (EAN-13 or UPC-A) (e.g. `00602527336510`)")] = Query(None, description="List of barcode IDs (EAN-13 or UPC-A) (e.g. &#x60;00602527336510&#x60;)", alias="filter[barcodeId]"),
    filter_grid: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of GRIDs (Global Release Identifier, ISO 7064) (e.g. `A10302B0013941653J`)")] = Query(None, description="List of GRIDs (Global Release Identifier, ISO 7064) (e.g. &#x60;A10302B0013941653J&#x60;)", alias="filter[grid]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: provider, subject")] = Query(None, description="Include related resources. Available relationships: provider, subject", alias="include", examples=["subject"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject", alias="replaceMedia", examples=["subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ProviderProductInfosMultiResourceDataDocument:
    """Retrieves multiple providerProductInfos by available filters, or without if applicable."""
    if not BaseProviderProductInfosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProviderProductInfosApi.subclasses[0]().provider_product_infos_get(filter_provider_id, country_code, filter_barcode_id, filter_grid, include, include_linkage, replace_media)


@router.get(
    "/providerProductInfos/{id}/relationships/provider",
    responses={
        200: {"model": ProviderProductInfosProviderSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["providerProductInfos"],
    summary="Get provider relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def provider_product_infos_id_relationships_provider_get(
    id: Annotated[str, Field(description="Provider product info id")] = Path(..., description="Provider product info id"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: provider")] = Query(None, description="Include related resources. Available relationships: provider", alias="include", examples=["provider"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ProviderProductInfosProviderSingleRelationshipDataDocument:
    """Retrieves provider relationship."""
    if not BaseProviderProductInfosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProviderProductInfosApi.subclasses[0]().provider_product_infos_id_relationships_provider_get(id, include)


@router.get(
    "/providerProductInfos/{id}/relationships/subject",
    responses={
        200: {"model": ProviderProductInfosSubjectSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["providerProductInfos"],
    summary="Get subject relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def provider_product_infos_id_relationships_subject_get(
    id: Annotated[str, Field(description="Provider product info id")] = Path(..., description="Provider product info id"),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject", alias="replaceMedia", examples=["subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ProviderProductInfosSubjectSingleRelationshipDataDocument:
    """Retrieves subject relationship."""
    if not BaseProviderProductInfosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProviderProductInfosApi.subclasses[0]().provider_product_infos_id_relationships_subject_get(id, country_code, include, replace_media)
