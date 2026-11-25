# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.content_claims_api_base import BaseContentClaimsApi
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
from tidal.models.content_claims_claimed_resource_single_relationship_data_document import ContentClaimsClaimedResourceSingleRelationshipDataDocument
from tidal.models.content_claims_claiming_artist_single_relationship_data_document import ContentClaimsClaimingArtistSingleRelationshipDataDocument
from tidal.models.content_claims_create_operation_payload import ContentClaimsCreateOperationPayload
from tidal.models.content_claims_create_single_resource_data_document import ContentClaimsCreateSingleResourceDataDocument
from tidal.models.content_claims_multi_resource_data_document import ContentClaimsMultiResourceDataDocument
from tidal.models.content_claims_owners_multi_relationship_data_document import ContentClaimsOwnersMultiRelationshipDataDocument
from tidal.models.content_claims_single_resource_data_document import ContentClaimsSingleResourceDataDocument
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
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/contentClaims",
    responses={
        200: {"model": ContentClaimsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["contentClaims"],
    summary="Get multiple contentClaims.",
    response_model_by_alias=True,
)
async def content_claims_get(
    filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="User id. Also accepts `me`.")] = Query(..., description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: claimedResource, claimingArtist, owners")] = Query(None, description="Include related resources. Available relationships: claimedResource, claimingArtist, owners", alias="include", examples=["claimedResource"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: claimedResource")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: claimedResource", alias="replaceMedia", examples=["claimedResource"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ContentClaimsMultiResourceDataDocument:
    """Retrieves multiple contentClaims by available filters, or without if applicable."""
    if not BaseContentClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContentClaimsApi.subclasses[0]().content_claims_get(filter_owners_id, include, include_linkage, replace_media)


@router.post(
    "/contentClaims",
    responses={
        201: {"model": ContentClaimsCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["contentClaims"],
    summary="Create single contentClaim.",
    response_model_by_alias=True,
)
async def content_claims_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    content_claims_create_operation_payload: Optional[ContentClaimsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> ContentClaimsCreateSingleResourceDataDocument:
    """Creates a new contentClaim."""
    if not BaseContentClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContentClaimsApi.subclasses[0]().content_claims_post(idempotency_key, content_claims_create_operation_payload)


@router.get(
    "/contentClaims/{id}",
    responses={
        200: {"model": ContentClaimsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["contentClaims"],
    summary="Get single contentClaim.",
    response_model_by_alias=True,
)
async def content_claims_id_get(
    id: Annotated[str, Field(description="Content claim id")] = Path(..., description="Content claim id", examples=["f47ac10b-58cc-4372-a567-0e02b2c3d479"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: claimedResource, claimingArtist, owners")] = Query(None, description="Include related resources. Available relationships: claimedResource, claimingArtist, owners", alias="include", examples=["claimedResource"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: claimedResource")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: claimedResource", alias="replaceMedia", examples=["claimedResource"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ContentClaimsSingleResourceDataDocument:
    """Retrieves single contentClaim by id."""
    if not BaseContentClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContentClaimsApi.subclasses[0]().content_claims_id_get(id, include, include_linkage, replace_media)


@router.get(
    "/contentClaims/{id}/relationships/claimedResource",
    responses={
        200: {"model": ContentClaimsClaimedResourceSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["contentClaims"],
    summary="Get claimedResource relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def content_claims_id_relationships_claimed_resource_get(
    id: Annotated[str, Field(description="Content claim id")] = Path(..., description="Content claim id", examples=["f47ac10b-58cc-4372-a567-0e02b2c3d479"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: claimedResource")] = Query(None, description="Include related resources. Available relationships: claimedResource", alias="include", examples=["claimedResource"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: claimedResource")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: claimedResource", alias="replaceMedia", examples=["claimedResource"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ContentClaimsClaimedResourceSingleRelationshipDataDocument:
    """Retrieves claimedResource relationship."""
    if not BaseContentClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContentClaimsApi.subclasses[0]().content_claims_id_relationships_claimed_resource_get(id, include, replace_media)


@router.get(
    "/contentClaims/{id}/relationships/claimingArtist",
    responses={
        200: {"model": ContentClaimsClaimingArtistSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["contentClaims"],
    summary="Get claimingArtist relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def content_claims_id_relationships_claiming_artist_get(
    id: Annotated[str, Field(description="Content claim id")] = Path(..., description="Content claim id", examples=["f47ac10b-58cc-4372-a567-0e02b2c3d479"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: claimingArtist")] = Query(None, description="Include related resources. Available relationships: claimingArtist", alias="include", examples=["claimingArtist.albums"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: claimingArtist.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: claimingArtist.albums", alias="replaceMedia", examples=["claimingArtist.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ContentClaimsClaimingArtistSingleRelationshipDataDocument:
    """Retrieves claimingArtist relationship."""
    if not BaseContentClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContentClaimsApi.subclasses[0]().content_claims_id_relationships_claiming_artist_get(id, include, replace_media)


@router.get(
    "/contentClaims/{id}/relationships/owners",
    responses={
        200: {"model": ContentClaimsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["contentClaims"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def content_claims_id_relationships_owners_get(
    id: Annotated[str, Field(description="Content claim id")] = Path(..., description="Content claim id", examples=["f47ac10b-58cc-4372-a567-0e02b2c3d479"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ContentClaimsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseContentClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContentClaimsApi.subclasses[0]().content_claims_id_relationships_owners_get(id, include, page_cursor)
