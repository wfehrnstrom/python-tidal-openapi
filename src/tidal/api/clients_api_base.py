# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.clients_certificates_multi_relationship_data_document import ClientsCertificatesMultiRelationshipDataDocument
from tidal.models.clients_create_operation_payload import ClientsCreateOperationPayload
from tidal.models.clients_create_single_resource_data_document import ClientsCreateSingleResourceDataDocument
from tidal.models.clients_multi_resource_data_document import ClientsMultiResourceDataDocument
from tidal.models.clients_owners_multi_relationship_data_document import ClientsOwnersMultiRelationshipDataDocument
from tidal.models.clients_single_resource_data_document import ClientsSingleResourceDataDocument
from tidal.models.clients_update_operation_payload import ClientsUpdateOperationPayload
from tidal.models.clients_update_single_resource_data_document import ClientsUpdateSingleResourceDataDocument
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
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseClientsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseClientsApi.subclasses = BaseClientsApi.subclasses + (cls,)
    async def clients_get(
        self,
        filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="User id. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: certificates, owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> ClientsMultiResourceDataDocument:
        """Retrieves multiple clients by available filters, or without if applicable."""
        ...


    async def clients_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        clients_create_operation_payload: Optional[ClientsCreateOperationPayload],
    ) -> ClientsCreateSingleResourceDataDocument:
        """Creates a new client."""
        ...


    async def clients_id_get(
        self,
        id: Annotated[str, Field(description="OAuth client identifier")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: certificates, owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> ClientsSingleResourceDataDocument:
        """Retrieves single client by id."""
        ...


    async def clients_id_delete(
        self,
        id: Annotated[str, Field(description="OAuth client identifier")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
    ) -> MutationResponseDocument:
        """Deletes existing client."""
        ...


    async def clients_id_patch(
        self,
        id: Annotated[str, Field(description="OAuth client identifier")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        clients_update_operation_payload: Optional[ClientsUpdateOperationPayload],
    ) -> ClientsUpdateSingleResourceDataDocument:
        """Updates existing client."""
        ...


    async def clients_id_relationships_certificates_get(
        self,
        id: Annotated[str, Field(description="OAuth client identifier")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: certificates")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ClientsCertificatesMultiRelationshipDataDocument:
        """Retrieves certificates relationship."""
        ...


    async def clients_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="OAuth client identifier")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ClientsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...
