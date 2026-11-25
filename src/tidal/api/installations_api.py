# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.installations_api_base import BaseInstallationsApi
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
from tidal.models.installations_create_operation_payload import InstallationsCreateOperationPayload
from tidal.models.installations_create_single_resource_data_document import InstallationsCreateSingleResourceDataDocument
from tidal.models.installations_multi_resource_data_document import InstallationsMultiResourceDataDocument
from tidal.models.installations_offline_inventory_multi_relationship_data_document import InstallationsOfflineInventoryMultiRelationshipDataDocument
from tidal.models.installations_offline_inventory_relationship_add_operation_payload import InstallationsOfflineInventoryRelationshipAddOperationPayload
from tidal.models.installations_offline_inventory_relationship_remove_operation_payload import InstallationsOfflineInventoryRelationshipRemoveOperationPayload
from tidal.models.installations_owners_multi_relationship_data_document import InstallationsOwnersMultiRelationshipDataDocument
from tidal.models.installations_single_resource_data_document import InstallationsSingleResourceDataDocument
from tidal.models.mutation_response_document import MutationResponseDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/installations",
    responses={
        200: {"model": InstallationsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["installations"],
    summary="Get multiple installations.",
    response_model_by_alias=True,
)
async def installations_get(
    filter_client_provided_installation_id: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="Client-provided installation identifier to filter by (e.g. `a468bee88def`)")] = Query(None, description="Client-provided installation identifier to filter by (e.g. &#x60;a468bee88def&#x60;)", alias="filter[clientProvidedInstallationId]"),
    filter_owners_id: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="User ID to filter by. Also accepts `me`.")] = Query(None, description="User ID to filter by. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: offlineInventory, owners")] = Query(None, description="Include related resources. Available relationships: offlineInventory, owners", alias="include", examples=["offlineInventory"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: offlineInventory")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: offlineInventory", alias="replaceMedia", examples=["offlineInventory"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> InstallationsMultiResourceDataDocument:
    """Retrieves multiple installations by available filters, or without if applicable."""
    if not BaseInstallationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseInstallationsApi.subclasses[0]().installations_get(filter_client_provided_installation_id, filter_owners_id, include, include_linkage, page_cursor, replace_media)


@router.post(
    "/installations",
    responses={
        201: {"model": InstallationsCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["installations"],
    summary="Create single installation.",
    response_model_by_alias=True,
)
async def installations_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    installations_create_operation_payload: Optional[InstallationsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> InstallationsCreateSingleResourceDataDocument:
    """Creates a new installation."""
    if not BaseInstallationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseInstallationsApi.subclasses[0]().installations_post(idempotency_key, installations_create_operation_payload)


@router.get(
    "/installations/{id}",
    responses={
        200: {"model": InstallationsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["installations"],
    summary="Get single installation.",
    response_model_by_alias=True,
)
async def installations_id_get(
    id: Annotated[str, Field(description="Installation id")] = Path(..., description="Installation id", examples=["a468bee88def"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: offlineInventory, owners")] = Query(None, description="Include related resources. Available relationships: offlineInventory, owners", alias="include", examples=["offlineInventory"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: offlineInventory")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: offlineInventory", alias="replaceMedia", examples=["offlineInventory"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> InstallationsSingleResourceDataDocument:
    """Retrieves single installation by id."""
    if not BaseInstallationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseInstallationsApi.subclasses[0]().installations_id_get(id, include, include_linkage, replace_media)


@router.get(
    "/installations/{id}/relationships/offlineInventory",
    responses={
        200: {"model": InstallationsOfflineInventoryMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["installations"],
    summary="Get offlineInventory relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def installations_id_relationships_offline_inventory_get(
    filter_type: Annotated[List[str], Field(description="One of: tracks, videos, albums, playlists, userCollectionTracks (e.g. `tracks`)")] = Query(..., description="One of: tracks, videos, albums, playlists, userCollectionTracks (e.g. &#x60;tracks&#x60;)", alias="filter[type]"),
    id: Annotated[str, Field(description="Installation id")] = Path(..., description="Installation id", examples=["a468bee88def"]),
    filter_client_storage_state: Annotated[Optional[List[str]], Field(description="One of: PENDING, STORED, FAILED (e.g. `PENDING`)")] = Query(None, description="One of: PENDING, STORED, FAILED (e.g. &#x60;PENDING&#x60;)", alias="filter[clientStorageState]"),
    filter_id: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="Offline item id (e.g. `1234`)")] = Query(None, description="Offline item id (e.g. &#x60;1234&#x60;)", alias="filter[id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: offlineInventory")] = Query(None, description="Include related resources. Available relationships: offlineInventory", alias="include", examples=["offlineInventory"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: offlineInventory")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: offlineInventory", alias="replaceMedia", examples=["offlineInventory"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> InstallationsOfflineInventoryMultiRelationshipDataDocument:
    """Retrieves offlineInventory relationship."""
    if not BaseInstallationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseInstallationsApi.subclasses[0]().installations_id_relationships_offline_inventory_get(filter_type, id, filter_client_storage_state, filter_id, include, page_cursor, replace_media)


@router.post(
    "/installations/{id}/relationships/offlineInventory",
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
    tags=["installations"],
    summary="Add to offlineInventory relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def installations_id_relationships_offline_inventory_post(
    id: Annotated[str, Field(description="Installation id")] = Path(..., description="Installation id", examples=["a468bee88def"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    installations_offline_inventory_relationship_add_operation_payload: Optional[InstallationsOfflineInventoryRelationshipAddOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Adds item(s) to offlineInventory relationship."""
    if not BaseInstallationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseInstallationsApi.subclasses[0]().installations_id_relationships_offline_inventory_post(id, idempotency_key, installations_offline_inventory_relationship_add_operation_payload)


@router.delete(
    "/installations/{id}/relationships/offlineInventory",
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
    tags=["installations"],
    summary="Delete from offlineInventory relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def installations_id_relationships_offline_inventory_delete(
    id: Annotated[str, Field(description="Installation id")] = Path(..., description="Installation id", examples=["a468bee88def"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    installations_offline_inventory_relationship_remove_operation_payload: Optional[InstallationsOfflineInventoryRelationshipRemoveOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes item(s) from offlineInventory relationship."""
    if not BaseInstallationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseInstallationsApi.subclasses[0]().installations_id_relationships_offline_inventory_delete(id, idempotency_key, installations_offline_inventory_relationship_remove_operation_payload)


@router.get(
    "/installations/{id}/relationships/owners",
    responses={
        200: {"model": InstallationsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["installations"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def installations_id_relationships_owners_get(
    id: Annotated[str, Field(description="Installation id")] = Path(..., description="Installation id", examples=["a468bee88def"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> InstallationsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseInstallationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseInstallationsApi.subclasses[0]().installations_id_relationships_owners_get(id, include, page_cursor)
