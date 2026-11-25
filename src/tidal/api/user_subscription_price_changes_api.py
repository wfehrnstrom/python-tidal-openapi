# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.user_subscription_price_changes_api_base import BaseUserSubscriptionPriceChangesApi
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
from tidal.models.user_subscription_price_changes_decision_single_relationship_data_document import UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument
from tidal.models.user_subscription_price_changes_multi_resource_data_document import UserSubscriptionPriceChangesMultiResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/userSubscriptionPriceChanges",
    responses={
        200: {"model": UserSubscriptionPriceChangesMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userSubscriptionPriceChanges"],
    summary="Get multiple userSubscriptionPriceChanges.",
    response_model_by_alias=True,
)
async def user_subscription_price_changes_get(
    filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="User id. Also accepts `me`.")] = Query(..., description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: decision")] = Query(None, description="Include related resources. Available relationships: decision", alias="include", examples=["decision"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> UserSubscriptionPriceChangesMultiResourceDataDocument:
    """Retrieves multiple userSubscriptionPriceChanges by available filters, or without if applicable."""
    if not BaseUserSubscriptionPriceChangesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserSubscriptionPriceChangesApi.subclasses[0]().user_subscription_price_changes_get(filter_owners_id, include, include_linkage)


@router.get(
    "/userSubscriptionPriceChanges/{id}/relationships/decision",
    responses={
        200: {"model": UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userSubscriptionPriceChanges"],
    summary="Get decision relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def user_subscription_price_changes_id_relationships_decision_get(
    id: Annotated[str, Field(description="Price change id")] = Path(..., description="Price change id", examples=["1AC1yHZWFAFVjnFOn8XoXA"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: decision")] = Query(None, description="Include related resources. Available relationships: decision", alias="include", examples=["decision"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument:
    """Retrieves decision relationship."""
    if not BaseUserSubscriptionPriceChangesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserSubscriptionPriceChangesApi.subclasses[0]().user_subscription_price_changes_id_relationships_decision_get(id, include)
