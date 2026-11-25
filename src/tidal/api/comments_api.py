# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.comments_api_base import BaseCommentsApi
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
from tidal.models.comments_author_single_relationship_data_document import CommentsAuthorSingleRelationshipDataDocument
from tidal.models.comments_comment_summary_single_relationship_data_document import CommentsCommentSummarySingleRelationshipDataDocument
from tidal.models.comments_create_operation_payload import CommentsCreateOperationPayload
from tidal.models.comments_create_single_resource_data_document import CommentsCreateSingleResourceDataDocument
from tidal.models.comments_multi_resource_data_document import CommentsMultiResourceDataDocument
from tidal.models.comments_owners_multi_relationship_data_document import CommentsOwnersMultiRelationshipDataDocument
from tidal.models.comments_reaction_summary_single_relationship_data_document import CommentsReactionSummarySingleRelationshipDataDocument
from tidal.models.comments_root_subject_single_relationship_data_document import CommentsRootSubjectSingleRelationshipDataDocument
from tidal.models.comments_single_resource_data_document import CommentsSingleResourceDataDocument
from tidal.models.comments_subject_single_relationship_data_document import CommentsSubjectSingleRelationshipDataDocument
from tidal.models.comments_update_operation_payload import CommentsUpdateOperationPayload
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
    "/comments",
    responses={
        200: {"model": CommentsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["comments"],
    summary="Get multiple comments.",
    response_model_by_alias=True,
)
async def comments_get(
    filter_subject: Annotated[str, Field(description="The immediate subject whose comments to return.")] = Query(..., description="The immediate subject whose comments to return.", alias="filter[subject]", regex=r"^(?:trackSourceFiles|comments):[^,]+$"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: author, commentSummary, owners, reactionSummary, rootSubject, subject")] = Query(None, description="Include related resources. Available relationships: author, commentSummary, owners, reactionSummary, rootSubject, subject", alias="include", examples=["author.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: author.albums", alias="replaceMedia", examples=["author.albums"]),
    sort: Annotated[Optional[List[str]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")] = Query(None, description="Values prefixed with \&quot;-\&quot; are sorted descending; values without it are sorted ascending.", alias="sort"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> CommentsMultiResourceDataDocument:
    """Returns root comments on a resource, or replies to a comment. Both support createdAt in either direction, newest first by default."""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comments_get(filter_subject, include, include_linkage, page_cursor, replace_media, sort)


@router.post(
    "/comments",
    responses={
        201: {"model": CommentsCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["comments"],
    summary="Create single comment.",
    response_model_by_alias=True,
)
async def comments_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    comments_create_operation_payload: Optional[CommentsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> CommentsCreateSingleResourceDataDocument:
    """Creates a root comment on a resource or a reply whose subject is a root comment. Replies to replies are rejected."""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comments_post(idempotency_key, comments_create_operation_payload)


@router.get(
    "/comments/{id}",
    responses={
        200: {"model": CommentsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["comments"],
    summary="Get single comment.",
    response_model_by_alias=True,
)
async def comments_id_get(
    id: Annotated[str, Field(description="Comment Id")] = Path(..., description="Comment Id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: author, commentSummary, owners, reactionSummary, rootSubject, subject")] = Query(None, description="Include related resources. Available relationships: author, commentSummary, owners, reactionSummary, rootSubject, subject", alias="include", examples=["author.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: author.albums", alias="replaceMedia", examples=["author.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> CommentsSingleResourceDataDocument:
    """Retrieves single comment by id."""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comments_id_get(id, include, include_linkage, replace_media)


@router.delete(
    "/comments/{id}",
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
    tags=["comments"],
    summary="Delete single comment.",
    response_model_by_alias=True,
)
async def comments_id_delete(
    id: Annotated[str, Field(description="Comment Id")] = Path(..., description="Comment Id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing comment."""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comments_id_delete(id, idempotency_key)


@router.patch(
    "/comments/{id}",
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
    tags=["comments"],
    summary="Update single comment.",
    response_model_by_alias=True,
)
async def comments_id_patch(
    id: Annotated[str, Field(description="Comment Id")] = Path(..., description="Comment Id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    comments_update_operation_payload: Optional[CommentsUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Updates existing comment."""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comments_id_patch(id, idempotency_key, comments_update_operation_payload)


@router.get(
    "/comments/{id}/relationships/author",
    responses={
        200: {"model": CommentsAuthorSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["comments"],
    summary="Get author relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def comments_id_relationships_author_get(
    id: Annotated[str, Field(description="Comment Id")] = Path(..., description="Comment Id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: author")] = Query(None, description="Include related resources. Available relationships: author", alias="include", examples=["author.albums"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: author.albums", alias="replaceMedia", examples=["author.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> CommentsAuthorSingleRelationshipDataDocument:
    """The artist who wrote the comment."""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comments_id_relationships_author_get(id, include, replace_media)


@router.get(
    "/comments/{id}/relationships/commentSummary",
    responses={
        200: {"model": CommentsCommentSummarySingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["comments"],
    summary="Get commentSummary relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def comments_id_relationships_comment_summary_get(
    id: Annotated[str, Field(description="Comment Id")] = Path(..., description="Comment Id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: commentSummary")] = Query(None, description="Include related resources. Available relationships: commentSummary", alias="include", examples=["commentSummary"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> CommentsCommentSummarySingleRelationshipDataDocument:
    """Retrieves commentSummary relationship."""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comments_id_relationships_comment_summary_get(id, include)


@router.get(
    "/comments/{id}/relationships/owners",
    responses={
        200: {"model": CommentsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["comments"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def comments_id_relationships_owners_get(
    id: Annotated[str, Field(description="Comment Id")] = Path(..., description="Comment Id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> CommentsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comments_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/comments/{id}/relationships/reactionSummary",
    responses={
        200: {"model": CommentsReactionSummarySingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["comments"],
    summary="Get reactionSummary relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def comments_id_relationships_reaction_summary_get(
    id: Annotated[str, Field(description="Comment Id")] = Path(..., description="Comment Id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: reactionSummary")] = Query(None, description="Include related resources. Available relationships: reactionSummary", alias="include", examples=["reactionSummary"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> CommentsReactionSummarySingleRelationshipDataDocument:
    """Retrieves reactionSummary relationship."""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comments_id_relationships_reaction_summary_get(id, include)


@router.get(
    "/comments/{id}/relationships/rootSubject",
    responses={
        200: {"model": CommentsRootSubjectSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["comments"],
    summary="Get rootSubject relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def comments_id_relationships_root_subject_get(
    id: Annotated[str, Field(description="Comment Id")] = Path(..., description="Comment Id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: rootSubject")] = Query(None, description="Include related resources. Available relationships: rootSubject", alias="include", examples=["rootSubject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> CommentsRootSubjectSingleRelationshipDataDocument:
    """Retrieves rootSubject relationship."""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comments_id_relationships_root_subject_get(id, include)


@router.get(
    "/comments/{id}/relationships/subject",
    responses={
        200: {"model": CommentsSubjectSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["comments"],
    summary="Get subject relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def comments_id_relationships_subject_get(
    id: Annotated[str, Field(description="Comment Id")] = Path(..., description="Comment Id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject.author.albums"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.author.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject.author.albums", alias="replaceMedia", examples=["subject.author.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> CommentsSubjectSingleRelationshipDataDocument:
    """Retrieves subject relationship."""
    if not BaseCommentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentsApi.subclasses[0]().comments_id_relationships_subject_get(id, include, replace_media)
