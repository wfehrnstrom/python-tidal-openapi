# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.downloads_api_base import BaseDownloadsApi
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
from tidal.models.downloads_multi_resource_data_document import DownloadsMultiResourceDataDocument
from tidal.models.downloads_owners_multi_relationship_data_document import DownloadsOwnersMultiRelationshipDataDocument
from tidal.models.downloads_single_resource_data_document import DownloadsSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/downloads",
    responses={
        200: {"model": DownloadsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["downloads"],
    summary="Get multiple downloads.",
    response_model_by_alias=True,
)
async def downloads_get(
    filter_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="Download id (e.g. `VFJBQ0tTOjEyMzQ1`)")] = Query(..., description="Download id (e.g. &#x60;VFJBQ0tTOjEyMzQ1&#x60;)", alias="filter[id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include"),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> DownloadsMultiResourceDataDocument:
    """Retrieves multiple downloads by available filters, or without if applicable."""
    if not BaseDownloadsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDownloadsApi.subclasses[0]().downloads_get(filter_id, include, include_linkage)


@router.get(
    "/downloads/{id}",
    responses={
        200: {"model": DownloadsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["downloads"],
    summary="Get single download.",
    response_model_by_alias=True,
)
async def downloads_id_get(
    id: Annotated[str, Field(description="Download id")] = Path(..., description="Download id", examples=["VFJBQ0tTOjEyMzQ1"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include"),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> DownloadsSingleResourceDataDocument:
    """Retrieves single download by id."""
    if not BaseDownloadsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDownloadsApi.subclasses[0]().downloads_id_get(id, include, include_linkage)


@router.get(
    "/downloads/{id}/relationships/owners",
    responses={
        200: {"model": DownloadsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["downloads"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def downloads_id_relationships_owners_get(
    id: Annotated[str, Field(description="Download id")] = Path(..., description="Download id", examples=["VFJBQ0tTOjEyMzQ1"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> DownloadsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseDownloadsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDownloadsApi.subclasses[0]().downloads_id_relationships_owners_get(id, include, page_cursor)
