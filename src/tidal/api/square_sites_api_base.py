# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field
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
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.square_sites_items_add_multi_data_relationship403_response_body import SquareSitesItemsAddMultiDataRelationship403ResponseBody
from tidal.models.square_sites_items_add_multi_data_relationship409_response_body import SquareSitesItemsAddMultiDataRelationship409ResponseBody
from tidal.models.square_sites_items_multi_relationship_data_document import SquareSitesItemsMultiRelationshipDataDocument
from tidal.models.square_sites_items_read_multi_data_relationship403_response_body import SquareSitesItemsReadMultiDataRelationship403ResponseBody
from tidal.models.square_sites_items_read_multi_data_relationship409_response_body import SquareSitesItemsReadMultiDataRelationship409ResponseBody
from tidal.models.square_sites_items_relationship_add_operation_payload import SquareSitesItemsRelationshipAddOperationPayload
from tidal.models.square_sites_items_relationship_remove_operation_payload import SquareSitesItemsRelationshipRemoveOperationPayload
from tidal.models.square_sites_items_remove_multi_data_relationship403_response_body import SquareSitesItemsRemoveMultiDataRelationship403ResponseBody
from tidal.models.square_sites_items_remove_multi_data_relationship409_response_body import SquareSitesItemsRemoveMultiDataRelationship409ResponseBody
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseSquareSitesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSquareSitesApi.subclasses = BaseSquareSitesApi.subclasses + (cls,)
    async def square_sites_id_relationships_items_get(
        self,
        id: Annotated[str, Field(description="Square Online site id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> SquareSitesItemsMultiRelationshipDataDocument:
        """Items published in the site, in title order. Missing catalog scopes return MISSING_ITEMS_SCOPE. A page can be short or empty and still have a next cursor."""
        ...


    async def square_sites_id_relationships_items_post(
        self,
        id: Annotated[str, Field(description="Square Online site id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        square_sites_items_relationship_add_operation_payload: Optional[SquareSitesItemsRelationshipAddOperationPayload],
    ) -> MutationResponseDocument:
        """Publishes the items in the site. Items already published and repeated items are left alone. An item missing from the catalog fails the request before anything changes."""
        ...


    async def square_sites_id_relationships_items_delete(
        self,
        id: Annotated[str, Field(description="Square Online site id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        square_sites_items_relationship_remove_operation_payload: Optional[SquareSitesItemsRelationshipRemoveOperationPayload],
    ) -> MutationResponseDocument:
        """Removes the items from the site; they stay in the catalog. Items not published and repeated items are left alone. An item missing from the catalog fails the request before anything changes."""
        ...
