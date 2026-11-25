# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.price_configurations_api_base import BasePriceConfigurationsApi
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
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.price_configurations_create_operation_payload import PriceConfigurationsCreateOperationPayload
from tidal.models.price_configurations_create_single_resource_data_document import PriceConfigurationsCreateSingleResourceDataDocument
from tidal.models.price_configurations_multi_resource_data_document import PriceConfigurationsMultiResourceDataDocument
from tidal.models.price_configurations_single_resource_data_document import PriceConfigurationsSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/priceConfigurations",
    responses={
        200: {"model": PriceConfigurationsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["priceConfigurations"],
    summary="Get multiple priceConfigurations.",
    response_model_by_alias=True,
)
async def price_configurations_get(
    filter_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20, description="List of price configurations IDs (e.g. `cHJpY2UtY29uZmlnLTEyMzpVUw`)")] = Query(..., description="List of price configurations IDs (e.g. &#x60;cHJpY2UtY29uZmlnLTEyMzpVUw&#x60;)", alias="filter[id]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> PriceConfigurationsMultiResourceDataDocument:
    """Retrieves multiple priceConfigurations by available filters, or without if applicable."""
    if not BasePriceConfigurationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePriceConfigurationsApi.subclasses[0]().price_configurations_get(filter_id)


@router.post(
    "/priceConfigurations",
    responses={
        201: {"model": PriceConfigurationsCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["priceConfigurations"],
    summary="Create single priceConfiguration.",
    response_model_by_alias=True,
)
async def price_configurations_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    price_configurations_create_operation_payload: Optional[PriceConfigurationsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> PriceConfigurationsCreateSingleResourceDataDocument:
    """Creates a new priceConfiguration."""
    if not BasePriceConfigurationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePriceConfigurationsApi.subclasses[0]().price_configurations_post(idempotency_key, price_configurations_create_operation_payload)


@router.get(
    "/priceConfigurations/{id}",
    responses={
        200: {"model": PriceConfigurationsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["priceConfigurations"],
    summary="Get single priceConfiguration.",
    response_model_by_alias=True,
)
async def price_configurations_id_get(
    id: Annotated[str, Field(description="Price configuration id")] = Path(..., description="Price configuration id", examples=["cHJpY2UtY29uZmlnLTEyMzpVUw"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> PriceConfigurationsSingleResourceDataDocument:
    """Retrieves single priceConfiguration by id."""
    if not BasePriceConfigurationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePriceConfigurationsApi.subclasses[0]().price_configurations_id_get(id)
