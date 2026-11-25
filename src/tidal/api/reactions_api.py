# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.reactions_api_base import BaseReactionsApi
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
from tidal.models.reactions_author_single_relationship_data_document import ReactionsAuthorSingleRelationshipDataDocument
from tidal.models.reactions_create_operation_payload import ReactionsCreateOperationPayload
from tidal.models.reactions_create_single_resource_data_document import ReactionsCreateSingleResourceDataDocument
from tidal.models.reactions_multi_resource_data_document import ReactionsMultiResourceDataDocument
from tidal.models.reactions_owners_multi_relationship_data_document import ReactionsOwnersMultiRelationshipDataDocument
from tidal.models.reactions_subject_single_relationship_data_document import ReactionsSubjectSingleRelationshipDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/reactions",
    responses={
        200: {"model": ReactionsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["reactions"],
    summary="Get multiple reactions.",
    response_model_by_alias=True,
)
async def reactions_get(
    filter_subject: Annotated[str, Field(description="The subject whose reactions to return.")] = Query(..., description="The subject whose reactions to return.", alias="filter[subject]", regex=r"^(?:trackSourceFiles|comments):[^,]+$"),
    filter_emoji: Annotated[Optional[List[Annotated[str, Field(min_length=1, max_length=32)]]], Field(description="Filter by emoji (e.g. `👍`)")] = Query(None, description="Filter by emoji (e.g. &#x60;👍&#x60;)", alias="filter[emoji]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: author, owners, subject")] = Query(None, description="Include related resources. Available relationships: author, owners, subject", alias="include", examples=["author.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: author.albums", alias="replaceMedia", examples=["author.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> ReactionsMultiResourceDataDocument:
    """Lists reactions on a source file or comment, newest first."""
    if not BaseReactionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReactionsApi.subclasses[0]().reactions_get(filter_subject, filter_emoji, include, include_linkage, page_cursor, replace_media)


@router.post(
    "/reactions",
    responses={
        201: {"model": ReactionsCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["reactions"],
    summary="Create single reaction.",
    response_model_by_alias=True,
)
async def reactions_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    reactions_create_operation_payload: Optional[ReactionsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> ReactionsCreateSingleResourceDataDocument:
    """Adds the caller&#39;s emoji reaction on a subject and exact time offsets. Omit both offsets for the whole subject, provide startOffset for a point, or both for a section. Offsets are supported only on source files and must be nonnegative, with endOffset at or after startOffset. Each user can add different emojis at the same position or section. Repeating the same emoji returns the existing reaction with its UUID and creation time unchanged."""
    if not BaseReactionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReactionsApi.subclasses[0]().reactions_post(idempotency_key, reactions_create_operation_payload)


@router.delete(
    "/reactions/{id}",
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
    tags=["reactions"],
    summary="Delete single reaction.",
    response_model_by_alias=True,
)
async def reactions_id_delete(
    id: Annotated[str, Field(description="Reaction Id")] = Path(..., description="Reaction Id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing reaction."""
    if not BaseReactionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReactionsApi.subclasses[0]().reactions_id_delete(id, idempotency_key)


@router.get(
    "/reactions/{id}/relationships/author",
    responses={
        200: {"model": ReactionsAuthorSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["reactions"],
    summary="Get author relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def reactions_id_relationships_author_get(
    id: Annotated[str, Field(description="Reaction Id")] = Path(..., description="Reaction Id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: author")] = Query(None, description="Include related resources. Available relationships: author", alias="include", examples=["author.albums"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: author.albums", alias="replaceMedia", examples=["author.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> ReactionsAuthorSingleRelationshipDataDocument:
    """The artist who left the reaction."""
    if not BaseReactionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReactionsApi.subclasses[0]().reactions_id_relationships_author_get(id, include, replace_media)


@router.get(
    "/reactions/{id}/relationships/owners",
    responses={
        200: {"model": ReactionsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["reactions"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def reactions_id_relationships_owners_get(
    id: Annotated[str, Field(description="Reaction Id")] = Path(..., description="Reaction Id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> ReactionsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseReactionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReactionsApi.subclasses[0]().reactions_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/reactions/{id}/relationships/subject",
    responses={
        200: {"model": ReactionsSubjectSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["reactions"],
    summary="Get subject relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def reactions_id_relationships_subject_get(
    id: Annotated[str, Field(description="Reaction Id")] = Path(..., description="Reaction Id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject.author.albums"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.author.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject.author.albums", alias="replaceMedia", examples=["subject.author.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> ReactionsSubjectSingleRelationshipDataDocument:
    """Retrieves subject relationship."""
    if not BaseReactionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReactionsApi.subclasses[0]().reactions_id_relationships_subject_get(id, include, replace_media)
