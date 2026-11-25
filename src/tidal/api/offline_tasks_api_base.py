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
from tidal.models.offline_tasks_collection_single_relationship_data_document import OfflineTasksCollectionSingleRelationshipDataDocument
from tidal.models.offline_tasks_item_single_relationship_data_document import OfflineTasksItemSingleRelationshipDataDocument
from tidal.models.offline_tasks_multi_resource_data_document import OfflineTasksMultiResourceDataDocument
from tidal.models.offline_tasks_owners_multi_relationship_data_document import OfflineTasksOwnersMultiRelationshipDataDocument
from tidal.models.offline_tasks_single_resource_data_document import OfflineTasksSingleResourceDataDocument
from tidal.models.offline_tasks_update_operation_payload import OfflineTasksUpdateOperationPayload
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseOfflineTasksApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseOfflineTasksApi.subclasses = BaseOfflineTasksApi.subclasses + (cls,)
    async def offline_tasks_get(
        self,
        filter_installation_id: Annotated[List[str], Field(description="List of offline task IDs (e.g. `a468bee88def`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: collection, item, owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: collection")],
    ) -> OfflineTasksMultiResourceDataDocument:
        """Retrieves multiple offlineTasks by available filters, or without if applicable."""
        ...


    async def offline_tasks_id_get(
        self,
        id: Annotated[str, Field(description="Offline task id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: collection, item, owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: collection")],
    ) -> OfflineTasksSingleResourceDataDocument:
        """Retrieves single offlineTask by id."""
        ...


    async def offline_tasks_id_patch(
        self,
        id: Annotated[str, Field(description="Offline task id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        offline_tasks_update_operation_payload: Optional[OfflineTasksUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Updates existing offlineTask."""
        ...


    async def offline_tasks_id_relationships_collection_get(
        self,
        id: Annotated[str, Field(description="Offline task id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: collection")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: collection")],
    ) -> OfflineTasksCollectionSingleRelationshipDataDocument:
        """Retrieves collection relationship."""
        ...


    async def offline_tasks_id_relationships_item_get(
        self,
        id: Annotated[str, Field(description="Offline task id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: item")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: item")],
    ) -> OfflineTasksItemSingleRelationshipDataDocument:
        """Retrieves item relationship."""
        ...


    async def offline_tasks_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Offline task id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> OfflineTasksOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...
