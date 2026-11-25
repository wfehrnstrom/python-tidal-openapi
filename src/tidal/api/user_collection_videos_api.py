# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.user_collection_videos_api_base import BaseUserCollectionVideosApi
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
from tidal.models.user_collection_videos_items_add_multi_data_relationship_with_response409_response_body import UserCollectionVideosItemsAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_collection_videos_items_add_multi_relationship_data_document import UserCollectionVideosItemsAddMultiRelationshipDataDocument
from tidal.models.user_collection_videos_items_multi_relationship_data_document import UserCollectionVideosItemsMultiRelationshipDataDocument
from tidal.models.user_collection_videos_items_read_multi_data_relationship403_response_body import UserCollectionVideosItemsReadMultiDataRelationship403ResponseBody
from tidal.models.user_collection_videos_items_relationship_add_operation_payload import UserCollectionVideosItemsRelationshipAddOperationPayload
from tidal.models.user_collection_videos_items_relationship_remove_operation_payload import UserCollectionVideosItemsRelationshipRemoveOperationPayload
from tidal.models.user_collection_videos_owners_multi_relationship_data_document import UserCollectionVideosOwnersMultiRelationshipDataDocument
from tidal.models.user_collection_videos_single_resource_data_document import UserCollectionVideosSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/userCollectionVideos/{id}",
    responses={
        200: {"model": UserCollectionVideosSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userCollectionVideos"],
    summary="Get single userCollectionVideo.",
    response_model_by_alias=True,
)
async def user_collection_videos_id_get(
    id: Annotated[str, Field(description="User collection videos id. Use `me` for the authenticated user's resource")] = Path(..., description="User collection videos id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items, owners")] = Query(None, description="Include related resources. Available relationships: items, owners", alias="include", examples=["items"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")] = Query('en-US', description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.", alias="locale", examples=["en-US"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items", alias="replaceMedia", examples=["items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
) -> UserCollectionVideosSingleResourceDataDocument:
    """Retrieves single userCollectionVideo by id."""
    if not BaseUserCollectionVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionVideosApi.subclasses[0]().user_collection_videos_id_get(id, include, include_linkage, locale, replace_media)


@router.get(
    "/userCollectionVideos/{id}/relationships/items",
    responses={
        200: {"model": UserCollectionVideosItemsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": UserCollectionVideosItemsReadMultiDataRelationship403ResponseBody, "description": "filter[self][matchesQuery] requires INTERNAL access tier"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userCollectionVideos"],
    summary="Get items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_collection_videos_id_relationships_items_get(
    id: Annotated[str, Field(description="User collection videos id. Use `me` for the authenticated user's resource")] = Path(..., description="User collection videos id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    filter_self_matches_query: Annotated[Optional[Annotated[str, Field(max_length=100)]], Field(description="Filter videos by a free-text query matched against the video title and artist names. Internal clients only (e.g. `love`)")] = Query(None, description="Filter videos by a free-text query matched against the video title and artist names. Internal clients only (e.g. &#x60;love&#x60;)", alias="filter[self][matchesQuery]", max_length=100),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")] = Query(None, description="Include related resources. Available relationships: items", alias="include", examples=["items"]),
    locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")] = Query('en-US', description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.", alias="locale", examples=["en-US"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items", alias="replaceMedia", examples=["items"]),
    sort: Annotated[Optional[List[str]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")] = Query(None, description="Values prefixed with \&quot;-\&quot; are sorted descending; values without it are sorted ascending.", alias="sort"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
) -> UserCollectionVideosItemsMultiRelationshipDataDocument:
    """Retrieves items relationship."""
    if not BaseUserCollectionVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionVideosApi.subclasses[0]().user_collection_videos_id_relationships_items_get(id, filter_self_matches_query, include, locale, page_cursor, replace_media, sort)


@router.post(
    "/userCollectionVideos/{id}/relationships/items",
    responses={
        200: {"model": UserCollectionVideosItemsAddMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": UserCollectionVideosItemsAddMultiDataRelationshipWithResponse409ResponseBody, "description": "Collection item limit reached; Collection already contains one or more items; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userCollectionVideos"],
    summary="Add to items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_collection_videos_id_relationships_items_post(
    id: Annotated[str, Field(description="User collection videos id. Use `me` for the authenticated user's resource")] = Path(..., description="User collection videos id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_collection_videos_items_relationship_add_operation_payload: Optional[UserCollectionVideosItemsRelationshipAddOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.write", "w_usr"]
    ),
) -> UserCollectionVideosItemsAddMultiRelationshipDataDocument:
    """Adds item(s) to items relationship."""
    if not BaseUserCollectionVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionVideosApi.subclasses[0]().user_collection_videos_id_relationships_items_post(id, idempotency_key, user_collection_videos_items_relationship_add_operation_payload)


@router.delete(
    "/userCollectionVideos/{id}/relationships/items",
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
    tags=["userCollectionVideos"],
    summary="Delete from items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_collection_videos_id_relationships_items_delete(
    id: Annotated[str, Field(description="User collection videos id. Use `me` for the authenticated user's resource")] = Path(..., description="User collection videos id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_collection_videos_items_relationship_remove_operation_payload: Optional[UserCollectionVideosItemsRelationshipRemoveOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes item(s) from items relationship."""
    if not BaseUserCollectionVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionVideosApi.subclasses[0]().user_collection_videos_id_relationships_items_delete(id, idempotency_key, user_collection_videos_items_relationship_remove_operation_payload)


@router.get(
    "/userCollectionVideos/{id}/relationships/owners",
    responses={
        200: {"model": UserCollectionVideosOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userCollectionVideos"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_collection_videos_id_relationships_owners_get(
    id: Annotated[str, Field(description="User collection videos id. Use `me` for the authenticated user's resource")] = Path(..., description="User collection videos id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["collection.read", "r_usr"]
    ),
) -> UserCollectionVideosOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseUserCollectionVideosApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserCollectionVideosApi.subclasses[0]().user_collection_videos_id_relationships_owners_get(id, include, page_cursor)
