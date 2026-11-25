# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.artist_claims_api_base import BaseArtistClaimsApi
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
from tidal.models.artist_claims_accepted_artists_multi_relationship_data_document import ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument
from tidal.models.artist_claims_accepted_artists_relationship_update_operation_payload import ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload
from tidal.models.artist_claims_create_operation_payload import ArtistClaimsCreateOperationPayload
from tidal.models.artist_claims_create_single_resource_data_document import ArtistClaimsCreateSingleResourceDataDocument
from tidal.models.artist_claims_multi_resource_data_document import ArtistClaimsMultiResourceDataDocument
from tidal.models.artist_claims_owners_multi_relationship_data_document import ArtistClaimsOwnersMultiRelationshipDataDocument
from tidal.models.artist_claims_recommended_artists_multi_relationship_data_document import ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument
from tidal.models.artist_claims_single_resource_data_document import ArtistClaimsSingleResourceDataDocument
from tidal.models.artist_claims_update_operation_payload import ArtistClaimsUpdateOperationPayload
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
    "/artistClaims",
    responses={
        200: {"model": ArtistClaimsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artistClaims"],
    summary="Get multiple artistClaims.",
    response_model_by_alias=True,
)
async def artist_claims_get(
    filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="User id. Also accepts `me`.")] = Query(..., description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: acceptedArtists, owners, recommendedArtists")] = Query(None, description="Include related resources. Available relationships: acceptedArtists, owners, recommendedArtists", alias="include", examples=["acceptedArtists.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: acceptedArtists.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: acceptedArtists.albums", alias="replaceMedia", examples=["acceptedArtists.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ArtistClaimsMultiResourceDataDocument:
    """Retrieves multiple artistClaims by available filters, or without if applicable."""
    if not BaseArtistClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistClaimsApi.subclasses[0]().artist_claims_get(filter_owners_id, include, include_linkage, replace_media)


@router.post(
    "/artistClaims",
    responses={
        201: {"model": ArtistClaimsCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["artistClaims"],
    summary="Create single artistClaim.",
    response_model_by_alias=True,
)
async def artist_claims_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    artist_claims_create_operation_payload: Optional[ArtistClaimsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> ArtistClaimsCreateSingleResourceDataDocument:
    """Creates a new artistClaim."""
    if not BaseArtistClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistClaimsApi.subclasses[0]().artist_claims_post(idempotency_key, artist_claims_create_operation_payload)


@router.get(
    "/artistClaims/{id}",
    responses={
        200: {"model": ArtistClaimsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artistClaims"],
    summary="Get single artistClaim.",
    response_model_by_alias=True,
)
async def artist_claims_id_get(
    id: Annotated[str, Field(description="Artist claim id")] = Path(..., description="Artist claim id", examples=["f47ac10b-58cc-4372-a567-0e02b2c3d479"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: acceptedArtists, owners, recommendedArtists")] = Query(None, description="Include related resources. Available relationships: acceptedArtists, owners, recommendedArtists", alias="include", examples=["acceptedArtists.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: acceptedArtists.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: acceptedArtists.albums", alias="replaceMedia", examples=["acceptedArtists.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ArtistClaimsSingleResourceDataDocument:
    """Retrieves single artistClaim by id."""
    if not BaseArtistClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistClaimsApi.subclasses[0]().artist_claims_id_get(id, include, include_linkage, replace_media)


@router.delete(
    "/artistClaims/{id}",
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
    tags=["artistClaims"],
    summary="Delete single artistClaim.",
    response_model_by_alias=True,
)
async def artist_claims_id_delete(
    id: Annotated[str, Field(description="Artist claim id")] = Path(..., description="Artist claim id", examples=["f47ac10b-58cc-4372-a567-0e02b2c3d479"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing artistClaim."""
    if not BaseArtistClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistClaimsApi.subclasses[0]().artist_claims_id_delete(id, idempotency_key)


@router.patch(
    "/artistClaims/{id}",
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
    tags=["artistClaims"],
    summary="Update single artistClaim.",
    response_model_by_alias=True,
)
async def artist_claims_id_patch(
    id: Annotated[str, Field(description="Artist claim id")] = Path(..., description="Artist claim id", examples=["f47ac10b-58cc-4372-a567-0e02b2c3d479"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    artist_claims_update_operation_payload: Optional[ArtistClaimsUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Updates existing artistClaim."""
    if not BaseArtistClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistClaimsApi.subclasses[0]().artist_claims_id_patch(id, idempotency_key, artist_claims_update_operation_payload)


@router.get(
    "/artistClaims/{id}/relationships/acceptedArtists",
    responses={
        200: {"model": ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artistClaims"],
    summary="Get acceptedArtists relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artist_claims_id_relationships_accepted_artists_get(
    id: Annotated[str, Field(description="Artist claim id")] = Path(..., description="Artist claim id", examples=["f47ac10b-58cc-4372-a567-0e02b2c3d479"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: acceptedArtists")] = Query(None, description="Include related resources. Available relationships: acceptedArtists", alias="include", examples=["acceptedArtists.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: acceptedArtists.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: acceptedArtists.albums", alias="replaceMedia", examples=["acceptedArtists.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument:
    """Retrieves acceptedArtists relationship."""
    if not BaseArtistClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistClaimsApi.subclasses[0]().artist_claims_id_relationships_accepted_artists_get(id, include, page_cursor, replace_media)


@router.patch(
    "/artistClaims/{id}/relationships/acceptedArtists",
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
    tags=["artistClaims"],
    summary="Update acceptedArtists relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artist_claims_id_relationships_accepted_artists_patch(
    id: Annotated[str, Field(description="Artist claim id")] = Path(..., description="Artist claim id", examples=["f47ac10b-58cc-4372-a567-0e02b2c3d479"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    artist_claims_accepted_artists_relationship_update_operation_payload: Optional[ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Accepts one recommended artist and processes the claim, merging profile metadata or moving claimed albums according to the recommendation. Empty data cancels the claim; it does not delete any artist. Returns an acknowledgement."""
    if not BaseArtistClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistClaimsApi.subclasses[0]().artist_claims_id_relationships_accepted_artists_patch(id, idempotency_key, artist_claims_accepted_artists_relationship_update_operation_payload)


@router.get(
    "/artistClaims/{id}/relationships/owners",
    responses={
        200: {"model": ArtistClaimsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artistClaims"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artist_claims_id_relationships_owners_get(
    id: Annotated[str, Field(description="Artist claim id")] = Path(..., description="Artist claim id", examples=["f47ac10b-58cc-4372-a567-0e02b2c3d479"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ArtistClaimsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseArtistClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistClaimsApi.subclasses[0]().artist_claims_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/artistClaims/{id}/relationships/recommendedArtists",
    responses={
        200: {"model": ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artistClaims"],
    summary="Get recommendedArtists relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artist_claims_id_relationships_recommended_artists_get(
    id: Annotated[str, Field(description="Artist claim id")] = Path(..., description="Artist claim id", examples=["f47ac10b-58cc-4372-a567-0e02b2c3d479"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: recommendedArtists")] = Query(None, description="Include related resources. Available relationships: recommendedArtists", alias="include", examples=["recommendedArtists.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: recommendedArtists.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: recommendedArtists.albums", alias="replaceMedia", examples=["recommendedArtists.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument:
    """Retrieves recommendedArtists relationship."""
    if not BaseArtistClaimsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistClaimsApi.subclasses[0]().artist_claims_id_relationships_recommended_artists_get(id, include, page_cursor, replace_media)
