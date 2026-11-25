# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.subscription_price_change_decisions_api_base import BaseSubscriptionPriceChangeDecisionsApi
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
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.subscription_price_change_decisions_create_operation_payload import SubscriptionPriceChangeDecisionsCreateOperationPayload
from tidal.models.subscription_price_change_decisions_create_single_resource_data_document import SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument
from tidal.models.subscription_price_change_decisions_multi_resource_data_document import SubscriptionPriceChangeDecisionsMultiResourceDataDocument
from tidal.models.subscription_price_change_decisions_price_change_single_relationship_data_document import SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument
from tidal.models.subscription_price_change_decisions_update_operation_payload import SubscriptionPriceChangeDecisionsUpdateOperationPayload
from tidal.models.subscription_price_change_decisions_update_single_resource_data_document import SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/subscriptionPriceChangeDecisions",
    responses={
        200: {"model": SubscriptionPriceChangeDecisionsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["subscriptionPriceChangeDecisions"],
    summary="Get multiple subscriptionPriceChangeDecisions.",
    response_model_by_alias=True,
)
async def subscription_price_change_decisions_get(
    filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="User id. Also accepts `me`.")] = Query(..., description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: priceChange")] = Query(None, description="Include related resources. Available relationships: priceChange", alias="include", examples=["priceChange"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> SubscriptionPriceChangeDecisionsMultiResourceDataDocument:
    """Retrieves multiple subscriptionPriceChangeDecisions by available filters, or without if applicable."""
    if not BaseSubscriptionPriceChangeDecisionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubscriptionPriceChangeDecisionsApi.subclasses[0]().subscription_price_change_decisions_get(filter_owners_id, include, include_linkage)


@router.post(
    "/subscriptionPriceChangeDecisions",
    responses={
        201: {"model": SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": Idempotency409ResponseBody, "description": "Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["subscriptionPriceChangeDecisions"],
    summary="Create single subscriptionPriceChangeDecision.",
    response_model_by_alias=True,
)
async def subscription_price_change_decisions_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    subscription_price_change_decisions_create_operation_payload: Optional[SubscriptionPriceChangeDecisionsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument:
    """Creates a new subscriptionPriceChangeDecision."""
    if not BaseSubscriptionPriceChangeDecisionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubscriptionPriceChangeDecisionsApi.subclasses[0]().subscription_price_change_decisions_post(idempotency_key, subscription_price_change_decisions_create_operation_payload)


@router.patch(
    "/subscriptionPriceChangeDecisions/{id}",
    responses={
        200: {"model": SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": Idempotency409ResponseBody, "description": "Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["subscriptionPriceChangeDecisions"],
    summary="Update single subscriptionPriceChangeDecision.",
    response_model_by_alias=True,
)
async def subscription_price_change_decisions_id_patch(
    id: Annotated[str, Field(description="Price change decision id")] = Path(..., description="Price change decision id", examples=["1AC1yHZWFAFVjnFOn8XoXA"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    subscription_price_change_decisions_update_operation_payload: Optional[SubscriptionPriceChangeDecisionsUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument:
    """Updates existing subscriptionPriceChangeDecision."""
    if not BaseSubscriptionPriceChangeDecisionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubscriptionPriceChangeDecisionsApi.subclasses[0]().subscription_price_change_decisions_id_patch(id, idempotency_key, subscription_price_change_decisions_update_operation_payload)


@router.get(
    "/subscriptionPriceChangeDecisions/{id}/relationships/priceChange",
    responses={
        200: {"model": SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["subscriptionPriceChangeDecisions"],
    summary="Get priceChange relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def subscription_price_change_decisions_id_relationships_price_change_get(
    id: Annotated[str, Field(description="Price change decision id")] = Path(..., description="Price change decision id", examples=["1AC1yHZWFAFVjnFOn8XoXA"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: priceChange")] = Query(None, description="Include related resources. Available relationships: priceChange", alias="include", examples=["priceChange"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument:
    """Retrieves priceChange relationship."""
    if not BaseSubscriptionPriceChangeDecisionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubscriptionPriceChangeDecisionsApi.subclasses[0]().subscription_price_change_decisions_id_relationships_price_change_get(id, include)
