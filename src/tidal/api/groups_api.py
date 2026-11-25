# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.groups_api_base import BaseGroupsApi
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
from typing import List
from typing_extensions import Annotated
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.models.groups_multi_resource_data_document import GroupsMultiResourceDataDocument
from tidal.models.groups_single_resource_data_document import GroupsSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/groups",
    responses={
        200: {"model": GroupsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["groups"],
    summary="Get multiple groups.",
    response_model_by_alias=True,
)
async def groups_get(
    filter_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20, description="Group ID. The built-in Everyone group has the case-sensitive ID `everyone`.")] = Query(..., description="Group ID. The built-in Everyone group has the case-sensitive ID &#x60;everyone&#x60;.", alias="filter[id]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> GroupsMultiResourceDataDocument:
    """Retrieves multiple groups by available filters, or without if applicable."""
    if not BaseGroupsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGroupsApi.subclasses[0]().groups_get(filter_id)


@router.get(
    "/groups/{id}",
    responses={
        200: {"model": GroupsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["groups"],
    summary="Get single group.",
    response_model_by_alias=True,
)
async def groups_id_get(
    id: Annotated[str, Field(description="Group ID. The built-in Everyone group has the case-sensitive ID `everyone`.")] = Path(..., description="Group ID. The built-in Everyone group has the case-sensitive ID &#x60;everyone&#x60;.", examples=["everyone"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> GroupsSingleResourceDataDocument:
    """Retrieves single group by id."""
    if not BaseGroupsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseGroupsApi.subclasses[0]().groups_id_get(id)
