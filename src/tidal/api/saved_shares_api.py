# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.saved_shares_api_base import BaseSavedSharesApi
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
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.saved_shares_create_operation_payload import SavedSharesCreateOperationPayload
from tidal.models.saved_shares_create_resource403_response_body import SavedSharesCreateResource403ResponseBody
from tidal.models.saved_shares_create_resource429_response_body import SavedSharesCreateResource429ResponseBody
from tidal.models.saved_shares_create_single_resource_data_document import SavedSharesCreateSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/savedShares",
    responses={
        201: {"model": SavedSharesCreateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SavedSharesCreateResource403ResponseBody, "description": "This share does not permit redemption; This share can no longer be accepted; The share is password protected; send its password; The share password is incorrect"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": Idempotency409ResponseBody, "description": "Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": SavedSharesCreateResource429ResponseBody, "description": "Too many share password attempts; try again later"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["savedShares"],
    summary="Create single savedShare.",
    response_model_by_alias=True,
)
async def saved_shares_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    saved_shares_create_operation_payload: Optional[SavedSharesCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> SavedSharesCreateSingleResourceDataDocument:
    """Redeem an active share with VOUCHER access mode for its offered role. A share without VOUCHER mode returns 403. Every save, repeated ones included, needs a password-protected share&#39;s password and counts as a use of a limited share; password attempts are rate limited. Deprecated for playlist shares: use &#x60;POST /resourceGrants&#x60; with an &#x60;invitation&#x60; relationship instead."""
    if not BaseSavedSharesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSavedSharesApi.subclasses[0]().saved_shares_post(idempotency_key, saved_shares_create_operation_payload)
