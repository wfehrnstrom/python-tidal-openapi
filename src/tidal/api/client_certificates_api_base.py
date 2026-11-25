# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.client_certificates_create_operation_payload import ClientCertificatesCreateOperationPayload
from tidal.models.client_certificates_create_single_resource_data_document import ClientCertificatesCreateSingleResourceDataDocument
from tidal.models.client_certificates_owners_multi_relationship_data_document import ClientCertificatesOwnersMultiRelationshipDataDocument
from tidal.models.client_certificates_single_resource_data_document import ClientCertificatesSingleResourceDataDocument
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
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseClientCertificatesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseClientCertificatesApi.subclasses = BaseClientCertificatesApi.subclasses + (cls,)
    async def client_certificates_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        client_certificates_create_operation_payload: Optional[ClientCertificatesCreateOperationPayload],
    ) -> ClientCertificatesCreateSingleResourceDataDocument:
        """Creates a new clientCertificate."""
        ...


    async def client_certificates_id_get(
        self,
        id: Annotated[str, Field(description="TIDAL Connect client certificate identifier")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> ClientCertificatesSingleResourceDataDocument:
        """Retrieves single clientCertificate by id."""
        ...


    async def client_certificates_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="TIDAL Connect client certificate identifier")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ClientCertificatesOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...
