# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.search_results_api_base import BaseSearchResultsApi
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
from tidal.models.search_results_albums_multi_relationship_data_document import SearchResultsAlbumsMultiRelationshipDataDocument
from tidal.models.search_results_artists_multi_relationship_data_document import SearchResultsArtistsMultiRelationshipDataDocument
from tidal.models.search_results_multi_resource_data_document import SearchResultsMultiResourceDataDocument
from tidal.models.search_results_playlists_multi_relationship_data_document import SearchResultsPlaylistsMultiRelationshipDataDocument
from tidal.models.search_results_top_hits_multi_relationship_data_document import SearchResultsTopHitsMultiRelationshipDataDocument
from tidal.models.search_results_tracks_multi_relationship_data_document import SearchResultsTracksMultiRelationshipDataDocument
from tidal.models.search_results_videos_multi_relationship_data_document import SearchResultsVideosMultiRelationshipDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/searchResults",
    responses={
        200: {"model": SearchResultsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["searchResults"],
    summary="Get search results by query.",
    response_model_by_alias=True,
)
async def search_results_get(
    filter_query: Annotated[str, Field(min_length=1, max_length=256, description="Search query (e.g. `hello`)")] = Query(..., description="Search query (e.g. &#x60;hello&#x60;)", alias="filter[query]", min_length=1, max_length=256),
    client_version: Annotated[Optional[str], Field(description="Client version number")] = Query(None, description="Client version number", alias="clientVersion", examples=["2026.0.1"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    device_type: Annotated[Optional[str], Field(description="The type of device making the request")] = Query(None, description="The type of device making the request", alias="deviceType", examples=["PHONE"]),
    explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")] = Query('INCLUDE', description="Explicit filter. Valid values: INCLUDE or EXCLUDE", alias="explicitFilter", examples=["INCLUDE"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums, artists, playlists, topHits, tracks, videos")] = Query(None, description="Include related resources. Available relationships: albums, artists, playlists, topHits, tracks, videos", alias="include", examples=["albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums", alias="replaceMedia", examples=["albums"]),
    system_type: Annotated[Optional[str], Field(description="The system type of the device making the request")] = Query(None, description="The system type of the device making the request", alias="systemType", examples=["IOS"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "search.read"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> SearchResultsMultiResourceDataDocument:
    """Searches for a query and returns a collection containing exactly one search results resource."""
    if not BaseSearchResultsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSearchResultsApi.subclasses[0]().search_results_get(filter_query, client_version, country_code, device_type, explicit_filter, include, include_linkage, replace_media, system_type)


@router.get(
    "/searchResults/{id}/relationships/albums",
    responses={
        200: {"model": SearchResultsAlbumsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["searchResults"],
    summary="Get albums relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def search_results_id_relationships_albums_get(
    id: Annotated[str, Field(description="An opaque search results identifier")] = Path(..., description="An opaque search results identifier"),
    client_version: Annotated[Optional[str], Field(description="Client version number")] = Query(None, description="Client version number", alias="clientVersion", examples=["2026.0.1"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    device_type: Annotated[Optional[str], Field(description="The type of device making the request")] = Query(None, description="The type of device making the request", alias="deviceType", examples=["PHONE"]),
    explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")] = Query('INCLUDE', description="Explicit filter. Valid values: INCLUDE or EXCLUDE", alias="explicitFilter", examples=["INCLUDE"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums")] = Query(None, description="Include related resources. Available relationships: albums", alias="include", examples=["albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums", alias="replaceMedia", examples=["albums"]),
    system_type: Annotated[Optional[str], Field(description="The system type of the device making the request")] = Query(None, description="The system type of the device making the request", alias="systemType", examples=["IOS"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "search.read"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> SearchResultsAlbumsMultiRelationshipDataDocument:
    """Retrieves albums relationship."""
    if not BaseSearchResultsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSearchResultsApi.subclasses[0]().search_results_id_relationships_albums_get(id, client_version, country_code, device_type, explicit_filter, include, page_cursor, replace_media, system_type)


@router.get(
    "/searchResults/{id}/relationships/artists",
    responses={
        200: {"model": SearchResultsArtistsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["searchResults"],
    summary="Get artists relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def search_results_id_relationships_artists_get(
    id: Annotated[str, Field(description="An opaque search results identifier")] = Path(..., description="An opaque search results identifier"),
    client_version: Annotated[Optional[str], Field(description="Client version number")] = Query(None, description="Client version number", alias="clientVersion", examples=["2026.0.1"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    device_type: Annotated[Optional[str], Field(description="The type of device making the request")] = Query(None, description="The type of device making the request", alias="deviceType", examples=["PHONE"]),
    explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")] = Query('INCLUDE', description="Explicit filter. Valid values: INCLUDE or EXCLUDE", alias="explicitFilter", examples=["INCLUDE"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artists")] = Query(None, description="Include related resources. Available relationships: artists", alias="include", examples=["artists.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums", alias="replaceMedia", examples=["artists.albums"]),
    system_type: Annotated[Optional[str], Field(description="The system type of the device making the request")] = Query(None, description="The system type of the device making the request", alias="systemType", examples=["IOS"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "search.read"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> SearchResultsArtistsMultiRelationshipDataDocument:
    """Retrieves artists relationship."""
    if not BaseSearchResultsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSearchResultsApi.subclasses[0]().search_results_id_relationships_artists_get(id, client_version, country_code, device_type, explicit_filter, include, page_cursor, replace_media, system_type)


@router.get(
    "/searchResults/{id}/relationships/playlists",
    responses={
        200: {"model": SearchResultsPlaylistsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["searchResults"],
    summary="Get playlists relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def search_results_id_relationships_playlists_get(
    id: Annotated[str, Field(description="An opaque search results identifier")] = Path(..., description="An opaque search results identifier"),
    client_version: Annotated[Optional[str], Field(description="Client version number")] = Query(None, description="Client version number", alias="clientVersion", examples=["2026.0.1"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    device_type: Annotated[Optional[str], Field(description="The type of device making the request")] = Query(None, description="The type of device making the request", alias="deviceType", examples=["PHONE"]),
    explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")] = Query('INCLUDE', description="Explicit filter. Valid values: INCLUDE or EXCLUDE", alias="explicitFilter", examples=["INCLUDE"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: playlists")] = Query(None, description="Include related resources. Available relationships: playlists", alias="include", examples=["playlists.items"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlists.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: playlists.items", alias="replaceMedia", examples=["playlists.items"]),
    system_type: Annotated[Optional[str], Field(description="The system type of the device making the request")] = Query(None, description="The system type of the device making the request", alias="systemType", examples=["IOS"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "search.read"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> SearchResultsPlaylistsMultiRelationshipDataDocument:
    """Retrieves playlists relationship."""
    if not BaseSearchResultsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSearchResultsApi.subclasses[0]().search_results_id_relationships_playlists_get(id, client_version, country_code, device_type, explicit_filter, include, page_cursor, replace_media, system_type)


@router.get(
    "/searchResults/{id}/relationships/topHits",
    responses={
        200: {"model": SearchResultsTopHitsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["searchResults"],
    summary="Get topHits relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def search_results_id_relationships_top_hits_get(
    id: Annotated[str, Field(description="An opaque search results identifier")] = Path(..., description="An opaque search results identifier"),
    client_version: Annotated[Optional[str], Field(description="Client version number")] = Query(None, description="Client version number", alias="clientVersion", examples=["2026.0.1"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    device_type: Annotated[Optional[str], Field(description="The type of device making the request")] = Query(None, description="The type of device making the request", alias="deviceType", examples=["PHONE"]),
    explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")] = Query('INCLUDE', description="Explicit filter. Valid values: INCLUDE or EXCLUDE", alias="explicitFilter", examples=["INCLUDE"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: topHits")] = Query(None, description="Include related resources. Available relationships: topHits", alias="include", examples=["topHits"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: topHits")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: topHits", alias="replaceMedia", examples=["topHits"]),
    system_type: Annotated[Optional[str], Field(description="The system type of the device making the request")] = Query(None, description="The system type of the device making the request", alias="systemType", examples=["IOS"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "search.read"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> SearchResultsTopHitsMultiRelationshipDataDocument:
    """Retrieves topHits relationship."""
    if not BaseSearchResultsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSearchResultsApi.subclasses[0]().search_results_id_relationships_top_hits_get(id, client_version, country_code, device_type, explicit_filter, include, page_cursor, replace_media, system_type)


@router.get(
    "/searchResults/{id}/relationships/tracks",
    responses={
        200: {"model": SearchResultsTracksMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["searchResults"],
    summary="Get tracks relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def search_results_id_relationships_tracks_get(
    id: Annotated[str, Field(description="An opaque search results identifier")] = Path(..., description="An opaque search results identifier"),
    client_version: Annotated[Optional[str], Field(description="Client version number")] = Query(None, description="Client version number", alias="clientVersion", examples=["2026.0.1"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    device_type: Annotated[Optional[str], Field(description="The type of device making the request")] = Query(None, description="The type of device making the request", alias="deviceType", examples=["PHONE"]),
    explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")] = Query('INCLUDE', description="Explicit filter. Valid values: INCLUDE or EXCLUDE", alias="explicitFilter", examples=["INCLUDE"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: tracks")] = Query(None, description="Include related resources. Available relationships: tracks", alias="include", examples=["tracks"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: tracks", alias="replaceMedia", examples=["tracks"]),
    system_type: Annotated[Optional[str], Field(description="The system type of the device making the request")] = Query(None, description="The system type of the device making the request", alias="systemType", examples=["IOS"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "search.read"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> SearchResultsTracksMultiRelationshipDataDocument:
    """Retrieves tracks relationship."""
    if not BaseSearchResultsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSearchResultsApi.subclasses[0]().search_results_id_relationships_tracks_get(id, client_version, country_code, device_type, explicit_filter, include, page_cursor, replace_media, system_type)


@router.get(
    "/searchResults/{id}/relationships/videos",
    responses={
        200: {"model": SearchResultsVideosMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["searchResults"],
    summary="Get videos relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def search_results_id_relationships_videos_get(
    id: Annotated[str, Field(description="An opaque search results identifier")] = Path(..., description="An opaque search results identifier"),
    client_version: Annotated[Optional[str], Field(description="Client version number")] = Query(None, description="Client version number", alias="clientVersion", examples=["2026.0.1"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    device_type: Annotated[Optional[str], Field(description="The type of device making the request")] = Query(None, description="The type of device making the request", alias="deviceType", examples=["PHONE"]),
    explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")] = Query('INCLUDE', description="Explicit filter. Valid values: INCLUDE or EXCLUDE", alias="explicitFilter", examples=["INCLUDE"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: videos")] = Query(None, description="Include related resources. Available relationships: videos", alias="include", examples=["videos"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: videos", alias="replaceMedia", examples=["videos"]),
    system_type: Annotated[Optional[str], Field(description="The system type of the device making the request")] = Query(None, description="The system type of the device making the request", alias="systemType", examples=["IOS"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "search.read"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> SearchResultsVideosMultiRelationshipDataDocument:
    """Retrieves videos relationship."""
    if not BaseSearchResultsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSearchResultsApi.subclasses[0]().search_results_id_relationships_videos_get(id, client_version, country_code, device_type, explicit_filter, include, page_cursor, replace_media, system_type)
