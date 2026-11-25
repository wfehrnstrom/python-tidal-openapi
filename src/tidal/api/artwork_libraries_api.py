# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.artwork_libraries_api_base import BaseArtworkLibrariesApi
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
from tidal.models.artwork_libraries_artworks_multi_relationship_data_document import ArtworkLibrariesArtworksMultiRelationshipDataDocument
from tidal.models.artwork_libraries_multi_resource_data_document import ArtworkLibrariesMultiResourceDataDocument
from tidal.models.artwork_libraries_random_artwork_single_relationship_data_document import ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument
from tidal.models.artwork_libraries_single_resource_data_document import ArtworkLibrariesSingleResourceDataDocument
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/artworkLibraries",
    responses={
        200: {"model": ArtworkLibrariesMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artworkLibraries"],
    summary="Get multiple artworkLibraries.",
    response_model_by_alias=True,
)
async def artwork_libraries_get(
    filter_name: Annotated[List[str], Field(min_length=1, max_length=20, description="Library names (e.g. `album-defaults`)")] = Query(..., description="Library names (e.g. &#x60;album-defaults&#x60;)", alias="filter[name]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks, randomArtwork")] = Query(None, description="Include related resources. Available relationships: artworks, randomArtwork", alias="include", examples=["artworks"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtworkLibrariesMultiResourceDataDocument:
    """Retrieves multiple artworkLibraries by available filters, or without if applicable."""
    if not BaseArtworkLibrariesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtworkLibrariesApi.subclasses[0]().artwork_libraries_get(filter_name, include, include_linkage)


@router.get(
    "/artworkLibraries/{id}",
    responses={
        200: {"model": ArtworkLibrariesSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artworkLibraries"],
    summary="Get single artworkLibrarie.",
    response_model_by_alias=True,
)
async def artwork_libraries_id_get(
    id: Annotated[str, Field(description="Artwork library ID")] = Path(..., description="Artwork library ID", examples=["AmX9i1vQ54Db3RZwLBr"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks, randomArtwork")] = Query(None, description="Include related resources. Available relationships: artworks, randomArtwork", alias="include", examples=["artworks"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtworkLibrariesSingleResourceDataDocument:
    """Retrieves single artworkLibrarie by id."""
    if not BaseArtworkLibrariesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtworkLibrariesApi.subclasses[0]().artwork_libraries_id_get(id, include, include_linkage)


@router.get(
    "/artworkLibraries/{id}/relationships/artworks",
    responses={
        200: {"model": ArtworkLibrariesArtworksMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artworkLibraries"],
    summary="Get artworks relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artwork_libraries_id_relationships_artworks_get(
    id: Annotated[str, Field(description="Artwork library ID")] = Path(..., description="Artwork library ID", examples=["AmX9i1vQ54Db3RZwLBr"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks")] = Query(None, description="Include related resources. Available relationships: artworks", alias="include", examples=["artworks"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtworkLibrariesArtworksMultiRelationshipDataDocument:
    """Artworks in the library that have finished processing and are not flagged or taken down, newest first"""
    if not BaseArtworkLibrariesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtworkLibrariesApi.subclasses[0]().artwork_libraries_id_relationships_artworks_get(id, include, page_cursor)


@router.get(
    "/artworkLibraries/{id}/relationships/randomArtwork",
    responses={
        200: {"model": ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artworkLibraries"],
    summary="Get randomArtwork relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def artwork_libraries_id_relationships_random_artwork_get(
    id: Annotated[str, Field(description="Artwork library ID")] = Path(..., description="Artwork library ID", examples=["AmX9i1vQ54Db3RZwLBr"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: randomArtwork")] = Query(None, description="Include related resources. Available relationships: randomArtwork", alias="include", examples=["randomArtwork"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument:
    """A random artwork from the library, used by clients to supply a default artwork, for example for albums without cover art. Picked per request from the artworks that have finished processing and are not flagged or taken down, and not stored; empty when there are none"""
    if not BaseArtworkLibrariesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtworkLibrariesApi.subclasses[0]().artwork_libraries_id_relationships_random_artwork_get(id, include)
