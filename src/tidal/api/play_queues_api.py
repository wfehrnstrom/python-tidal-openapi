# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.play_queues_api_base import BasePlayQueuesApi
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
from tidal.models.play_queues_change_event_stream_single_relationship_data_document import PlayQueuesChangeEventStreamSingleRelationshipDataDocument
from tidal.models.play_queues_create_operation_payload import PlayQueuesCreateOperationPayload
from tidal.models.play_queues_create_single_resource_data_document import PlayQueuesCreateSingleResourceDataDocument
from tidal.models.play_queues_current_relationship_update_operation_payload import PlayQueuesCurrentRelationshipUpdateOperationPayload
from tidal.models.play_queues_current_single_relationship_data_document import PlayQueuesCurrentSingleRelationshipDataDocument
from tidal.models.play_queues_current_update_single_relationship_data_document import PlayQueuesCurrentUpdateSingleRelationshipDataDocument
from tidal.models.play_queues_future_add_multi_relationship_data_document import PlayQueuesFutureAddMultiRelationshipDataDocument
from tidal.models.play_queues_future_multi_relationship_data_document import PlayQueuesFutureMultiRelationshipDataDocument
from tidal.models.play_queues_future_relationship_add_operation_payload import PlayQueuesFutureRelationshipAddOperationPayload
from tidal.models.play_queues_future_relationship_remove_operation_payload import PlayQueuesFutureRelationshipRemoveOperationPayload
from tidal.models.play_queues_future_relationship_update_operation_payload import PlayQueuesFutureRelationshipUpdateOperationPayload
from tidal.models.play_queues_future_update_multi_relationship_data_document import PlayQueuesFutureUpdateMultiRelationshipDataDocument
from tidal.models.play_queues_multi_resource_data_document import PlayQueuesMultiResourceDataDocument
from tidal.models.play_queues_owners_multi_relationship_data_document import PlayQueuesOwnersMultiRelationshipDataDocument
from tidal.models.play_queues_past_multi_relationship_data_document import PlayQueuesPastMultiRelationshipDataDocument
from tidal.models.play_queues_single_resource_data_document import PlayQueuesSingleResourceDataDocument
from tidal.models.play_queues_update_operation_payload import PlayQueuesUpdateOperationPayload
from tidal.models.play_queues_update_single_resource_data_document import PlayQueuesUpdateSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/playQueues",
    responses={
        200: {"model": PlayQueuesMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playQueues"],
    summary="Get multiple playQueues.",
    response_model_by_alias=True,
)
async def play_queues_get(
    filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="User id. Also accepts `me`.")] = Query(..., description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: changeEventStream, current, future, owners, past")] = Query(None, description="Include related resources. Available relationships: changeEventStream, current, future, owners, past", alias="include", examples=["current"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: current")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: current", alias="replaceMedia", examples=["current"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> PlayQueuesMultiResourceDataDocument:
    """Retrieves multiple playQueues by available filters, or without if applicable."""
    if not BasePlayQueuesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlayQueuesApi.subclasses[0]().play_queues_get(filter_owners_id, include, include_linkage, page_cursor, replace_media)


