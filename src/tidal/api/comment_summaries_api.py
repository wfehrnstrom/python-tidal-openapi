# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.comment_summaries_api_base import BaseCommentSummariesApi
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
from tidal.models.comment_summaries_multi_resource_data_document import CommentSummariesMultiResourceDataDocument
from tidal.models.comment_summaries_subject_single_relationship_data_document import CommentSummariesSubjectSingleRelationshipDataDocument
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/commentSummaries",
    responses={
        200: {"model": CommentSummariesMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["commentSummaries"],
    summary="Get multiple commentSummaries.",
    response_model_by_alias=True,
)
async def comment_summaries_get(
    filter_subject: Annotated[List[str], Field(min_length=1, max_length=20, description="Subjects whose counts to return.")] = Query(..., description="Subjects whose counts to return.", alias="filter[subject]"),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject.author.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.author.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject.author.albums", alias="replaceMedia", examples=["subject.author.albums"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> CommentSummariesMultiResourceDataDocument:
    """Returns one current summary per accessible subject, for up to 20 subjects. Duplicates are returned once. Inaccessible or missing subjects are omitted. Empty supported subjects still have a summary. IDs remain stable as counts change. Counts include root comments on source files and direct replies on comments."""
    if not BaseCommentSummariesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentSummariesApi.subclasses[0]().comment_summaries_get(filter_subject, country_code, include, include_linkage, replace_media, share_code)


@router.get(
    "/commentSummaries/{id}/relationships/subject",
    responses={
        200: {"model": CommentSummariesSubjectSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["commentSummaries"],
    summary="Get subject relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def comment_summaries_id_relationships_subject_get(
    id: Annotated[str, Field(description="Opaque identifier of one subject's current summary")] = Path(..., description="Opaque identifier of one subject&#39;s current summary"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject.author.albums"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.author.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject.author.albums", alias="replaceMedia", examples=["subject.author.albums"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> CommentSummariesSubjectSingleRelationshipDataDocument:
    """Retrieves subject relationship."""
    if not BaseCommentSummariesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCommentSummariesApi.subclasses[0]().comment_summaries_id_relationships_subject_get(id, include, replace_media, share_code)
