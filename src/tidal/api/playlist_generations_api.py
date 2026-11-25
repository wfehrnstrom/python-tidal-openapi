# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.playlist_generations_api_base import BasePlaylistGenerationsApi
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
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.playlist_generations_base_generation_single_relationship_data_document import PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument
from tidal.models.playlist_generations_create_operation_payload import PlaylistGenerationsCreateOperationPayload
from tidal.models.playlist_generations_create_resource409_response_body import PlaylistGenerationsCreateResource409ResponseBody
from tidal.models.playlist_generations_create_single_resource_data_document import PlaylistGenerationsCreateSingleResourceDataDocument
from tidal.models.playlist_generations_multi_resource_data_document import PlaylistGenerationsMultiResourceDataDocument
from tidal.models.playlist_generations_playlist_single_relationship_data_document import PlaylistGenerationsPlaylistSingleRelationshipDataDocument
from tidal.models.playlist_generations_single_resource_data_document import PlaylistGenerationsSingleResourceDataDocument
from tidal.models.playlist_generations_track_preferences_add_multi_data_relationship_with_response409_response_body import PlaylistGenerationsTrackPreferencesAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.playlist_generations_track_preferences_add_multi_relationship_data_document import PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocument
from tidal.models.playlist_generations_track_preferences_multi_relationship_data_document import PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument
from tidal.models.playlist_generations_track_preferences_relationship_add_operation_payload import PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload
from tidal.models.playlist_generations_track_preferences_relationship_remove_operation_payload import PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload
from tidal.models.playlist_generations_track_preferences_relationship_update_operation_payload import PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload
from tidal.models.playlist_generations_track_preferences_remove_multi_data_relationship409_response_body import PlaylistGenerationsTrackPreferencesRemoveMultiDataRelationship409ResponseBody
from tidal.models.playlist_generations_track_preferences_update_multi_data_relationship409_response_body import PlaylistGenerationsTrackPreferencesUpdateMultiDataRelationship409ResponseBody
from tidal.models.playlist_generations_track_preferences_update_multi_relationship_data_document import PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/playlistGenerations",
    responses={
        200: {"model": PlaylistGenerationsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlistGenerations"],
    summary="Get multiple playlistGenerations.",
    response_model_by_alias=True,
)
async def playlist_generations_get(
    filter_playlist_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="Playlist id (e.g. `550e8400-e29b-41d4-a716-446655440000`)")] = Query(..., description="Playlist id (e.g. &#x60;550e8400-e29b-41d4-a716-446655440000&#x60;)", alias="filter[playlist.id]"),
    generation_view: Annotated[Optional[str], Field(description="CURRENT selects the committed generation. LATEST selects the newest accepted attempt, regardless of status. New values may be added at any time.")] = Query('CURRENT', description="CURRENT selects the committed generation. LATEST selects the newest accepted attempt, regardless of status. New values may be added at any time.", alias="generationView"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: baseGeneration, playlist, trackPreferences")] = Query(None, description="Include related resources. Available relationships: baseGeneration, playlist, trackPreferences", alias="include", examples=["baseGeneration.trackPreferences"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: baseGeneration.trackPreferences")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: baseGeneration.trackPreferences", alias="replaceMedia", examples=["baseGeneration.trackPreferences"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.read", "r_usr"]
    ),
) -> PlaylistGenerationsMultiResourceDataDocument:
    """Retrieves multiple playlistGenerations by available filters, or without if applicable."""
    if not BasePlaylistGenerationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationsApi.subclasses[0]().playlist_generations_get(filter_playlist_id, generation_view, include, include_linkage, replace_media)


