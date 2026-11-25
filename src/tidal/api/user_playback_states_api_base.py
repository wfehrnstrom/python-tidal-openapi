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
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseUserPlaybackStatesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUserPlaybackStatesApi.subclasses = BaseUserPlaybackStatesApi.subclasses + (cls,)
    async def user_playback_states_id_get(
        self,
        id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: activePlayer, availablePlayers, changeEventStream, playQueue")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: activePlayer.offlineInventory")],
    ) -> UserPlaybackStatesSingleResourceDataDocument:
        """Retrieves single userPlaybackState by id."""
        ...


    async def user_playback_states_id_patch(
        self,
        id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_playback_states_update_operation_payload: Optional[UserPlaybackStatesUpdateOperationPayload],
    ) -> UserPlaybackStatesUpdateSingleResourceDataDocument:
        """Updates existing userPlaybackState."""
        ...


    async def user_playback_states_id_relationships_active_player_get(
        self,
        id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: activePlayer")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: activePlayer.offlineInventory")],
    ) -> UserPlaybackStatesActivePlayerSingleRelationshipDataDocument:
        """Retrieves activePlayer relationship."""
        ...


    async def user_playback_states_id_relationships_active_player_patch(
        self,
        id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_playback_states_active_player_relationship_update_operation_payload: Optional[UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload],
    ) -> UserPlaybackStatesActivePlayerUpdateSingleRelationshipDataDocument:
        """Replaces the active-player selection with the supplied owned installation. Explicit null data releases the player without deleting the installation. Returns null linkage when released or when the selected installation has no live attachment. An unavailable selection is retained and becomes visible again when its attachment is refreshed."""
        ...


    async def user_playback_states_id_relationships_available_players_get(
        self,
        id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: availablePlayers")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: availablePlayers.offlineInventory")],
    ) -> UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument:
        """Retrieves availablePlayers relationship."""
        ...


    async def user_playback_states_id_relationships_available_players_post(
        self,
        id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_playback_states_available_players_relationship_add_operation_payload: Optional[UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload],
    ) -> UserPlaybackStatesAvailablePlayersAddMultiRelationshipDataDocument:
        """Attaches or refreshes one owned installation as an available player, preserving other attachments. Returns all currently available player linkage."""
        ...


    async def user_playback_states_id_relationships_available_players_delete(
        self,
        id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_playback_states_available_players_relationship_remove_operation_payload: Optional[UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload],
    ) -> MutationResponseDocument:
        """Detaches one installation without deleting it. Also releases the active player when it is that installation. Returns an acknowledgement."""
        ...


    async def user_playback_states_id_relationships_change_event_stream_get(
        self,
        id: str,
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: changeEventStream")],
    ) -> UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument:
        """Retrieves changeEventStream relationship."""
        ...


    async def user_playback_states_id_relationships_play_queue_get(
        self,
        id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: playQueue")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playQueue.current")],
    ) -> UserPlaybackStatesPlayQueueSingleRelationshipDataDocument:
        """Retrieves playQueue relationship."""
        ...


    async def user_playback_states_id_relationships_play_queue_patch(
        self,
        id: Annotated[str, Field(description="User playback session id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_playback_states_play_queue_relationship_update_operation_payload: Optional[UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload],
    ) -> UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument:
        """Replaces the selected play queue. Explicit null data clears the selection without deleting the queue. Returns the selected queue linkage, or null data when cleared."""
        ...
