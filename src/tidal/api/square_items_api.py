# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.square_items_api_base import BaseSquareItemsApi
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
    if not BaseSquareItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemsApi.subclasses[0]().operations_post(idempotency_key, atomic_operations_request)


@router.get(
    "/squareItems",
    responses={
        200: {"model": SquareItemsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareItemsReadByFilter403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareItemsReadByFilter409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItems"],
    summary="Get multiple squareItems.",
    response_model_by_alias=True,
)
async def square_items_get(
    filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="User id. Also accepts `me`.")] = Query(..., description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    filter_origin: Annotated[Optional[str], Field(description="Only items with this origin (e.g. `TIDAL`)")] = Query(None, description="Only items with this origin (e.g. &#x60;TIDAL&#x60;)", alias="filter[origin]"),
    filter_self_matches_query: Annotated[Optional[Annotated[str, Field(min_length=1, max_length=255)]], Field(description="Word-prefix match on item titles, descriptions and abbreviations, and on variation names, SKUs and UPCs (e.g. `tee`)")] = Query(None, description="Word-prefix match on item titles, descriptions and abbreviations, and on variation names, SKUs and UPCs (e.g. &#x60;tee&#x60;)", alias="filter[self][matchesQuery]", min_length=1, max_length=255),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks, owners, variations")] = Query(None, description="Include related resources. Available relationships: artworks, owners, variations", alias="include", examples=["artworks"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> SquareItemsMultiResourceDataDocument:
    """Retrieves multiple squareItems by available filters, or without if applicable."""
    if not BaseSquareItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemsApi.subclasses[0]().square_items_get(filter_owners_id, filter_origin, filter_self_matches_query, include, include_linkage, page_cursor)


@router.get(
    "/squareItems/{id}",
    responses={
        200: {"model": SquareItemsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareItemsReadById403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareItemsReadById409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItems"],
    summary="Get single squareItem.",
    response_model_by_alias=True,
)
async def square_items_id_get(
    id: Annotated[str, Field(description="Square item id")] = Path(..., description="Square item id", examples=["p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks, owners, variations")] = Query(None, description="Include related resources. Available relationships: artworks, owners, variations", alias="include", examples=["artworks"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> SquareItemsSingleResourceDataDocument:
    """Retrieves single squareItem by id."""
    if not BaseSquareItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemsApi.subclasses[0]().square_items_id_get(id, include, include_linkage)


@router.delete(
    "/squareItems/{id}",
    responses={
        200: {"model": MutationResponseDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareItemsDeleteResource403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareItemsDeleteResource409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Another request is changing the Square catalog; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItems"],
    summary="Delete single squareItem.",
    response_model_by_alias=True,
)
async def square_items_id_delete(
    id: Annotated[str, Field(description="Square item id")] = Path(..., description="Square item id", examples=["p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing squareItem."""
    if not BaseSquareItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemsApi.subclasses[0]().square_items_id_delete(id, idempotency_key)


@router.patch(
    "/squareItems/{id}",
    responses={
        200: {"model": SquareItemsUpdateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareItemsUpdateResource403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareItemsUpdateResource409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Another request is changing the Square catalog; Square catalog item changed; reload it before editing; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItems"],
    summary="Update single squareItem.",
    response_model_by_alias=True,
)
async def square_items_id_patch(
    id: Annotated[str, Field(description="Square item id")] = Path(..., description="Square item id", examples=["p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay"]),
    idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(..., description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    square_items_update_operation_payload: Optional[SquareItemsUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> SquareItemsUpdateSingleResourceDataDocument:
    """Updates existing squareItem."""
    if not BaseSquareItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemsApi.subclasses[0]().square_items_id_patch(id, idempotency_key, square_items_update_operation_payload)


@router.get(
    "/squareItems/{id}/relationships/artworks",
    responses={
        200: {"model": SquareItemsArtworksMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareItemsArtworksReadMultiDataRelationship409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItems"],
    summary="Get artworks relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def square_items_id_relationships_artworks_get(
    id: Annotated[str, Field(description="Square item id")] = Path(..., description="Square item id", examples=["p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks")] = Query(None, description="Include related resources. Available relationships: artworks", alias="include", examples=["artworks"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> SquareItemsArtworksMultiRelationshipDataDocument:
    """A photo Square has no URL for stays in the list and its artwork has no files."""
    if not BaseSquareItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemsApi.subclasses[0]().square_items_id_relationships_artworks_get(id, include, page_cursor)


@router.patch(
    "/squareItems/{id}/relationships/artworks",
    responses={
        200: {"model": SquareItemsArtworksUpdateMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareItemsArtworksUpdateMultiDataRelationship403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareItemsArtworksUpdateMultiDataRelationship409ResponseBody, "description": "Square item changed; reload it before editing its artworks; Another request is changing the Square catalog; Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Request already in progress for this idempotency key"},
        413: {"model": SquareItemsArtworksUpdateMultiDataRelationship413ResponseBody, "description": "Square images must be at most 15 MB (15,000,000 bytes)"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItems"],
    summary="Update artworks relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def square_items_id_relationships_artworks_patch(
    id: Annotated[str, Field(description="Square item id")] = Path(..., description="Square item id", examples=["p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay"]),
    idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(..., description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    square_items_artworks_relationship_update_operation_payload: Optional[SquareItemsArtworksRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> SquareItemsArtworksUpdateMultiRelationshipDataDocument:
    """Replaces the item&#39;s photos with the complete ordered list. Omitted photos are detached and stay in the seller&#39;s Square catalog; an empty list clears them. The first artwork is the primary photo. Duplicate artwork IDs are rejected. Uploaded TIDAL JPEG artworks, at most 15,000,000 bytes, are copied to Square and attached under new artwork IDs; their originals stay unchanged. Existing Square artworks must belong to this seller and are attached directly. Returns the complete resulting linkage in display order and the committed item revision. Copies may remain in Square if the replacement fails. Retry unchanged with the original Idempotency-Key after a timeout or 5xx. Recovery is bounded by Marketplace receipts and Square&#39;s idempotency retention, and can be blocked if the item is deleted or a source becomes unavailable or ineligible. Read the item again to reconcile its current state."""
    if not BaseSquareItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemsApi.subclasses[0]().square_items_id_relationships_artworks_patch(id, idempotency_key, square_items_artworks_relationship_update_operation_payload)


@router.get(
    "/squareItems/{id}/relationships/owners",
    responses={
        200: {"model": SquareItemsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItems"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def square_items_id_relationships_owners_get(
    id: Annotated[str, Field(description="Square item id")] = Path(..., description="Square item id", examples=["p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> SquareItemsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseSquareItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemsApi.subclasses[0]().square_items_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/squareItems/{id}/relationships/variations",
    responses={
        200: {"model": SquareItemsVariationsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareItemsVariationsReadMultiDataRelationship403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareItemsVariationsReadMultiDataRelationship409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItems"],
    summary="Get variations relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def square_items_id_relationships_variations_get(
    id: Annotated[str, Field(description="Square item id")] = Path(..., description="Square item id", examples=["p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: variations")] = Query(None, description="Include related resources. Available relationships: variations", alias="include", examples=["variations"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> SquareItemsVariationsMultiRelationshipDataDocument:
    """Variations in Square&#39;s display order."""
    if not BaseSquareItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemsApi.subclasses[0]().square_items_id_relationships_variations_get(id, include, page_cursor)


@router.patch(
    "/squareItems/{id}/relationships/variations",
    responses={
        200: {"model": SquareItemsVariationsUpdateMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareItemsVariationsUpdateMultiDataRelationship403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareItemsVariationsUpdateMultiDataRelationship409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Square catalog item changed; reload it before editing; Another request is changing the Square catalog; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareItems"],
    summary="Update variations relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def square_items_id_relationships_variations_patch(
    id: Annotated[str, Field(description="Square item id")] = Path(..., description="Square item id", examples=["p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay"]),
    idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(..., description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    square_items_variations_relationship_update_operation_payload: Optional[SquareItemsVariationsRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> SquareItemsVariationsUpdateMultiRelationshipDataDocument:
    """Incrementally moves the selected variations as an ordered block before positionBefore, or to the end when omitted. Memberships are preserved; unselected variations retain their metadata and relative order. Empty data is rejected. Returns the affected linkage only and the updated item revision. After a timeout or &#x60;5xx&#x60;, retry unchanged with the original Idempotency-Key. Replay protection is bounded by receipt availability and Square&#39;s idempotency retention."""
    if not BaseSquareItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareItemsApi.subclasses[0]().square_items_id_relationships_variations_patch(id, idempotency_key, square_items_variations_relationship_update_operation_payload)
