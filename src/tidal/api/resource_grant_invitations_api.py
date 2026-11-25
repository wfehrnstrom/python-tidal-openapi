# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.resource_grant_invitations_api_base import BaseResourceGrantInvitationsApi
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
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.resource_grant_invitations_create_operation_payload import ResourceGrantInvitationsCreateOperationPayload
from tidal.models.resource_grant_invitations_create_single_resource_data_document import ResourceGrantInvitationsCreateSingleResourceDataDocument
from tidal.models.resource_grant_invitations_multi_resource_data_document import ResourceGrantInvitationsMultiResourceDataDocument
from tidal.models.resource_grant_invitations_owners_multi_relationship_data_document import ResourceGrantInvitationsOwnersMultiRelationshipDataDocument
from tidal.models.resource_grant_invitations_preview_grant_single_relationship_data_document import ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument
from tidal.models.resource_grant_invitations_single_resource_data_document import ResourceGrantInvitationsSingleResourceDataDocument
from tidal.models.resource_grant_invitations_subject_single_relationship_data_document import ResourceGrantInvitationsSubjectSingleRelationshipDataDocument
from tidal.models.resource_grant_invitations_update_operation_payload import ResourceGrantInvitationsUpdateOperationPayload
from tidal.models.resource_grant_invitations_update_single_resource_data_document import ResourceGrantInvitationsUpdateSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/resourceGrantInvitations",
    responses={
        200: {"model": ResourceGrantInvitationsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["resourceGrantInvitations"],
    summary="Get multiple resourceGrantInvitations.",
    response_model_by_alias=True,
)
async def resource_grant_invitations_get(
    filter_code: Annotated[Optional[Annotated[str, Field(min_length=1)]], Field(description="Invitation code (e.g. `42179b73-6f0c-405c-b926-2fdb45363c44`)")] = Query(None, description="Invitation code (e.g. &#x60;42179b73-6f0c-405c-b926-2fdb45363c44&#x60;)", alias="filter[code]", min_length=1),
    filter_self_applies_to: Annotated[Optional[str], Field(description="Album, track or folder owned by the caller. Selects undeleted, unexpired invitations on the resource or its ancestors; used-up ones are included. Each keeps its own subject. Cannot be combined with other filters. Missing or non-owned resources and subjects without a live access node return no records. Ordered by expiry then ID; at most 20 invitations per page. Also accepts `folders:me`.")] = Query(None, description="Album, track or folder owned by the caller. Selects undeleted, unexpired invitations on the resource or its ancestors; used-up ones are included. Each keeps its own subject. Cannot be combined with other filters. Missing or non-owned resources and subjects without a live access node return no records. Ordered by expiry then ID; at most 20 invitations per page. Also accepts &#x60;folders:me&#x60;.", alias="filter[self][appliesTo]", regex=r"^(?:tracks|albums|folders):[^,]+$"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, previewGrant, subject")] = Query(None, description="Include related resources. Available relationships: owners, previewGrant, subject", alias="include", examples=["previewGrant.subject"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: previewGrant.subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: previewGrant.subject", alias="replaceMedia", examples=["previewGrant.subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ResourceGrantInvitationsMultiResourceDataDocument:
    """Retrieves multiple resourceGrantInvitations by available filters, or without if applicable."""
    if not BaseResourceGrantInvitationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantInvitationsApi.subclasses[0]().resource_grant_invitations_get(filter_code, filter_self_applies_to, include, include_linkage, page_cursor, replace_media)


@router.post(
    "/resourceGrantInvitations",
    responses={
        201: {"model": ResourceGrantInvitationsCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["resourceGrantInvitations"],
    summary="Create single resourceGrantInvitation.",
    response_model_by_alias=True,
)
async def resource_grant_invitations_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    resource_grant_invitations_create_operation_payload: Optional[ResourceGrantInvitationsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> ResourceGrantInvitationsCreateSingleResourceDataDocument:
    """Creates a new resourceGrantInvitation."""
    if not BaseResourceGrantInvitationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantInvitationsApi.subclasses[0]().resource_grant_invitations_post(idempotency_key, resource_grant_invitations_create_operation_payload)


@router.get(
    "/resourceGrantInvitations/{id}",
    responses={
        200: {"model": ResourceGrantInvitationsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["resourceGrantInvitations"],
    summary="Get single resourceGrantInvitation.",
    response_model_by_alias=True,
)
async def resource_grant_invitations_id_get(
    id: Annotated[str, Field(description="Invitation id")] = Path(..., description="Invitation id", examples=["e0163a07-8eee-4d30-ae44-75d44b1e47b0"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, previewGrant, subject")] = Query(None, description="Include related resources. Available relationships: owners, previewGrant, subject", alias="include", examples=["previewGrant.subject"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: previewGrant.subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: previewGrant.subject", alias="replaceMedia", examples=["previewGrant.subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ResourceGrantInvitationsSingleResourceDataDocument:
    """Retrieves single resourceGrantInvitation by id."""
    if not BaseResourceGrantInvitationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantInvitationsApi.subclasses[0]().resource_grant_invitations_id_get(id, include, include_linkage, replace_media)


@router.delete(
    "/resourceGrantInvitations/{id}",
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
    tags=["resourceGrantInvitations"],
    summary="Delete single resourceGrantInvitation.",
    response_model_by_alias=True,
)
async def resource_grant_invitations_id_delete(
    id: Annotated[str, Field(description="Invitation id")] = Path(..., description="Invitation id", examples=["e0163a07-8eee-4d30-ae44-75d44b1e47b0"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    revoke_grants: Annotated[Optional[bool], Field(description="Also revoke the grants redemptions issued; access from other sources stays. Defaults to false.")] = Query(None, description="Also revoke the grants redemptions issued; access from other sources stays. Defaults to false.", alias="revokeGrants"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Delete the invitation, ending redemption and its preview."""
    if not BaseResourceGrantInvitationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantInvitationsApi.subclasses[0]().resource_grant_invitations_id_delete(id, idempotency_key, revoke_grants)


@router.patch(
    "/resourceGrantInvitations/{id}",
    responses={
        200: {"model": ResourceGrantInvitationsUpdateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["resourceGrantInvitations"],
    summary="Update single resourceGrantInvitation.",
    response_model_by_alias=True,
)
async def resource_grant_invitations_id_patch(
    id: Annotated[str, Field(description="Invitation id")] = Path(..., description="Invitation id", examples=["e0163a07-8eee-4d30-ae44-75d44b1e47b0"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    resource_grant_invitations_update_operation_payload: Optional[ResourceGrantInvitationsUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> ResourceGrantInvitationsUpdateSingleResourceDataDocument:
    """Set, change or remove the password, or turn the preview on or off. Users who redeemed keep their grants."""
    if not BaseResourceGrantInvitationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantInvitationsApi.subclasses[0]().resource_grant_invitations_id_patch(id, idempotency_key, resource_grant_invitations_update_operation_payload)


@router.get(
    "/resourceGrantInvitations/{id}/relationships/owners",
    responses={
        200: {"model": ResourceGrantInvitationsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["resourceGrantInvitations"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def resource_grant_invitations_id_relationships_owners_get(
    id: Annotated[str, Field(description="Invitation id")] = Path(..., description="Invitation id", examples=["e0163a07-8eee-4d30-ae44-75d44b1e47b0"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ResourceGrantInvitationsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseResourceGrantInvitationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantInvitationsApi.subclasses[0]().resource_grant_invitations_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/resourceGrantInvitations/{id}/relationships/previewGrant",
    responses={
        200: {"model": ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["resourceGrantInvitations"],
    summary="Get previewGrant relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def resource_grant_invitations_id_relationships_preview_grant_get(
    id: Annotated[str, Field(description="Invitation id")] = Path(..., description="Invitation id", examples=["e0163a07-8eee-4d30-ae44-75d44b1e47b0"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: previewGrant")] = Query(None, description="Include related resources. Available relationships: previewGrant", alias="include", examples=["previewGrant.subject"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: previewGrant.subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: previewGrant.subject", alias="replaceMedia", examples=["previewGrant.subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument:
    """Retrieves previewGrant relationship."""
    if not BaseResourceGrantInvitationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantInvitationsApi.subclasses[0]().resource_grant_invitations_id_relationships_preview_grant_get(id, include, replace_media)


@router.get(
    "/resourceGrantInvitations/{id}/relationships/subject",
    responses={
        200: {"model": ResourceGrantInvitationsSubjectSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["resourceGrantInvitations"],
    summary="Get subject relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def resource_grant_invitations_id_relationships_subject_get(
    id: Annotated[str, Field(description="Invitation id")] = Path(..., description="Invitation id", examples=["e0163a07-8eee-4d30-ae44-75d44b1e47b0"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject", alias="replaceMedia", examples=["subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ResourceGrantInvitationsSubjectSingleRelationshipDataDocument:
    """Retrieves subject relationship."""
    if not BaseResourceGrantInvitationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantInvitationsApi.subclasses[0]().resource_grant_invitations_id_relationships_subject_get(id, include, replace_media)
