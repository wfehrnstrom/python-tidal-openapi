# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.credits_api_base import BaseCreditsApi
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
from tidal.models.credits_artist_single_relationship_data_document import CreditsArtistSingleRelationshipDataDocument
from tidal.models.credits_category_single_relationship_data_document import CreditsCategorySingleRelationshipDataDocument
from tidal.models.credits_single_resource_data_document import CreditsSingleResourceDataDocument
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
    "/credits/{id}",
    responses={
        200: {"model": CreditsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["credits"],
    summary="Get single credit.",
    response_model_by_alias=True,
)
async def credits_id_get(
    id: Annotated[str, Field(description="Credit id")] = Path(..., description="Credit id", examples=["3fG7kLmN2pQrStUv"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artist, category")] = Query(None, description="Include related resources. Available relationships: artist, category", alias="include", examples=["artist.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artist.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artist.albums", alias="replaceMedia", examples=["artist.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> CreditsSingleResourceDataDocument:
    """Retrieves single credit by id."""
    if not BaseCreditsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCreditsApi.subclasses[0]().credits_id_get(id, include, include_linkage, replace_media)


@router.get(
    "/credits/{id}/relationships/artist",
    responses={
        200: {"model": CreditsArtistSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["credits"],
    summary="Get artist relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def credits_id_relationships_artist_get(
    id: Annotated[str, Field(description="Credit id")] = Path(..., description="Credit id", examples=["3fG7kLmN2pQrStUv"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artist")] = Query(None, description="Include related resources. Available relationships: artist", alias="include", examples=["artist.albums"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artist.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artist.albums", alias="replaceMedia", examples=["artist.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> CreditsArtistSingleRelationshipDataDocument:
    """Retrieves artist relationship."""
    if not BaseCreditsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCreditsApi.subclasses[0]().credits_id_relationships_artist_get(id, include, replace_media)


@router.get(
    "/credits/{id}/relationships/category",
    responses={
        200: {"model": CreditsCategorySingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["credits"],
    summary="Get category relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def credits_id_relationships_category_get(
    id: Annotated[str, Field(description="Credit id")] = Path(..., description="Credit id", examples=["3fG7kLmN2pQrStUv"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: category")] = Query(None, description="Include related resources. Available relationships: category", alias="include", examples=["category"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> CreditsCategorySingleRelationshipDataDocument:
    """Retrieves category relationship."""
    if not BaseCreditsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCreditsApi.subclasses[0]().credits_id_relationships_category_get(id, include)
