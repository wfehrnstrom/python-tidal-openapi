# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.artists_api_base import BaseArtistsApi
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
from tidal.models.artists_albums_multi_relationship_data_document import ArtistsAlbumsMultiRelationshipDataDocument
from tidal.models.artists_banner_art_multi_relationship_data_document import ArtistsBannerArtMultiRelationshipDataDocument
from tidal.models.artists_banner_art_relationship_update_operation_payload import ArtistsBannerArtRelationshipUpdateOperationPayload
from tidal.models.artists_biography_single_relationship_data_document import ArtistsBiographySingleRelationshipDataDocument
from tidal.models.artists_claim_status_single_relationship_data_document import ArtistsClaimStatusSingleRelationshipDataDocument
from tidal.models.artists_create_operation_payload import ArtistsCreateOperationPayload
from tidal.models.artists_create_single_resource_data_document import ArtistsCreateSingleResourceDataDocument
from tidal.models.artists_followers_multi_relationship_data_document import ArtistsFollowersMultiRelationshipDataDocument
from tidal.models.artists_following_multi_relationship_data_document import ArtistsFollowingMultiRelationshipDataDocument
from tidal.models.artists_following_relationship_add_operation_payload import ArtistsFollowingRelationshipAddOperationPayload
from tidal.models.artists_following_relationship_remove_operation_payload import ArtistsFollowingRelationshipRemoveOperationPayload
from tidal.models.artists_logo_art_multi_relationship_data_document import ArtistsLogoArtMultiRelationshipDataDocument
from tidal.models.artists_logo_art_relationship_update_operation_payload import ArtistsLogoArtRelationshipUpdateOperationPayload
from tidal.models.artists_multi_resource_data_document import ArtistsMultiResourceDataDocument
from tidal.models.artists_owners_multi_relationship_data_document import ArtistsOwnersMultiRelationshipDataDocument
from tidal.models.artists_profile_art_multi_relationship_data_document import ArtistsProfileArtMultiRelationshipDataDocument
from tidal.models.artists_profile_art_relationship_update_operation_payload import ArtistsProfileArtRelationshipUpdateOperationPayload
from tidal.models.artists_radio_multi_relationship_data_document import ArtistsRadioMultiRelationshipDataDocument
from tidal.models.artists_roles_multi_relationship_data_document import ArtistsRolesMultiRelationshipDataDocument
from tidal.models.artists_similar_artists_multi_relationship_data_document import ArtistsSimilarArtistsMultiRelationshipDataDocument
from tidal.models.artists_single_resource_data_document import ArtistsSingleResourceDataDocument
from tidal.models.artists_track_providers_multi_relationship_data_document import ArtistsTrackProvidersMultiRelationshipDataDocument
from tidal.models.artists_tracks_multi_relationship_data_document import ArtistsTracksMultiRelationshipDataDocument
from tidal.models.artists_update_operation_payload import ArtistsUpdateOperationPayload
from tidal.models.artists_videos_multi_relationship_data_document import ArtistsVideosMultiRelationshipDataDocument
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
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/artists",
    responses={
        200: {"model": ArtistsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get multiple artists.",
    response_model_by_alias=True,
)
async def artists_get(
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    filter_handle: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="Artist handle (e.g. `jayz`)")] = Query(None, description="Artist handle (e.g. &#x60;jayz&#x60;)", alias="filter[handle]"),
    filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of artist IDs (e.g. `1566`)")] = Query(None, description="List of artist IDs (e.g. &#x60;1566&#x60;)", alias="filter[id]"),
    filter_owners_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1)]], Field(description="User id. Also accepts `me`.")] = Query(None, description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos")] = Query(None, description="Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos", alias="include", examples=["albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums", alias="replaceMedia", examples=["albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtistsMultiResourceDataDocument:
    """Retrieves multiple artists by available filters, or without if applicable."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_get(country_code, filter_handle, filter_id, filter_owners_id, include, include_linkage, replace_media)


@router.post(
    "/artists",
    responses={
        200: {"model": MutationResponseDocument, "description": "Successful dry run"},
        201: {"model": ArtistsCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["artists"],
    summary="Create single artist.",
    response_model_by_alias=True,
)
async def artists_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    artists_create_operation_payload: Optional[ArtistsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Creates a new artist."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_post(idempotency_key, artists_create_operation_payload)


@router.get(
    "/artists/{id}",
    responses={
        200: {"model": ArtistsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get single artist.",
    response_model_by_alias=True,
)
async def artists_id_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos")] = Query(None, description="Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos", alias="include", examples=["albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums", alias="replaceMedia", examples=["albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtistsSingleResourceDataDocument:
    """Retrieves single artist by id."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_get(id, country_code, include, include_linkage, replace_media)


@router.patch(
    "/artists/{id}",
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
    tags=["artists"],
    summary="Update single artist.",
    response_model_by_alias=True,
)
async def artists_id_patch(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    artists_update_operation_payload: Optional[ArtistsUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """When both profile colours are available, they must have at least 3:1 contrast."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_patch(id, idempotency_key, artists_update_operation_payload)


@router.get(
    "/artists/{id}/relationships/albums",
    responses={
        200: {"model": ArtistsAlbumsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get albums relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_albums_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums")] = Query(None, description="Include related resources. Available relationships: albums", alias="include", examples=["albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums", alias="replaceMedia", examples=["albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtistsAlbumsMultiRelationshipDataDocument:
    """Retrieves albums relationship."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_albums_get(id, country_code, include, page_cursor, replace_media)


@router.get(
    "/artists/{id}/relationships/bannerArt",
    responses={
        200: {"model": ArtistsBannerArtMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get bannerArt relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_banner_art_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: bannerArt")] = Query(None, description="Include related resources. Available relationships: bannerArt", alias="include", examples=["bannerArt"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtistsBannerArtMultiRelationshipDataDocument:
    """Reads the selected header banner artwork."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_banner_art_get(id, country_code, include, page_cursor)


@router.patch(
    "/artists/{id}/relationships/bannerArt",
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
    tags=["artists"],
    summary="Update bannerArt relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_banner_art_patch(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    artists_banner_art_relationship_update_operation_payload: Optional[ArtistsBannerArtRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Selects one owned, attachable IMAGE artwork by ID, replacing the selection. Empty data clears the selection; null data and more than one entry are rejected. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_banner_art_patch(id, idempotency_key, artists_banner_art_relationship_update_operation_payload)


@router.get(
    "/artists/{id}/relationships/biography",
    responses={
        200: {"model": ArtistsBiographySingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get biography relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_biography_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: biography")] = Query(None, description="Include related resources. Available relationships: biography", alias="include", examples=["biography"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtistsBiographySingleRelationshipDataDocument:
    """Retrieves biography relationship."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_biography_get(id, country_code, include)


@router.get(
    "/artists/{id}/relationships/claimStatus",
    responses={
        200: {"model": ArtistsClaimStatusSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get claimStatus relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_claim_status_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: claimStatus")] = Query(None, description="Include related resources. Available relationships: claimStatus", alias="include", examples=["claimStatus"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> ArtistsClaimStatusSingleRelationshipDataDocument:
    """Retrieves claimStatus relationship."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_claim_status_get(id, include)


@router.get(
    "/artists/{id}/relationships/followers",
    responses={
        200: {"model": ArtistsFollowersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get followers relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_followers_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: followers")] = Query(None, description="Include related resources. Available relationships: followers", alias="include", examples=["followers.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: followers.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: followers.albums", alias="replaceMedia", examples=["followers.albums"]),
    viewer_context: Optional[str] = Query(None, description="", alias="viewerContext"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> ArtistsFollowersMultiRelationshipDataDocument:
    """Retrieves followers relationship."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_followers_get(id, include, page_cursor, replace_media, viewer_context)


@router.get(
    "/artists/{id}/relationships/following",
    responses={
        200: {"model": ArtistsFollowingMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get following relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_following_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: following")] = Query(None, description="Include related resources. Available relationships: following", alias="include", examples=["following.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: following.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: following.albums", alias="replaceMedia", examples=["following.albums"]),
    viewer_context: Optional[str] = Query(None, description="", alias="viewerContext"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> ArtistsFollowingMultiRelationshipDataDocument:
    """Retrieves following relationship."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_following_get(id, include, page_cursor, replace_media, viewer_context)


@router.post(
    "/artists/{id}/relationships/following",
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
    tags=["artists"],
    summary="Add to following relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_following_post(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    artists_following_relationship_add_operation_payload: Optional[ArtistsFollowingRelationshipAddOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Adds item(s) to following relationship."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_following_post(id, idempotency_key, artists_following_relationship_add_operation_payload)


@router.delete(
    "/artists/{id}/relationships/following",
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
    tags=["artists"],
    summary="Delete from following relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_following_delete(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    artists_following_relationship_remove_operation_payload: Optional[ArtistsFollowingRelationshipRemoveOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes item(s) from following relationship."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_following_delete(id, idempotency_key, artists_following_relationship_remove_operation_payload)


@router.get(
    "/artists/{id}/relationships/logoArt",
    responses={
        200: {"model": ArtistsLogoArtMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get logoArt relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_logo_art_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: logoArt")] = Query(None, description="Include related resources. Available relationships: logoArt", alias="include", examples=["logoArt"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtistsLogoArtMultiRelationshipDataDocument:
    """Reads the selected logo artwork."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_logo_art_get(id, country_code, include, page_cursor)


@router.patch(
    "/artists/{id}/relationships/logoArt",
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
    tags=["artists"],
    summary="Update logoArt relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_logo_art_patch(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    artists_logo_art_relationship_update_operation_payload: Optional[ArtistsLogoArtRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Selects one owned, attachable IMAGE artwork by ID, replacing the selection. Empty data clears the selection; null data and more than one entry are rejected. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_logo_art_patch(id, idempotency_key, artists_logo_art_relationship_update_operation_payload)


@router.get(
    "/artists/{id}/relationships/owners",
    responses={
        200: {"model": ArtistsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_owners_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtistsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/artists/{id}/relationships/profileArt",
    responses={
        200: {"model": ArtistsProfileArtMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get profileArt relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_profile_art_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: profileArt")] = Query(None, description="Include related resources. Available relationships: profileArt", alias="include", examples=["profileArt"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtistsProfileArtMultiRelationshipDataDocument:
    """Reads the artist&#39;s avatar artwork."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_profile_art_get(id, country_code, include, page_cursor)


@router.patch(
    "/artists/{id}/relationships/profileArt",
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
    tags=["artists"],
    summary="Update profileArt relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_profile_art_patch(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    artists_profile_art_relationship_update_operation_payload: Optional[ArtistsProfileArtRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Replaces the artist&#39;s uploaded avatar selection with one owned, attachable artwork. Empty data clears the uploaded selection; legacy pictures or album fallback artwork may still appear in profileArt. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_profile_art_patch(id, idempotency_key, artists_profile_art_relationship_update_operation_payload)


@router.get(
    "/artists/{id}/relationships/radio",
    responses={
        200: {"model": ArtistsRadioMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get radio relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_radio_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: radio")] = Query(None, description="Include related resources. Available relationships: radio", alias="include", examples=["radio.items"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: radio.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: radio.items", alias="replaceMedia", examples=["radio.items"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtistsRadioMultiRelationshipDataDocument:
    """Retrieves radio relationship."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_radio_get(id, country_code, include, page_cursor, replace_media)


@router.get(
    "/artists/{id}/relationships/roles",
    responses={
        200: {"model": ArtistsRolesMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get roles relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_roles_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: roles")] = Query(None, description="Include related resources. Available relationships: roles", alias="include", examples=["roles"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtistsRolesMultiRelationshipDataDocument:
    """Retrieves roles relationship."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_roles_get(id, include, page_cursor)


@router.get(
    "/artists/{id}/relationships/similarArtists",
    responses={
        200: {"model": ArtistsSimilarArtistsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get similarArtists relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_similar_artists_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: similarArtists")] = Query(None, description="Include related resources. Available relationships: similarArtists", alias="include", examples=["similarArtists.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarArtists.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: similarArtists.albums", alias="replaceMedia", examples=["similarArtists.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtistsSimilarArtistsMultiRelationshipDataDocument:
    """Retrieves similarArtists relationship."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_similar_artists_get(id, country_code, include, page_cursor, replace_media)


@router.get(
    "/artists/{id}/relationships/trackProviders",
    responses={
        200: {"model": ArtistsTrackProvidersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get trackProviders relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_track_providers_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: trackProviders")] = Query(None, description="Include related resources. Available relationships: trackProviders", alias="include", examples=["trackProviders"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtistsTrackProvidersMultiRelationshipDataDocument:
    """Retrieves trackProviders relationship."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_track_providers_get(id, include, page_cursor)


@router.get(
    "/artists/{id}/relationships/tracks",
    responses={
        200: {"model": ArtistsTracksMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get tracks relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_tracks_get(
    collapse_by: Annotated[str, Field(description="Collapse by options for getting artist tracks. Available options: FINGERPRINT, ID. FINGERPRINT option might collapse similar tracks based entry fingerprints while collapsing by ID always returns all available items.")] = Query(..., description="Collapse by options for getting artist tracks. Available options: FINGERPRINT, ID. FINGERPRINT option might collapse similar tracks based entry fingerprints while collapsing by ID always returns all available items.", alias="collapseBy", examples=["FINGERPRINT"]),
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: tracks")] = Query(None, description="Include related resources. Available relationships: tracks", alias="include", examples=["tracks"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: tracks", alias="replaceMedia", examples=["tracks"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtistsTracksMultiRelationshipDataDocument:
    """Retrieves tracks relationship."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_tracks_get(collapse_by, id, country_code, include, page_cursor, replace_media)


@router.get(
    "/artists/{id}/relationships/videos",
    responses={
        200: {"model": ArtistsVideosMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["artists"],
    summary="Get videos relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def artists_id_relationships_videos_get(
    id: Annotated[str, Field(description="Artist id")] = Path(..., description="Artist id", examples=["1566"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: videos")] = Query(None, description="Include related resources. Available relationships: videos", alias="include", examples=["videos"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: videos", alias="replaceMedia", examples=["videos"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> ArtistsVideosMultiRelationshipDataDocument:
    """Retrieves videos relationship."""
    if not BaseArtistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseArtistsApi.subclasses[0]().artists_id_relationships_videos_get(id, country_code, include, page_cursor, replace_media)
