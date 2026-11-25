# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.user_feed_items_api_base import BaseUserFeedItemsApi
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
from tidal.models.user_feed_items_actors_multi_relationship_data_document import UserFeedItemsActorsMultiRelationshipDataDocument
from tidal.models.user_feed_items_multi_resource_data_document import UserFeedItemsMultiResourceDataDocument
from tidal.models.user_feed_items_subject_single_relationship_data_document import UserFeedItemsSubjectSingleRelationshipDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/userFeedItems",
    responses={
        200: {"model": UserFeedItemsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userFeedItems"],
    summary="Get multiple userFeedItems.",
    response_model_by_alias=True,
)
async def user_feed_items_get(
    filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="User id. Also accepts `me`.")] = Query(..., description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    filter_surface: Annotated[str, Field(description="Feed surface to read (e.g. `INBOX`)")] = Query(..., description="Feed surface to read (e.g. &#x60;INBOX&#x60;)", alias="filter[surface]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: actors, subject")] = Query(None, description="Include related resources. Available relationships: actors, subject", alias="include", examples=["actors.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: actors.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: actors.albums", alias="replaceMedia", examples=["actors.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> UserFeedItemsMultiResourceDataDocument:
    """The authenticated user&#39;s activity on the selected feed surface."""
    if not BaseUserFeedItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserFeedItemsApi.subclasses[0]().user_feed_items_get(filter_owners_id, filter_surface, include, include_linkage, page_cursor, replace_media)


@router.get(
    "/userFeedItems/{id}/relationships/actors",
    responses={
        200: {"model": UserFeedItemsActorsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userFeedItems"],
    summary="Get actors relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_feed_items_id_relationships_actors_get(
    id: Annotated[str, Field(min_length=1, max_length=432, description="Opaque identifier of a user feed item.")] = Path(..., description="Opaque identifier of a user feed item.", regex=r"^[0-9A-Za-z]+$", min_length=1, max_length=432, examples=["49XlsRIbQZSrRDe0QZhJ0y9nGzecOTVBOUN8MUUeD1iEbppZTWCgdLaxmzUvtk0K0JodRqxYgJrDQ5DAfi16j2ICfJGJ9MH9S6IvYuKzQAn1UWWSCdMA"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: actors")] = Query(None, description="Include related resources. Available relationships: actors", alias="include", examples=["actors.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: actors.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: actors.albums", alias="replaceMedia", examples=["actors.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> UserFeedItemsActorsMultiRelationshipDataDocument:
    """Artists attributed to the activity. Always empty for &#x60;ALBUM_FAVOURITED&#x60;, &#x60;TRACK_FAVOURITED&#x60; and &#x60;TRACK_PLAYLISTED&#x60;, which are counts only, and for &#x60;HISTORY_MIX_READY&#x60; and &#x60;TRACK_PLAY_MILESTONE&#x60;, which nobody else acted on."""
    if not BaseUserFeedItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserFeedItemsApi.subclasses[0]().user_feed_items_id_relationships_actors_get(id, include, page_cursor, replace_media)


@router.get(
    "/userFeedItems/{id}/relationships/subject",
    responses={
        200: {"model": UserFeedItemsSubjectSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userFeedItems"],
    summary="Get subject relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def user_feed_items_id_relationships_subject_get(
    id: Annotated[str, Field(min_length=1, max_length=432, description="Opaque identifier of a user feed item.")] = Path(..., description="Opaque identifier of a user feed item.", regex=r"^[0-9A-Za-z]+$", min_length=1, max_length=432, examples=["49XlsRIbQZSrRDe0QZhJ0y9nGzecOTVBOUN8MUUeD1iEbppZTWCgdLaxmzUvtk0K0JodRqxYgJrDQ5DAfi16j2ICfJGJ9MH9S6IvYuKzQAn1UWWSCdMA"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject", alias="replaceMedia", examples=["subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> UserFeedItemsSubjectSingleRelationshipDataDocument:
    """The resource the activity concerns. For &#x60;HISTORY_MIX_READY&#x60;, the viewer&#39;s history mix as a playlist."""
    if not BaseUserFeedItemsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserFeedItemsApi.subclasses[0]().user_feed_items_id_relationships_subject_get(id, include, replace_media)
