# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.studio_home_music_tiles_api_base import BaseStudioHomeMusicTilesApi
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
from tidal.models.studio_home_music_tiles_items_multi_relationship_data_document import StudioHomeMusicTilesItemsMultiRelationshipDataDocument
from tidal.models.studio_home_music_tiles_single_resource_data_document import StudioHomeMusicTilesSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/studioHomeMusicTiles/{id}",
    responses={
        200: {"model": StudioHomeMusicTilesSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["studioHomeMusicTiles"],
    summary="Get single studioHomeMusicTile.",
    response_model_by_alias=True,
)
async def studio_home_music_tiles_id_get(
    id: Annotated[str, Field(description="Studio Home music tile id. Use `me` for the authenticated user's resource")] = Path(..., description="Studio Home music tile id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")] = Query(None, description="Include related resources. Available relationships: items", alias="include", examples=["items"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items", alias="replaceMedia", examples=["items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> StudioHomeMusicTilesSingleResourceDataDocument:
    """Retrieves single studioHomeMusicTile by id."""
    if not BaseStudioHomeMusicTilesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseStudioHomeMusicTilesApi.subclasses[0]().studio_home_music_tiles_id_get(id, include, include_linkage, replace_media)


@router.get(
    "/studioHomeMusicTiles/{id}/relationships/items",
    responses={
        200: {"model": StudioHomeMusicTilesItemsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["studioHomeMusicTiles"],
    summary="Get items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def studio_home_music_tiles_id_relationships_items_get(
    id: Annotated[str, Field(description="Studio Home music tile id. Use `me` for the authenticated user's resource")] = Path(..., description="Studio Home music tile id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")] = Query(None, description="Include related resources. Available relationships: items", alias="include", examples=["items"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items", alias="replaceMedia", examples=["items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> StudioHomeMusicTilesItemsMultiRelationshipDataDocument:
    """The user&#39;s uploaded albums, newest first."""
    if not BaseStudioHomeMusicTilesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseStudioHomeMusicTilesApi.subclasses[0]().studio_home_music_tiles_id_relationships_items_get(id, include, page_cursor, replace_media)
