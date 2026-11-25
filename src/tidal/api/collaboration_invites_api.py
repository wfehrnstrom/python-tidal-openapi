# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.collaboration_invites_api_base import BaseCollaborationInvitesApi
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
from tidal.models.collaboration_invites_create_operation_payload import CollaborationInvitesCreateOperationPayload
from tidal.models.collaboration_invites_create_single_resource_data_document import CollaborationInvitesCreateSingleResourceDataDocument
from tidal.models.collaboration_invites_multi_resource_data_document import CollaborationInvitesMultiResourceDataDocument
from tidal.models.collaboration_invites_owners_multi_relationship_data_document import CollaborationInvitesOwnersMultiRelationshipDataDocument
from tidal.models.collaboration_invites_single_resource_data_document import CollaborationInvitesSingleResourceDataDocument
from tidal.models.collaboration_invites_subject_single_relationship_data_document import CollaborationInvitesSubjectSingleRelationshipDataDocument
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
    "/collaborationInvites",
    responses={
        200: {"model": CollaborationInvitesMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["collaborationInvites"],
    summary="Get multiple collaborationInvites.",
    response_model_by_alias=True,
)
async def collaboration_invites_get(
    filter_code: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="Invite code")] = Query(..., description="Invite code", alias="filter[code]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, subject")] = Query(None, description="Include related resources. Available relationships: owners, subject", alias="include", examples=["subject.items"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject.items", alias="replaceMedia", examples=["subject.items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> CollaborationInvitesMultiResourceDataDocument:
    """Retrieves multiple collaborationInvites by available filters, or without if applicable."""
    if not BaseCollaborationInvitesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCollaborationInvitesApi.subclasses[0]().collaboration_invites_get(filter_code, include, include_linkage, replace_media)


@router.post(
    "/collaborationInvites",
    responses={
        201: {"model": CollaborationInvitesCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["collaborationInvites"],
    summary="Create single collaborationInvite.",
    response_model_by_alias=True,
)
async def collaboration_invites_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    collaboration_invites_create_operation_payload: Optional[CollaborationInvitesCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> CollaborationInvitesCreateSingleResourceDataDocument:
    """Creates a new collaborationInvite."""
    if not BaseCollaborationInvitesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCollaborationInvitesApi.subclasses[0]().collaboration_invites_post(idempotency_key, collaboration_invites_create_operation_payload)


@router.get(
    "/collaborationInvites/{id}",
    responses={
        200: {"model": CollaborationInvitesSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["collaborationInvites"],
    summary="Get single collaborationInvite.",
    response_model_by_alias=True,
)
async def collaboration_invites_id_get(
    id: Annotated[str, Field(description="Collaboration invite id")] = Path(..., description="Collaboration invite id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, subject")] = Query(None, description="Include related resources. Available relationships: owners, subject", alias="include", examples=["subject.items"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject.items", alias="replaceMedia", examples=["subject.items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> CollaborationInvitesSingleResourceDataDocument:
    """Retrieves single collaborationInvite by id."""
    if not BaseCollaborationInvitesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCollaborationInvitesApi.subclasses[0]().collaboration_invites_id_get(id, include, include_linkage, replace_media)


@router.delete(
    "/collaborationInvites/{id}",
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
    tags=["collaborationInvites"],
    summary="Delete single collaborationInvite.",
    response_model_by_alias=True,
)
async def collaboration_invites_id_delete(
    id: Annotated[str, Field(description="Collaboration invite id")] = Path(..., description="Collaboration invite id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing collaborationInvite."""
    if not BaseCollaborationInvitesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCollaborationInvitesApi.subclasses[0]().collaboration_invites_id_delete(id, idempotency_key)


@router.get(
    "/collaborationInvites/{id}/relationships/owners",
    responses={
        200: {"model": CollaborationInvitesOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["collaborationInvites"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def collaboration_invites_id_relationships_owners_get(
    id: Annotated[str, Field(description="Collaboration invite id")] = Path(..., description="Collaboration invite id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> CollaborationInvitesOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseCollaborationInvitesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCollaborationInvitesApi.subclasses[0]().collaboration_invites_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/collaborationInvites/{id}/relationships/subject",
    responses={
        200: {"model": CollaborationInvitesSubjectSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["collaborationInvites"],
    summary="Get subject relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def collaboration_invites_id_relationships_subject_get(
    id: Annotated[str, Field(description="Collaboration invite id")] = Path(..., description="Collaboration invite id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject.items"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject.items", alias="replaceMedia", examples=["subject.items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> CollaborationInvitesSubjectSingleRelationshipDataDocument:
    """Retrieves subject relationship."""
    if not BaseCollaborationInvitesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCollaborationInvitesApi.subclasses[0]().collaboration_invites_id_relationships_subject_get(id, include, replace_media)
