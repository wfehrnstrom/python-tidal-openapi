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
from tidal.models.square_connections_create_operation_payload import SquareConnectionsCreateOperationPayload
from tidal.models.square_connections_create_single_resource_data_document import SquareConnectionsCreateSingleResourceDataDocument
from tidal.models.square_connections_read_by_id403_response_body import SquareConnectionsReadById403ResponseBody
from tidal.models.square_connections_selected_site_read_single_data_relationship403_response_body import SquareConnectionsSelectedSiteReadSingleDataRelationship403ResponseBody
from tidal.models.square_connections_selected_site_relationship_update_operation_payload import SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload
from tidal.models.square_connections_selected_site_single_relationship_data_document import SquareConnectionsSelectedSiteSingleRelationshipDataDocument
from tidal.models.square_connections_selected_site_update_single_data_relationship403_response_body import SquareConnectionsSelectedSiteUpdateSingleDataRelationship403ResponseBody
from tidal.models.square_connections_selected_site_update_single_data_relationship409_response_body import SquareConnectionsSelectedSiteUpdateSingleDataRelationship409ResponseBody
from tidal.models.square_connections_selected_site_update_single_relationship_data_document import SquareConnectionsSelectedSiteUpdateSingleRelationshipDataDocument
from tidal.models.square_connections_single_resource_data_document import SquareConnectionsSingleResourceDataDocument
from tidal.models.square_connections_sites_multi_relationship_data_document import SquareConnectionsSitesMultiRelationshipDataDocument
from tidal.models.square_connections_sites_read_multi_data_relationship403_response_body import SquareConnectionsSitesReadMultiDataRelationship403ResponseBody
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseSquareConnectionsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSquareConnectionsApi.subclasses = BaseSquareConnectionsApi.subclasses + (cls,)
    async def square_connections_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        square_connections_create_operation_payload: Optional[SquareConnectionsCreateOperationPayload],
    ) -> SquareConnectionsCreateSingleResourceDataDocument:
        """Creates a new squareConnection."""
        ...


    async def square_connections_id_get(
        self,
        id: Annotated[str, Field(description="Square connection id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: selectedSite, sites")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> SquareConnectionsSingleResourceDataDocument:
        """Retrieves single squareConnection by id."""
        ...


    async def square_connections_id_relationships_selected_site_get(
        self,
        id: Annotated[str, Field(description="Square connection id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: selectedSite")],
    ) -> SquareConnectionsSelectedSiteSingleRelationshipDataDocument:
        """Retrieves selectedSite relationship."""
        ...


    async def square_connections_id_relationships_selected_site_patch(
        self,
        id: Annotated[str, Field(description="Square connection id. Use `me` for the authenticated user's resource")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        square_connections_selected_site_relationship_update_operation_payload: Optional[SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload],
    ) -> SquareConnectionsSelectedSiteUpdateSingleRelationshipDataDocument:
        """Replaces the selected Square site. Explicit null data clears the selection without deleting the site. Returns the selected site linkage, or null data when cleared."""
        ...


    async def square_connections_id_relationships_sites_get(
        self,
        id: Annotated[str, Field(description="Square connection id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: sites")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> SquareConnectionsSitesMultiRelationshipDataDocument:
        """Retrieves sites relationship."""
        ...
