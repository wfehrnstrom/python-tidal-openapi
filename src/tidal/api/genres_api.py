# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.genres_api_base import BaseGenresApi
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

from pydantic import Field
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
from tidal.models.genres_multi_resource_data_document import GenresMultiResourceDataDocument
from tidal.models.genres_single_resource_data_document import GenresSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/genres",
    responses={
        200: {"model": GenresMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["genres"],
    summary="Get multiple genres.",
    response_model_by_alias=True,
)
async def genres_get(
    filter_id: Annotated[List[str], Field(description="Allows filtering by genre id(s). USER_SELECTABLE is special value used to return specific genres which users can select from (e.g. `'1,2,3' or 'USER_SELECTABLE'`)")] = Query(..., description="Allows filtering by genre id(s). USER_SELECTABLE is special value used to return specific genres which users can select from (e.g. &#x60;&#39;1,2,3&#39; or &#39;USER_SELECTABLE&#39;&#x60;)", alias="filter[id]"),
    locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")] = Query('en-US', description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.", alias="locale", examples=["en-US"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> GenresMultiResourceDataDocument:
    """Retrieves multiple genres by available filters, or without if applicable."""
    if not BaseGenresApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGenresApi.subclasses[0]().genres_get(filter_id, locale, page_cursor)


@router.get(
    "/genres/{id}",
    responses={
        200: {"model": GenresSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["genres"],
    summary="Get single genre.",
    response_model_by_alias=True,
)
async def genres_id_get(
    id: Annotated[str, Field(description="Genre id")] = Path(..., description="Genre id", examples=["123"]),
    locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")] = Query('en-US', description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.", alias="locale", examples=["en-US"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> GenresSingleResourceDataDocument:
    """Retrieves single genre by id."""
    if not BaseGenresApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGenresApi.subclasses[0]().genres_id_get(id, locale)
