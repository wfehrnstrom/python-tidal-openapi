# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.lyrics_api_base import BaseLyricsApi
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
from tidal.models.lyrics_create_operation_payload import LyricsCreateOperationPayload
from tidal.models.lyrics_create_single_resource_data_document import LyricsCreateSingleResourceDataDocument
from tidal.models.lyrics_owners_multi_relationship_data_document import LyricsOwnersMultiRelationshipDataDocument
from tidal.models.lyrics_single_resource_data_document import LyricsSingleResourceDataDocument
from tidal.models.lyrics_track_single_relationship_data_document import LyricsTrackSingleRelationshipDataDocument
from tidal.models.lyrics_update_operation_payload import LyricsUpdateOperationPayload
from tidal.models.mutation_response_document import MutationResponseDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/lyrics",
    responses={
        201: {"model": LyricsCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["lyrics"],
    summary="Create single lyric.",
    response_model_by_alias=True,
)
async def lyrics_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    lyrics_create_operation_payload: Optional[LyricsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> LyricsCreateSingleResourceDataDocument:
    """Creates a new lyric."""
    if not BaseLyricsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLyricsApi.subclasses[0]().lyrics_post(idempotency_key, lyrics_create_operation_payload)


@router.get(
    "/lyrics/{id}",
    responses={
        200: {"model": LyricsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["lyrics"],
    summary="Get single lyric.",
    response_model_by_alias=True,
)
async def lyrics_id_get(
    id: Annotated[str, Field(description="Lyrics Id")] = Path(..., description="Lyrics Id", examples=["nejMcAhh5N8S3EQ4LaqysVdI0cZZ"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, track")] = Query(None, description="Include related resources. Available relationships: owners, track", alias="include", examples=["track"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: track")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: track", alias="replaceMedia", examples=["track"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> LyricsSingleResourceDataDocument:
    """Retrieves single lyric by id."""
    if not BaseLyricsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLyricsApi.subclasses[0]().lyrics_id_get(id, include, include_linkage, replace_media)


@router.delete(
    "/lyrics/{id}",
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
    tags=["lyrics"],
    summary="Delete single lyric.",
    response_model_by_alias=True,
)
async def lyrics_id_delete(
    id: Annotated[str, Field(description="Lyrics Id")] = Path(..., description="Lyrics Id", examples=["nejMcAhh5N8S3EQ4LaqysVdI0cZZ"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> MutationResponseDocument:
    """Deletes existing lyric."""
    if not BaseLyricsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLyricsApi.subclasses[0]().lyrics_id_delete(id, idempotency_key)


@router.patch(
    "/lyrics/{id}",
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
    tags=["lyrics"],
    summary="Update single lyric.",
    response_model_by_alias=True,
)
async def lyrics_id_patch(
    id: Annotated[str, Field(description="Lyrics Id")] = Path(..., description="Lyrics Id", examples=["nejMcAhh5N8S3EQ4LaqysVdI0cZZ"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    lyrics_update_operation_payload: Optional[LyricsUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Updates existing lyric."""
    if not BaseLyricsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLyricsApi.subclasses[0]().lyrics_id_patch(id, idempotency_key, lyrics_update_operation_payload)


@router.get(
    "/lyrics/{id}/relationships/owners",
    responses={
        200: {"model": LyricsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["lyrics"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def lyrics_id_relationships_owners_get(
    id: Annotated[str, Field(description="Lyrics Id")] = Path(..., description="Lyrics Id", examples=["nejMcAhh5N8S3EQ4LaqysVdI0cZZ"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> LyricsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseLyricsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLyricsApi.subclasses[0]().lyrics_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/lyrics/{id}/relationships/track",
    responses={
        200: {"model": LyricsTrackSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["lyrics"],
    summary="Get track relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def lyrics_id_relationships_track_get(
    id: Annotated[str, Field(description="Lyrics Id")] = Path(..., description="Lyrics Id", examples=["nejMcAhh5N8S3EQ4LaqysVdI0cZZ"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: track")] = Query(None, description="Include related resources. Available relationships: track", alias="include", examples=["track"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: track")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: track", alias="replaceMedia", examples=["track"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> LyricsTrackSingleRelationshipDataDocument:
    """Retrieves track relationship."""
    if not BaseLyricsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLyricsApi.subclasses[0]().lyrics_id_relationships_track_get(id, country_code, include, replace_media)
