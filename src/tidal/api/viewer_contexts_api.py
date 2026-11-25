# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.viewer_contexts_api_base import BaseViewerContextsApi
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
from tidal.models.viewer_contexts_comments_multi_relationship_data_document import ViewerContextsCommentsMultiRelationshipDataDocument
from tidal.models.viewer_contexts_multi_resource_data_document import ViewerContextsMultiResourceDataDocument
from tidal.models.viewer_contexts_reactions_multi_relationship_data_document import ViewerContextsReactionsMultiRelationshipDataDocument
from tidal.models.viewer_contexts_single_resource_data_document import ViewerContextsSingleResourceDataDocument
from tidal.models.viewer_contexts_subject_single_relationship_data_document import ViewerContextsSubjectSingleRelationshipDataDocument
from tidal.models.viewer_contexts_viewer_single_relationship_data_document import ViewerContextsViewerSingleRelationshipDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/viewerContexts",
    responses={
        200: {"model": ViewerContextsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["viewerContexts"],
    summary="Get multiple viewerContexts.",
    response_model_by_alias=True,
)
async def viewer_contexts_get(
    filter_subject: Annotated[List[str], Field(min_length=1, max_length=20, description="Original subjects to look up. Also accepts `folders:me`.")] = Query(..., description="Original subjects to look up. Also accepts &#x60;folders:me&#x60;.", alias="filter[subject]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: comments, reactions, subject, viewer")] = Query(None, description="Include related resources. Available relationships: comments, reactions, subject, viewer", alias="include", examples=["comments.author.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: comments.author.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: comments.author.albums", alias="replaceMedia", examples=["comments.author.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ViewerContextsMultiResourceDataDocument:
    """Returns viewer contexts for up to 20 original subjects. Duplicate subjects are returned once."""
    if not BaseViewerContextsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseViewerContextsApi.subclasses[0]().viewer_contexts_get(filter_subject, include, include_linkage, replace_media)


@router.get(
    "/viewerContexts/{id}",
    responses={
        200: {"model": ViewerContextsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["viewerContexts"],
    summary="Get single viewerContext.",
    response_model_by_alias=True,
)
async def viewer_contexts_id_get(
    id: Annotated[str, Field(min_length=1, max_length=256, description="Opaque identifier of one authenticated viewer and original subject pair")] = Path(..., description="Opaque identifier of one authenticated viewer and original subject pair", regex=r"^[0-9A-Za-z]+$", min_length=1, max_length=256),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: comments, reactions, subject, viewer")] = Query(None, description="Include related resources. Available relationships: comments, reactions, subject, viewer", alias="include", examples=["comments.author.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: comments.author.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: comments.author.albums", alias="replaceMedia", examples=["comments.author.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ViewerContextsSingleResourceDataDocument:
    """Retrieves single viewerContext by id."""
    if not BaseViewerContextsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseViewerContextsApi.subclasses[0]().viewer_contexts_id_get(id, include, include_linkage, replace_media)


@router.get(
    "/viewerContexts/{id}/relationships/comments",
    responses={
        200: {"model": ViewerContextsCommentsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["viewerContexts"],
    summary="Get comments relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def viewer_contexts_id_relationships_comments_get(
    id: Annotated[str, Field(min_length=1, max_length=256, description="Opaque identifier of one authenticated viewer and original subject pair")] = Path(..., description="Opaque identifier of one authenticated viewer and original subject pair", regex=r"^[0-9A-Za-z]+$", min_length=1, max_length=256),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: comments")] = Query(None, description="Include related resources. Available relationships: comments", alias="include", examples=["comments.author.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: comments.author.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: comments.author.albums", alias="replaceMedia", examples=["comments.author.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ViewerContextsCommentsMultiRelationshipDataDocument:
    """Returns the viewer&#39;s comments on the subject."""
    if not BaseViewerContextsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseViewerContextsApi.subclasses[0]().viewer_contexts_id_relationships_comments_get(id, include, page_cursor, replace_media)


@router.get(
    "/viewerContexts/{id}/relationships/reactions",
    responses={
        200: {"model": ViewerContextsReactionsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["viewerContexts"],
    summary="Get reactions relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def viewer_contexts_id_relationships_reactions_get(
    id: Annotated[str, Field(min_length=1, max_length=256, description="Opaque identifier of one authenticated viewer and original subject pair")] = Path(..., description="Opaque identifier of one authenticated viewer and original subject pair", regex=r"^[0-9A-Za-z]+$", min_length=1, max_length=256),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: reactions")] = Query(None, description="Include related resources. Available relationships: reactions", alias="include", examples=["reactions.author.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: reactions.author.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: reactions.author.albums", alias="replaceMedia", examples=["reactions.author.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ViewerContextsReactionsMultiRelationshipDataDocument:
    """Returns the viewer&#39;s reactions on the subject."""
    if not BaseViewerContextsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseViewerContextsApi.subclasses[0]().viewer_contexts_id_relationships_reactions_get(id, include, page_cursor, replace_media)


@router.get(
    "/viewerContexts/{id}/relationships/subject",
    responses={
        200: {"model": ViewerContextsSubjectSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["viewerContexts"],
    summary="Get subject relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def viewer_contexts_id_relationships_subject_get(
    id: Annotated[str, Field(min_length=1, max_length=256, description="Opaque identifier of one authenticated viewer and original subject pair")] = Path(..., description="Opaque identifier of one authenticated viewer and original subject pair", regex=r"^[0-9A-Za-z]+$", min_length=1, max_length=256),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject", alias="replaceMedia", examples=["subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ViewerContextsSubjectSingleRelationshipDataDocument:
    """Returns the subject of this viewer context."""
    if not BaseViewerContextsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseViewerContextsApi.subclasses[0]().viewer_contexts_id_relationships_subject_get(id, include, replace_media)


@router.get(
    "/viewerContexts/{id}/relationships/viewer",
    responses={
        200: {"model": ViewerContextsViewerSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["viewerContexts"],
    summary="Get viewer relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def viewer_contexts_id_relationships_viewer_get(
    id: Annotated[str, Field(min_length=1, max_length=256, description="Opaque identifier of one authenticated viewer and original subject pair")] = Path(..., description="Opaque identifier of one authenticated viewer and original subject pair", regex=r"^[0-9A-Za-z]+$", min_length=1, max_length=256),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: viewer")] = Query(None, description="Include related resources. Available relationships: viewer", alias="include", examples=["viewer.artist.albums"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: viewer.artist.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: viewer.artist.albums", alias="replaceMedia", examples=["viewer.artist.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ViewerContextsViewerSingleRelationshipDataDocument:
    """Returns the authenticated viewer of this context."""
    if not BaseViewerContextsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseViewerContextsApi.subclasses[0]().viewer_contexts_id_relationships_viewer_get(id, include, replace_media)
