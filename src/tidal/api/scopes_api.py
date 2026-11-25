# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.scopes_api_base import BaseScopesApi
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
from tidal.models.scopes_multi_resource_data_document import ScopesMultiResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/scopes",
    responses={
        200: {"model": ScopesMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["scopes"],
    summary="Get multiple scopes.",
    response_model_by_alias=True,
)
async def scopes_get(
    filter_required_access_tier: Annotated[Optional[Annotated[List[str], Field(min_length=1, max_length=20)]], Field(description="Filters scopes by their required client access tier. (e.g. `THIRD_PARTY`)")] = Query(None, description="Filters scopes by their required client access tier. (e.g. &#x60;THIRD_PARTY&#x60;)", alias="filter[requiredAccessTier]"),
    filter_required_access_tier_satisfied_by: Annotated[Optional[str], Field(description="Selects scopes whose required access tier is satisfied by the client tier. (e.g. `PARTNER`)")] = Query(None, description="Selects scopes whose required access tier is satisfied by the client tier. (e.g. &#x60;PARTNER&#x60;)", alias="filter[requiredAccessTier][satisfiedBy]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> ScopesMultiResourceDataDocument:
    """Retrieves multiple scopes by available filters, or without if applicable."""
    if not BaseScopesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseScopesApi.subclasses[0]().scopes_get(filter_required_access_tier, filter_required_access_tier_satisfied_by)
