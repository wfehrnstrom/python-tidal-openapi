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
from tidal.models.square_item_variations_artworks_multi_relationship_data_document import SquareItemVariationsArtworksMultiRelationshipDataDocument
from tidal.models.square_item_variations_artworks_read_multi_data_relationship403_response_body import SquareItemVariationsArtworksReadMultiDataRelationship403ResponseBody
from tidal.models.square_item_variations_artworks_read_multi_data_relationship409_response_body import SquareItemVariationsArtworksReadMultiDataRelationship409ResponseBody
from tidal.models.square_item_variations_artworks_relationship_update_operation_payload import SquareItemVariationsArtworksRelationshipUpdateOperationPayload
from tidal.models.square_item_variations_artworks_update_multi_data_relationship403_response_body import SquareItemVariationsArtworksUpdateMultiDataRelationship403ResponseBody
from tidal.models.square_item_variations_artworks_update_multi_data_relationship409_response_body import SquareItemVariationsArtworksUpdateMultiDataRelationship409ResponseBody
from tidal.models.square_item_variations_artworks_update_multi_data_relationship413_response_body import SquareItemVariationsArtworksUpdateMultiDataRelationship413ResponseBody
from tidal.models.square_item_variations_artworks_update_multi_relationship_data_document import SquareItemVariationsArtworksUpdateMultiRelationshipDataDocument
from tidal.models.square_item_variations_create_operation_payload import SquareItemVariationsCreateOperationPayload
from tidal.models.square_item_variations_create_resource403_response_body import SquareItemVariationsCreateResource403ResponseBody
from tidal.models.square_item_variations_create_resource409_response_body import SquareItemVariationsCreateResource409ResponseBody
from tidal.models.square_item_variations_create_single_resource_data_document import SquareItemVariationsCreateSingleResourceDataDocument
from tidal.models.square_item_variations_delete_resource403_response_body import SquareItemVariationsDeleteResource403ResponseBody
from tidal.models.square_item_variations_delete_resource409_response_body import SquareItemVariationsDeleteResource409ResponseBody
from tidal.models.square_item_variations_owners_multi_relationship_data_document import SquareItemVariationsOwnersMultiRelationshipDataDocument
from tidal.models.square_item_variations_read_by_id403_response_body import SquareItemVariationsReadById403ResponseBody
from tidal.models.square_item_variations_read_by_id409_response_body import SquareItemVariationsReadById409ResponseBody
from tidal.models.square_item_variations_single_resource_data_document import SquareItemVariationsSingleResourceDataDocument
from tidal.models.square_item_variations_update_operation_payload import SquareItemVariationsUpdateOperationPayload
from tidal.models.square_item_variations_update_resource403_response_body import SquareItemVariationsUpdateResource403ResponseBody
from tidal.models.square_item_variations_update_resource409_response_body import SquareItemVariationsUpdateResource409ResponseBody
from tidal.models.square_item_variations_update_single_resource_data_document import SquareItemVariationsUpdateSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseSquareItemVariationsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSquareItemVariationsApi.subclasses = BaseSquareItemVariationsApi.subclasses + (cls,)
    async def operations_post(
        self,
        idempotency_key: Annotated[str, Field(min_length=1, max_length=128, description="Retry an unchanged request with the original key after a timeout or server error. Replay is bounded by downstream receipt and idempotency retention.")],
        atomic_operations_request: AtomicOperationsRequest,
    ) -> AtomicOperationsResponse:
        """Commits a supported group of resource creations together. Only add operations without ref or href are supported. Local linkage must reference an earlier creation. Each resource&#39;s mutation policy applies. After a timeout or server error, retry unchanged with the original Idempotency-Key. Replay is bounded by downstream receipt and idempotency retention."""
        ...


    async def square_item_variations_post(
        self,
        idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        square_item_variations_create_operation_payload: Optional[SquareItemVariationsCreateOperationPayload],
    ) -> SquareItemVariationsCreateSingleResourceDataDocument:
        """Adds a fixed-price variation at the end of the item&#39;s display order, preserving all existing variations and their pricing modes. After a timeout or &#x60;5xx&#x60;, retry unchanged with the original Idempotency-Key. Replay protection is bounded by receipt availability and Square&#39;s idempotency retention."""
        ...


    async def square_item_variations_id_get(
        self,
        id: Annotated[str, Field(description="Square variation id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks, owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> SquareItemVariationsSingleResourceDataDocument:
        """Retrieves single squareItemVariation by id."""
        ...


    async def square_item_variations_id_delete(
        self,
        id: Annotated[str, Field(description="Square variation id")],
        idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
    ) -> MutationResponseDocument:
        """Deletes this variation by ID without a revision precondition, preserving its siblings. The last variation cannot be deleted; delete the item instead. Returns an acknowledgement; read the parent item for its current revision. After a timeout or &#x60;5xx&#x60;, retry unchanged with the original Idempotency-Key. Replay protection is bounded by receipt availability and Square&#39;s idempotency retention."""
        ...


    async def square_item_variations_id_patch(
        self,
        id: Annotated[str, Field(description="Square variation id")],
        idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        square_item_variations_update_operation_payload: Optional[SquareItemVariationsUpdateOperationPayload],
    ) -> SquareItemVariationsUpdateSingleResourceDataDocument:
        """Updates the variation&#39;s global name or its price and stock tracking at the selected site&#39;s shipping location, with merchant-main fallback. Stock quantity is changed through physical-count submissions. Price changes require existing positive fixed pricing at that location; name and stock tracking preserve other pricing modes. After a timeout or &#x60;5xx&#x60;, retry unchanged with the original Idempotency-Key. Replay protection is bounded by receipt availability and Square&#39;s idempotency retention."""
        ...


    async def square_item_variations_id_relationships_artworks_get(
        self,
        id: Annotated[str, Field(description="Square variation id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> SquareItemVariationsArtworksMultiRelationshipDataDocument:
        """Artworks of the variation&#39;s Square catalog images in Square&#39;s display order. An image Square has no URL for stays in the list and its artwork has no files. Returns the variation revision the list was read at."""
        ...


    async def square_item_variations_id_relationships_artworks_patch(
        self,
        id: Annotated[str, Field(description="Square variation id")],
        idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        square_item_variations_artworks_relationship_update_operation_payload: Optional[SquareItemVariationsArtworksRelationshipUpdateOperationPayload],
    ) -> SquareItemVariationsArtworksUpdateMultiRelationshipDataDocument:
        """Replaces the variation&#39;s photos with the complete ordered list. Omitted photos are detached and stay in the seller&#39;s Square catalog; an empty list clears them. The first artwork is the primary photo. Duplicate artwork IDs are rejected. Uploaded TIDAL JPEG artworks, at most 15,000,000 bytes, are copied to Square and attached under new artwork IDs; their originals stay unchanged. Existing Square artworks must belong to this seller and are attached directly; they need not be the item&#39;s photos. Returns the complete resulting linkage in display order and the committed variation revision. Copies may remain in Square if the replacement fails. Retry unchanged with the original Idempotency-Key after a timeout or 5xx. Recovery is bounded by Marketplace receipts and Square&#39;s idempotency retention, and can be blocked if the variation is deleted or a source becomes unavailable or ineligible. Read the variation again to reconcile its current state."""
        ...


    async def square_item_variations_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Square variation id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> SquareItemVariationsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...