@router.post(
    "/playQueues",
    responses={
        201: {"model": PlayQueuesCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["playQueues"],
    summary="Create single playQueue.",
    response_model_by_alias=True,
)
async def play_queues_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    play_queues_create_operation_payload: Optional[PlayQueuesCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> PlayQueuesCreateSingleResourceDataDocument:
    """Creates a new playQueue."""
    if not BasePlayQueuesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlayQueuesApi.subclasses[0]().play_queues_post(idempotency_key, play_queues_create_operation_payload)


@router.get(
    "/playQueues/{id}",
    responses={
        200: {"model": PlayQueuesSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playQueues"],
    summary="Get single playQueue.",
    response_model_by_alias=True,
)
async def play_queues_id_get(
    id: Annotated[str, Field(description="Play queue id")] = Path(..., description="Play queue id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: changeEventStream, current, future, owners, past")] = Query(None, description="Include related resources. Available relationships: changeEventStream, current, future, owners, past", alias="include", examples=["current"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: current")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: current", alias="replaceMedia", examples=["current"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> PlayQueuesSingleResourceDataDocument:
    """Retrieves single playQueue by id."""
    if not BasePlayQueuesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlayQueuesApi.subclasses[0]().play_queues_id_get(id, include, include_linkage, replace_media)


@router.delete(
    "/playQueues/{id}",
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
    tags=["playQueues"],
    summary="Delete single playQueue.",
    response_model_by_alias=True,
)
async def play_queues_id_delete(
    id: Annotated[str, Field(description="Play queue id")] = Path(..., description="Play queue id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing playQueue."""
    if not BasePlayQueuesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlayQueuesApi.subclasses[0]().play_queues_id_delete(id, idempotency_key)


@router.patch(
    "/playQueues/{id}",
    responses={
        200: {"model": PlayQueuesUpdateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["playQueues"],
    summary="Update single playQueue.",
    response_model_by_alias=True,
)
async def play_queues_id_patch(
    id: Annotated[str, Field(description="Play queue id")] = Path(..., description="Play queue id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    play_queues_update_operation_payload: Optional[PlayQueuesUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> PlayQueuesUpdateSingleResourceDataDocument:
    """Atomically applies attributes, future items, then current selection."""
    if not BasePlayQueuesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlayQueuesApi.subclasses[0]().play_queues_id_patch(id, idempotency_key, play_queues_update_operation_payload)


@router.get(
    "/playQueues/{id}/relationships/changeEventStream",
    responses={
        200: {"model": PlayQueuesChangeEventStreamSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playQueues"],
    summary="Get changeEventStream relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def play_queues_id_relationships_change_event_stream_get(
    id: str = Path(..., description=""),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: changeEventStream")] = Query(None, description="Include related resources. Available relationships: changeEventStream", alias="include", examples=["changeEventStream"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> PlayQueuesChangeEventStreamSingleRelationshipDataDocument:
    """Retrieves changeEventStream relationship."""
    if not BasePlayQueuesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlayQueuesApi.subclasses[0]().play_queues_id_relationships_change_event_stream_get(id, include)


@router.get(
    "/playQueues/{id}/relationships/current",
    responses={
        200: {"model": PlayQueuesCurrentSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playQueues"],
    summary="Get current relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def play_queues_id_relationships_current_get(
    id: Annotated[str, Field(description="Play queue id")] = Path(..., description="Play queue id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: current")] = Query(None, description="Include related resources. Available relationships: current", alias="include", examples=["current"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: current")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: current", alias="replaceMedia", examples=["current"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> PlayQueuesCurrentSingleRelationshipDataDocument:
    """Retrieves current relationship."""
    if not BasePlayQueuesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlayQueuesApi.subclasses[0]().play_queues_id_relationships_current_get(id, include, replace_media)


@router.patch(
    "/playQueues/{id}/relationships/current",
    responses={
        200: {"model": PlayQueuesCurrentUpdateSingleRelationshipDataDocument, "description": "Successful response"},
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
    tags=["playQueues"],
    summary="Update current relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def play_queues_id_relationships_current_patch(
    id: Annotated[str, Field(description="Play queue id")] = Path(..., description="Play queue id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    play_queues_current_relationship_update_operation_payload: Optional[PlayQueuesCurrentRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> PlayQueuesCurrentUpdateSingleRelationshipDataDocument:
    """Sets the current item to the existing queue occurrence identified by data.meta.itemId, changing which entries are past and future. Null data is rejected. Optional position and updatedByInstallationId must be supplied together. Returns the current item linkage and queue revision."""
    if not BasePlayQueuesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlayQueuesApi.subclasses[0]().play_queues_id_relationships_current_patch(id, idempotency_key, play_queues_current_relationship_update_operation_payload)


@router.get(
    "/playQueues/{id}/relationships/future",
    responses={
        200: {"model": PlayQueuesFutureMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playQueues"],
    summary="Get future relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def play_queues_id_relationships_future_get(
    id: Annotated[str, Field(description="Play queue id")] = Path(..., description="Play queue id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: future")] = Query(None, description="Include related resources. Available relationships: future", alias="include", examples=["future"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: future")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: future", alias="replaceMedia", examples=["future"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> PlayQueuesFutureMultiRelationshipDataDocument:
    """Retrieves future relationship."""
    if not BasePlayQueuesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlayQueuesApi.subclasses[0]().play_queues_id_relationships_future_get(id, include, page_cursor, replace_media)


@router.post(
    "/playQueues/{id}/relationships/future",
    responses={
        200: {"model": PlayQueuesFutureAddMultiRelationshipDataDocument, "description": "Successful response"},
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
    tags=["playQueues"],
    summary="Add to future relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def play_queues_id_relationships_future_post(
    id: Annotated[str, Field(description="Play queue id")] = Path(..., description="Play queue id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    play_queues_future_relationship_add_operation_payload: Optional[PlayQueuesFutureRelationshipAddOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> PlayQueuesFutureAddMultiRelationshipDataDocument:
    """Omitting top-level meta or setting it to null defaults to REPLACE_ALL, replacing future entries. Use ADD_TO_FRONT, ADD_TO_BACK or ADD_BEFORE in meta.mode to add without replacing existing entries. ADD_BEFORE requires meta.positionBefore. REPLACE_ALL_AND_CURRENT replaces future entries; ADD_TO_FRONT_REPLACE_CURRENT prepends entries. Both select the first newly inserted entry in the active queue order as current, which may differ from request order when shuffled. With empty data and no source, replacement modes clear future entries; the current entry is unchanged when no entries are inserted. With meta.source, startIndex selects an entry in the first page&#39;s data before unsupported types are skipped. Tracks and videos are added in page order, retaining duplicates; other types are skipped without expansion. Reaching 1000 added items or 100 pages queues the collected prefix. Invalid sources or indexes, a suffix with no playable items, repeated pages, and read failures encountered before a cap leave the queue unchanged. Returns empty data and meta.revision as an acknowledgement."""
    if not BasePlayQueuesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlayQueuesApi.subclasses[0]().play_queues_id_relationships_future_post(id, idempotency_key, play_queues_future_relationship_add_operation_payload)


@router.delete(
    "/playQueues/{id}/relationships/future",
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
    tags=["playQueues"],
    summary="Delete from future relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def play_queues_id_relationships_future_delete(
    id: Annotated[str, Field(description="Play queue id")] = Path(..., description="Play queue id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    play_queues_future_relationship_remove_operation_payload: Optional[PlayQueuesFutureRelationshipRemoveOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Removes the future occurrences selected by data[].meta.itemId without deleting their tracks or videos. Other queue entries are preserved. Returns an acknowledgement."""
    if not BasePlayQueuesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlayQueuesApi.subclasses[0]().play_queues_id_relationships_future_delete(id, idempotency_key, play_queues_future_relationship_remove_operation_payload)


@router.patch(
    "/playQueues/{id}/relationships/future",
    responses={
        200: {"model": PlayQueuesFutureUpdateMultiRelationshipDataDocument, "description": "Successful response"},
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
    tags=["playQueues"],
    summary="Update future relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def play_queues_id_relationships_future_patch(
    id: Annotated[str, Field(description="Play queue id")] = Path(..., description="Play queue id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    play_queues_future_relationship_update_operation_payload: Optional[PlayQueuesFutureRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> PlayQueuesFutureUpdateMultiRelationshipDataDocument:
    """Incrementally moves existing future occurrences selected by data[].meta.itemId, in their current queue order, before meta.positionBefore. Preserves memberships and unselected entries&#39; metadata and relative order. Empty data is rejected. Returns empty data and meta.revision as an acknowledgement."""
    if not BasePlayQueuesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlayQueuesApi.subclasses[0]().play_queues_id_relationships_future_patch(id, idempotency_key, play_queues_future_relationship_update_operation_payload)


@router.get(
    "/playQueues/{id}/relationships/owners",
    responses={
        200: {"model": PlayQueuesOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playQueues"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def play_queues_id_relationships_owners_get(
    id: Annotated[str, Field(description="Play queue id")] = Path(..., description="Play queue id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> PlayQueuesOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BasePlayQueuesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlayQueuesApi.subclasses[0]().play_queues_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/playQueues/{id}/relationships/past",
    responses={
        200: {"model": PlayQueuesPastMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playQueues"],
    summary="Get past relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def play_queues_id_relationships_past_get(
    id: Annotated[str, Field(description="Play queue id")] = Path(..., description="Play queue id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: past")] = Query(None, description="Include related resources. Available relationships: past", alias="include", examples=["past"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: past")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: past", alias="replaceMedia", examples=["past"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> PlayQueuesPastMultiRelationshipDataDocument:
    """Retrieves past relationship."""
    if not BasePlayQueuesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlayQueuesApi.subclasses[0]().play_queues_id_relationships_past_get(id, include, page_cursor, replace_media)
