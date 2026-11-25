# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.usage_rules_api_base import BaseUsageRulesApi
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
from typing import Optional
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
from tidal.models.usage_rules_create_operation_payload import UsageRulesCreateOperationPayload
from tidal.models.usage_rules_create_resource403_response_body import UsageRulesCreateResource403ResponseBody
from tidal.models.usage_rules_create_single_resource_data_document import UsageRulesCreateSingleResourceDataDocument
from tidal.models.usage_rules_single_resource_data_document import UsageRulesSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/usageRules",
    responses={
        201: {"model": UsageRulesCreateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": UsageRulesCreateResource403ResponseBody, "description": "An active seller connection is required for paid usage rules"},
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
    tags=["usageRules"],
    summary="Create single usageRule.",
    response_model_by_alias=True,
)
async def usage_rules_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    usage_rules_create_operation_payload: Optional[UsageRulesCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> UsageRulesCreateSingleResourceDataDocument:
    """Creates a new usageRule."""
    if not BaseUsageRulesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsageRulesApi.subclasses[0]().usage_rules_post(idempotency_key, usage_rules_create_operation_payload)


@router.get(
    "/usageRules/{id}",
    responses={
        200: {"model": UsageRulesSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["usageRules"],
    summary="Get single usageRule.",
    response_model_by_alias=True,
)
async def usage_rules_id_get(
    id: Annotated[str, Field(description="Usage rules id")] = Path(..., description="Usage rules id", examples=["VFJBQ0tTOjEyMzpOTw"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> UsageRulesSingleResourceDataDocument:
    """Retrieves single usageRule by id."""
    if not BaseUsageRulesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsageRulesApi.subclasses[0]().usage_rules_id_get(id)
