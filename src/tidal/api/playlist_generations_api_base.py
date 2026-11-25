# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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
from tidal.security_api import get_token_Authorization_Code_PKCE

class BasePlaylistGenerationsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePlaylistGenerationsApi.subclasses = BasePlaylistGenerationsApi.subclasses + (cls,)
    async def playlist_generations_get(
        self,
        filter_playlist_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="Playlist id (e.g. `550e8400-e29b-41d4-a716-446655440000`)")],
        generation_view: Annotated[Optional[str], Field(description="CURRENT selects the committed generation. LATEST selects the newest accepted attempt, regardless of status. New values may be added at any time.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: baseGeneration, playlist, trackPreferences")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: baseGeneration.trackPreferences")],
    ) -> PlaylistGenerationsMultiResourceDataDocument:
        """Retrieves multiple playlistGenerations by available filters, or without if applicable."""
        ...


    async def playlist_generations_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        playlist_generations_create_operation_payload: Optional[PlaylistGenerationsCreateOperationPayload],
    ) -> PlaylistGenerationsCreateSingleResourceDataDocument:
        """Creates a new playlistGeneration."""
        ...


    async def playlist_generations_id_get(
        self,
        id: Annotated[str, Field(max_length=64, description="Playlist generation id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: baseGeneration, playlist, trackPreferences")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: baseGeneration.trackPreferences")],
    ) -> PlaylistGenerationsSingleResourceDataDocument:
        """Retrieves single playlistGeneration by id."""
        ...


    async def playlist_generations_id_relationships_base_generation_get(
        self,
        id: Annotated[str, Field(max_length=64, description="Playlist generation id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: baseGeneration")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: baseGeneration.trackPreferences")],
    ) -> PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument:
        """Retrieves baseGeneration relationship."""
        ...


    async def playlist_generations_id_relationships_playlist_get(
        self,
        id: Annotated[str, Field(max_length=64, description="Playlist generation id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: playlist")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlist.items")],
    ) -> PlaylistGenerationsPlaylistSingleRelationshipDataDocument:
        """Retrieves playlist relationship."""
        ...


    async def playlist_generations_id_relationships_track_preferences_get(
        self,
        id: Annotated[str, Field(max_length=64, description="Playlist generation id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: trackPreferences")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: trackPreferences")],
    ) -> PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument:
        """Retrieves trackPreferences relationship."""
        ...


    async def playlist_generations_id_relationships_track_preferences_post(
        self,
        id: Annotated[str, Field(max_length=64, description="Playlist generation id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        playlist_generations_track_preferences_relationship_add_operation_payload: Optional[PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload],
    ) -> PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocument:
        """Adds feedback for one track. An existing entry is unchanged, including its preference. Returns the complete preference snapshot. All writes require the current meta.preferenceVersion as meta.expectedPreferenceVersion; stale versions return 409."""
        ...


    async def playlist_generations_id_relationships_track_preferences_delete(
        self,
        id: Annotated[str, Field(max_length=64, description="Playlist generation id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        playlist_generations_track_preferences_relationship_remove_operation_payload: Optional[PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload],
    ) -> MutationResponseDocument:
        """Removes feedback for one track without removing the track from the playlist. An absent entry is unchanged. Returns an acknowledgement; read the relationship again for its current preference version. Requires the current meta.preferenceVersion as meta.expectedPreferenceVersion; stale versions return 409."""
        ...


    async def playlist_generations_id_relationships_track_preferences_patch(
        self,
        id: Annotated[str, Field(max_length=64, description="Playlist generation id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        playlist_generations_track_preferences_relationship_update_operation_payload: Optional[PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload],
    ) -> PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocument:
        """Incrementally updates feedback for one existing track preference, leaving other entries unchanged. Empty data is rejected; a missing entry returns 409. Returns the complete preference snapshot. Requires the current meta.preferenceVersion as meta.expectedPreferenceVersion; stale versions return 409."""
        ...
