# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.user_recommendation_blocks_api_base import BaseUserRecommendationBlocksApi
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
from tidal.models.user_recommendation_blocks_artists_add_multi_data_relationship_with_response409_response_body import UserRecommendationBlocksArtistsAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_recommendation_blocks_artists_add_multi_relationship_data_document import UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_artists_multi_relationship_data_document import UserRecommendationBlocksArtistsMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_artists_relationship_add_operation_payload import UserRecommendationBlocksArtistsRelationshipAddOperationPayload
from tidal.models.user_recommendation_blocks_artists_relationship_remove_operation_payload import UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload
from tidal.models.user_recommendation_blocks_owners_multi_relationship_data_document import UserRecommendationBlocksOwnersMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_single_resource_data_document import UserRecommendationBlocksSingleResourceDataDocument
from tidal.models.user_recommendation_blocks_tracks_add_multi_data_relationship_with_response409_response_body import UserRecommendationBlocksTracksAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_recommendation_blocks_tracks_add_multi_relationship_data_document import UserRecommendationBlocksTracksAddMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_tracks_multi_relationship_data_document import UserRecommendationBlocksTracksMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_tracks_relationship_add_operation_payload import UserRecommendationBlocksTracksRelationshipAddOperationPayload
from tidal.models.user_recommendation_blocks_tracks_relationship_remove_operation_payload import UserRecommendationBlocksTracksRelationshipRemoveOperationPayload
from tidal.models.user_recommendation_blocks_videos_add_multi_data_relationship_with_response409_response_body import UserRecommendationBlocksVideosAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.user_recommendation_blocks_videos_add_multi_relationship_data_document import UserRecommendationBlocksVideosAddMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_videos_multi_relationship_data_document import UserRecommendationBlocksVideosMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_videos_relationship_add_operation_payload import UserRecommendationBlocksVideosRelationshipAddOperationPayload
from tidal.models.user_recommendation_blocks_videos_relationship_remove_operation_payload import UserRecommendationBlocksVideosRelationshipRemoveOperationPayload
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/userRecommendationBlocks/{id}",
    responses={
        200: {"model": UserRecommendationBlocksSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userRecommendationBlocks"],
    summary="Get single userRecommendationBlock.",
    response_model_by_alias=True,
)
async def user_recommendation_blocks_id_get(
    id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")] = Path(..., description="User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artists, owners, tracks, videos")] = Query(None, description="Include related resources. Available relationships: artists, owners, tracks, videos", alias="include", examples=["artists.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")] = Query('en-US', description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.", alias="locale", examples=["en-US"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums", alias="replaceMedia", examples=["artists.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "recommendations.read"]
    ),
) -> UserRecommendationBlocksSingleResourceDataDocument:
    """Retrieves single userRecommendationBlock by id."""
    if not BaseUserRecommendationBlocksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserRecommendationBlocksApi.subclasses[0]().user_recommendation_blocks_id_get(id, include, include_linkage, locale, replace_media)


@router.get(
    "/userRecommendationBlocks/{id}/relationships/artists",
    responses={
        200: {"model": UserRecommendationBlocksArtistsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userRecommendationBlocks"],
    summary="Get artists relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_recommendation_blocks_id_relationships_artists_get(
    id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")] = Path(..., description="User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artists")] = Query(None, description="Include related resources. Available relationships: artists", alias="include", examples=["artists.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums", alias="replaceMedia", examples=["artists.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "recommendations.read"]
    ),
) -> UserRecommendationBlocksArtistsMultiRelationshipDataDocument:
    """Retrieves artists relationship."""
    if not BaseUserRecommendationBlocksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserRecommendationBlocksApi.subclasses[0]().user_recommendation_blocks_id_relationships_artists_get(id, include, page_cursor, replace_media)


