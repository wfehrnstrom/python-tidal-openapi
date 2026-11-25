# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BasePlaylistsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePlaylistsApi.subclasses = BasePlaylistsApi.subclasses + (cls,)
    async def playlists_get(
        self,
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        filter_collaborators_id: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="User id. Also accepts `me`.")],
        filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of playlist IDs (e.g. `550e8400-e29b-41d4-a716-446655440000`)")],
        filter_owners_id: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="User id. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: collaboratorProfiles, collaborators, coverArt, curators, items, ownerProfiles, owners, suggestedCoverArts")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: curators.albums")],
        sort: Annotated[Optional[List[str]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")],
    ) -> PlaylistsMultiResourceDataDocument:
        """Retrieves multiple playlists by available filters, or without if applicable."""
        ...


    async def playlists_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        playlists_create_operation_payload: Optional[PlaylistsCreateOperationPayload],
    ) -> PlaylistsCreateSingleResourceDataDocument:
        """Creates a new playlist."""
        ...


    async def playlists_id_get(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: collaboratorProfiles, collaborators, coverArt, curators, items, ownerProfiles, owners, suggestedCoverArts")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: curators.albums")],
    ) -> PlaylistsSingleResourceDataDocument:
        """Retrieves single playlist by id."""
        ...


    async def playlists_id_delete(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
    ) -> MutationResponseDocument:
        """Deletes existing playlist."""
        ...


    async def playlists_id_patch(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        playlists_update_operation_payload: Optional[PlaylistsUpdateOperationPayload],
    ) -> PlaylistsUpdateSingleResourceDataDocument:
        """Updates existing playlist."""
        ...


    async def playlists_id_relationships_collaborator_profiles_get(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: collaboratorProfiles")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> PlaylistsCollaboratorProfilesMultiRelationshipDataDocument:
        """Deprecated. Use curators for attribution."""
        ...


    async def playlists_id_relationships_collaborator_profiles_delete(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        playlists_collaborator_profiles_relationship_remove_operation_payload: Optional[PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload],
    ) -> MutationResponseDocument:
        """Deletes item(s) from collaboratorProfiles relationship."""
        ...


    async def playlists_id_relationships_collaborators_get(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: collaborators")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> PlaylistsCollaboratorsMultiRelationshipDataDocument:
        """Retrieves collaborators relationship."""
        ...


    async def playlists_id_relationships_cover_art_get(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: coverArt")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> PlaylistsCoverArtMultiRelationshipDataDocument:
        """Retrieves coverArt relationship."""
        ...


    async def playlists_id_relationships_cover_art_patch(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        playlists_cover_art_relationship_update_operation_payload: Optional[PlaylistsCoverArtRelationshipUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Replaces the custom cover artwork selection with one attachable artwork. Empty data clears the custom selection. Previously attached uploaded artwork is soft-deleted unless system-managed. Returns an acknowledgement."""
        ...


    async def playlists_id_relationships_curators_get(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: curators")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: curators.albums")],
    ) -> PlaylistsCuratorsMultiRelationshipDataDocument:
        """Artist profiles credited for the playlist"""
        ...


    async def playlists_id_relationships_items_get(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        filter_self_matches_query: Annotated[Optional[Annotated[str, Field(max_length=100)]], Field(description="Filter playlist items by a free-text query (e.g. `halo`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")],
        sort: Annotated[Optional[List[str]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")],
    ) -> PlaylistsItemsMultiRelationshipDataDocument:
        """Retrieves items relationship."""
        ...


    async def playlists_id_relationships_items_post(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        playlists_items_relationship_add_operation_payload: Optional[PlaylistsItemsRelationshipAddOperationPayload],
    ) -> PlaylistsItemsAddMultiRelationshipDataDocument:
        """Adds item(s) to items relationship."""
        ...


    async def playlists_id_relationships_items_delete(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        playlists_items_relationship_remove_operation_payload: Optional[PlaylistsItemsRelationshipRemoveOperationPayload],
    ) -> MutationResponseDocument:
        """Deletes item(s) from items relationship."""
        ...


    async def playlists_id_relationships_items_patch(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        playlists_items_relationship_update_operation_payload: Optional[PlaylistsItemsRelationshipUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Incrementally moves the occurrences selected by data[].meta.itemId before meta.positionBefore, or to the end when meta is omitted. Preserves unselected memberships, their metadata and relative order; no items are added or removed. Empty data is rejected. Returns an acknowledgement."""
        ...


    async def playlists_id_relationships_owner_profiles_get(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: ownerProfiles")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> PlaylistsOwnerProfilesMultiRelationshipDataDocument:
        """Deprecated. Use curators for attribution."""
        ...


    async def playlists_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> PlaylistsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def playlists_id_relationships_suggested_cover_arts_get(
        self,
        id: Annotated[str, Field(description="Playlist id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: suggestedCoverArts")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument:
        """Retrieves suggestedCoverArts relationship."""
        ...
