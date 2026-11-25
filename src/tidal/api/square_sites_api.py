# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.square_sites_api_base import BaseSquareSitesApi
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
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/squareSites/{id}/relationships/items",
    responses={
        200: {"model": SquareSitesItemsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareSitesItemsReadMultiDataRelationship403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareSitesItemsReadMultiDataRelationship409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect; The site isn&#39;t the seller&#39;s selected Square Online site; select it to manage its items"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareSites"],
    summary="Get items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def square_sites_id_relationships_items_get(
    id: Annotated[str, Field(description="Square Online site id")] = Path(..., description="Square Online site id", examples=["IhETt7taHSVV2MUu9kqjMDengjnhVZa"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")] = Query(None, description="Include related resources. Available relationships: items", alias="include", examples=["items"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> SquareSitesItemsMultiRelationshipDataDocument:
    """Items published in the site, in title order. Missing catalog scopes return MISSING_ITEMS_SCOPE. A page can be short or empty and still have a next cursor."""
    if not BaseSquareSitesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareSitesApi.subclasses[0]().square_sites_id_relationships_items_get(id, include, page_cursor)


@router.post(
    "/squareSites/{id}/relationships/items",
    responses={
        200: {"model": MutationResponseDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareSitesItemsAddMultiDataRelationship403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareSitesItemsAddMultiDataRelationship409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Another request is changing the Square catalog; The site isn&#39;t the seller&#39;s selected Square Online site; select it to manage its items; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareSites"],
    summary="Add to items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def square_sites_id_relationships_items_post(
    id: Annotated[str, Field(description="Square Online site id")] = Path(..., description="Square Online site id", examples=["IhETt7taHSVV2MUu9kqjMDengjnhVZa"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    square_sites_items_relationship_add_operation_payload: Optional[SquareSitesItemsRelationshipAddOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Publishes the items in the site. Items already published and repeated items are left alone. An item missing from the catalog fails the request before anything changes."""
    if not BaseSquareSitesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareSitesApi.subclasses[0]().square_sites_id_relationships_items_post(id, idempotency_key, square_sites_items_relationship_add_operation_payload)


@router.delete(
    "/squareSites/{id}/relationships/items",
    responses={
        200: {"model": MutationResponseDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareSitesItemsRemoveMultiDataRelationship403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareSitesItemsRemoveMultiDataRelationship409ResponseBody, "description": "Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Another request is changing the Square catalog; The site isn&#39;t the seller&#39;s selected Square Online site; select it to manage its items; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareSites"],
    summary="Delete from items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def square_sites_id_relationships_items_delete(
    id: Annotated[str, Field(description="Square Online site id")] = Path(..., description="Square Online site id", examples=["IhETt7taHSVV2MUu9kqjMDengjnhVZa"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    square_sites_items_relationship_remove_operation_payload: Optional[SquareSitesItemsRelationshipRemoveOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Removes the items from the site; they stay in the catalog. Items not published and repeated items are left alone. An item missing from the catalog fails the request before anything changes."""
    if not BaseSquareSitesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareSitesApi.subclasses[0]().square_sites_id_relationships_items_delete(id, idempotency_key, square_sites_items_relationship_remove_operation_payload)
