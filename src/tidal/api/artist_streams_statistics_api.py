# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.artist_streams_statistics_api_base import BaseArtistStreamsStatisticsApi
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
from tidal.models.artist_streams_statistics_artist_single_relationship_data_document import ArtistStreamsStatisticsArtistSingleRelationshipDataDocument
from tidal.models.artist_streams_statistics_multi_resource_data_document import ArtistStreamsStatisticsMultiResourceDataDocument
from tidal.models.artist_streams_statistics_top_tracks_multi_relationship_data_document import ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/artistStreamsStatistics",
    responses={
        200: {"model": ArtistStreamsStatisticsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artistStreamsStatistics"],
    summary="Get multiple artistStreamsStatistics.",
    response_model_by_alias=True,
)
async def artist_streams_statistics_get(
    filter_artist_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="Artist ID. Every published range of the artist is returned (e.g. `1566`)")] = Query(..., description="Artist ID. Every published range of the artist is returned (e.g. &#x60;1566&#x60;)", alias="filter[artist.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artist, topTracks")] = Query(None, description="Include related resources. Available relationships: artist, topTracks", alias="include", examples=["artist.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artist.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artist.albums", alias="replaceMedia", examples=["artist.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ArtistStreamsStatisticsMultiResourceDataDocument:
    """Retrieves multiple artistStreamsStatistics by available filters, or without if applicable."""
    if not BaseArtistStreamsStatisticsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistStreamsStatisticsApi.subclasses[0]().artist_streams_statistics_get(filter_artist_id, include, include_linkage, replace_media)


@router.get(
    "/artistStreamsStatistics/{id}/relationships/artist",
    responses={
        200: {"model": ArtistStreamsStatisticsArtistSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artistStreamsStatistics"],
    summary="Get artist relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def artist_streams_statistics_id_relationships_artist_get(
    id: Annotated[str, Field(description="Artist streams statistics id")] = Path(..., description="Artist streams statistics id", examples=["LPtReLsCUO7kRhYq"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artist")] = Query(None, description="Include related resources. Available relationships: artist", alias="include", examples=["artist.albums"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artist.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artist.albums", alias="replaceMedia", examples=["artist.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ArtistStreamsStatisticsArtistSingleRelationshipDataDocument:
    """Retrieves artist relationship."""
    if not BaseArtistStreamsStatisticsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistStreamsStatisticsApi.subclasses[0]().artist_streams_statistics_id_relationships_artist_get(id, include, replace_media)


@router.get(
    "/artistStreamsStatistics/{id}/relationships/topTracks",
    responses={
        200: {"model": ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artistStreamsStatistics"],
    summary="Get topTracks relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artist_streams_statistics_id_relationships_top_tracks_get(
    id: Annotated[str, Field(description="Artist streams statistics id")] = Path(..., description="Artist streams statistics id", examples=["LPtReLsCUO7kRhYq"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: topTracks")] = Query(None, description="Include related resources. Available relationships: topTracks", alias="include", examples=["topTracks"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: topTracks")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: topTracks", alias="replaceMedia", examples=["topTracks"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument:
    """Retrieves topTracks relationship."""
    if not BaseArtistStreamsStatisticsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistStreamsStatisticsApi.subclasses[0]().artist_streams_statistics_id_relationships_top_tracks_get(id, include, page_cursor, replace_media)
