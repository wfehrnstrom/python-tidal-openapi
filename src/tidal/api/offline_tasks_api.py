# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.offline_tasks_api_base import BaseOfflineTasksApi
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
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.offline_tasks_collection_single_relationship_data_document import OfflineTasksCollectionSingleRelationshipDataDocument
from tidal.models.offline_tasks_item_single_relationship_data_document import OfflineTasksItemSingleRelationshipDataDocument
from tidal.models.offline_tasks_multi_resource_data_document import OfflineTasksMultiResourceDataDocument
from tidal.models.offline_tasks_owners_multi_relationship_data_document import OfflineTasksOwnersMultiRelationshipDataDocument
from tidal.models.offline_tasks_single_resource_data_document import OfflineTasksSingleResourceDataDocument
from tidal.models.offline_tasks_update_operation_payload import OfflineTasksUpdateOperationPayload
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/offlineTasks",
    responses={
        200: {"model": OfflineTasksMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["offlineTasks"],
    summary="Get multiple offlineTasks.",
    response_model_by_alias=True,
)
async def offline_tasks_get(
    filter_installation_id: Annotated[List[str], Field(description="List of offline task IDs (e.g. `a468bee88def`)")] = Query(..., description="List of offline task IDs (e.g. &#x60;a468bee88def&#x60;)", alias="filter[installation.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: collection, item, owners")] = Query(None, description="Include related resources. Available relationships: collection, item, owners", alias="include", examples=["collection"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: collection")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: collection", alias="replaceMedia", examples=["collection"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> OfflineTasksMultiResourceDataDocument:
    """Retrieves multiple offlineTasks by available filters, or without if applicable."""
    if not BaseOfflineTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseOfflineTasksApi.subclasses[0]().offline_tasks_get(filter_installation_id, include, include_linkage, page_cursor, replace_media)


@router.get(
    "/offlineTasks/{id}",
    responses={
        200: {"model": OfflineTasksSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["offlineTasks"],
    summary="Get single offlineTask.",
    response_model_by_alias=True,
)
async def offline_tasks_id_get(
    id: Annotated[str, Field(description="Offline task id")] = Path(..., description="Offline task id", examples=["a468bee8-8def-4a1b-8c1e-123456789abc"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: collection, item, owners")] = Query(None, description="Include related resources. Available relationships: collection, item, owners", alias="include", examples=["collection"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: collection")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: collection", alias="replaceMedia", examples=["collection"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> OfflineTasksSingleResourceDataDocument:
    """Retrieves single offlineTask by id."""
    if not BaseOfflineTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseOfflineTasksApi.subclasses[0]().offline_tasks_id_get(id, include, include_linkage, replace_media)


@router.patch(
    "/offlineTasks/{id}",
    responses={
        200: {"model": MutationResponseDocument, "description": "Successful response"},
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
    tags=["offlineTasks"],
    summary="Update single offlineTask.",
    response_model_by_alias=True,
)
async def offline_tasks_id_patch(
    id: Annotated[str, Field(description="Offline task id")] = Path(..., description="Offline task id", examples=["a468bee8-8def-4a1b-8c1e-123456789abc"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    offline_tasks_update_operation_payload: Optional[OfflineTasksUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Updates existing offlineTask."""
    if not BaseOfflineTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseOfflineTasksApi.subclasses[0]().offline_tasks_id_patch(id, idempotency_key, offline_tasks_update_operation_payload)


@router.get(
    "/offlineTasks/{id}/relationships/collection",
    responses={
        200: {"model": OfflineTasksCollectionSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["offlineTasks"],
    summary="Get collection relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def offline_tasks_id_relationships_collection_get(
    id: Annotated[str, Field(description="Offline task id")] = Path(..., description="Offline task id", examples=["a468bee8-8def-4a1b-8c1e-123456789abc"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: collection")] = Query(None, description="Include related resources. Available relationships: collection", alias="include", examples=["collection"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: collection")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: collection", alias="replaceMedia", examples=["collection"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> OfflineTasksCollectionSingleRelationshipDataDocument:
    """Retrieves collection relationship."""
    if not BaseOfflineTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseOfflineTasksApi.subclasses[0]().offline_tasks_id_relationships_collection_get(id, include, replace_media)


@router.get(
    "/offlineTasks/{id}/relationships/item",
    responses={
        200: {"model": OfflineTasksItemSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["offlineTasks"],
    summary="Get item relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def offline_tasks_id_relationships_item_get(
    id: Annotated[str, Field(description="Offline task id")] = Path(..., description="Offline task id", examples=["a468bee8-8def-4a1b-8c1e-123456789abc"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: item")] = Query(None, description="Include related resources. Available relationships: item", alias="include", examples=["item"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: item")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: item", alias="replaceMedia", examples=["item"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> OfflineTasksItemSingleRelationshipDataDocument:
    """Retrieves item relationship."""
    if not BaseOfflineTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseOfflineTasksApi.subclasses[0]().offline_tasks_id_relationships_item_get(id, include, replace_media)


@router.get(
    "/offlineTasks/{id}/relationships/owners",
    responses={
        200: {"model": OfflineTasksOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["offlineTasks"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def offline_tasks_id_relationships_owners_get(
    id: Annotated[str, Field(description="Offline task id")] = Path(..., description="Offline task id", examples=["a468bee8-8def-4a1b-8c1e-123456789abc"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> OfflineTasksOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseOfflineTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseOfflineTasksApi.subclasses[0]().offline_tasks_id_relationships_owners_get(id, include, page_cursor)
