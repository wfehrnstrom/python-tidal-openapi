# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.search_suggestions_api_base import BaseSearchSuggestionsApi
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
from tidal.models.search_suggestions_direct_hits_multi_relationship_data_document import SearchSuggestionsDirectHitsMultiRelationshipDataDocument
from tidal.models.search_suggestions_history_multi_relationship_data_document import SearchSuggestionsHistoryMultiRelationshipDataDocument
from tidal.models.search_suggestions_multi_resource_data_document import SearchSuggestionsMultiResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/searchSuggestions",
    responses={
        200: {"model": SearchSuggestionsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["searchSuggestions"],
    summary="Get search suggestions by query.",
    response_model_by_alias=True,
)
async def search_suggestions_get(
    filter_query: Annotated[str, Field(min_length=1, max_length=256, description="Search query (e.g. `hello`)")] = Query(..., description="Search query (e.g. &#x60;hello&#x60;)", alias="filter[query]", min_length=1, max_length=256),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")] = Query('INCLUDE', description="Explicit filter. Valid values: INCLUDE or EXCLUDE", alias="explicitFilter", examples=["INCLUDE"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: directHits, history")] = Query(None, description="Include related resources. Available relationships: directHits, history", alias="include", examples=["directHits"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: directHits")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: directHits", alias="replaceMedia", examples=["directHits"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "search.read"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> SearchSuggestionsMultiResourceDataDocument:
    """Searches for a query and returns a collection containing exactly one search suggestions resource."""
    if not BaseSearchSuggestionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSearchSuggestionsApi.subclasses[0]().search_suggestions_get(filter_query, country_code, explicit_filter, include, include_linkage, replace_media)


@router.get(
    "/searchSuggestions/{id}/relationships/directHits",
    responses={
        200: {"model": SearchSuggestionsDirectHitsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["searchSuggestions"],
    summary="Get directHits relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def search_suggestions_id_relationships_direct_hits_get(
    id: Annotated[str, Field(description="An opaque search suggestions identifier")] = Path(..., description="An opaque search suggestions identifier"),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")] = Query('INCLUDE', description="Explicit filter. Valid values: INCLUDE or EXCLUDE", alias="explicitFilter", examples=["INCLUDE"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: directHits")] = Query(None, description="Include related resources. Available relationships: directHits", alias="include", examples=["directHits"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: directHits")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: directHits", alias="replaceMedia", examples=["directHits"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "search.read"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> SearchSuggestionsDirectHitsMultiRelationshipDataDocument:
    """Retrieves directHits relationship."""
    if not BaseSearchSuggestionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSearchSuggestionsApi.subclasses[0]().search_suggestions_id_relationships_direct_hits_get(id, country_code, explicit_filter, include, page_cursor, replace_media)


@router.get(
    "/searchSuggestions/{id}/relationships/history",
    responses={
        200: {"model": SearchSuggestionsHistoryMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["searchSuggestions"],
    summary="Get history relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def search_suggestions_id_relationships_history_get(
    id: Annotated[str, Field(description="An opaque search suggestions identifier")] = Path(..., description="An opaque search suggestions identifier"),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")] = Query('INCLUDE', description="Explicit filter. Valid values: INCLUDE or EXCLUDE", alias="explicitFilter", examples=["INCLUDE"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: history")] = Query(None, description="Include related resources. Available relationships: history", alias="include", examples=["history"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "search.read"]
    ),
) -> SearchSuggestionsHistoryMultiRelationshipDataDocument:
    """Retrieves history relationship."""
    if not BaseSearchSuggestionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSearchSuggestionsApi.subclasses[0]().search_suggestions_id_relationships_history_get(id, country_code, explicit_filter, include, page_cursor)
