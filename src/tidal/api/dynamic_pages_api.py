# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.dynamic_pages_api_base import BaseDynamicPagesApi
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
from tidal.models.dynamic_pages_modules_multi_relationship_data_document import DynamicPagesModulesMultiRelationshipDataDocument
from tidal.models.dynamic_pages_multi_resource_data_document import DynamicPagesMultiResourceDataDocument
from tidal.models.dynamic_pages_subject_single_relationship_data_document import DynamicPagesSubjectSingleRelationshipDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/dynamicPages",
    responses={
        200: {"model": DynamicPagesMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["dynamicPages"],
    summary="Get multiple dynamicPages.",
    response_model_by_alias=True,
)
async def dynamic_pages_get(
    client_version: Annotated[str, Field(description="Client version number")] = Query(..., description="Client version number", alias="clientVersion", examples=["2026.0.1"]),
    device_type: Annotated[str, Field(description="The type of device making the request")] = Query(..., description="The type of device making the request", alias="deviceType", examples=["PHONE"]),
    filter_page_type: Annotated[List[str], Field(description="Type of the page (e.g. `ARTIST`)")] = Query(..., description="Type of the page (e.g. &#x60;ARTIST&#x60;)", alias="filter[pageType]"),
    system_type: Annotated[str, Field(description="The system type of the device making the request")] = Query(..., description="The system type of the device making the request", alias="systemType", examples=["IOS"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    filter_subject: Annotated[Optional[str], Field(description="The page subject. Its type must match pageType. Required except for HOME_FREE, where it must be omitted. Also accepts `users:me`.")] = Query(None, description="The page subject. Its type must match pageType. Required except for HOME_FREE, where it must be omitted. Also accepts &#x60;users:me&#x60;.", alias="filter[subject]", regex=r"^(?:users|artists|albums|playlists|tracks|videos):[^,]+$"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: modules, subject")] = Query(None, description="Include related resources. Available relationships: modules, subject", alias="include", examples=["modules.items"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")] = Query('en-US', description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.", alias="locale", examples=["en-US"]),
    refresh_seed: Annotated[Optional[str], Field(description="Stable seed used to keep dynamic page and module results consistent across a client session.")] = Query(None, description="Stable seed used to keep dynamic page and module results consistent across a client session.", alias="refreshSeed"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: modules.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: modules.items", alias="replaceMedia", examples=["modules.items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> DynamicPagesMultiResourceDataDocument:
    """Retrieves multiple dynamicPages by available filters, or without if applicable."""
    if not BaseDynamicPagesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDynamicPagesApi.subclasses[0]().dynamic_pages_get(client_version, device_type, filter_page_type, system_type, country_code, filter_subject, include, include_linkage, locale, refresh_seed, replace_media)


@router.get(
    "/dynamicPages/{id}/relationships/modules",
    responses={
        200: {"model": DynamicPagesModulesMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["dynamicPages"],
    summary="Get modules relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def dynamic_pages_id_relationships_modules_get(
    client_version: Annotated[str, Field(description="Client version number")] = Query(..., description="Client version number", alias="clientVersion", examples=["2026.0.1"]),
    device_type: Annotated[str, Field(description="The type of device making the request")] = Query(..., description="The type of device making the request", alias="deviceType", examples=["PHONE"]),
    id: Annotated[str, Field(description="DynamicPages Id")] = Path(..., description="DynamicPages Id", examples=["nejMcAhh5N8S3EQ4LaqysVdI0cZZ"]),
    system_type: Annotated[str, Field(description="The system type of the device making the request")] = Query(..., description="The system type of the device making the request", alias="systemType", examples=["IOS"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: modules")] = Query(None, description="Include related resources. Available relationships: modules", alias="include", examples=["modules.items"]),
    locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")] = Query('en-US', description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.", alias="locale", examples=["en-US"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    refresh_seed: Annotated[Optional[str], Field(description="Stable seed used to keep dynamic page and module results consistent across a client session.")] = Query(None, description="Stable seed used to keep dynamic page and module results consistent across a client session.", alias="refreshSeed"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: modules.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: modules.items", alias="replaceMedia", examples=["modules.items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> DynamicPagesModulesMultiRelationshipDataDocument:
    """The page&#39;s modules, in display order."""
    if not BaseDynamicPagesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDynamicPagesApi.subclasses[0]().dynamic_pages_id_relationships_modules_get(client_version, device_type, id, system_type, country_code, include, locale, page_cursor, refresh_seed, replace_media)


@router.get(
    "/dynamicPages/{id}/relationships/subject",
    responses={
        200: {"model": DynamicPagesSubjectSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["dynamicPages"],
    summary="Get subject relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def dynamic_pages_id_relationships_subject_get(
    id: Annotated[str, Field(description="DynamicPages Id")] = Path(..., description="DynamicPages Id", examples=["nejMcAhh5N8S3EQ4LaqysVdI0cZZ"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject", alias="replaceMedia", examples=["subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> DynamicPagesSubjectSingleRelationshipDataDocument:
    """Retrieves subject relationship."""
    if not BaseDynamicPagesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDynamicPagesApi.subclasses[0]().dynamic_pages_id_relationships_subject_get(id, include, replace_media)
