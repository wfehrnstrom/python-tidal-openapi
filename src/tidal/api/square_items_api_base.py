# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.atomic_operations400_response_body import AtomicOperations400ResponseBody
from tidal.models.atomic_operations403_response_body import AtomicOperations403ResponseBody
from tidal.models.atomic_operations404_response_body import AtomicOperations404ResponseBody
from tidal.models.atomic_operations405_response_body import AtomicOperations405ResponseBody
from tidal.models.atomic_operations406_response_body import AtomicOperations406ResponseBody
from tidal.models.atomic_operations409_response_body import AtomicOperations409ResponseBody
from tidal.models.atomic_operations415_response_body import AtomicOperations415ResponseBody
from tidal.models.atomic_operations422_response_body import AtomicOperations422ResponseBody
from tidal.models.atomic_operations429_response_body import AtomicOperations429ResponseBody
from tidal.models.atomic_operations500_response_body import AtomicOperations500ResponseBody
from tidal.models.atomic_operations503_response_body import AtomicOperations503ResponseBody
from tidal.models.atomic_operations_request import AtomicOperationsRequest
from tidal.models.atomic_operations_response import AtomicOperationsResponse
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
from tidal.models.square_items_artworks_multi_relationship_data_document import SquareItemsArtworksMultiRelationshipDataDocument
from tidal.models.square_items_artworks_read_multi_data_relationship409_response_body import SquareItemsArtworksReadMultiDataRelationship409ResponseBody
from tidal.models.square_items_artworks_relationship_update_operation_payload import SquareItemsArtworksRelationshipUpdateOperationPayload
from tidal.models.square_items_artworks_update_multi_data_relationship403_response_body import SquareItemsArtworksUpdateMultiDataRelationship403ResponseBody
from tidal.models.square_items_artworks_update_multi_data_relationship409_response_body import SquareItemsArtworksUpdateMultiDataRelationship409ResponseBody
from tidal.models.square_items_artworks_update_multi_data_relationship413_response_body import SquareItemsArtworksUpdateMultiDataRelationship413ResponseBody
from tidal.models.square_items_artworks_update_multi_relationship_data_document import SquareItemsArtworksUpdateMultiRelationshipDataDocument
from tidal.models.square_items_delete_resource403_response_body import SquareItemsDeleteResource403ResponseBody
from tidal.models.square_items_delete_resource409_response_body import SquareItemsDeleteResource409ResponseBody
from tidal.models.square_items_multi_resource_data_document import SquareItemsMultiResourceDataDocument
from tidal.models.square_items_owners_multi_relationship_data_document import SquareItemsOwnersMultiRelationshipDataDocument
from tidal.models.square_items_read_by_filter403_response_body import SquareItemsReadByFilter403ResponseBody
from tidal.models.square_items_read_by_filter409_response_body import SquareItemsReadByFilter409ResponseBody
from tidal.models.square_items_read_by_id403_response_body import SquareItemsReadById403ResponseBody
from tidal.models.square_items_read_by_id409_response_body import SquareItemsReadById409ResponseBody
from tidal.models.square_items_single_resource_data_document import SquareItemsSingleResourceDataDocument
from tidal.models.square_items_update_operation_payload import SquareItemsUpdateOperationPayload
from tidal.models.square_items_update_resource403_response_body import SquareItemsUpdateResource403ResponseBody
from tidal.models.square_items_update_resource409_response_body import SquareItemsUpdateResource409ResponseBody
from tidal.models.square_items_update_single_resource_data_document import SquareItemsUpdateSingleResourceDataDocument
from tidal.models.square_items_variations_multi_relationship_data_document import SquareItemsVariationsMultiRelationshipDataDocument
from tidal.models.square_items_variations_read_multi_data_relationship403_response_body import SquareItemsVariationsReadMultiDataRelationship403ResponseBody
from tidal.models.square_items_variations_read_multi_data_relationship409_response_body import SquareItemsVariationsReadMultiDataRelationship409ResponseBody
from tidal.models.square_items_variations_relationship_update_operation_payload import SquareItemsVariationsRelationshipUpdateOperationPayload
from tidal.models.square_items_variations_update_multi_data_relationship403_response_body import SquareItemsVariationsUpdateMultiDataRelationship403ResponseBody
from tidal.models.square_items_variations_update_multi_data_relationship409_response_body import SquareItemsVariationsUpdateMultiDataRelationship409ResponseBody
from tidal.models.square_items_variations_update_multi_relationship_data_document import SquareItemsVariationsUpdateMultiRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseSquareItemsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSquareItemsApi.subclasses = BaseSquareItemsApi.subclasses + (cls,)
    async def operations_post(
        self,
        idempotency_key: Annotated[str, Field(min_length=1, max_length=128, description="Retry an unchanged request with the original key after a timeout or server error. Replay is bounded by downstream receipt and idempotency retention.")],
        atomic_operations_request: AtomicOperationsRequest,
    ) -> AtomicOperationsResponse:
        """Commits a supported group of resource creations together. Only add operations without ref or href are supported. Local linkage must reference an earlier creation. Each resource&#39;s mutation policy applies. After a timeout or server error, retry unchanged with the original Idempotency-Key. Replay is bounded by downstream receipt and idempotency retention."""
        ...


    async def square_items_get(
        self,
        filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="User id. Also accepts `me`.")],
        filter_origin: Annotated[Optional[str], Field(description="Only items with this origin (e.g. `TIDAL`)")],
        filter_self_matches_query: Annotated[Optional[Annotated[str, Field(min_length=1, max_length=255)]], Field(description="Word-prefix match on item titles, descriptions and abbreviations, and on variation names, SKUs and UPCs (e.g. `tee`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks, owners, variations")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> SquareItemsMultiResourceDataDocument:
        """Retrieves multiple squareItems by available filters, or without if applicable."""
        ...


    async def square_items_id_get(
        self,
        id: Annotated[str, Field(description="Square item id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks, owners, variations")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> SquareItemsSingleResourceDataDocument:
        """Retrieves single squareItem by id."""
        ...


    async def square_items_id_delete(
        self,
        id: Annotated[str, Field(description="Square item id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
    ) -> MutationResponseDocument:
        """Deletes existing squareItem."""
        ...


    async def square_items_id_patch(
        self,
        id: Annotated[str, Field(description="Square item id")],
        idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        square_items_update_operation_payload: Optional[SquareItemsUpdateOperationPayload],
    ) -> SquareItemsUpdateSingleResourceDataDocument:
        """Updates existing squareItem."""
        ...


    async def square_items_id_relationships_artworks_get(
        self,
        id: Annotated[str, Field(description="Square item id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> SquareItemsArtworksMultiRelationshipDataDocument:
        """A photo Square has no URL for stays in the list and its artwork has no files."""
        ...


    async def square_items_id_relationships_artworks_patch(
        self,
        id: Annotated[str, Field(description="Square item id")],
        idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        square_items_artworks_relationship_update_operation_payload: Optional[SquareItemsArtworksRelationshipUpdateOperationPayload],
    ) -> SquareItemsArtworksUpdateMultiRelationshipDataDocument:
        """Replaces the item&#39;s photos with the complete ordered list. Omitted photos are detached and stay in the seller&#39;s Square catalog; an empty list clears them. The first artwork is the primary photo. Duplicate artwork IDs are rejected. Uploaded TIDAL JPEG artworks, at most 15,000,000 bytes, are copied to Square and attached under new artwork IDs; their originals stay unchanged. Existing Square artworks must belong to this seller and are attached directly. Returns the complete resulting linkage in display order and the committed item revision. Copies may remain in Square if the replacement fails. Retry unchanged with the original Idempotency-Key after a timeout or 5xx. Recovery is bounded by Marketplace receipts and Square&#39;s idempotency retention, and can be blocked if the item is deleted or a source becomes unavailable or ineligible. Read the item again to reconcile its current state."""
        ...


    async def square_items_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Square item id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> SquareItemsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def square_items_id_relationships_variations_get(
        self,
        id: Annotated[str, Field(description="Square item id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: variations")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> SquareItemsVariationsMultiRelationshipDataDocument:
        """Variations in Square&#39;s display order."""
        ...


    async def square_items_id_relationships_variations_patch(
        self,
        id: Annotated[str, Field(description="Square item id")],
        idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        square_items_variations_relationship_update_operation_payload: Optional[SquareItemsVariationsRelationshipUpdateOperationPayload],
    ) -> SquareItemsVariationsUpdateMultiRelationshipDataDocument:
        """Incrementally moves the selected variations as an ordered block before positionBefore, or to the end when omitted. Memberships are preserved; unselected variations retain their metadata and relative order. Empty data is rejected. Returns the affected linkage only and the updated item revision. After a timeout or &#x60;5xx&#x60;, retry unchanged with the original Idempotency-Key. Replay protection is bounded by receipt availability and Square&#39;s idempotency retention."""
        ...
