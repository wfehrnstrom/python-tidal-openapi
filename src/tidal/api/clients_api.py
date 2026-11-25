# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.clients_api_base import BaseClientsApi
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
from tidal.models.clients_certificates_multi_relationship_data_document import ClientsCertificatesMultiRelationshipDataDocument
from tidal.models.clients_create_operation_payload import ClientsCreateOperationPayload
from tidal.models.clients_create_single_resource_data_document import ClientsCreateSingleResourceDataDocument
from tidal.models.clients_multi_resource_data_document import ClientsMultiResourceDataDocument
from tidal.models.clients_owners_multi_relationship_data_document import ClientsOwnersMultiRelationshipDataDocument
from tidal.models.clients_single_resource_data_document import ClientsSingleResourceDataDocument
from tidal.models.clients_update_operation_payload import ClientsUpdateOperationPayload
from tidal.models.clients_update_single_resource_data_document import ClientsUpdateSingleResourceDataDocument
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
from tidal.models.mutation_response_document import MutationResponseDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/clients",
    responses={
        200: {"model": ClientsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["clients"],
    summary="Get multiple clients.",
    response_model_by_alias=True,
)
async def clients_get(
    filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="User id. Also accepts `me`.")] = Query(..., description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: certificates, owners")] = Query(None, description="Include related resources. Available relationships: certificates, owners", alias="include", examples=["certificates"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ClientsMultiResourceDataDocument:
    """Retrieves multiple clients by available filters, or without if applicable."""
    if not BaseClientsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseClientsApi.subclasses[0]().clients_get(filter_owners_id, include, include_linkage)


@router.post(
    "/clients",
    responses={
        201: {"model": ClientsCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["clients"],
    summary="Create single client.",
    response_model_by_alias=True,
)
async def clients_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    clients_create_operation_payload: Optional[ClientsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> ClientsCreateSingleResourceDataDocument:
    """Creates a new client."""
    if not BaseClientsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseClientsApi.subclasses[0]().clients_post(idempotency_key, clients_create_operation_payload)


@router.get(
    "/clients/{id}",
    responses={
        200: {"model": ClientsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["clients"],
    summary="Get single client.",
    response_model_by_alias=True,
)
async def clients_id_get(
    id: Annotated[str, Field(description="OAuth client identifier")] = Path(..., description="OAuth client identifier", examples=["a468bee88def"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: certificates, owners")] = Query(None, description="Include related resources. Available relationships: certificates, owners", alias="include", examples=["certificates"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ClientsSingleResourceDataDocument:
    """Retrieves single client by id."""
    if not BaseClientsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseClientsApi.subclasses[0]().clients_id_get(id, include, include_linkage)


@router.delete(
    "/clients/{id}",
    responses={
        200: {"model": MutationResponseDocument, "description": "Successful response"},
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
    tags=["clients"],
    summary="Delete single client.",
    response_model_by_alias=True,
)
async def clients_id_delete(
    id: Annotated[str, Field(description="OAuth client identifier")] = Path(..., description="OAuth client identifier", examples=["a468bee88def"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing client."""
    if not BaseClientsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseClientsApi.subclasses[0]().clients_id_delete(id, idempotency_key)


@router.patch(
    "/clients/{id}",
    responses={
        200: {"model": ClientsUpdateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["clients"],
    summary="Update single client.",
    response_model_by_alias=True,
)
async def clients_id_patch(
    id: Annotated[str, Field(description="OAuth client identifier")] = Path(..., description="OAuth client identifier", examples=["a468bee88def"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    clients_update_operation_payload: Optional[ClientsUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> ClientsUpdateSingleResourceDataDocument:
    """Updates existing client."""
    if not BaseClientsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseClientsApi.subclasses[0]().clients_id_patch(id, idempotency_key, clients_update_operation_payload)


@router.get(
    "/clients/{id}/relationships/certificates",
    responses={
        200: {"model": ClientsCertificatesMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["clients"],
    summary="Get certificates relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def clients_id_relationships_certificates_get(
    id: Annotated[str, Field(description="OAuth client identifier")] = Path(..., description="OAuth client identifier", examples=["a468bee88def"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: certificates")] = Query(None, description="Include related resources. Available relationships: certificates", alias="include", examples=["certificates"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ClientsCertificatesMultiRelationshipDataDocument:
    """Retrieves certificates relationship."""
    if not BaseClientsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseClientsApi.subclasses[0]().clients_id_relationships_certificates_get(id, include, page_cursor)


@router.get(
    "/clients/{id}/relationships/owners",
    responses={
        200: {"model": ClientsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["clients"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def clients_id_relationships_owners_get(
    id: Annotated[str, Field(description="OAuth client identifier")] = Path(..., description="OAuth client identifier", examples=["a468bee88def"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ClientsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseClientsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseClientsApi.subclasses[0]().clients_id_relationships_owners_get(id, include, page_cursor)
