# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.playlists_api_base import BasePlaylistsApi
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
from tidal.models.playlists_collaborator_profiles_multi_relationship_data_document import PlaylistsCollaboratorProfilesMultiRelationshipDataDocument
from tidal.models.playlists_collaborator_profiles_relationship_remove_operation_payload import PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload
from tidal.models.playlists_collaborators_multi_relationship_data_document import PlaylistsCollaboratorsMultiRelationshipDataDocument
from tidal.models.playlists_cover_art_multi_relationship_data_document import PlaylistsCoverArtMultiRelationshipDataDocument
from tidal.models.playlists_cover_art_relationship_update_operation_payload import PlaylistsCoverArtRelationshipUpdateOperationPayload
from tidal.models.playlists_create_operation_payload import PlaylistsCreateOperationPayload
from tidal.models.playlists_create_single_resource_data_document import PlaylistsCreateSingleResourceDataDocument
from tidal.models.playlists_curators_multi_relationship_data_document import PlaylistsCuratorsMultiRelationshipDataDocument
from tidal.models.playlists_items_add_multi_data_relationship_with_response409_response_body import PlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBody
from tidal.models.playlists_items_add_multi_relationship_data_document import PlaylistsItemsAddMultiRelationshipDataDocument
from tidal.models.playlists_items_multi_relationship_data_document import PlaylistsItemsMultiRelationshipDataDocument
from tidal.models.playlists_items_relationship_add_operation_payload import PlaylistsItemsRelationshipAddOperationPayload
from tidal.models.playlists_items_relationship_remove_operation_payload import PlaylistsItemsRelationshipRemoveOperationPayload
from tidal.models.playlists_items_relationship_update_operation_payload import PlaylistsItemsRelationshipUpdateOperationPayload
from tidal.models.playlists_multi_resource_data_document import PlaylistsMultiResourceDataDocument
from tidal.models.playlists_owner_profiles_multi_relationship_data_document import PlaylistsOwnerProfilesMultiRelationshipDataDocument
from tidal.models.playlists_owners_multi_relationship_data_document import PlaylistsOwnersMultiRelationshipDataDocument
from tidal.models.playlists_single_resource_data_document import PlaylistsSingleResourceDataDocument
from tidal.models.playlists_suggested_cover_arts_multi_relationship_data_document import PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument
from tidal.models.playlists_update_operation_payload import PlaylistsUpdateOperationPayload
from tidal.models.playlists_update_single_resource_data_document import PlaylistsUpdateSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/playlists",
    responses={
        200: {"model": PlaylistsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlists"],
    summary="Get multiple playlists.",
    response_model_by_alias=True,
)
async def playlists_get(
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    filter_collaborators_id: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="User id. Also accepts `me`.")] = Query(None, description="User id. Also accepts &#x60;me&#x60;.", alias="filter[collaborators.id]"),
    filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of playlist IDs (e.g. `550e8400-e29b-41d4-a716-446655440000`)")] = Query(None, description="List of playlist IDs (e.g. &#x60;550e8400-e29b-41d4-a716-446655440000&#x60;)", alias="filter[id]"),
    filter_owners_id: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="User id. Also accepts `me`.")] = Query(None, description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: collaboratorProfiles, collaborators, coverArt, curators, items, ownerProfiles, owners, suggestedCoverArts")] = Query(None, description="Include related resources. Available relationships: collaboratorProfiles, collaborators, coverArt, curators, items, ownerProfiles, owners, suggestedCoverArts", alias="include", examples=["curators.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: curators.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: curators.albums", alias="replaceMedia", examples=["curators.albums"]),
    sort: Annotated[Optional[List[str]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")] = Query(None, description="Values prefixed with \&quot;-\&quot; are sorted descending; values without it are sorted ascending.", alias="sort"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.read", "r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> PlaylistsMultiResourceDataDocument:
    """Retrieves multiple playlists by available filters, or without if applicable."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_get(country_code, filter_collaborators_id, filter_id, filter_owners_id, include, include_linkage, page_cursor, replace_media, sort)


@router.post(
    "/playlists",
    responses={
        201: {"model": PlaylistsCreateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["playlists"],
    summary="Create single playlist.",
    response_model_by_alias=True,
)
async def playlists_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    playlists_create_operation_payload: Optional[PlaylistsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> PlaylistsCreateSingleResourceDataDocument:
    """Creates a new playlist."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_post(idempotency_key, playlists_create_operation_payload)


@router.get(
    "/playlists/{id}",
    responses={
        200: {"model": PlaylistsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlists"],
    summary="Get single playlist.",
    response_model_by_alias=True,
)
async def playlists_id_get(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: collaboratorProfiles, collaborators, coverArt, curators, items, ownerProfiles, owners, suggestedCoverArts")] = Query(None, description="Include related resources. Available relationships: collaboratorProfiles, collaborators, coverArt, curators, items, ownerProfiles, owners, suggestedCoverArts", alias="include", examples=["curators.albums"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: curators.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: curators.albums", alias="replaceMedia", examples=["curators.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> PlaylistsSingleResourceDataDocument:
    """Retrieves single playlist by id."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_get(id, country_code, include, include_linkage, replace_media)


@router.delete(
    "/playlists/{id}",
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
    tags=["playlists"],
    summary="Delete single playlist.",
    response_model_by_alias=True,
)
async def playlists_id_delete(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes existing playlist."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_delete(id, idempotency_key)


@router.patch(
    "/playlists/{id}",
    responses={
        200: {"model": PlaylistsUpdateSingleResourceDataDocument, "description": "Successful response"},
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
    tags=["playlists"],
    summary="Update single playlist.",
    response_model_by_alias=True,
)
async def playlists_id_patch(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    playlists_update_operation_payload: Optional[PlaylistsUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> PlaylistsUpdateSingleResourceDataDocument:
    """Updates existing playlist."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_patch(id, idempotency_key, playlists_update_operation_payload)


@router.get(
    "/playlists/{id}/relationships/collaboratorProfiles",
    responses={
        200: {"model": PlaylistsCollaboratorProfilesMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlists"],
    summary="Get collaboratorProfiles relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlists_id_relationships_collaborator_profiles_get(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: collaboratorProfiles")] = Query(None, description="Include related resources. Available relationships: collaboratorProfiles", alias="include", examples=["collaboratorProfiles"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> PlaylistsCollaboratorProfilesMultiRelationshipDataDocument:
    """Deprecated. Use curators for attribution."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_relationships_collaborator_profiles_get(id, include, page_cursor)


@router.delete(
    "/playlists/{id}/relationships/collaboratorProfiles",
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
    tags=["playlists"],
    summary="Delete from collaboratorProfiles relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlists_id_relationships_collaborator_profiles_delete(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    playlists_collaborator_profiles_relationship_remove_operation_payload: Optional[PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes item(s) from collaboratorProfiles relationship."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_relationships_collaborator_profiles_delete(id, idempotency_key, playlists_collaborator_profiles_relationship_remove_operation_payload)


@router.get(
    "/playlists/{id}/relationships/collaborators",
    responses={
        200: {"model": PlaylistsCollaboratorsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlists"],
    summary="Get collaborators relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlists_id_relationships_collaborators_get(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: collaborators")] = Query(None, description="Include related resources. Available relationships: collaborators", alias="include", examples=["collaborators"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> PlaylistsCollaboratorsMultiRelationshipDataDocument:
    """Retrieves collaborators relationship."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_relationships_collaborators_get(id, include, page_cursor)


@router.get(
    "/playlists/{id}/relationships/coverArt",
    responses={
        200: {"model": PlaylistsCoverArtMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlists"],
    summary="Get coverArt relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlists_id_relationships_cover_art_get(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: coverArt")] = Query(None, description="Include related resources. Available relationships: coverArt", alias="include", examples=["coverArt"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> PlaylistsCoverArtMultiRelationshipDataDocument:
    """Retrieves coverArt relationship."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_relationships_cover_art_get(id, country_code, include, page_cursor)


@router.patch(
    "/playlists/{id}/relationships/coverArt",
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
    tags=["playlists"],
    summary="Update coverArt relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlists_id_relationships_cover_art_patch(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    playlists_cover_art_relationship_update_operation_payload: Optional[PlaylistsCoverArtRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Replaces the custom cover artwork selection with one attachable artwork. Empty data clears the custom selection. Previously attached uploaded artwork is soft-deleted unless system-managed. Returns an acknowledgement."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_relationships_cover_art_patch(id, idempotency_key, playlists_cover_art_relationship_update_operation_payload)


@router.get(
    "/playlists/{id}/relationships/curators",
    responses={
        200: {"model": PlaylistsCuratorsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlists"],
    summary="Get curators relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlists_id_relationships_curators_get(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: curators")] = Query(None, description="Include related resources. Available relationships: curators", alias="include", examples=["curators.albums"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: curators.albums")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: curators.albums", alias="replaceMedia", examples=["curators.albums"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> PlaylistsCuratorsMultiRelationshipDataDocument:
    """Artist profiles credited for the playlist"""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_relationships_curators_get(id, include, page_cursor, replace_media)


@router.get(
    "/playlists/{id}/relationships/items",
    responses={
        200: {"model": PlaylistsItemsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlists"],
    summary="Get items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlists_id_relationships_items_get(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")] = Query(None, description="ISO 3166-1 alpha-2 country code", alias="countryCode", examples=["US"]),
    filter_self_matches_query: Annotated[Optional[Annotated[str, Field(max_length=100)]], Field(description="Filter playlist items by a free-text query (e.g. `halo`)")] = Query(None, description="Filter playlist items by a free-text query (e.g. &#x60;halo&#x60;)", alias="filter[self][matchesQuery]", max_length=100),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")] = Query(None, description="Include related resources. Available relationships: items", alias="include", examples=["items"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items", alias="replaceMedia", examples=["items"]),
    sort: Annotated[Optional[List[str]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")] = Query(None, description="Values prefixed with \&quot;-\&quot; are sorted descending; values without it are sorted ascending.", alias="sort"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> PlaylistsItemsMultiRelationshipDataDocument:
    """Retrieves items relationship."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_relationships_items_get(id, country_code, filter_self_matches_query, include, page_cursor, replace_media, sort)


@router.post(
    "/playlists/{id}/relationships/items",
    responses={
        200: {"model": PlaylistsItemsAddMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": PlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBody, "description": "Playlist already contains one or more requested items; Playlist item limit reached; Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlists"],
    summary="Add to items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlists_id_relationships_items_post(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    playlists_items_relationship_add_operation_payload: Optional[PlaylistsItemsRelationshipAddOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> PlaylistsItemsAddMultiRelationshipDataDocument:
    """Adds item(s) to items relationship."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_relationships_items_post(id, idempotency_key, playlists_items_relationship_add_operation_payload)


@router.delete(
    "/playlists/{id}/relationships/items",
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
    tags=["playlists"],
    summary="Delete from items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlists_id_relationships_items_delete(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    playlists_items_relationship_remove_operation_payload: Optional[PlaylistsItemsRelationshipRemoveOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Deletes item(s) from items relationship."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_relationships_items_delete(id, idempotency_key, playlists_items_relationship_remove_operation_payload)


@router.patch(
    "/playlists/{id}/relationships/items",
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
    tags=["playlists"],
    summary="Update items relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlists_id_relationships_items_patch(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    playlists_items_relationship_update_operation_payload: Optional[PlaylistsItemsRelationshipUpdateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playlists.write", "w_usr"]
    ),
) -> MutationResponseDocument:
    """Incrementally moves the occurrences selected by data[].meta.itemId before meta.positionBefore, or to the end when meta is omitted. Preserves unselected memberships, their metadata and relative order; no items are added or removed. Empty data is rejected. Returns an acknowledgement."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_relationships_items_patch(id, idempotency_key, playlists_items_relationship_update_operation_payload)


@router.get(
    "/playlists/{id}/relationships/ownerProfiles",
    responses={
        200: {"model": PlaylistsOwnerProfilesMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlists"],
    summary="Get ownerProfiles relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlists_id_relationships_owner_profiles_get(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: ownerProfiles")] = Query(None, description="Include related resources. Available relationships: ownerProfiles", alias="include", examples=["ownerProfiles"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> PlaylistsOwnerProfilesMultiRelationshipDataDocument:
    """Deprecated. Use curators for attribution."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_relationships_owner_profiles_get(id, include, page_cursor)


@router.get(
    "/playlists/{id}/relationships/owners",
    responses={
        200: {"model": PlaylistsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlists"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlists_id_relationships_owners_get(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> PlaylistsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/playlists/{id}/relationships/suggestedCoverArts",
    responses={
        200: {"model": PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["playlists"],
    summary="Get suggestedCoverArts relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def playlists_id_relationships_suggested_cover_arts_get(
    id: Annotated[str, Field(description="Playlist id")] = Path(..., description="Playlist id", examples=["550e8400-e29b-41d4-a716-446655440000"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: suggestedCoverArts")] = Query(None, description="Include related resources. Available relationships: suggestedCoverArts", alias="include", examples=["suggestedCoverArts"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument:
    """Retrieves suggestedCoverArts relationship."""
    if not BasePlaylistsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePlaylistsApi.subclasses[0]().playlists_id_relationships_suggested_cover_arts_get(id, include, page_cursor)
