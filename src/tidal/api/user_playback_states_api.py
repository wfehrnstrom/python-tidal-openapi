# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.user_playback_states_api_base import BaseUserPlaybackStatesApi
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
from tidal.models.user_playback_states_active_player_relationship_update_operation_payload import UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload
from tidal.models.user_playback_states_active_player_single_relationship_data_document import UserPlaybackStatesActivePlayerSingleRelationshipDataDocument
from tidal.models.user_playback_states_active_player_update_single_relationship_data_document import UserPlaybackStatesActivePlayerUpdateSingleRelationshipDataDocument
from tidal.models.user_playback_states_available_players_add_multi_relationship_data_document import UserPlaybackStatesAvailablePlayersAddMultiRelationshipDataDocument
from tidal.models.user_playback_states_available_players_multi_relationship_data_document import UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument
from tidal.models.user_playback_states_available_players_relationship_add_operation_payload import UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload
from tidal.models.user_playback_states_available_players_relationship_remove_operation_payload import UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload
from tidal.models.user_playback_states_change_event_stream_single_relationship_data_document import UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument
from tidal.models.user_playback_states_play_queue_relationship_update_operation_payload import UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload
from tidal.models.user_playback_states_play_queue_single_relationship_data_document import UserPlaybackStatesPlayQueueSingleRelationshipDataDocument
from tidal.models.user_playback_states_play_queue_update_single_relationship_data_document import UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument
from tidal.models.user_playback_states_single_resource_data_document import UserPlaybackStatesSingleResourceDataDocument
from tidal.models.user_playback_states_update_operation_payload import UserPlaybackStatesUpdateOperationPayload
from tidal.models.user_playback_states_update_single_resource_data_document import UserPlaybackStatesUpdateSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/userPlaybackStates/{id}",
    responses={
        200: {"model": UserPlaybackStatesSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userPlaybackStates"],
    summary="Get single userPlaybackState.",
    response_model_by_alias=True,
)
async def user_playback_states_id_get(
    id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")] = Path(..., description="User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: activePlayer, availablePlayers, changeEventStream, playQueue")] = Query(None, description="Include related resources. Available relationships: activePlayer, availablePlayers, changeEventStream, playQueue", alias="include", examples=["activePlayer.offlineInventory"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: activePlayer.offlineInventory")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: activePlayer.offlineInventory", alias="replaceMedia", examples=["activePlayer.offlineInventory"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> UserPlaybackStatesSingleResourceDataDocument:
    """Retrieves single userPlaybackState by id."""
    if not BaseUserPlaybackStatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserPlaybackStatesApi.subclasses[0]().user_playback_states_id_get(id, include, include_linkage, replace_media)


@router.patch(
    "/userPlaybackStates/{id}",
    responses={
        200: {"model": UserPlaybackStatesUpdateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["userPlaybackStates"],
    summary="Update single userPlaybackState.",
    response_model_by_alias=True,
)
async def user_playback_states_id_patch(
    id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")] = Path(..., description="User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_playback_states_update_operation_payload: Optional[UserPlaybackStatesUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> UserPlaybackStatesUpdateSingleResourceDataDocument:
    """Updates existing userPlaybackState."""
    if not BaseUserPlaybackStatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserPlaybackStatesApi.subclasses[0]().user_playback_states_id_patch(id, idempotency_key, user_playback_states_update_operation_payload)


@router.get(
    "/userPlaybackStates/{id}/relationships/activePlayer",
    responses={
        200: {"model": UserPlaybackStatesActivePlayerSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userPlaybackStates"],
    summary="Get activePlayer relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def user_playback_states_id_relationships_active_player_get(
    id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")] = Path(..., description="User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: activePlayer")] = Query(None, description="Include related resources. Available relationships: activePlayer", alias="include", examples=["activePlayer.offlineInventory"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: activePlayer.offlineInventory")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: activePlayer.offlineInventory", alias="replaceMedia", examples=["activePlayer.offlineInventory"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> UserPlaybackStatesActivePlayerSingleRelationshipDataDocument:
    """Retrieves activePlayer relationship."""
    if not BaseUserPlaybackStatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserPlaybackStatesApi.subclasses[0]().user_playback_states_id_relationships_active_player_get(id, include, replace_media)


@router.patch(
    "/userPlaybackStates/{id}/relationships/activePlayer",
    responses={
        200: {"model": UserPlaybackStatesActivePlayerUpdateSingleRelationshipDataDocument, "description": "Successful response"},
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
    tags=["userPlaybackStates"],
    summary="Update activePlayer relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def user_playback_states_id_relationships_active_player_patch(
    id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")] = Path(..., description="User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_playback_states_active_player_relationship_update_operation_payload: Optional[UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> UserPlaybackStatesActivePlayerUpdateSingleRelationshipDataDocument:
    """Replaces the active-player selection with the supplied owned installation. Explicit null data releases the player without deleting the installation. Returns null linkage when released or when the selected installation has no live attachment. An unavailable selection is retained and becomes visible again when its attachment is refreshed."""
    if not BaseUserPlaybackStatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserPlaybackStatesApi.subclasses[0]().user_playback_states_id_relationships_active_player_patch(id, idempotency_key, user_playback_states_active_player_relationship_update_operation_payload)


@router.get(
    "/userPlaybackStates/{id}/relationships/availablePlayers",
    responses={
        200: {"model": UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userPlaybackStates"],
    summary="Get availablePlayers relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_playback_states_id_relationships_available_players_get(
    id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")] = Path(..., description="User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: availablePlayers")] = Query(None, description="Include related resources. Available relationships: availablePlayers", alias="include", examples=["availablePlayers.offlineInventory"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: availablePlayers.offlineInventory")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: availablePlayers.offlineInventory", alias="replaceMedia", examples=["availablePlayers.offlineInventory"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument:
    """Retrieves availablePlayers relationship."""
    if not BaseUserPlaybackStatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserPlaybackStatesApi.subclasses[0]().user_playback_states_id_relationships_available_players_get(id, include, page_cursor, replace_media)


@router.post(
    "/userPlaybackStates/{id}/relationships/availablePlayers",
    responses={
        200: {"model": UserPlaybackStatesAvailablePlayersAddMultiRelationshipDataDocument, "description": "Successful response"},
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
    tags=["userPlaybackStates"],
    summary="Add to availablePlayers relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_playback_states_id_relationships_available_players_post(
    id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")] = Path(..., description="User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_playback_states_available_players_relationship_add_operation_payload: Optional[UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> UserPlaybackStatesAvailablePlayersAddMultiRelationshipDataDocument:
    """Attaches or refreshes one owned installation as an available player, preserving other attachments. Returns all currently available player linkage."""
    if not BaseUserPlaybackStatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserPlaybackStatesApi.subclasses[0]().user_playback_states_id_relationships_available_players_post(id, idempotency_key, user_playback_states_available_players_relationship_add_operation_payload)


@router.delete(
    "/userPlaybackStates/{id}/relationships/availablePlayers",
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
    tags=["userPlaybackStates"],
    summary="Delete from availablePlayers relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_playback_states_id_relationships_available_players_delete(
    id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")] = Path(..., description="User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_playback_states_available_players_relationship_remove_operation_payload: Optional[UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Detaches one installation without deleting it. Also releases the active player when it is that installation. Returns an acknowledgement."""
    if not BaseUserPlaybackStatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserPlaybackStatesApi.subclasses[0]().user_playback_states_id_relationships_available_players_delete(id, idempotency_key, user_playback_states_available_players_relationship_remove_operation_payload)


@router.get(
    "/userPlaybackStates/{id}/relationships/changeEventStream",
    responses={
        200: {"model": UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userPlaybackStates"],
    summary="Get changeEventStream relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def user_playback_states_id_relationships_change_event_stream_get(
    id: str = Path(..., description=""),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: changeEventStream")] = Query(None, description="Include related resources. Available relationships: changeEventStream", alias="include", examples=["changeEventStream"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument:
    """Retrieves changeEventStream relationship."""
    if not BaseUserPlaybackStatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserPlaybackStatesApi.subclasses[0]().user_playback_states_id_relationships_change_event_stream_get(id, include)


@router.get(
    "/userPlaybackStates/{id}/relationships/playQueue",
    responses={
        200: {"model": UserPlaybackStatesPlayQueueSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userPlaybackStates"],
    summary="Get playQueue relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def user_playback_states_id_relationships_play_queue_get(
    id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")] = Path(..., description="User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: playQueue")] = Query(None, description="Include related resources. Available relationships: playQueue", alias="include", examples=["playQueue.current"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playQueue.current")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: playQueue.current", alias="replaceMedia", examples=["playQueue.current"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> UserPlaybackStatesPlayQueueSingleRelationshipDataDocument:
    """Retrieves playQueue relationship."""
    if not BaseUserPlaybackStatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserPlaybackStatesApi.subclasses[0]().user_playback_states_id_relationships_play_queue_get(id, include, replace_media)


@router.patch(
    "/userPlaybackStates/{id}/relationships/playQueue",
    responses={
        200: {"model": UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument, "description": "Successful response"},
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
    tags=["userPlaybackStates"],
    summary="Update playQueue relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def user_playback_states_id_relationships_play_queue_patch(
    id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")] = Path(..., description="User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_playback_states_play_queue_relationship_update_operation_payload: Optional[UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument:
    """Replaces the selected play queue. Explicit null data clears the selection without deleting the queue. Returns the selected queue linkage, or null data when cleared."""
    if not BaseUserPlaybackStatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserPlaybackStatesApi.subclasses[0]().user_playback_states_id_relationships_play_queue_patch(id, idempotency_key, user_playback_states_play_queue_relationship_update_operation_payload)
