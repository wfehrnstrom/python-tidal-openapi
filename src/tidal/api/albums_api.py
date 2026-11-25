# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.albums_api_base import BaseAlbumsApi
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
from tidal.models.albums_album_statistics_single_relationship_data_document import AlbumsAlbumStatisticsSingleRelationshipDataDocument
from tidal.models.albums_artists_multi_relationship_data_document import AlbumsArtistsMultiRelationshipDataDocument
from tidal.models.albums_artists_relationship_update_operation_payload import AlbumsArtistsRelationshipUpdateOperationPayload
from tidal.models.albums_cover_art_multi_relationship_data_document import AlbumsCoverArtMultiRelationshipDataDocument
from tidal.models.albums_cover_art_relationship_update_operation_payload import AlbumsCoverArtRelationshipUpdateOperationPayload
from tidal.models.albums_create_operation_payload import AlbumsCreateOperationPayload
from tidal.models.albums_create_single_resource_data_document import AlbumsCreateSingleResourceDataDocument
from tidal.models.albums_genres_multi_relationship_data_document import AlbumsGenresMultiRelationshipDataDocument
from tidal.models.albums_items_multi_relationship_data_document import AlbumsItemsMultiRelationshipDataDocument
from tidal.models.albums_items_relationship_update_operation_payload import AlbumsItemsRelationshipUpdateOperationPayload
from tidal.models.albums_multi_resource_data_document import AlbumsMultiResourceDataDocument
from tidal.models.albums_owners_multi_relationship_data_document import AlbumsOwnersMultiRelationshipDataDocument
from tidal.models.albums_price_config_single_relationship_data_document import AlbumsPriceConfigSingleRelationshipDataDocument
from tidal.models.albums_providers_multi_relationship_data_document import AlbumsProvidersMultiRelationshipDataDocument
from tidal.models.albums_replacement_single_relationship_data_document import AlbumsReplacementSingleRelationshipDataDocument
from tidal.models.albums_shares_multi_relationship_data_document import AlbumsSharesMultiRelationshipDataDocument
from tidal.models.albums_similar_albums_multi_relationship_data_document import AlbumsSimilarAlbumsMultiRelationshipDataDocument
from tidal.models.albums_single_resource_data_document import AlbumsSingleResourceDataDocument
from tidal.models.albums_suggested_cover_arts_multi_relationship_data_document import AlbumsSuggestedCoverArtsMultiRelationshipDataDocument
from tidal.models.albums_update_operation_payload import AlbumsUpdateOperationPayload
from tidal.models.albums_usage_rules_single_relationship_data_document import AlbumsUsageRulesSingleRelationshipDataDocument
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
    "/albums",
    responses={
        200: {"model": AlbumsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get multiple albums.",
    response_model_by_alias=True,
)
async def albums_get(
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    filter_barcode_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of barcode IDs (EAN-13 or UPC-A). NOTE: Supplying more than one barcode ID will currently only return one album per barcode ID. (e.g. `196589525444`)")] = Query(None, description="List of barcode IDs (EAN-13 or UPC-A). NOTE: Supplying more than one barcode ID will currently only return one album per barcode ID. (e.g. &#x60;196589525444&#x60;)", alias="filter[barcodeId]"),
    filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of album IDs (e.g. `251380836`)")] = Query(None, description="List of album IDs (e.g. &#x60;251380836&#x60;)", alias="filter[id]"),
    filter_owners_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1)]], Field(description="User id. Also accepts `me`.")] = Query(None, description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules")] = Query(None, description="Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules", alias="include", examples=["artists.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums", alias="replaceMedia", examples=["artists.albums"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    sort: Annotated[Optional[List[str]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")] = Query(None, description="Values prefixed with \&quot;-\&quot; are sorted descending; values without it are sorted ascending.", alias="sort"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> AlbumsMultiResourceDataDocument:
    """Retrieves multiple albums by available filters, or without if applicable."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_get(country_code, filter_barcode_id, filter_id, filter_owners_id, include, include_linkage, page_cursor, replace_media, share_code, sort)


@router.post(
    "/albums",
    responses={
        201: {"model": AlbumsCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["albums"],
    summary="Create single album.",
    response_model_by_alias=True,
)
async def albums_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    albums_create_operation_payload: Optional[AlbumsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> AlbumsCreateSingleResourceDataDocument:
    """Creates an uploaded album. Album creation is not atomic with its artist assignment, so the caller must be OWNER of every listed artist; COLLABORATOR, or a role on an album, is not enough until the album exists."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_post(idempotency_key, albums_create_operation_payload)


@router.get(
    "/albums/{id}",
    responses={
        200: {"model": AlbumsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get single album.",
    response_model_by_alias=True,
)
async def albums_id_get(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules")] = Query(None, description="Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules", alias="include", examples=["artists.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums", alias="replaceMedia", examples=["artists.albums"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> AlbumsSingleResourceDataDocument:
    """Retrieves single album by id."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_get(id, country_code, include, include_linkage, replace_media, share_code)


@router.delete(
    "/albums/{id}",
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
    tags=["albums"],
    summary="Delete single album.",
    response_model_by_alias=True,
)
async def albums_id_delete(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing album."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_delete(id, idempotency_key, share_code)


@router.patch(
    "/albums/{id}",
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
    tags=["albums"],
    summary="Update single album.",
    response_model_by_alias=True,
)
async def albums_id_patch(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    albums_update_operation_payload: Optional[AlbumsUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Updates existing album. A COLLABORATOR on the album may update it; changing accessType, published or barcodeId needs OWNER."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_patch(id, idempotency_key, share_code, albums_update_operation_payload)


@router.get(
    "/albums/{id}/relationships/albumStatistics",
    responses={
        200: {"model": AlbumsAlbumStatisticsSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get albumStatistics relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_album_statistics_get(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albumStatistics")] = Query(None, description="Include related resources. Available relationships: albumStatistics", alias="include", examples=["albumStatistics"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> AlbumsAlbumStatisticsSingleRelationshipDataDocument:
    """Retrieves albumStatistics relationship."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_album_statistics_get(id, include, share_code)


@router.get(
    "/albums/{id}/relationships/artists",
    responses={
        200: {"model": AlbumsArtistsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get artists relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_artists_get(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
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
) -> AlbumsArtistsMultiRelationshipDataDocument:
    """Retrieves artists relationship."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_artists_get(id, country_code, include, page_cursor, replace_media, share_code)


@router.patch(
    "/albums/{id}/relationships/artists",
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
    tags=["albums"],
    summary="Update artists relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_artists_patch(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    albums_artists_relationship_update_operation_payload: Optional[AlbumsArtistsRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Sets the album&#39;s artists, replacing the current list. Artists are listed in the order given. Provide 1 to 10 distinct artists. You can add your own artist profile and the profiles of users who have owner or collaborator access to the album. Owners and collaborators can change its artists. Returns an acknowledgement."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_artists_patch(id, idempotency_key, share_code, albums_artists_relationship_update_operation_payload)


@router.get(
    "/albums/{id}/relationships/coverArt",
    responses={
        200: {"model": AlbumsCoverArtMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get coverArt relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_cover_art_get(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: coverArt")] = Query(None, description="Include related resources. Available relationships: coverArt", alias="include", examples=["coverArt"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> AlbumsCoverArtMultiRelationshipDataDocument:
    """Retrieves coverArt relationship."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_cover_art_get(id, country_code, include, page_cursor, share_code)


@router.patch(
    "/albums/{id}/relationships/coverArt",
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
    tags=["albums"],
    summary="Update coverArt relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_cover_art_patch(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    albums_cover_art_relationship_update_operation_payload: Optional[AlbumsCoverArtRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Replaces the uploaded cover artwork selection with one attachable artwork. Empty data clears the selection. Previously attached uploaded artwork is soft-deleted unless system-managed. Returns an acknowledgement."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_cover_art_patch(id, idempotency_key, share_code, albums_cover_art_relationship_update_operation_payload)


@router.get(
    "/albums/{id}/relationships/genres",
    responses={
        200: {"model": AlbumsGenresMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get genres relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_genres_get(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
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
) -> AlbumsGenresMultiRelationshipDataDocument:
    """Retrieves genres relationship."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_genres_get(id, country_code, include, page_cursor, share_code)


@router.get(
    "/albums/{id}/relationships/items",
    responses={
        200: {"model": AlbumsItemsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_items_get(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")] = Query(None, description="Include related resources. Available relationships: items", alias="include", examples=["items"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items", alias="replaceMedia", examples=["items"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> AlbumsItemsMultiRelationshipDataDocument:
    """Retrieves items relationship."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_items_get(id, country_code, include, page_cursor, replace_media, share_code)


@router.patch(
    "/albums/{id}/relationships/items",
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
    tags=["albums"],
    summary="Update items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_items_patch(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    albums_items_relationship_update_operation_payload: Optional[AlbumsItemsRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> MutationResponseDocument:
    """Incrementally updates one existing track&#39;s 1-based track number to meta.positionIndex. Does not replace the album&#39;s items or add or remove tracks. Empty data is rejected. A COLLABORATOR on the album may reorder. Returns an acknowledgement."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_items_patch(id, idempotency_key, share_code, albums_items_relationship_update_operation_payload)


@router.get(
    "/albums/{id}/relationships/owners",
    responses={
        200: {"model": AlbumsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_owners_get(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> AlbumsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_owners_get(id, include, page_cursor, share_code)


@router.get(
    "/albums/{id}/relationships/priceConfig",
    responses={
        200: {"model": AlbumsPriceConfigSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get priceConfig relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_price_config_get(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: priceConfig")] = Query(None, description="Include related resources. Available relationships: priceConfig", alias="include", examples=["priceConfig"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> AlbumsPriceConfigSingleRelationshipDataDocument:
    """Retrieves priceConfig relationship."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_price_config_get(id, country_code, include, share_code)


@router.get(
    "/albums/{id}/relationships/providers",
    responses={
        200: {"model": AlbumsProvidersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get providers relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_providers_get(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
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
) -> AlbumsProvidersMultiRelationshipDataDocument:
    """Retrieves providers relationship."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_providers_get(id, country_code, include, page_cursor, share_code)


@router.get(
    "/albums/{id}/relationships/replacement",
    responses={
        200: {"model": AlbumsReplacementSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get replacement relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_replacement_get(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
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
) -> AlbumsReplacementSingleRelationshipDataDocument:
    """Retrieves replacement relationship."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_replacement_get(id, country_code, include, replace_media, share_code)


@router.get(
    "/albums/{id}/relationships/shares",
    responses={
        200: {"model": AlbumsSharesMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get shares relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_shares_get(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: shares")] = Query(None, description="Include related resources. Available relationships: shares", alias="include", examples=["shares.sharedResources"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: shares.sharedResources")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: shares.sharedResources", alias="replaceMedia", examples=["shares.sharedResources"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> AlbumsSharesMultiRelationshipDataDocument:
    """The album&#39;s share links, active and expired, newest first."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_shares_get(id, include, page_cursor, replace_media, share_code)


@router.get(
    "/albums/{id}/relationships/similarAlbums",
    responses={
        200: {"model": AlbumsSimilarAlbumsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get similarAlbums relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_similar_albums_get(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: similarAlbums")] = Query(None, description="Include related resources. Available relationships: similarAlbums", alias="include", examples=["similarAlbums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarAlbums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: similarAlbums", alias="replaceMedia", examples=["similarAlbums"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> AlbumsSimilarAlbumsMultiRelationshipDataDocument:
    """Retrieves similarAlbums relationship."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_similar_albums_get(id, country_code, include, page_cursor, replace_media, share_code)


@router.get(
    "/albums/{id}/relationships/suggestedCoverArts",
    responses={
        200: {"model": AlbumsSuggestedCoverArtsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get suggestedCoverArts relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_suggested_cover_arts_get(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: suggestedCoverArts")] = Query(None, description="Include related resources. Available relationships: suggestedCoverArts", alias="include", examples=["suggestedCoverArts"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> AlbumsSuggestedCoverArtsMultiRelationshipDataDocument:
    """Retrieves suggestedCoverArts relationship."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_suggested_cover_arts_get(id, include, page_cursor, share_code)


@router.get(
    "/albums/{id}/relationships/usageRules",
    responses={
        200: {"model": AlbumsUsageRulesSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["albums"],
    summary="Get usageRules relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def albums_id_relationships_usage_rules_get(
    id: Annotated[str, Field(description="Album id")] = Path(..., description="Album id", examples=["251380836"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: usageRules")] = Query(None, description="Include related resources. Available relationships: usageRules", alias="include", examples=["usageRules"]),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> AlbumsUsageRulesSingleRelationshipDataDocument:
    """Retrieves usageRules relationship."""
    if not BaseAlbumsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAlbumsApi.subclasses[0]().albums_id_relationships_usage_rules_get(id, country_code, include, share_code)
