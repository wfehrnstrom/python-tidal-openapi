# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.videos_api_base import BaseVideosApi
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
from tidal.models.videos_albums_multi_relationship_data_document import VideosAlbumsMultiRelationshipDataDocument
from tidal.models.videos_artists_multi_relationship_data_document import VideosArtistsMultiRelationshipDataDocument
from tidal.models.videos_credits_multi_relationship_data_document import VideosCreditsMultiRelationshipDataDocument
from tidal.models.videos_multi_resource_data_document import VideosMultiResourceDataDocument
from tidal.models.videos_providers_multi_relationship_data_document import VideosProvidersMultiRelationshipDataDocument
from tidal.models.videos_replacement_single_relationship_data_document import VideosReplacementSingleRelationshipDataDocument
from tidal.models.videos_similar_videos_multi_relationship_data_document import VideosSimilarVideosMultiRelationshipDataDocument
from tidal.models.videos_single_resource_data_document import VideosSingleResourceDataDocument
from tidal.models.videos_suggested_videos_multi_relationship_data_document import VideosSuggestedVideosMultiRelationshipDataDocument
from tidal.models.videos_thumbnail_art_multi_relationship_data_document import VideosThumbnailArtMultiRelationshipDataDocument
from tidal.models.videos_usage_rules_single_relationship_data_document import VideosUsageRulesSingleRelationshipDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/videos",
    responses={
        200: {"model": VideosMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["videos"],
    summary="Get multiple videos.",
    response_model_by_alias=True,
)
async def videos_get(
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of video IDs (e.g. `75623239`)")] = Query(None, description="List of video IDs (e.g. &#x60;75623239&#x60;)", alias="filter[id]"),
    filter_isrc: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of ISRCs (e.g. `QMJMT1701237`)")] = Query(None, description="List of ISRCs (e.g. &#x60;QMJMT1701237&#x60;)", alias="filter[isrc]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums, artists, credits, providers, replacement, similarVideos, suggestedVideos, thumbnailArt, usageRules")] = Query(None, description="Include related resources. Available relationships: albums, artists, credits, providers, replacement, similarVideos, suggestedVideos, thumbnailArt, usageRules", alias="include", examples=["albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums", alias="replaceMedia", examples=["albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> VideosMultiResourceDataDocument:
    """Retrieves multiple videos by available filters, or without if applicable."""
    if not BaseVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVideosApi.subclasses[0]().videos_get(country_code, filter_id, filter_isrc, include, include_linkage, replace_media)


@router.get(
    "/videos/{id}",
    responses={
        200: {"model": VideosSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["videos"],
    summary="Get single video.",
    response_model_by_alias=True,
)
async def videos_id_get(
    id: Annotated[str, Field(description="Video id")] = Path(..., description="Video id", examples=["75623239"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums, artists, credits, providers, replacement, similarVideos, suggestedVideos, thumbnailArt, usageRules")] = Query(None, description="Include related resources. Available relationships: albums, artists, credits, providers, replacement, similarVideos, suggestedVideos, thumbnailArt, usageRules", alias="include", examples=["albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums", alias="replaceMedia", examples=["albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> VideosSingleResourceDataDocument:
    """Retrieves single video by id."""
    if not BaseVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVideosApi.subclasses[0]().videos_id_get(id, country_code, include, include_linkage, replace_media)


@router.get(
    "/videos/{id}/relationships/albums",
    responses={
        200: {"model": VideosAlbumsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["videos"],
    summary="Get albums relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def videos_id_relationships_albums_get(
    id: Annotated[str, Field(description="Video id")] = Path(..., description="Video id", examples=["75623239"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums")] = Query(None, description="Include related resources. Available relationships: albums", alias="include", examples=["albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums", alias="replaceMedia", examples=["albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> VideosAlbumsMultiRelationshipDataDocument:
    """Retrieves albums relationship."""
    if not BaseVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVideosApi.subclasses[0]().videos_id_relationships_albums_get(id, country_code, include, page_cursor, replace_media)


@router.get(
    "/videos/{id}/relationships/artists",
    responses={
        200: {"model": VideosArtistsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["videos"],
    summary="Get artists relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def videos_id_relationships_artists_get(
    id: Annotated[str, Field(description="Video id")] = Path(..., description="Video id", examples=["75623239"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artists")] = Query(None, description="Include related resources. Available relationships: artists", alias="include", examples=["artists.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums", alias="replaceMedia", examples=["artists.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> VideosArtistsMultiRelationshipDataDocument:
    """Retrieves artists relationship."""
    if not BaseVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVideosApi.subclasses[0]().videos_id_relationships_artists_get(id, country_code, include, page_cursor, replace_media)


@router.get(
    "/videos/{id}/relationships/credits",
    responses={
        200: {"model": VideosCreditsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["videos"],
    summary="Get credits relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def videos_id_relationships_credits_get(
    id: Annotated[str, Field(description="Video id")] = Path(..., description="Video id", examples=["75623239"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: credits")] = Query(None, description="Include related resources. Available relationships: credits", alias="include", examples=["credits.artist.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: credits.artist.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: credits.artist.albums", alias="replaceMedia", examples=["credits.artist.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> VideosCreditsMultiRelationshipDataDocument:
    """Retrieves credits relationship."""
    if not BaseVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVideosApi.subclasses[0]().videos_id_relationships_credits_get(id, include, page_cursor, replace_media)


@router.get(
    "/videos/{id}/relationships/providers",
    responses={
        200: {"model": VideosProvidersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["videos"],
    summary="Get providers relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def videos_id_relationships_providers_get(
    id: Annotated[str, Field(description="Video id")] = Path(..., description="Video id", examples=["75623239"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: providers")] = Query(None, description="Include related resources. Available relationships: providers", alias="include", examples=["providers"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> VideosProvidersMultiRelationshipDataDocument:
    """Retrieves providers relationship."""
    if not BaseVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVideosApi.subclasses[0]().videos_id_relationships_providers_get(id, country_code, include, page_cursor)


@router.get(
    "/videos/{id}/relationships/replacement",
    responses={
        200: {"model": VideosReplacementSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["videos"],
    summary="Get replacement relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def videos_id_relationships_replacement_get(
    id: Annotated[str, Field(description="Video id")] = Path(..., description="Video id", examples=["75623239"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: replacement")] = Query(None, description="Include related resources. Available relationships: replacement", alias="include", examples=["replacement"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: replacement")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: replacement", alias="replaceMedia", examples=["replacement"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> VideosReplacementSingleRelationshipDataDocument:
    """Retrieves replacement relationship."""
    if not BaseVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVideosApi.subclasses[0]().videos_id_relationships_replacement_get(id, country_code, include, replace_media)


@router.get(
    "/videos/{id}/relationships/similarVideos",
    responses={
        200: {"model": VideosSimilarVideosMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["videos"],
    summary="Get similarVideos relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def videos_id_relationships_similar_videos_get(
    id: Annotated[str, Field(description="Video id")] = Path(..., description="Video id", examples=["75623239"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: similarVideos")] = Query(None, description="Include related resources. Available relationships: similarVideos", alias="include", examples=["similarVideos"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarVideos")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: similarVideos", alias="replaceMedia", examples=["similarVideos"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> VideosSimilarVideosMultiRelationshipDataDocument:
    """Retrieves similarVideos relationship."""
    if not BaseVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVideosApi.subclasses[0]().videos_id_relationships_similar_videos_get(id, country_code, include, page_cursor, replace_media)


@router.get(
    "/videos/{id}/relationships/suggestedVideos",
    responses={
        200: {"model": VideosSuggestedVideosMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["videos"],
    summary="Get suggestedVideos relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def videos_id_relationships_suggested_videos_get(
    id: Annotated[str, Field(description="Video id")] = Path(..., description="Video id", examples=["75623239"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: suggestedVideos")] = Query(None, description="Include related resources. Available relationships: suggestedVideos", alias="include", examples=["suggestedVideos"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: suggestedVideos")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: suggestedVideos", alias="replaceMedia", examples=["suggestedVideos"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> VideosSuggestedVideosMultiRelationshipDataDocument:
    """Retrieves suggestedVideos relationship."""
    if not BaseVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVideosApi.subclasses[0]().videos_id_relationships_suggested_videos_get(id, country_code, include, page_cursor, replace_media)


@router.get(
    "/videos/{id}/relationships/thumbnailArt",
    responses={
        200: {"model": VideosThumbnailArtMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["videos"],
    summary="Get thumbnailArt relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def videos_id_relationships_thumbnail_art_get(
    id: Annotated[str, Field(description="Video id")] = Path(..., description="Video id", examples=["75623239"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: thumbnailArt")] = Query(None, description="Include related resources. Available relationships: thumbnailArt", alias="include", examples=["thumbnailArt"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> VideosThumbnailArtMultiRelationshipDataDocument:
    """Retrieves thumbnailArt relationship."""
    if not BaseVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVideosApi.subclasses[0]().videos_id_relationships_thumbnail_art_get(id, country_code, include, page_cursor)


@router.get(
    "/videos/{id}/relationships/usageRules",
    responses={
        200: {"model": VideosUsageRulesSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["videos"],
    summary="Get usageRules relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def videos_id_relationships_usage_rules_get(
    id: Annotated[str, Field(description="Video id")] = Path(..., description="Video id", examples=["75623239"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: usageRules")] = Query(None, description="Include related resources. Available relationships: usageRules", alias="include", examples=["usageRules"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> VideosUsageRulesSingleRelationshipDataDocument:
    """Retrieves usageRules relationship."""
    if not BaseVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVideosApi.subclasses[0]().videos_id_relationships_usage_rules_get(id, country_code, include)
