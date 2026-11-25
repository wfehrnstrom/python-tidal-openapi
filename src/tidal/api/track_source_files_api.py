# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.track_source_files_api_base import BaseTrackSourceFilesApi
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
from tidal.models.track_source_files_comment_summary_single_relationship_data_document import TrackSourceFilesCommentSummarySingleRelationshipDataDocument
from tidal.models.track_source_files_create_operation_payload import TrackSourceFilesCreateOperationPayload
from tidal.models.track_source_files_create_single_resource_data_document import TrackSourceFilesCreateSingleResourceDataDocument
from tidal.models.track_source_files_owners_multi_relationship_data_document import TrackSourceFilesOwnersMultiRelationshipDataDocument
from tidal.models.track_source_files_reaction_summary_single_relationship_data_document import TrackSourceFilesReactionSummarySingleRelationshipDataDocument
from tidal.models.track_source_files_single_resource_data_document import TrackSourceFilesSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/trackSourceFiles",
    responses={
        201: {"model": TrackSourceFilesCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["trackSourceFiles"],
    summary="Create single trackSourceFile.",
    response_model_by_alias=True,
)
async def track_source_files_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    track_source_files_create_operation_payload: Optional[TrackSourceFilesCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> TrackSourceFilesCreateSingleResourceDataDocument:
    """Create a track source file. &lt;p/&gt; The response contains a upload link that must be used to upload the actual content.&lt;p/&gt; The headers in the upload link response must be sent doing the actual upload. """
    if not BaseTrackSourceFilesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTrackSourceFilesApi.subclasses[0]().track_source_files_post(idempotency_key, track_source_files_create_operation_payload)


@router.get(
    "/trackSourceFiles/{id}",
    responses={
        200: {"model": TrackSourceFilesSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["trackSourceFiles"],
    summary="Get single trackSourceFile.",
    response_model_by_alias=True,
)
async def track_source_files_id_get(
    id: Annotated[str, Field(description="Track source file id")] = Path(..., description="Track source file id", examples=["a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: commentSummary, owners, reactionSummary")] = Query(None, description="Include related resources. Available relationships: commentSummary, owners, reactionSummary", alias="include", examples=["commentSummary"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TrackSourceFilesSingleResourceDataDocument:
    """Retrieves single trackSourceFile by id."""
    if not BaseTrackSourceFilesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTrackSourceFilesApi.subclasses[0]().track_source_files_id_get(id, include, include_linkage, share_code)


@router.get(
    "/trackSourceFiles/{id}/relationships/commentSummary",
    responses={
        200: {"model": TrackSourceFilesCommentSummarySingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["trackSourceFiles"],
    summary="Get commentSummary relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def track_source_files_id_relationships_comment_summary_get(
    id: Annotated[str, Field(description="Track source file id")] = Path(..., description="Track source file id", examples=["a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: commentSummary")] = Query(None, description="Include related resources. Available relationships: commentSummary", alias="include", examples=["commentSummary"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> TrackSourceFilesCommentSummarySingleRelationshipDataDocument:
    """Retrieves commentSummary relationship."""
    if not BaseTrackSourceFilesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTrackSourceFilesApi.subclasses[0]().track_source_files_id_relationships_comment_summary_get(id, include, share_code)


@router.get(
    "/trackSourceFiles/{id}/relationships/owners",
    responses={
        200: {"model": TrackSourceFilesOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["trackSourceFiles"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def track_source_files_id_relationships_owners_get(
    id: Annotated[str, Field(description="Track source file id")] = Path(..., description="Track source file id", examples=["a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> TrackSourceFilesOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseTrackSourceFilesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTrackSourceFilesApi.subclasses[0]().track_source_files_id_relationships_owners_get(id, include, page_cursor, share_code)


@router.get(
    "/trackSourceFiles/{id}/relationships/reactionSummary",
    responses={
        200: {"model": TrackSourceFilesReactionSummarySingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["trackSourceFiles"],
    summary="Get reactionSummary relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def track_source_files_id_relationships_reaction_summary_get(
    id: Annotated[str, Field(description="Track source file id")] = Path(..., description="Track source file id", examples=["a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: reactionSummary")] = Query(None, description="Include related resources. Available relationships: reactionSummary", alias="include", examples=["reactionSummary"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> TrackSourceFilesReactionSummarySingleRelationshipDataDocument:
    """Retrieves reactionSummary relationship."""
    if not BaseTrackSourceFilesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTrackSourceFilesApi.subclasses[0]().track_source_files_id_relationships_reaction_summary_get(id, include, share_code)
