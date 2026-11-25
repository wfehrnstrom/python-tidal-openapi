# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.square_item_variations_api_base import BaseSquareItemVariationsApi
import tidal.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

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
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/operations",
    responses={
        200: {"model": AtomicOperationsResponse, "description": "Committed results, in the order of the requested operations"},
        400: {"model": AtomicOperations400ResponseBody, "description": "Invalid request"},
        403: {"model": AtomicOperations403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": AtomicOperations404ResponseBody, "description": "Resource not found"},
        405: {"model": AtomicOperations405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": AtomicOperations406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": AtomicOperations409ResponseBody, "description": "Request already in progress for this idempotency key; Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Another request is changing the Square catalog; The site isn&#39;t the seller&#39;s selected Square Online site; select it to manage its items"},
        415: {"model": AtomicOperations415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": AtomicOperations422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": AtomicOperations429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": AtomicOperations500ResponseBody, "description": "Internal server error"},
        503: {"model": AtomicOperations503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItemVariations","squareItems"],
    summary="Commit atomic resource operations",
    response_model_by_alias=True,
)
async def operations_post(
    idempotency_key: Annotated[str, Field(min_length=1, max_length=128, description="Retry an unchanged request with the original key after a timeout or server error. Replay is bounded by downstream receipt and idempotency retention.")] = Header(..., description="Retry an unchanged request with the original key after a timeout or server error. Replay is bounded by downstream receipt and idempotency retention.", min_length=1, max_length=128),
    atomic_operations_request: AtomicOperationsRequest = Body(..., description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> AtomicOperationsResponse:
    """Commits a supported group of resource creations together. Only add operations without ref or href are supported. Local linkage must reference an earlier creation. Each resource&#39;s mutation policy applies. After a timeout or server error, retry unchanged with the original Idempotency-Key. Replay is bounded by downstream receipt and idempotency retention."""
    if not BaseSquareItemVariationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemVariationsApi.subclasses[0]().operations_post(idempotency_key, atomic_operations_request)


@router.post(
    "/squareItemVariations",
    responses={
        201: {"model": SquareItemVariationsCreateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareItemVariationsCreateResource403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareItemVariationsCreateResource409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Square item changed; reload it before changing its variations; Another request is changing the Square catalog; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItemVariations"],
    summary="Create single squareItemVariation.",
    response_model_by_alias=True,
)
async def square_item_variations_post(
    idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(..., description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    square_item_variations_create_operation_payload: Optional[SquareItemVariationsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> SquareItemVariationsCreateSingleResourceDataDocument:
    """Adds a fixed-price variation at the end of the item&#39;s display order, preserving all existing variations and their pricing modes. After a timeout or &#x60;5xx&#x60;, retry unchanged with the original Idempotency-Key. Replay protection is bounded by receipt availability and Square&#39;s idempotency retention."""
    if not BaseSquareItemVariationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemVariationsApi.subclasses[0]().square_item_variations_post(idempotency_key, square_item_variations_create_operation_payload)


@router.get(
    "/squareItemVariations/{id}",
    responses={
        200: {"model": SquareItemVariationsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareItemVariationsReadById403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareItemVariationsReadById409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItemVariations"],
    summary="Get single squareItemVariation.",
    response_model_by_alias=True,
)
async def square_item_variations_id_get(
    id: Annotated[str, Field(description="Square variation id")] = Path(..., description="Square variation id", examples=["p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks, owners")] = Query(None, description="Include related resources. Available relationships: artworks, owners", alias="include", examples=["artworks"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> SquareItemVariationsSingleResourceDataDocument:
    """Retrieves single squareItemVariation by id."""
    if not BaseSquareItemVariationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemVariationsApi.subclasses[0]().square_item_variations_id_get(id, include, include_linkage)


@router.delete(
    "/squareItemVariations/{id}",
    responses={
        200: {"model": MutationResponseDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareItemVariationsDeleteResource403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareItemVariationsDeleteResource409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Square item changed; reload it before changing its variations; An item must retain at least one variation; Another request is changing the Square catalog; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItemVariations"],
    summary="Delete single squareItemVariation.",
    response_model_by_alias=True,
)
async def square_item_variations_id_delete(
    id: Annotated[str, Field(description="Square variation id")] = Path(..., description="Square variation id", examples=["p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm"]),
    idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(..., description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes this variation by ID without a revision precondition, preserving its siblings. The last variation cannot be deleted; delete the item instead. Returns an acknowledgement; read the parent item for its current revision. After a timeout or &#x60;5xx&#x60;, retry unchanged with the original Idempotency-Key. Replay protection is bounded by receipt availability and Square&#39;s idempotency retention."""
    if not BaseSquareItemVariationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemVariationsApi.subclasses[0]().square_item_variations_id_delete(id, idempotency_key)


@router.patch(
    "/squareItemVariations/{id}",
    responses={
        200: {"model": SquareItemVariationsUpdateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareItemVariationsUpdateResource403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareItemVariationsUpdateResource409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Square variation changed; reload it before editing; This variation&#39;s pricing cannot be edited here; edit it in Square Dashboard; Another request is changing the Square catalog; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItemVariations"],
    summary="Update single squareItemVariation.",
    response_model_by_alias=True,
)
async def square_item_variations_id_patch(
    id: Annotated[str, Field(description="Square variation id")] = Path(..., description="Square variation id", examples=["p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm"]),
    idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(..., description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    square_item_variations_update_operation_payload: Optional[SquareItemVariationsUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> SquareItemVariationsUpdateSingleResourceDataDocument:
    """Updates the variation&#39;s global name or its price and stock tracking at the selected site&#39;s shipping location, with merchant-main fallback. Stock quantity is changed through physical-count submissions. Price changes require existing positive fixed pricing at that location; name and stock tracking preserve other pricing modes. After a timeout or &#x60;5xx&#x60;, retry unchanged with the original Idempotency-Key. Replay protection is bounded by receipt availability and Square&#39;s idempotency retention."""
    if not BaseSquareItemVariationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemVariationsApi.subclasses[0]().square_item_variations_id_patch(id, idempotency_key, square_item_variations_update_operation_payload)


@router.get(
    "/squareItemVariations/{id}/relationships/artworks",
    responses={
        200: {"model": SquareItemVariationsArtworksMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareItemVariationsArtworksReadMultiDataRelationship403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareItemVariationsArtworksReadMultiDataRelationship409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Another request is changing the Square catalog"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItemVariations"],
    summary="Get artworks relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def square_item_variations_id_relationships_artworks_get(
    id: Annotated[str, Field(description="Square variation id")] = Path(..., description="Square variation id", examples=["p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks")] = Query(None, description="Include related resources. Available relationships: artworks", alias="include", examples=["artworks"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> SquareItemVariationsArtworksMultiRelationshipDataDocument:
    """Artworks of the variation&#39;s Square catalog images in Square&#39;s display order. An image Square has no URL for stays in the list and its artwork has no files. Returns the variation revision the list was read at."""
    if not BaseSquareItemVariationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemVariationsApi.subclasses[0]().square_item_variations_id_relationships_artworks_get(id, include, page_cursor)


@router.patch(
    "/squareItemVariations/{id}/relationships/artworks",
    responses={
        200: {"model": SquareItemVariationsArtworksUpdateMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareItemVariationsArtworksUpdateMultiDataRelationship403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareItemVariationsArtworksUpdateMultiDataRelationship409ResponseBody, "description": "Square variation changed; reload it before editing its artworks; Another request is changing the Square catalog; Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Request already in progress for this idempotency key"},
        413: {"model": SquareItemVariationsArtworksUpdateMultiDataRelationship413ResponseBody, "description": "Square images must be at most 15 MB (15,000,000 bytes)"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItemVariations"],
    summary="Update artworks relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def square_item_variations_id_relationships_artworks_patch(
    id: Annotated[str, Field(description="Square variation id")] = Path(..., description="Square variation id", examples=["p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm"]),
    idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(..., description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    square_item_variations_artworks_relationship_update_operation_payload: Optional[SquareItemVariationsArtworksRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> SquareItemVariationsArtworksUpdateMultiRelationshipDataDocument:
    """Replaces the variation&#39;s photos with the complete ordered list. Omitted photos are detached and stay in the seller&#39;s Square catalog; an empty list clears them. The first artwork is the primary photo. Duplicate artwork IDs are rejected. Uploaded TIDAL JPEG artworks, at most 15,000,000 bytes, are copied to Square and attached under new artwork IDs; their originals stay unchanged. Existing Square artworks must belong to this seller and are attached directly; they need not be the item&#39;s photos. Returns the complete resulting linkage in display order and the committed variation revision. Copies may remain in Square if the replacement fails. Retry unchanged with the original Idempotency-Key after a timeout or 5xx. Recovery is bounded by Marketplace receipts and Square&#39;s idempotency retention, and can be blocked if the variation is deleted or a source becomes unavailable or ineligible. Read the variation again to reconcile its current state."""
    if not BaseSquareItemVariationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemVariationsApi.subclasses[0]().square_item_variations_id_relationships_artworks_patch(id, idempotency_key, square_item_variations_artworks_relationship_update_operation_payload)


@router.get(
    "/squareItemVariations/{id}/relationships/owners",
    responses={
        200: {"model": SquareItemVariationsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItemVariations"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def square_item_variations_id_relationships_owners_get(
    id: Annotated[str, Field(description="Square variation id")] = Path(..., description="Square variation id", examples=["p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> SquareItemVariationsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseSquareItemVariationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemVariationsApi.subclasses[0]().square_item_variations_id_relationships_owners_get(id, include, page_cursor)