@router.post(
    "/userRecommendationBlocks/{id}/relationships/artists",
    responses={
        200: {"model": UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": UserRecommendationBlocksArtistsAddMultiDataRelationshipWithResponse409ResponseBody, "description": "Recommendation block limit reached; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userRecommendationBlocks"],
    summary="Add to artists relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_recommendation_blocks_id_relationships_artists_post(
    id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")] = Path(..., description="User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_recommendation_blocks_artists_relationship_add_operation_payload: Optional[UserRecommendationBlocksArtistsRelationshipAddOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument:
    """Adds item(s) to artists relationship."""
    if not BaseUserRecommendationBlocksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserRecommendationBlocksApi.subclasses[0]().user_recommendation_blocks_id_relationships_artists_post(id, idempotency_key, user_recommendation_blocks_artists_relationship_add_operation_payload)


@router.delete(
    "/userRecommendationBlocks/{id}/relationships/artists",
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
    tags=["userRecommendationBlocks"],
    summary="Delete from artists relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_recommendation_blocks_id_relationships_artists_delete(
    id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")] = Path(..., description="User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_recommendation_blocks_artists_relationship_remove_operation_payload: Optional[UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes item(s) from artists relationship."""
    if not BaseUserRecommendationBlocksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserRecommendationBlocksApi.subclasses[0]().user_recommendation_blocks_id_relationships_artists_delete(id, idempotency_key, user_recommendation_blocks_artists_relationship_remove_operation_payload)


@router.get(
    "/userRecommendationBlocks/{id}/relationships/owners",
    responses={
        200: {"model": UserRecommendationBlocksOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userRecommendationBlocks"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_recommendation_blocks_id_relationships_owners_get(
    id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")] = Path(..., description="User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "recommendations.read"]
    ),
) -> UserRecommendationBlocksOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseUserRecommendationBlocksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserRecommendationBlocksApi.subclasses[0]().user_recommendation_blocks_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/userRecommendationBlocks/{id}/relationships/tracks",
    responses={
        200: {"model": UserRecommendationBlocksTracksMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userRecommendationBlocks"],
    summary="Get tracks relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_recommendation_blocks_id_relationships_tracks_get(
    id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")] = Path(..., description="User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: tracks")] = Query(None, description="Include related resources. Available relationships: tracks", alias="include", examples=["tracks"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: tracks", alias="replaceMedia", examples=["tracks"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "recommendations.read"]
    ),
) -> UserRecommendationBlocksTracksMultiRelationshipDataDocument:
    """Retrieves tracks relationship."""
    if not BaseUserRecommendationBlocksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserRecommendationBlocksApi.subclasses[0]().user_recommendation_blocks_id_relationships_tracks_get(id, include, page_cursor, replace_media)


@router.post(
    "/userRecommendationBlocks/{id}/relationships/tracks",
    responses={
        200: {"model": UserRecommendationBlocksTracksAddMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": UserRecommendationBlocksTracksAddMultiDataRelationshipWithResponse409ResponseBody, "description": "Recommendation block limit reached; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userRecommendationBlocks"],
    summary="Add to tracks relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_recommendation_blocks_id_relationships_tracks_post(
    id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")] = Path(..., description="User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_recommendation_blocks_tracks_relationship_add_operation_payload: Optional[UserRecommendationBlocksTracksRelationshipAddOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> UserRecommendationBlocksTracksAddMultiRelationshipDataDocument:
    """Adds item(s) to tracks relationship."""
    if not BaseUserRecommendationBlocksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserRecommendationBlocksApi.subclasses[0]().user_recommendation_blocks_id_relationships_tracks_post(id, idempotency_key, user_recommendation_blocks_tracks_relationship_add_operation_payload)


@router.delete(
    "/userRecommendationBlocks/{id}/relationships/tracks",
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
    tags=["userRecommendationBlocks"],
    summary="Delete from tracks relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_recommendation_blocks_id_relationships_tracks_delete(
    id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")] = Path(..., description="User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_recommendation_blocks_tracks_relationship_remove_operation_payload: Optional[UserRecommendationBlocksTracksRelationshipRemoveOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes item(s) from tracks relationship."""
    if not BaseUserRecommendationBlocksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserRecommendationBlocksApi.subclasses[0]().user_recommendation_blocks_id_relationships_tracks_delete(id, idempotency_key, user_recommendation_blocks_tracks_relationship_remove_operation_payload)


@router.get(
    "/userRecommendationBlocks/{id}/relationships/videos",
    responses={
        200: {"model": UserRecommendationBlocksVideosMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userRecommendationBlocks"],
    summary="Get videos relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_recommendation_blocks_id_relationships_videos_get(
    id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")] = Path(..., description="User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: videos")] = Query(None, description="Include related resources. Available relationships: videos", alias="include", examples=["videos"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: videos", alias="replaceMedia", examples=["videos"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr", "recommendations.read"]
    ),
) -> UserRecommendationBlocksVideosMultiRelationshipDataDocument:
    """Retrieves videos relationship."""
    if not BaseUserRecommendationBlocksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserRecommendationBlocksApi.subclasses[0]().user_recommendation_blocks_id_relationships_videos_get(id, include, page_cursor, replace_media)


@router.post(
    "/userRecommendationBlocks/{id}/relationships/videos",
    responses={
        200: {"model": UserRecommendationBlocksVideosAddMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": UserRecommendationBlocksVideosAddMultiDataRelationshipWithResponse409ResponseBody, "description": "Recommendation block limit reached; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["userRecommendationBlocks"],
    summary="Add to videos relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_recommendation_blocks_id_relationships_videos_post(
    id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")] = Path(..., description="User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_recommendation_blocks_videos_relationship_add_operation_payload: Optional[UserRecommendationBlocksVideosRelationshipAddOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> UserRecommendationBlocksVideosAddMultiRelationshipDataDocument:
    """Adds item(s) to videos relationship."""
    if not BaseUserRecommendationBlocksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserRecommendationBlocksApi.subclasses[0]().user_recommendation_blocks_id_relationships_videos_post(id, idempotency_key, user_recommendation_blocks_videos_relationship_add_operation_payload)


@router.delete(
    "/userRecommendationBlocks/{id}/relationships/videos",
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
    tags=["userRecommendationBlocks"],
    summary="Delete from videos relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def user_recommendation_blocks_id_relationships_videos_delete(
    id: Annotated[str, Field(description="User recommendation blocks id. Use `me` for the authenticated user's resource")] = Path(..., description="User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource", examples=["me"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    user_recommendation_blocks_videos_relationship_remove_operation_payload: Optional[UserRecommendationBlocksVideosRelationshipRemoveOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes item(s) from videos relationship."""
    if not BaseUserRecommendationBlocksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUserRecommendationBlocksApi.subclasses[0]().user_recommendation_blocks_id_relationships_videos_delete(id, idempotency_key, user_recommendation_blocks_videos_relationship_remove_operation_payload)
