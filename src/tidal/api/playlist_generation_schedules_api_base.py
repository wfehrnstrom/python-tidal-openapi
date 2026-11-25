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
from tidal.security_api import get_token_Authorization_Code_PKCE

class BasePlaylistGenerationSchedulesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePlaylistGenerationSchedulesApi.subclasses = BasePlaylistGenerationSchedulesApi.subclasses + (cls,)
    async def playlist_generation_schedules_get(
        self,
        filter_playlist_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="Playlist id (e.g. `550e8400-e29b-41d4-a716-446655440000`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: playlist")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlist.items")],
    ) -> PlaylistGenerationSchedulesMultiResourceDataDocument:
        """Retrieves multiple playlistGenerationSchedules by available filters, or without if applicable."""
        ...


    async def playlist_generation_schedules_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        playlist_generation_schedules_create_operation_payload: Optional[PlaylistGenerationSchedulesCreateOperationPayload],
    ) -> PlaylistGenerationSchedulesCreateSingleResourceDataDocument:
        """Creates a new playlistGenerationSchedule."""
        ...


    async def playlist_generation_schedules_id_get(
        self,
        id: Annotated[str, Field(max_length=64)],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: playlist")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlist.items")],
    ) -> PlaylistGenerationSchedulesSingleResourceDataDocument:
        """Retrieves single playlistGenerationSchedule by id."""
        ...


    async def playlist_generation_schedules_id_delete(
        self,
        id: Annotated[str, Field(max_length=64)],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
    ) -> MutationResponseDocument:
        """Deletes existing playlistGenerationSchedule."""
        ...


    async def playlist_generation_schedules_id_patch(
        self,
        id: Annotated[str, Field(max_length=64)],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        playlist_generation_schedules_update_operation_payload: Optional[PlaylistGenerationSchedulesUpdateOperationPayload],
    ) -> PlaylistGenerationSchedulesUpdateSingleResourceDataDocument:
        """Updates existing playlistGenerationSchedule."""
        ...


    async def playlist_generation_schedules_id_relationships_playlist_get(
        self,
        id: Annotated[str, Field(max_length=64)],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: playlist")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlist.items")],
    ) -> PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument:
        """Retrieves playlist relationship."""
        ...