@router.post(
    "/playlistGenerations",
    responses={
        201: {"model": PlaylistGenerationsCreateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": PlaylistGenerationsCreateResource409ResponseBody, "description": "The playlist state conflicts with the request: the preference version or base generation is stale, or the track preference selected for update does not exist. Refresh the current generation and track preferences before retrying.; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlistGenerations"],
    summary="Create single playlistGeneration.",
    response_model_by_alias=True,
)
async def playlist_generations_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    playlist_generations_create_operation_payload: Optional[PlaylistGenerationsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> PlaylistGenerationsCreateSingleResourceDataDocument:
    """Creates a new playlistGeneration."""
    if not BasePlaylistGenerationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationsApi.subclasses[0]().playlist_generations_post(idempotency_key, playlist_generations_create_operation_payload)


@router.get(
    "/playlistGenerations/{id}",
    responses={
        200: {"model": PlaylistGenerationsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlistGenerations"],
    summary="Get single playlistGeneration.",
    response_model_by_alias=True,
)
async def playlist_generations_id_get(
    id: Annotated[str, Field(max_length=64, description="Playlist generation id")] = Path(..., description="Playlist generation id", max_length=64, examples=["10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: baseGeneration, playlist, trackPreferences")] = Query(None, description="Include related resources. Available relationships: baseGeneration, playlist, trackPreferences", alias="include", examples=["baseGeneration.trackPreferences"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: baseGeneration.trackPreferences")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: baseGeneration.trackPreferences", alias="replaceMedia", examples=["baseGeneration.trackPreferences"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.read", "r_usr"]
    ),
) -> PlaylistGenerationsSingleResourceDataDocument:
    """Retrieves single playlistGeneration by id."""
    if not BasePlaylistGenerationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationsApi.subclasses[0]().playlist_generations_id_get(id, include, include_linkage, replace_media)


@router.get(
    "/playlistGenerations/{id}/relationships/baseGeneration",
    responses={
        200: {"model": PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlistGenerations"],
    summary="Get baseGeneration relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def playlist_generations_id_relationships_base_generation_get(
    id: Annotated[str, Field(max_length=64, description="Playlist generation id")] = Path(..., description="Playlist generation id", max_length=64, examples=["10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: baseGeneration")] = Query(None, description="Include related resources. Available relationships: baseGeneration", alias="include", examples=["baseGeneration.trackPreferences"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: baseGeneration.trackPreferences")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: baseGeneration.trackPreferences", alias="replaceMedia", examples=["baseGeneration.trackPreferences"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.read", "r_usr"]
    ),
) -> PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument:
    """Retrieves baseGeneration relationship."""
    if not BasePlaylistGenerationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationsApi.subclasses[0]().playlist_generations_id_relationships_base_generation_get(id, include, replace_media)


@router.get(
    "/playlistGenerations/{id}/relationships/playlist",
    responses={
        200: {"model": PlaylistGenerationsPlaylistSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlistGenerations"],
    summary="Get playlist relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def playlist_generations_id_relationships_playlist_get(
    id: Annotated[str, Field(max_length=64, description="Playlist generation id")] = Path(..., description="Playlist generation id", max_length=64, examples=["10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: playlist")] = Query(None, description="Include related resources. Available relationships: playlist", alias="include", examples=["playlist.items"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlist.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: playlist.items", alias="replaceMedia", examples=["playlist.items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.read", "r_usr"]
    ),
) -> PlaylistGenerationsPlaylistSingleRelationshipDataDocument:
    """Retrieves playlist relationship."""
    if not BasePlaylistGenerationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationsApi.subclasses[0]().playlist_generations_id_relationships_playlist_get(id, include, replace_media)


@router.get(
    "/playlistGenerations/{id}/relationships/trackPreferences",
    responses={
        200: {"model": PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlistGenerations"],
    summary="Get trackPreferences relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlist_generations_id_relationships_track_preferences_get(
    id: Annotated[str, Field(max_length=64, description="Playlist generation id")] = Path(..., description="Playlist generation id", max_length=64, examples=["10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: trackPreferences")] = Query(None, description="Include related resources. Available relationships: trackPreferences", alias="include", examples=["trackPreferences"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: trackPreferences")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: trackPreferences", alias="replaceMedia", examples=["trackPreferences"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.read", "r_usr"]
    ),
) -> PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument:
    """Retrieves trackPreferences relationship."""
    if not BasePlaylistGenerationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationsApi.subclasses[0]().playlist_generations_id_relationships_track_preferences_get(id, include, page_cursor, replace_media)


@router.post(
    "/playlistGenerations/{id}/relationships/trackPreferences",
    responses={
        200: {"model": PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": PlaylistGenerationsTrackPreferencesAddMultiDataRelationshipWithResponse409ResponseBody, "description": "The playlist state conflicts with the request: the preference version or base generation is stale, or the track preference selected for update does not exist. Refresh the current generation and track preferences before retrying.; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlistGenerations"],
    summary="Add to trackPreferences relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlist_generations_id_relationships_track_preferences_post(
    id: Annotated[str, Field(max_length=64, description="Playlist generation id")] = Path(..., description="Playlist generation id", max_length=64, examples=["10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    playlist_generations_track_preferences_relationship_add_operation_payload: Optional[PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocument:
    """Adds feedback for one track. An existing entry is unchanged, including its preference. Returns the complete preference snapshot. All writes require the current meta.preferenceVersion as meta.expectedPreferenceVersion; stale versions return 409."""
    if not BasePlaylistGenerationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationsApi.subclasses[0]().playlist_generations_id_relationships_track_preferences_post(id, idempotency_key, playlist_generations_track_preferences_relationship_add_operation_payload)


@router.delete(
    "/playlistGenerations/{id}/relationships/trackPreferences",
    responses={
        200: {"model": MutationResponseDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": PlaylistGenerationsTrackPreferencesRemoveMultiDataRelationship409ResponseBody, "description": "The playlist state conflicts with the request: the preference version or base generation is stale, or the track preference selected for update does not exist. Refresh the current generation and track preferences before retrying.; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlistGenerations"],
    summary="Delete from trackPreferences relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlist_generations_id_relationships_track_preferences_delete(
    id: Annotated[str, Field(max_length=64, description="Playlist generation id")] = Path(..., description="Playlist generation id", max_length=64, examples=["10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    playlist_generations_track_preferences_relationship_remove_operation_payload: Optional[PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Removes feedback for one track without removing the track from the playlist. An absent entry is unchanged. Returns an acknowledgement; read the relationship again for its current preference version. Requires the current meta.preferenceVersion as meta.expectedPreferenceVersion; stale versions return 409."""
    if not BasePlaylistGenerationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationsApi.subclasses[0]().playlist_generations_id_relationships_track_preferences_delete(id, idempotency_key, playlist_generations_track_preferences_relationship_remove_operation_payload)


@router.patch(
    "/playlistGenerations/{id}/relationships/trackPreferences",
    responses={
        200: {"model": PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": PlaylistGenerationsTrackPreferencesUpdateMultiDataRelationship409ResponseBody, "description": "The playlist state conflicts with the request: the preference version or base generation is stale, or the track preference selected for update does not exist. Refresh the current generation and track preferences before retrying.; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlistGenerations"],
    summary="Update trackPreferences relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlist_generations_id_relationships_track_preferences_patch(
    id: Annotated[str, Field(max_length=64, description="Playlist generation id")] = Path(..., description="Playlist generation id", max_length=64, examples=["10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    playlist_generations_track_preferences_relationship_update_operation_payload: Optional[PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocument:
    """Incrementally updates feedback for one existing track preference, leaving other entries unchanged. Empty data is rejected; a missing entry returns 409. Returns the complete preference snapshot. Requires the current meta.preferenceVersion as meta.expectedPreferenceVersion; stale versions return 409."""
    if not BasePlaylistGenerationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistGenerationsApi.subclasses[0]().playlist_generations_id_relationships_track_preferences_patch(id, idempotency_key, playlist_generations_track_preferences_relationship_update_operation_payload)
