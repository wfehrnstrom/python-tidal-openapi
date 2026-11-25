# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.studio_home_merch_tiles_api_base import BaseStudioHomeMerchTilesApi
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
from tidal.models.studio_home_merch_tiles_items_multi_relationship_data_document import StudioHomeMerchTilesItemsMultiRelationshipDataDocument
from tidal.models.studio_home_merch_tiles_single_resource_data_document import StudioHomeMerchTilesSingleResourceDataDocument
from tidal.models.studio_home_merch_tiles_square_connection_single_relationship_data_document import StudioHomeMerchTilesSquareConnectionSingleRelationshipDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/studioHomeMerchTiles/{id}",
    responses={
        200: {"model": StudioHomeMerchTilesSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["studioHomeMerchTiles"],
    summary="Get single studioHomeMerchTile.",
    response_model_by_alias=True,
)
async def studio_home_merch_tiles_id_get(
    id: Annotated[str, Field(description="Studio Home merch tile id. Use `me` for the authenticated user's resource")] = Path(..., description="Studio Home merch tile id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items, squareConnection")] = Query(None, description="Include related resources. Available relationships: items, squareConnection", alias="include", examples=["items"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> StudioHomeMerchTilesSingleResourceDataDocument:
    """Retrieves single studioHomeMerchTile by id."""
    if not BaseStudioHomeMerchTilesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseStudioHomeMerchTilesApi.subclasses[0]().studio_home_merch_tiles_id_get(id, include, include_linkage)


@router.get(
    "/studioHomeMerchTiles/{id}/relationships/items",
    responses={
        200: {"model": StudioHomeMerchTilesItemsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["studioHomeMerchTiles"],
    summary="Get items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def studio_home_merch_tiles_id_relationships_items_get(
    id: Annotated[str, Field(description="Studio Home merch tile id. Use `me` for the authenticated user's resource")] = Path(..., description="Studio Home merch tile id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")] = Query(None, description="Include related resources. Available relationships: items", alias="include", examples=["items"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> StudioHomeMerchTilesItemsMultiRelationshipDataDocument:
    """The seller&#39;s catalog items, in title order; empty until the latest merch guidelines are accepted. A page can be short or empty and still have a next cursor."""
    if not BaseStudioHomeMerchTilesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseStudioHomeMerchTilesApi.subclasses[0]().studio_home_merch_tiles_id_relationships_items_get(id, include, page_cursor)


@router.get(
    "/studioHomeMerchTiles/{id}/relationships/squareConnection",
    responses={
        200: {"model": StudioHomeMerchTilesSquareConnectionSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["studioHomeMerchTiles"],
    summary="Get squareConnection relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def studio_home_merch_tiles_id_relationships_square_connection_get(
    id: Annotated[str, Field(description="Studio Home merch tile id. Use `me` for the authenticated user's resource")] = Path(..., description="Studio Home merch tile id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: squareConnection")] = Query(None, description="Include related resources. Available relationships: squareConnection", alias="include", examples=["squareConnection"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> StudioHomeMerchTilesSquareConnectionSingleRelationshipDataDocument:
    """The seller&#39;s Square connection; empty when they have none."""
    if not BaseStudioHomeMerchTilesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseStudioHomeMerchTilesApi.subclasses[0]().studio_home_merch_tiles_id_relationships_square_connection_get(id, include)
