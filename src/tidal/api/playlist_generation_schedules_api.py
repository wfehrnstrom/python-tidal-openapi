# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.playlist_generation_schedules_api_base import BasePlaylistGenerationSchedulesApi
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
from tidal.models.playlist_generation_schedules_create_operation_payload import PlaylistGenerationSchedulesCreateOperationPayload
from tidal.models.playlist_generation_schedules_create_resource403_response_body import PlaylistGenerationSchedulesCreateResource403ResponseBody
from tidal.models.playlist_generation_schedules_create_single_resource_data_document import PlaylistGenerationSchedulesCreateSingleResourceDataDocument
from tidal.models.playlist_generation_schedules_multi_resource_data_document import PlaylistGenerationSchedulesMultiResourceDataDocument
from tidal.models.playlist_generation_schedules_playlist_single_relationship_data_document import PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument
from tidal.models.playlist_generation_schedules_single_resource_data_document import PlaylistGenerationSchedulesSingleResourceDataDocument
from tidal.models.playlist_generation_schedules_update_operation_payload import PlaylistGenerationSchedulesUpdateOperationPayload
from tidal.models.playlist_generation_schedules_update_single_resource_data_document import PlaylistGenerationSchedulesUpdateSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/playlistGenerationSchedules",
    responses={
        200: {"model": PlaylistGenerationSchedulesMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlistGenerationSchedules"],
    summary="Get multiple playlistGenerationSchedules.",
    response_model_by_alias=True,
)
async def playlist_generation_schedules_get(
    filter_playlist_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="Playlist id (e.g. `550e8400-e29b-41d4-a716-446655440000`)")] = Query(..., description="Playlist id (e.g. &#x60;550e8400-e29b-41d4-a716-446655440000&#x60;)", alias="filter[playlist.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: playlist")] = Query(None, description="Include related resources. Available relationships: playlist", alias="include", examples=["playlist.items"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlist.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: playlist.items", alias="replaceMedia", examples=["playlist.items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.read", "r_usr"]
    ),
) -> PlaylistGenerationSchedulesMultiResourceDataDocument:
    """Retrieves multiple playlistGenerationSchedules by available filters, or without if applicable."""
    if not BasePlaylistGenerationSchedulesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationSchedulesApi.subclasses[0]().playlist_generation_schedules_get(filter_playlist_id, include, include_linkage, replace_media)


@router.post(
    "/playlistGenerationSchedules",
    responses={
        201: {"model": PlaylistGenerationSchedulesCreateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": PlaylistGenerationSchedulesCreateResource403ResponseBody, "description": "Active playlist schedule limit reached"},
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
    tags=["playlistGenerationSchedules"],
    summary="Create single playlistGenerationSchedule.",
    response_model_by_alias=True,
)
async def playlist_generation_schedules_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    playlist_generation_schedules_create_operation_payload: Optional[PlaylistGenerationSchedulesCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> PlaylistGenerationSchedulesCreateSingleResourceDataDocument:
    """Creates a new playlistGenerationSchedule."""
    if not BasePlaylistGenerationSchedulesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationSchedulesApi.subclasses[0]().playlist_generation_schedules_post(idempotency_key, playlist_generation_schedules_create_operation_payload)


@router.get(
    "/playlistGenerationSchedules/{id}",
    responses={
        200: {"model": PlaylistGenerationSchedulesSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlistGenerationSchedules"],
    summary="Get single playlistGenerationSchedule.",
    response_model_by_alias=True,
)
async def playlist_generation_schedules_id_get(
    id: Annotated[str, Field(max_length=64)] = Path(..., description="", max_length=64),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: playlist")] = Query(None, description="Include related resources. Available relationships: playlist", alias="include", examples=["playlist.items"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlist.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: playlist.items", alias="replaceMedia", examples=["playlist.items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.read", "r_usr"]
    ),
) -> PlaylistGenerationSchedulesSingleResourceDataDocument:
    """Retrieves single playlistGenerationSchedule by id."""
    if not BasePlaylistGenerationSchedulesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationSchedulesApi.subclasses[0]().playlist_generation_schedules_id_get(id, include, include_linkage, replace_media)


@router.delete(
    "/playlistGenerationSchedules/{id}",
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
    tags=["playlistGenerationSchedules"],
    summary="Delete single playlistGenerationSchedule.",
    response_model_by_alias=True,
)
async def playlist_generation_schedules_id_delete(
    id: Annotated[str, Field(max_length=64)] = Path(..., description="", max_length=64),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing playlistGenerationSchedule."""
    if not BasePlaylistGenerationSchedulesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationSchedulesApi.subclasses[0]().playlist_generation_schedules_id_delete(id, idempotency_key)


@router.patch(
    "/playlistGenerationSchedules/{id}",
    responses={
        200: {"model": PlaylistGenerationSchedulesUpdateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["playlistGenerationSchedules"],
    summary="Update single playlistGenerationSchedule.",
    response_model_by_alias=True,
)
async def playlist_generation_schedules_id_patch(
    id: Annotated[str, Field(max_length=64)] = Path(..., description="", max_length=64),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    playlist_generation_schedules_update_operation_payload: Optional[PlaylistGenerationSchedulesUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> PlaylistGenerationSchedulesUpdateSingleResourceDataDocument:
    """Updates existing playlistGenerationSchedule."""
    if not BasePlaylistGenerationSchedulesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationSchedulesApi.subclasses[0]().playlist_generation_schedules_id_patch(id, idempotency_key, playlist_generation_schedules_update_operation_payload)


@router.get(
    "/playlistGenerationSchedules/{id}/relationships/playlist",
    responses={
        200: {"model": PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlistGenerationSchedules"],
    summary="Get playlist relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def playlist_generation_schedules_id_relationships_playlist_get(
    id: Annotated[str, Field(max_length=64)] = Path(..., description="", max_length=64),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: playlist")] = Query(None, description="Include related resources. Available relationships: playlist", alias="include", examples=["playlist.items"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlist.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: playlist.items", alias="replaceMedia", examples=["playlist.items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.read", "r_usr"]
    ),
) -> PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument:
    """Retrieves playlist relationship."""
    if not BasePlaylistGenerationSchedulesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationSchedulesApi.subclasses[0]().playlist_generation_schedules_id_relationships_playlist_get(id, include, replace_media)
