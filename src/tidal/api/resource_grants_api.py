# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.resource_grants_api_base import BaseResourceGrantsApi
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
from tidal.models.resource_grants_create_operation_payload import ResourceGrantsCreateOperationPayload
from tidal.models.resource_grants_create_resource403_response_body import ResourceGrantsCreateResource403ResponseBody
from tidal.models.resource_grants_create_resource429_response_body import ResourceGrantsCreateResource429ResponseBody
from tidal.models.resource_grants_create_single_resource_data_document import ResourceGrantsCreateSingleResourceDataDocument
from tidal.models.resource_grants_grantee_single_relationship_data_document import ResourceGrantsGranteeSingleRelationshipDataDocument
from tidal.models.resource_grants_invitation_single_relationship_data_document import ResourceGrantsInvitationSingleRelationshipDataDocument
from tidal.models.resource_grants_multi_resource_data_document import ResourceGrantsMultiResourceDataDocument
from tidal.models.resource_grants_single_resource_data_document import ResourceGrantsSingleResourceDataDocument
from tidal.models.resource_grants_subject_single_relationship_data_document import ResourceGrantsSubjectSingleRelationshipDataDocument
from tidal.models.resource_grants_update_operation_payload import ResourceGrantsUpdateOperationPayload
from tidal.models.resource_grants_update_single_resource_data_document import ResourceGrantsUpdateSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/resourceGrants",
    responses={
        200: {"model": ResourceGrantsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["resourceGrants"],
    summary="Get multiple resourceGrants.",
    response_model_by_alias=True,
)
async def resource_grants_get(
    filter_grantee: Annotated[Optional[str], Field(description="Filter by grantee. Use `groups:everyone` for the Everyone group. Also accepts `users:me`.")] = Query(None, description="Filter by grantee. Use &#x60;groups:everyone&#x60; for the Everyone group. Also accepts &#x60;users:me&#x60;.", alias="filter[grantee]", regex=r"^(?:users|groups):[^,]+$"),
    filter_role: Annotated[Optional[str], Field(description="One of: VIEWER, COLLABORATOR, OWNER (e.g. `VIEWER`)")] = Query(None, description="One of: VIEWER, COLLABORATOR, OWNER (e.g. &#x60;VIEWER&#x60;)", alias="filter[role]"),
    filter_self_applies_to: Annotated[Optional[str], Field(description="Album, track or folder whose grants are listed, including those on its ancestor folders and albums. Each grant keeps the subject it is stored on. Also accepts `folders:me`.")] = Query(None, description="Album, track or folder whose grants are listed, including those on its ancestor folders and albums. Each grant keeps the subject it is stored on. Also accepts &#x60;folders:me&#x60;.", alias="filter[self][appliesTo]", regex=r"^(?:albums|tracks|folders|playlists):[^,]+$"),
    filter_subject: Annotated[Optional[str], Field(description="Filter by subject. Required unless `filter[self][appliesTo]` is used. The subject's owner reads all its grants; other callers read only grants made directly to them. Also accepts `folders:me`.")] = Query(None, description="Filter by subject. Required unless &#x60;filter[self][appliesTo]&#x60; is used. The subject&#39;s owner reads all its grants; other callers read only grants made directly to them. Also accepts &#x60;folders:me&#x60;.", alias="filter[subject]", regex=r"^(?:albums|tracks|folders|playlists):[^,]+$"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: grantee, invitation, subject")] = Query(None, description="Include related resources. Available relationships: grantee, invitation, subject", alias="include", examples=["grantee.artist.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: grantee.artist.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: grantee.artist.albums", alias="replaceMedia", examples=["grantee.artist.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ResourceGrantsMultiResourceDataDocument:
    """Retrieves multiple resourceGrants by available filters, or without if applicable."""
    if not BaseResourceGrantsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantsApi.subclasses[0]().resource_grants_get(filter_grantee, filter_role, filter_self_applies_to, filter_subject, include, include_linkage, page_cursor, replace_media)


@router.post(
    "/resourceGrants",
    responses={
        201: {"model": ResourceGrantsCreateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": ResourceGrantsCreateResource403ResponseBody, "description": "This invitation can no longer be accepted; The invitation is password protected; send its password; The invitation password is incorrect"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": Idempotency409ResponseBody, "description": "Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": ResourceGrantsCreateResource429ResponseBody, "description": "Too many invitation password attempts; try again later"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["resourceGrants"],
    summary="Create single resourceGrant.",
    response_model_by_alias=True,
)
async def resource_grants_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    resource_grants_create_operation_payload: Optional[ResourceGrantsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> ResourceGrantsCreateSingleResourceDataDocument:
    """Create a direct grant from &#x60;role&#x60;, &#x60;subject&#x60; and &#x60;grantee&#x60;. Alternatively, redeem an invitation with only the &#x60;invitation&#x60; relationship: the caller receives the invitation&#39;s role on its subject, and the response is the caller&#39;s grant. Redeeming again returns the same grant. Every redemption, repeated ones included, needs a password-protected invitation&#39;s password and counts as a use of a limited invitation; password attempts are rate limited. The invitation&#39;s creator cannot redeem it."""
    if not BaseResourceGrantsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantsApi.subclasses[0]().resource_grants_post(idempotency_key, resource_grants_create_operation_payload)


@router.get(
    "/resourceGrants/{id}",
    responses={
        200: {"model": ResourceGrantsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["resourceGrants"],
    summary="Get single resourceGrant.",
    response_model_by_alias=True,
)
async def resource_grants_id_get(
    id: Annotated[str, Field(description="Opaque resource grant ID")] = Path(..., description="Opaque resource grant ID"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: grantee, invitation, subject")] = Query(None, description="Include related resources. Available relationships: grantee, invitation, subject", alias="include", examples=["grantee.artist.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: grantee.artist.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: grantee.artist.albums", alias="replaceMedia", examples=["grantee.artist.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ResourceGrantsSingleResourceDataDocument:
    """Retrieves single resourceGrant by id."""
    if not BaseResourceGrantsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantsApi.subclasses[0]().resource_grants_id_get(id, include, include_linkage, replace_media)


@router.delete(
    "/resourceGrants/{id}",
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
    tags=["resourceGrants"],
    summary="Delete single resourceGrant.",
    response_model_by_alias=True,
)
async def resource_grants_id_delete(
    id: Annotated[str, Field(description="Opaque resource grant ID")] = Path(..., description="Opaque resource grant ID"),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing resourceGrant."""
    if not BaseResourceGrantsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantsApi.subclasses[0]().resource_grants_id_delete(id, idempotency_key)


@router.patch(
    "/resourceGrants/{id}",
    responses={
        200: {"model": ResourceGrantsUpdateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["resourceGrants"],
    summary="Update single resourceGrant.",
    response_model_by_alias=True,
)
async def resource_grants_id_patch(
    id: Annotated[str, Field(description="Opaque resource grant ID")] = Path(..., description="Opaque resource grant ID"),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    resource_grants_update_operation_payload: Optional[ResourceGrantsUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> ResourceGrantsUpdateSingleResourceDataDocument:
    """Updates existing resourceGrant."""
    if not BaseResourceGrantsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantsApi.subclasses[0]().resource_grants_id_patch(id, idempotency_key, resource_grants_update_operation_payload)


@router.get(
    "/resourceGrants/{id}/relationships/grantee",
    responses={
        200: {"model": ResourceGrantsGranteeSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["resourceGrants"],
    summary="Get grantee relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def resource_grants_id_relationships_grantee_get(
    id: Annotated[str, Field(description="Opaque resource grant ID")] = Path(..., description="Opaque resource grant ID"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: grantee")] = Query(None, description="Include related resources. Available relationships: grantee", alias="include", examples=["grantee.artist.albums"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: grantee.artist.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: grantee.artist.albums", alias="replaceMedia", examples=["grantee.artist.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ResourceGrantsGranteeSingleRelationshipDataDocument:
    """Retrieves grantee relationship."""
    if not BaseResourceGrantsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantsApi.subclasses[0]().resource_grants_id_relationships_grantee_get(id, include, replace_media)


@router.get(
    "/resourceGrants/{id}/relationships/invitation",
    responses={
        200: {"model": ResourceGrantsInvitationSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["resourceGrants"],
    summary="Get invitation relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def resource_grants_id_relationships_invitation_get(
    id: Annotated[str, Field(description="Opaque resource grant ID")] = Path(..., description="Opaque resource grant ID"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: invitation")] = Query(None, description="Include related resources. Available relationships: invitation", alias="include", examples=["invitation.subject"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: invitation.subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: invitation.subject", alias="replaceMedia", examples=["invitation.subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ResourceGrantsInvitationSingleRelationshipDataDocument:
    """Retrieves invitation relationship."""
    if not BaseResourceGrantsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantsApi.subclasses[0]().resource_grants_id_relationships_invitation_get(id, include, replace_media)


@router.get(
    "/resourceGrants/{id}/relationships/subject",
    responses={
        200: {"model": ResourceGrantsSubjectSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["resourceGrants"],
    summary="Get subject relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def resource_grants_id_relationships_subject_get(
    id: Annotated[str, Field(description="Opaque resource grant ID")] = Path(..., description="Opaque resource grant ID"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject", alias="replaceMedia", examples=["subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ResourceGrantsSubjectSingleRelationshipDataDocument:
    """Retrieves subject relationship."""
    if not BaseResourceGrantsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseResourceGrantsApi.subclasses[0]().resource_grants_id_relationships_subject_get(id, include, replace_media)
