# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.studio_home_event_tiles_api_base import BaseStudioHomeEventTilesApi
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
from typing_extensions import Annotated
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.models.studio_home_event_tiles_single_resource_data_document import StudioHomeEventTilesSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/studioHomeEventTiles/{id}",
    responses={
        200: {"model": StudioHomeEventTilesSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["studioHomeEventTiles"],
    summary="Get single studioHomeEventTile.",
    response_model_by_alias=True,
)
async def studio_home_event_tiles_id_get(
    id: Annotated[str, Field(description="Studio Home event tile id. Use `me` for the authenticated user's resource")] = Path(..., description="Studio Home event tile id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> StudioHomeEventTilesSingleResourceDataDocument:
    """Retrieves single studioHomeEventTile by id."""
    if not BaseStudioHomeEventTilesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseStudioHomeEventTilesApi.subclasses[0]().studio_home_event_tiles_id_get(id)
