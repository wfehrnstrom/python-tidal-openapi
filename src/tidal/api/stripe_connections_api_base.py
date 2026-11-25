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
from tidal.models.stripe_connections_create_operation_payload import StripeConnectionsCreateOperationPayload
from tidal.models.stripe_connections_create_single_resource_data_document import StripeConnectionsCreateSingleResourceDataDocument
from tidal.models.stripe_connections_multi_resource_data_document import StripeConnectionsMultiResourceDataDocument
from tidal.models.stripe_connections_owners_multi_relationship_data_document import StripeConnectionsOwnersMultiRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseStripeConnectionsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseStripeConnectionsApi.subclasses = BaseStripeConnectionsApi.subclasses + (cls,)
    async def stripe_connections_get(
        self,
        filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="User id. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> StripeConnectionsMultiResourceDataDocument:
        """Retrieves multiple stripeConnections by available filters, or without if applicable."""
        ...


    async def stripe_connections_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        stripe_connections_create_operation_payload: Optional[StripeConnectionsCreateOperationPayload],
    ) -> StripeConnectionsCreateSingleResourceDataDocument:
        """Creates a new stripeConnection."""
        ...


    async def stripe_connections_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Stripe connection id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> StripeConnectionsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...
