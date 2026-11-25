# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.accepted_terms_create_operation_payload import AcceptedTermsCreateOperationPayload
from tidal.models.accepted_terms_create_single_resource_data_document import AcceptedTermsCreateSingleResourceDataDocument
from tidal.models.accepted_terms_multi_resource_data_document import AcceptedTermsMultiResourceDataDocument
from tidal.models.accepted_terms_owners_multi_relationship_data_document import AcceptedTermsOwnersMultiRelationshipDataDocument
from tidal.models.accepted_terms_terms_single_relationship_data_document import AcceptedTermsTermsSingleRelationshipDataDocument
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

class BaseAcceptedTermsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseAcceptedTermsApi.subclasses = BaseAcceptedTermsApi.subclasses + (cls,)
    async def accepted_terms_get(
        self,
        filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="User id. Also accepts `me`.")],
        filter_terms_terms_type: Annotated[List[str], Field(description="One of: DEVELOPER, UPLOAD_MARKETPLACE, MERCH_GUIDELINES, TIDAL_CONNECT_DEVELOPER (e.g. `DEVELOPER`)")],
        filter_terms_is_latest_version: Annotated[Optional[List[str]], Field(description="Filter by terms.isLatestVersion")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, terms")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> AcceptedTermsMultiResourceDataDocument:
        """Retrieves multiple acceptedTerms by available filters, or without if applicable."""
        ...


    async def accepted_terms_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        accepted_terms_create_operation_payload: Optional[AcceptedTermsCreateOperationPayload],
    ) -> AcceptedTermsCreateSingleResourceDataDocument:
        """Creates a new acceptedTerm."""
        ...


    async def accepted_terms_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Accepted terms id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> AcceptedTermsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def accepted_terms_id_relationships_terms_get(
        self,
        id: Annotated[str, Field(description="Accepted terms id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: terms")],
    ) -> AcceptedTermsTermsSingleRelationshipDataDocument:
        """Retrieves terms relationship."""
        ...
