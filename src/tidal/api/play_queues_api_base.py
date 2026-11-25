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
from tidal.security_api import get_token_Authorization_Code_PKCE

class BasePlayQueuesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePlayQueuesApi.subclasses = BasePlayQueuesApi.subclasses + (cls,)
    async def play_queues_get(
        self,
        filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="User id. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: changeEventStream, current, future, owners, past")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: current")],
    ) -> PlayQueuesMultiResourceDataDocument:
        """Retrieves multiple playQueues by available filters, or without if applicable."""
        ...


    async def play_queues_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        play_queues_create_operation_payload: Optional[PlayQueuesCreateOperationPayload],
    ) -> PlayQueuesCreateSingleResourceDataDocument:
        """Creates a new playQueue."""
        ...


    async def play_queues_id_get(
        self,
        id: Annotated[str, Field(description="Play queue id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: changeEventStream, current, future, owners, past")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: current")],
    ) -> PlayQueuesSingleResourceDataDocument:
        """Retrieves single playQueue by id."""
        ...


    async def play_queues_id_delete(
        self,
        id: Annotated[str, Field(description="Play queue id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
    ) -> MutationResponseDocument:
        """Deletes existing playQueue."""
        ...


    async def play_queues_id_patch(
        self,
        id: Annotated[str, Field(description="Play queue id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        play_queues_update_operation_payload: Optional[PlayQueuesUpdateOperationPayload],
    ) -> PlayQueuesUpdateSingleResourceDataDocument:
        """Atomically applies attributes, future items, then current selection."""
        ...


    async def play_queues_id_relationships_change_event_stream_get(
        self,
        id: str,
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: changeEventStream")],
    ) -> PlayQueuesChangeEventStreamSingleRelationshipDataDocument:
        """Retrieves changeEventStream relationship."""
        ...


    async def play_queues_id_relationships_current_get(
        self,
        id: Annotated[str, Field(description="Play queue id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: current")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: current")],
    ) -> PlayQueuesCurrentSingleRelationshipDataDocument:
        """Retrieves current relationship."""
        ...


    async def play_queues_id_relationships_current_patch(
        self,
        id: Annotated[str, Field(description="Play queue id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        play_queues_current_relationship_update_operation_payload: Optional[PlayQueuesCurrentRelationshipUpdateOperationPayload],
    ) -> PlayQueuesCurrentUpdateSingleRelationshipDataDocument:
        """Sets the current item to the existing queue occurrence identified by data.meta.itemId, changing which entries are past and future. Null data is rejected. Optional position and updatedByInstallationId must be supplied together. Returns the current item linkage and queue revision."""
        ...


    async def play_queues_id_relationships_future_get(
        self,
        id: Annotated[str, Field(description="Play queue id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: future")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: future")],
    ) -> PlayQueuesFutureMultiRelationshipDataDocument:
        """Retrieves future relationship."""
        ...


    async def play_queues_id_relationships_future_post(
        self,
        id: Annotated[str, Field(description="Play queue id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        play_queues_future_relationship_add_operation_payload: Optional[PlayQueuesFutureRelationshipAddOperationPayload],
    ) -> PlayQueuesFutureAddMultiRelationshipDataDocument:
        """Omitting top-level meta or setting it to null defaults to REPLACE_ALL, replacing future entries. Use ADD_TO_FRONT, ADD_TO_BACK or ADD_BEFORE in meta.mode to add without replacing existing entries. ADD_BEFORE requires meta.positionBefore. REPLACE_ALL_AND_CURRENT replaces future entries; ADD_TO_FRONT_REPLACE_CURRENT prepends entries. Both select the first newly inserted entry in the active queue order as current, which may differ from request order when shuffled. With empty data and no source, replacement modes clear future entries; the current entry is unchanged when no entries are inserted. With meta.source, startIndex selects an entry in the first page&#39;s data before unsupported types are skipped. Tracks and videos are added in page order, retaining duplicates; other types are skipped without expansion. Reaching 1000 added items or 100 pages queues the collected prefix. Invalid sources or indexes, a suffix with no playable items, repeated pages, and read failures encountered before a cap leave the queue unchanged. Returns empty data and meta.revision as an acknowledgement."""
        ...


    async def play_queues_id_relationships_future_delete(
        self,
        id: Annotated[str, Field(description="Play queue id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        play_queues_future_relationship_remove_operation_payload: Optional[PlayQueuesFutureRelationshipRemoveOperationPayload],
    ) -> MutationResponseDocument:
        """Removes the future occurrences selected by data[].meta.itemId without deleting their tracks or videos. Other queue entries are preserved. Returns an acknowledgement."""
        ...


    async def play_queues_id_relationships_future_patch(
        self,
        id: Annotated[str, Field(description="Play queue id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        play_queues_future_relationship_update_operation_payload: Optional[PlayQueuesFutureRelationshipUpdateOperationPayload],
    ) -> PlayQueuesFutureUpdateMultiRelationshipDataDocument:
        """Incrementally moves existing future occurrences selected by data[].meta.itemId, in their current queue order, before meta.positionBefore. Preserves memberships and unselected entries&#39; metadata and relative order. Empty data is rejected. Returns empty data and meta.revision as an acknowledgement."""
        ...


    async def play_queues_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Play queue id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> PlayQueuesOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def play_queues_id_relationships_past_get(
        self,
        id: Annotated[str, Field(description="Play queue id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: past")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: past")],
    ) -> PlayQueuesPastMultiRelationshipDataDocument:
        """Retrieves past relationship."""
        ...
