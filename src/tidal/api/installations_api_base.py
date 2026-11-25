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
from tidal.models.installations_create_operation_payload import InstallationsCreateOperationPayload
from tidal.models.installations_create_single_resource_data_document import InstallationsCreateSingleResourceDataDocument
from tidal.models.installations_multi_resource_data_document import InstallationsMultiResourceDataDocument
from tidal.models.installations_offline_inventory_multi_relationship_data_document import InstallationsOfflineInventoryMultiRelationshipDataDocument
from tidal.models.installations_offline_inventory_relationship_add_operation_payload import InstallationsOfflineInventoryRelationshipAddOperationPayload
from tidal.models.installations_offline_inventory_relationship_remove_operation_payload import InstallationsOfflineInventoryRelationshipRemoveOperationPayload
from tidal.models.installations_owners_multi_relationship_data_document import InstallationsOwnersMultiRelationshipDataDocument
from tidal.models.installations_single_resource_data_document import InstallationsSingleResourceDataDocument
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseInstallationsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseInstallationsApi.subclasses = BaseInstallationsApi.subclasses + (cls,)
    async def installations_get(
        self,
        filter_client_provided_installation_id: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="Client-provided installation identifier to filter by (e.g. `a468bee88def`)")],
        filter_owners_id: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="User ID to filter by. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: offlineInventory, owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: offlineInventory")],
    ) -> InstallationsMultiResourceDataDocument:
        """Retrieves multiple installations by available filters, or without if applicable."""
        ...


    async def installations_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        installations_create_operation_payload: Optional[InstallationsCreateOperationPayload],
    ) -> InstallationsCreateSingleResourceDataDocument:
        """Creates a new installation."""
        ...


    async def installations_id_get(
        self,
        id: Annotated[str, Field(description="Installation id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: offlineInventory, owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: offlineInventory")],
    ) -> InstallationsSingleResourceDataDocument:
        """Retrieves single installation by id."""
        ...


    async def installations_id_relationships_offline_inventory_get(
        self,
        filter_type: Annotated[List[str], Field(description="One of: tracks, videos, albums, playlists, userCollectionTracks (e.g. `tracks`)")],
        id: Annotated[str, Field(description="Installation id")],
        filter_client_storage_state: Annotated[Optional[List[str]], Field(description="One of: PENDING, STORED, FAILED (e.g. `PENDING`)")],
        filter_id: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="Offline item id (e.g. `1234`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: offlineInventory")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: offlineInventory")],
    ) -> InstallationsOfflineInventoryMultiRelationshipDataDocument:
        """Retrieves offlineInventory relationship."""
        ...


    async def installations_id_relationships_offline_inventory_post(
        self,
        id: Annotated[str, Field(description="Installation id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        installations_offline_inventory_relationship_add_operation_payload: Optional[InstallationsOfflineInventoryRelationshipAddOperationPayload],
    ) -> MutationResponseDocument:
        """Adds item(s) to offlineInventory relationship."""
        ...


    async def installations_id_relationships_offline_inventory_delete(
        self,
        id: Annotated[str, Field(description="Installation id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        installations_offline_inventory_relationship_remove_operation_payload: Optional[InstallationsOfflineInventoryRelationshipRemoveOperationPayload],
    ) -> MutationResponseDocument:
        """Deletes item(s) from offlineInventory relationship."""
        ...


    async def installations_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Installation id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> InstallationsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...
