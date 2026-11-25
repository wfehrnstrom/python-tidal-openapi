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
from tidal.models.shares_create_operation_payload import SharesCreateOperationPayload
from tidal.models.shares_create_single_resource_data_document import SharesCreateSingleResourceDataDocument
from tidal.models.shares_multi_resource_data_document import SharesMultiResourceDataDocument
from tidal.models.shares_owners_multi_relationship_data_document import SharesOwnersMultiRelationshipDataDocument
from tidal.models.shares_shared_resources_multi_relationship_data_document import SharesSharedResourcesMultiRelationshipDataDocument
from tidal.models.shares_single_resource_data_document import SharesSingleResourceDataDocument
from tidal.models.shares_update_operation_payload import SharesUpdateOperationPayload
from tidal.models.shares_update_single_resource_data_document import SharesUpdateSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseSharesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSharesApi.subclasses = BaseSharesApi.subclasses + (cls,)
    async def shares_get(
        self,
        filter_code: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="A share code (e.g. `xyz`)")],
        filter_self_applies_to: Annotated[Optional[str], Field(description="Album or track owned by the caller. Selects undeleted, unexpired links on the resource or its album. Exhausted links are included. Each link keeps its own sharedResources. Cannot be combined with other filters. Missing or non-owned resources and subjects without a live access node return no records. Ordered by expiry then share ID; at most 20 links per page.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, sharedResources")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: sharedResources")],
    ) -> SharesMultiResourceDataDocument:
        """Retrieves multiple shares by available filters, or without if applicable."""
        ...


    async def shares_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        shares_create_operation_payload: Optional[SharesCreateOperationPayload],
    ) -> SharesCreateSingleResourceDataDocument:
        """Creates a new share. Deprecated for playlists: use &#x60;resourceGrantInvitations&#x60; instead."""
        ...


    async def shares_id_get(
        self,
        id: Annotated[str, Field(description="Share id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, sharedResources")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: sharedResources")],
    ) -> SharesSingleResourceDataDocument:
        """Retrieves single share by id."""
        ...


    async def shares_id_delete(
        self,
        id: Annotated[str, Field(description="Share id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        revoke_grants: Annotated[Optional[bool], Field(description="Also revoke the access granted to everyone who saved this share; access from other sources stays. Defaults to false. Not supported for playlist shares or for owners not yet on the access store; there true is rejected with 400.")],
    ) -> MutationResponseDocument:
        """Delete share. Effectively revokes bearer access and acceptance."""
        ...


    async def shares_id_patch(
        self,
        id: Annotated[str, Field(description="Share id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        shares_update_operation_payload: Optional[SharesUpdateOperationPayload],
    ) -> SharesUpdateSingleResourceDataDocument:
        """Set, change or remove the share&#39;s password. Setting one also removes BEARER access; removing one leaves the access modes unchanged. Existing savers keep their access."""
        ...


    async def shares_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Share id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> SharesOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def shares_id_relationships_shared_resources_get(
        self,
        id: Annotated[str, Field(description="Share id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: sharedResources")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: sharedResources")],
    ) -> SharesSharedResourcesMultiRelationshipDataDocument:
        """Retrieves sharedResources relationship."""
        ...
