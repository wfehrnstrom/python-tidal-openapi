# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.square_connections_api_base import BaseSquareConnectionsApi
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
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/squareConnections",
    responses={
        201: {"model": SquareConnectionsCreateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": Idempotency409ResponseBody, "description": "Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareConnections"],
    summary="Create single squareConnection.",
    response_model_by_alias=True,
)
async def square_connections_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    square_connections_create_operation_payload: Optional[SquareConnectionsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> SquareConnectionsCreateSingleResourceDataDocument:
    """Creates a new squareConnection."""
    if not BaseSquareConnectionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareConnectionsApi.subclasses[0]().square_connections_post(idempotency_key, square_connections_create_operation_payload)


@router.get(
    "/squareConnections/{id}",
    responses={
        200: {"model": SquareConnectionsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareConnectionsReadById403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareConnections"],
    summary="Get single squareConnection.",
    response_model_by_alias=True,
)
async def square_connections_id_get(
    id: Annotated[str, Field(description="Square connection id. Use `me` for the authenticated user's resource")] = Path(..., description="Square connection id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: selectedSite, sites")] = Query(None, description="Include related resources. Available relationships: selectedSite, sites", alias="include", examples=["selectedSite"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> SquareConnectionsSingleResourceDataDocument:
    """Retrieves single squareConnection by id."""
    if not BaseSquareConnectionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareConnectionsApi.subclasses[0]().square_connections_id_get(id, include, include_linkage)


@router.get(
    "/squareConnections/{id}/relationships/selectedSite",
    responses={
        200: {"model": SquareConnectionsSelectedSiteSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareConnectionsSelectedSiteReadSingleDataRelationship403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareConnections"],
    summary="Get selectedSite relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def square_connections_id_relationships_selected_site_get(
    id: Annotated[str, Field(description="Square connection id. Use `me` for the authenticated user's resource")] = Path(..., description="Square connection id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: selectedSite")] = Query(None, description="Include related resources. Available relationships: selectedSite", alias="include", examples=["selectedSite"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> SquareConnectionsSelectedSiteSingleRelationshipDataDocument:
    """Retrieves selectedSite relationship."""
    if not BaseSquareConnectionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareConnectionsApi.subclasses[0]().square_connections_id_relationships_selected_site_get(id, include)


@router.patch(
    "/squareConnections/{id}/relationships/selectedSite",
    responses={
        200: {"model": SquareConnectionsSelectedSiteUpdateSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareConnectionsSelectedSiteUpdateSingleDataRelationship403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": SquareConnectionsSelectedSiteUpdateSingleDataRelationship409ResponseBody, "description": "Square credential lacks required site scopes; run Square onboarding again; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareConnections"],
    summary="Update selectedSite relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def square_connections_id_relationships_selected_site_patch(
    id: Annotated[str, Field(description="Square connection id. Use `me` for the authenticated user's resource")] = Path(..., description="Square connection id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    square_connections_selected_site_relationship_update_operation_payload: Optional[SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> SquareConnectionsSelectedSiteUpdateSingleRelationshipDataDocument:
    """Replaces the selected Square site. Explicit null data clears the selection without deleting the site. Returns the selected site linkage, or null data when cleared."""
    if not BaseSquareConnectionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareConnectionsApi.subclasses[0]().square_connections_id_relationships_selected_site_patch(id, idempotency_key, square_connections_selected_site_relationship_update_operation_payload)


@router.get(
    "/squareConnections/{id}/relationships/sites",
    responses={
        200: {"model": SquareConnectionsSitesMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": SquareConnectionsSitesReadMultiDataRelationship403ResponseBody, "description": "Latest terms and conditions must be accepted"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["squareConnections"],
    summary="Get sites relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def square_connections_id_relationships_sites_get(
    id: Annotated[str, Field(description="Square connection id. Use `me` for the authenticated user's resource")] = Path(..., description="Square connection id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: sites")] = Query(None, description="Include related resources. Available relationships: sites", alias="include", examples=["sites"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> SquareConnectionsSitesMultiRelationshipDataDocument:
    """Retrieves sites relationship."""
    if not BaseSquareConnectionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSquareConnectionsApi.subclasses[0]().square_connections_id_relationships_sites_get(id, include, page_cursor)
