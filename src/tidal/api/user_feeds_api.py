# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.user_feeds_api_base import BaseUserFeedsApi
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
from tidal.models.user_feeds_single_resource_data_document import UserFeedsSingleResourceDataDocument
from tidal.models.user_feeds_update_operation_payload import UserFeedsUpdateOperationPayload
from tidal.models.user_feeds_update_single_resource_data_document import UserFeedsUpdateSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/userFeeds/{id}",
    responses={
        200: {"model": UserFeedsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userFeeds"],
    summary="Get single userFeed.",
    response_model_by_alias=True,
)
async def user_feeds_id_get(
    id: Annotated[str, Field(description="Opaque identifier of a user's feed state. Use `me` for the authenticated user's resource")] = Path(..., description="Opaque identifier of a user&#39;s feed state. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> UserFeedsSingleResourceDataDocument:
    """Retrieves single userFeed by id."""
    if not BaseUserFeedsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserFeedsApi.subclasses[0]().user_feeds_id_get(id)


@router.patch(
    "/userFeeds/{id}",
    responses={
        200: {"model": UserFeedsUpdateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["userFeeds"],
    summary="Update single userFeed.",
    response_model_by_alias=True,
)
async def user_feeds_id_patch(
    id: Annotated[str, Field(description="Opaque identifier of a user's feed state. Use `me` for the authenticated user's resource")] = Path(..., description="Opaque identifier of a user&#39;s feed state. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_feeds_update_operation_payload: Optional[UserFeedsUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> UserFeedsUpdateSingleResourceDataDocument:
    """Advances the supplied seen positions and returns the updated feed state."""
    if not BaseUserFeedsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserFeedsApi.subclasses[0]().user_feeds_id_patch(id, idempotency_key, user_feeds_update_operation_payload)
