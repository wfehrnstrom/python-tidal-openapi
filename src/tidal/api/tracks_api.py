# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.tracks_api_base import BaseTracksApi
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
from tidal.models.tracks_albums_multi_relationship_data_document import TracksAlbumsMultiRelationshipDataDocument
from tidal.models.tracks_albums_relationship_update_operation_payload import TracksAlbumsRelationshipUpdateOperationPayload
from tidal.models.tracks_artists_multi_relationship_data_document import TracksArtistsMultiRelationshipDataDocument
from tidal.models.tracks_artists_relationship_update_operation_payload import TracksArtistsRelationshipUpdateOperationPayload
from tidal.models.tracks_create_operation_payload import TracksCreateOperationPayload
from tidal.models.tracks_create_single_resource_data_document import TracksCreateSingleResourceDataDocument
from tidal.models.tracks_credits_multi_relationship_data_document import TracksCreditsMultiRelationshipDataDocument
from tidal.models.tracks_download_single_relationship_data_document import TracksDownloadSingleRelationshipDataDocument
from tidal.models.tracks_genres_multi_relationship_data_document import TracksGenresMultiRelationshipDataDocument
from tidal.models.tracks_lyrics_multi_relationship_data_document import TracksLyricsMultiRelationshipDataDocument
from tidal.models.tracks_metadata_status_single_relationship_data_document import TracksMetadataStatusSingleRelationshipDataDocument
from tidal.models.tracks_multi_resource_data_document import TracksMultiResourceDataDocument
from tidal.models.tracks_owners_multi_relationship_data_document import TracksOwnersMultiRelationshipDataDocument
from tidal.models.tracks_price_config_single_relationship_data_document import TracksPriceConfigSingleRelationshipDataDocument
from tidal.models.tracks_providers_multi_relationship_data_document import TracksProvidersMultiRelationshipDataDocument
from tidal.models.tracks_radio_multi_relationship_data_document import TracksRadioMultiRelationshipDataDocument
from tidal.models.tracks_replacement_single_relationship_data_document import TracksReplacementSingleRelationshipDataDocument
from tidal.models.tracks_shares_multi_relationship_data_document import TracksSharesMultiRelationshipDataDocument
from tidal.models.tracks_similar_tracks_multi_relationship_data_document import TracksSimilarTracksMultiRelationshipDataDocument
from tidal.models.tracks_single_resource_data_document import TracksSingleResourceDataDocument
from tidal.models.tracks_source_file_single_relationship_data_document import TracksSourceFileSingleRelationshipDataDocument
from tidal.models.tracks_suggested_tracks_multi_relationship_data_document import TracksSuggestedTracksMultiRelationshipDataDocument
from tidal.models.tracks_track_statistics_single_relationship_data_document import TracksTrackStatisticsSingleRelationshipDataDocument
from tidal.models.tracks_update_operation_payload import TracksUpdateOperationPayload
from tidal.models.tracks_usage_rules_single_relationship_data_document import TracksUsageRulesSingleRelationshipDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/tracks",
    responses={
        200: {"model": TracksMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get multiple tracks.",
    response_model_by_alias=True,
)
async def tracks_get(
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of track IDs (e.g. `75413016`)")] = Query(None, description="List of track IDs (e.g. &#x60;75413016&#x60;)", alias="filter[id]"),
    filter_isrc: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of ISRCs. When a single ISRC is provided, pagination is supported and multiple tracks may be returned. When multiple ISRCs are provided, one track per ISRC is returned without pagination. (e.g. `QMJMT1701237`)")] = Query(None, description="List of ISRCs. When a single ISRC is provided, pagination is supported and multiple tracks may be returned. When multiple ISRCs are provided, one track per ISRC is returned without pagination. (e.g. &#x60;QMJMT1701237&#x60;)", alias="filter[isrc]"),
    filter_owners_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1)]], Field(description="User id. Also accepts `me`.")] = Query(None, description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums, artists, credits, download, genres, lyrics, metadataStatus, owners, priceConfig, providers, radio, replacement, shares, similarTracks, sourceFile, suggestedTracks, trackStatistics, usageRules")] = Query(None, description="Include related resources. Available relationships: albums, artists, credits, download, genres, lyrics, metadataStatus, owners, priceConfig, providers, radio, replacement, shares, similarTracks, sourceFile, suggestedTracks, trackStatistics, usageRules", alias="include", examples=["albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums", alias="replaceMedia", examples=["albums"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    sort: Annotated[Optional[List[str]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")] = Query(None, description="Values prefixed with \&quot;-\&quot; are sorted descending; values without it are sorted ascending.", alias="sort"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksMultiResourceDataDocument:
    """Retrieves multiple tracks by available filters, or without if applicable."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_get(country_code, filter_id, filter_isrc, filter_owners_id, include, include_linkage, page_cursor, replace_media, share_code, sort)


@router.post(
    "/tracks",
    responses={
        201: {"model": TracksCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["tracks"],
    summary="Create single track.",
    response_model_by_alias=True,
)
async def tracks_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    tracks_create_operation_payload: Optional[TracksCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> TracksCreateSingleResourceDataDocument:
    """Creates a new track."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_post(idempotency_key, tracks_create_operation_payload)


@router.get(
    "/tracks/{id}",
    responses={
        200: {"model": TracksSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get single track.",
    response_model_by_alias=True,
)
async def tracks_id_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums, artists, credits, download, genres, lyrics, metadataStatus, owners, priceConfig, providers, radio, replacement, shares, similarTracks, sourceFile, suggestedTracks, trackStatistics, usageRules")] = Query(None, description="Include related resources. Available relationships: albums, artists, credits, download, genres, lyrics, metadataStatus, owners, priceConfig, providers, radio, replacement, shares, similarTracks, sourceFile, suggestedTracks, trackStatistics, usageRules", alias="include", examples=["albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums", alias="replaceMedia", examples=["albums"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksSingleResourceDataDocument:
    """Retrieves single track by id."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_get(id, country_code, include, include_linkage, replace_media, share_code)


@router.delete(
    "/tracks/{id}",
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
    tags=["tracks"],
    summary="Delete single track.",
    response_model_by_alias=True,
)
async def tracks_id_delete(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing track."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_delete(id, idempotency_key, share_code)


@router.patch(
    "/tracks/{id}",
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
    tags=["tracks"],
    summary="Update single track.",
    response_model_by_alias=True,
)
async def tracks_id_patch(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    tracks_update_operation_payload: Optional[TracksUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Updates existing track. A COLLABORATOR on the track may update it; changing accessType or isrc needs OWNER."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_patch(id, idempotency_key, share_code, tracks_update_operation_payload)


@router.get(
    "/tracks/{id}/relationships/albums",
    responses={
        200: {"model": TracksAlbumsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get albums relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_albums_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums")] = Query(None, description="Include related resources. Available relationships: albums", alias="include", examples=["albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums", alias="replaceMedia", examples=["albums"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksAlbumsMultiRelationshipDataDocument:
    """Retrieves albums relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_albums_get(id, country_code, include, page_cursor, replace_media, share_code)


@router.patch(
    "/tracks/{id}/relationships/albums",
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
    tags=["tracks"],
    summary="Update albums relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_albums_patch(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    tracks_albums_relationship_update_operation_payload: Optional[TracksAlbumsRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Moves the uploaded track to the supplied album, replacing its previous album association. Exactly one album is required; empty data cannot clear it. The caller needs COLLABORATOR on the track and the album. The album must be in the same user&#39;s folders as the track (409 otherwise). Returns an acknowledgement."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_albums_patch(id, idempotency_key, share_code, tracks_albums_relationship_update_operation_payload)


@router.get(
    "/tracks/{id}/relationships/artists",
    responses={
        200: {"model": TracksArtistsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get artists relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_artists_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artists")] = Query(None, description="Include related resources. Available relationships: artists", alias="include", examples=["artists.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums", alias="replaceMedia", examples=["artists.albums"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksArtistsMultiRelationshipDataDocument:
    """Retrieves artists relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_artists_get(id, country_code, include, page_cursor, replace_media, share_code)


@router.patch(
    "/tracks/{id}/relationships/artists",
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
    tags=["tracks"],
    summary="Update artists relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_artists_patch(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    tracks_artists_relationship_update_operation_payload: Optional[TracksArtistsRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Sets the track&#39;s artists, replacing the current list. Artists are listed in the order given. Provide 1 to 10 distinct artists. You can add your own artist profile and the profiles of users who have owner or collaborator access to the track or its album. Owners and collaborators can change its artists. Returns an acknowledgement."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_artists_patch(id, idempotency_key, share_code, tracks_artists_relationship_update_operation_payload)


@router.get(
    "/tracks/{id}/relationships/credits",
    responses={
        200: {"model": TracksCreditsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get credits relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_credits_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: credits")] = Query(None, description="Include related resources. Available relationships: credits", alias="include", examples=["credits.artist.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: credits.artist.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: credits.artist.albums", alias="replaceMedia", examples=["credits.artist.albums"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksCreditsMultiRelationshipDataDocument:
    """Retrieves credits relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_credits_get(id, include, page_cursor, replace_media, share_code)


@router.get(
    "/tracks/{id}/relationships/download",
    responses={
        200: {"model": TracksDownloadSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get download relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_download_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: download")] = Query(None, description="Include related resources. Available relationships: download", alias="include", examples=["download"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> TracksDownloadSingleRelationshipDataDocument:
    """Retrieves download relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_download_get(id, include, share_code)


@router.get(
    "/tracks/{id}/relationships/genres",
    responses={
        200: {"model": TracksGenresMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get genres relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_genres_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: genres")] = Query(None, description="Include related resources. Available relationships: genres", alias="include", examples=["genres"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksGenresMultiRelationshipDataDocument:
    """Retrieves genres relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_genres_get(id, country_code, include, page_cursor, share_code)


@router.get(
    "/tracks/{id}/relationships/lyrics",
    responses={
        200: {"model": TracksLyricsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get lyrics relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_lyrics_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: lyrics")] = Query(None, description="Include related resources. Available relationships: lyrics", alias="include", examples=["lyrics.track"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: lyrics.track")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: lyrics.track", alias="replaceMedia", examples=["lyrics.track"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksLyricsMultiRelationshipDataDocument:
    """Retrieves lyrics relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_lyrics_get(id, include, page_cursor, replace_media, share_code)


@router.get(
    "/tracks/{id}/relationships/metadataStatus",
    responses={
        200: {"model": TracksMetadataStatusSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get metadataStatus relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_metadata_status_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: metadataStatus")] = Query(None, description="Include related resources. Available relationships: metadataStatus", alias="include", examples=["metadataStatus"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> TracksMetadataStatusSingleRelationshipDataDocument:
    """Retrieves metadataStatus relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_metadata_status_get(id, include, share_code)


@router.get(
    "/tracks/{id}/relationships/owners",
    responses={
        200: {"model": TracksOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_owners_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_owners_get(id, include, page_cursor, share_code)


@router.get(
    "/tracks/{id}/relationships/priceConfig",
    responses={
        200: {"model": TracksPriceConfigSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get priceConfig relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_price_config_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: priceConfig")] = Query(None, description="Include related resources. Available relationships: priceConfig", alias="include", examples=["priceConfig"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksPriceConfigSingleRelationshipDataDocument:
    """Retrieves priceConfig relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_price_config_get(id, country_code, include, share_code)


@router.get(
    "/tracks/{id}/relationships/providers",
    responses={
        200: {"model": TracksProvidersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get providers relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_providers_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: providers")] = Query(None, description="Include related resources. Available relationships: providers", alias="include", examples=["providers"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksProvidersMultiRelationshipDataDocument:
    """Retrieves providers relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_providers_get(id, country_code, include, page_cursor, share_code)


@router.get(
    "/tracks/{id}/relationships/radio",
    responses={
        200: {"model": TracksRadioMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get radio relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_radio_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: radio")] = Query(None, description="Include related resources. Available relationships: radio", alias="include", examples=["radio.items"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: radio.items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: radio.items", alias="replaceMedia", examples=["radio.items"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksRadioMultiRelationshipDataDocument:
    """Retrieves radio relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_radio_get(id, include, page_cursor, replace_media, share_code)


@router.get(
    "/tracks/{id}/relationships/replacement",
    responses={
        200: {"model": TracksReplacementSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get replacement relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_replacement_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: replacement")] = Query(None, description="Include related resources. Available relationships: replacement", alias="include", examples=["replacement"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: replacement")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: replacement", alias="replaceMedia", examples=["replacement"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksReplacementSingleRelationshipDataDocument:
    """Retrieves replacement relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_replacement_get(id, country_code, include, replace_media, share_code)


@router.get(
    "/tracks/{id}/relationships/shares",
    responses={
        200: {"model": TracksSharesMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get shares relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_shares_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: shares")] = Query(None, description="Include related resources. Available relationships: shares", alias="include", examples=["shares.sharedResources"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: shares.sharedResources")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: shares.sharedResources", alias="replaceMedia", examples=["shares.sharedResources"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> TracksSharesMultiRelationshipDataDocument:
    """The track&#39;s share links, active and expired, newest first."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_shares_get(id, include, page_cursor, replace_media, share_code)


@router.get(
    "/tracks/{id}/relationships/similarTracks",
    responses={
        200: {"model": TracksSimilarTracksMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get similarTracks relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_similar_tracks_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: similarTracks")] = Query(None, description="Include related resources. Available relationships: similarTracks", alias="include", examples=["similarTracks"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarTracks")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: similarTracks", alias="replaceMedia", examples=["similarTracks"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksSimilarTracksMultiRelationshipDataDocument:
    """Retrieves similarTracks relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_similar_tracks_get(id, country_code, include, page_cursor, replace_media, share_code)


@router.get(
    "/tracks/{id}/relationships/sourceFile",
    responses={
        200: {"model": TracksSourceFileSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get sourceFile relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_source_file_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: sourceFile")] = Query(None, description="Include related resources. Available relationships: sourceFile", alias="include", examples=["sourceFile"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksSourceFileSingleRelationshipDataDocument:
    """Retrieves sourceFile relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_source_file_get(id, include, share_code)


@router.get(
    "/tracks/{id}/relationships/suggestedTracks",
    responses={
        200: {"model": TracksSuggestedTracksMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get suggestedTracks relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_suggested_tracks_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: suggestedTracks")] = Query(None, description="Include related resources. Available relationships: suggestedTracks", alias="include", examples=["suggestedTracks"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: suggestedTracks")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: suggestedTracks", alias="replaceMedia", examples=["suggestedTracks"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksSuggestedTracksMultiRelationshipDataDocument:
    """Retrieves suggestedTracks relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_suggested_tracks_get(id, country_code, include, page_cursor, replace_media, share_code)


@router.get(
    "/tracks/{id}/relationships/trackStatistics",
    responses={
        200: {"model": TracksTrackStatisticsSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get trackStatistics relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_track_statistics_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: trackStatistics")] = Query(None, description="Include related resources. Available relationships: trackStatistics", alias="include", examples=["trackStatistics"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
) -> TracksTrackStatisticsSingleRelationshipDataDocument:
    """Retrieves trackStatistics relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_track_statistics_get(id, include, share_code)


@router.get(
    "/tracks/{id}/relationships/usageRules",
    responses={
        200: {"model": TracksUsageRulesSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["tracks"],
    summary="Get usageRules relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def tracks_id_relationships_usage_rules_get(
    id: Annotated[str, Field(description="Track id")] = Path(..., description="Track id", examples=["75413016"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: usageRules")] = Query(None, description="Include related resources. Available relationships: usageRules", alias="include", examples=["usageRules"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TracksUsageRulesSingleRelationshipDataDocument:
    """Retrieves usageRules relationship."""
    if not BaseTracksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTracksApi.subclasses[0]().tracks_id_relationships_usage_rules_get(id, country_code, include, share_code)
