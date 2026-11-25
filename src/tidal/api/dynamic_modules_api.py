# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.dynamic_modules_api_base import BaseDynamicModulesApi
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
from tidal.models.dynamic_modules_items_multi_relationship_data_document import DynamicModulesItemsMultiRelationshipDataDocument
from tidal.models.dynamic_modules_multi_resource_data_document import DynamicModulesMultiResourceDataDocument
from tidal.models.dynamic_modules_seed_item_single_relationship_data_document import DynamicModulesSeedItemSingleRelationshipDataDocument
from tidal.models.dynamic_modules_single_resource_data_document import DynamicModulesSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/dynamicModules",
    responses={
        200: {"model": DynamicModulesMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["dynamicModules"],
    summary="Get multiple dynamicModules.",
    response_model_by_alias=True,
)
async def dynamic_modules_get(
    client_version: Annotated[str, Field(description="Client version number")] = Query(..., description="Client version number", alias="clientVersion", examples=["2026.0.1"]),
    device_type: Annotated[str, Field(description="The type of device making the request")] = Query(..., description="The type of device making the request", alias="deviceType", examples=["PHONE"]),
    filter_id: Annotated[List[str], Field(min_length=1, max_length=20, description="DynamicModules Id (e.g. `nejMcAhh5N8S3EQ4LaqysVdI0cZZ`)")] = Query(..., description="DynamicModules Id (e.g. &#x60;nejMcAhh5N8S3EQ4LaqysVdI0cZZ&#x60;)", alias="filter[id]"),
    system_type: Annotated[str, Field(description="The system type of the device making the request")] = Query(..., description="The system type of the device making the request", alias="systemType", examples=["IOS"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items, seedItem")] = Query(None, description="Include related resources. Available relationships: items, seedItem", alias="include", examples=["items"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")] = Query('en-US', description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.", alias="locale", examples=["en-US"]),
    refresh_seed: Annotated[Optional[str], Field(description="Stable seed used to keep dynamic page and module results consistent across a client session.")] = Query(None, description="Stable seed used to keep dynamic page and module results consistent across a client session.", alias="refreshSeed"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items", alias="replaceMedia", examples=["items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> DynamicModulesMultiResourceDataDocument:
    """Retrieves multiple dynamicModules by available filters, or without if applicable."""
    if not BaseDynamicModulesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDynamicModulesApi.subclasses[0]().dynamic_modules_get(client_version, device_type, filter_id, system_type, country_code, include, include_linkage, locale, refresh_seed, replace_media)


@router.get(
    "/dynamicModules/{id}",
    responses={
        200: {"model": DynamicModulesSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["dynamicModules"],
    summary="Get single dynamicModule.",
    response_model_by_alias=True,
)
async def dynamic_modules_id_get(
    client_version: Annotated[str, Field(description="Client version number")] = Query(..., description="Client version number", alias="clientVersion", examples=["2026.0.1"]),
    device_type: Annotated[str, Field(description="The type of device making the request")] = Query(..., description="The type of device making the request", alias="deviceType", examples=["PHONE"]),
    id: Annotated[str, Field(description="DynamicModules Id")] = Path(..., description="DynamicModules Id", examples=["nejMcAhh5N8S3EQ4LaqysVdI0cZZ"]),
    system_type: Annotated[str, Field(description="The system type of the device making the request")] = Query(..., description="The system type of the device making the request", alias="systemType", examples=["IOS"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items, seedItem")] = Query(None, description="Include related resources. Available relationships: items, seedItem", alias="include", examples=["items"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")] = Query('en-US', description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.", alias="locale", examples=["en-US"]),
    refresh_seed: Annotated[Optional[str], Field(description="Stable seed used to keep dynamic page and module results consistent across a client session.")] = Query(None, description="Stable seed used to keep dynamic page and module results consistent across a client session.", alias="refreshSeed"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items", alias="replaceMedia", examples=["items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> DynamicModulesSingleResourceDataDocument:
    """Retrieves single dynamicModule by id."""
    if not BaseDynamicModulesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDynamicModulesApi.subclasses[0]().dynamic_modules_id_get(client_version, device_type, id, system_type, country_code, include, include_linkage, locale, refresh_seed, replace_media)


@router.get(
    "/dynamicModules/{id}/relationships/items",
    responses={
        200: {"model": DynamicModulesItemsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["dynamicModules"],
    summary="Get items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def dynamic_modules_id_relationships_items_get(
    client_version: Annotated[str, Field(description="Client version number")] = Query(..., description="Client version number", alias="clientVersion", examples=["2026.0.1"]),
    device_type: Annotated[str, Field(description="The type of device making the request")] = Query(..., description="The type of device making the request", alias="deviceType", examples=["PHONE"]),
    id: Annotated[str, Field(description="DynamicModules Id")] = Path(..., description="DynamicModules Id", examples=["nejMcAhh5N8S3EQ4LaqysVdI0cZZ"]),
    system_type: Annotated[str, Field(description="The system type of the device making the request")] = Query(..., description="The system type of the device making the request", alias="systemType", examples=["IOS"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")] = Query(None, description="Include related resources. Available relationships: items", alias="include", examples=["items"]),
    locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")] = Query('en-US', description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.", alias="locale", examples=["en-US"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    refresh_seed: Annotated[Optional[str], Field(description="Stable seed used to keep dynamic page and module results consistent across a client session.")] = Query(None, description="Stable seed used to keep dynamic page and module results consistent across a client session.", alias="refreshSeed"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items", alias="replaceMedia", examples=["items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> DynamicModulesItemsMultiRelationshipDataDocument:
    """The module&#39;s items, in order — one stable collection per module, consistent for a given refreshSeed. Reads without a cursor return the first page (the slice a page shelf renders, sized for the module&#39;s previewLayout and device) with a continuation cursor; passing the cursor returns subsequent pages."""
    if not BaseDynamicModulesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDynamicModulesApi.subclasses[0]().dynamic_modules_id_relationships_items_get(client_version, device_type, id, system_type, country_code, include, locale, page_cursor, refresh_seed, replace_media)


@router.get(
    "/dynamicModules/{id}/relationships/seedItem",
    responses={
        200: {"model": DynamicModulesSeedItemSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["dynamicModules"],
    summary="Get seedItem relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def dynamic_modules_id_relationships_seed_item_get(
    client_version: Annotated[str, Field(description="Client version number")] = Query(..., description="Client version number", alias="clientVersion", examples=["2026.0.1"]),
    device_type: Annotated[str, Field(description="The type of device making the request")] = Query(..., description="The type of device making the request", alias="deviceType", examples=["PHONE"]),
    id: Annotated[str, Field(description="DynamicModules Id")] = Path(..., description="DynamicModules Id", examples=["nejMcAhh5N8S3EQ4LaqysVdI0cZZ"]),
    system_type: Annotated[str, Field(description="The system type of the device making the request")] = Query(..., description="The system type of the device making the request", alias="systemType", examples=["IOS"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: seedItem")] = Query(None, description="Include related resources. Available relationships: seedItem", alias="include", examples=["seedItem"]),
    locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")] = Query('en-US', description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.", alias="locale", examples=["en-US"]),
    refresh_seed: Annotated[Optional[str], Field(description="Stable seed used to keep dynamic page and module results consistent across a client session.")] = Query(None, description="Stable seed used to keep dynamic page and module results consistent across a client session.", alias="refreshSeed"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: seedItem")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: seedItem", alias="replaceMedia", examples=["seedItem"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> DynamicModulesSeedItemSingleRelationshipDataDocument:
    """The item whose listen or add event seeded this module&#39;s collection (e.g. the album a BECAUSE_YOU_* module is based on); null for modules that are not seeded by an item."""
    if not BaseDynamicModulesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDynamicModulesApi.subclasses[0]().dynamic_modules_id_relationships_seed_item_get(client_version, device_type, id, system_type, country_code, include, locale, refresh_seed, replace_media)
