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
from tidal.models.search_results_albums_multi_relationship_data_document import SearchResultsAlbumsMultiRelationshipDataDocument
from tidal.models.search_results_artists_multi_relationship_data_document import SearchResultsArtistsMultiRelationshipDataDocument
from tidal.models.search_results_multi_resource_data_document import SearchResultsMultiResourceDataDocument
from tidal.models.search_results_playlists_multi_relationship_data_document import SearchResultsPlaylistsMultiRelationshipDataDocument
from tidal.models.search_results_top_hits_multi_relationship_data_document import SearchResultsTopHitsMultiRelationshipDataDocument
from tidal.models.search_results_tracks_multi_relationship_data_document import SearchResultsTracksMultiRelationshipDataDocument
from tidal.models.search_results_videos_multi_relationship_data_document import SearchResultsVideosMultiRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseSearchResultsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSearchResultsApi.subclasses = BaseSearchResultsApi.subclasses + (cls,)
    async def search_results_get(
        self,
        filter_query: Annotated[str, Field(min_length=1, max_length=256, description="Search query (e.g. `hello`)")],
        client_version: Annotated[Optional[str], Field(description="Client version number")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        device_type: Annotated[Optional[str], Field(description="The type of device making the request")],
        explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums, artists, playlists, topHits, tracks, videos")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")],
        system_type: Annotated[Optional[str], Field(description="The system type of the device making the request")],
    ) -> SearchResultsMultiResourceDataDocument:
        """Searches for a query and returns a collection containing exactly one search results resource."""
        ...


    async def search_results_id_relationships_albums_get(
        self,
        id: Annotated[str, Field(description="An opaque search results identifier")],
        client_version: Annotated[Optional[str], Field(description="Client version number")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        device_type: Annotated[Optional[str], Field(description="The type of device making the request")],
        explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")],
        system_type: Annotated[Optional[str], Field(description="The system type of the device making the request")],
    ) -> SearchResultsAlbumsMultiRelationshipDataDocument:
        """Retrieves albums relationship."""
        ...


    async def search_results_id_relationships_artists_get(
        self,
        id: Annotated[str, Field(description="An opaque search results identifier")],
        client_version: Annotated[Optional[str], Field(description="Client version number")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        device_type: Annotated[Optional[str], Field(description="The type of device making the request")],
        explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artists")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")],
        system_type: Annotated[Optional[str], Field(description="The system type of the device making the request")],
    ) -> SearchResultsArtistsMultiRelationshipDataDocument:
        """Retrieves artists relationship."""
        ...


    async def search_results_id_relationships_playlists_get(
        self,
        id: Annotated[str, Field(description="An opaque search results identifier")],
        client_version: Annotated[Optional[str], Field(description="Client version number")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        device_type: Annotated[Optional[str], Field(description="The type of device making the request")],
        explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: playlists")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlists.items")],
        system_type: Annotated[Optional[str], Field(description="The system type of the device making the request")],
    ) -> SearchResultsPlaylistsMultiRelationshipDataDocument:
        """Retrieves playlists relationship."""
        ...


    async def search_results_id_relationships_top_hits_get(
        self,
        id: Annotated[str, Field(description="An opaque search results identifier")],
        client_version: Annotated[Optional[str], Field(description="Client version number")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        device_type: Annotated[Optional[str], Field(description="The type of device making the request")],
        explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: topHits")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: topHits")],
        system_type: Annotated[Optional[str], Field(description="The system type of the device making the request")],
    ) -> SearchResultsTopHitsMultiRelationshipDataDocument:
        """Retrieves topHits relationship."""
        ...


    async def search_results_id_relationships_tracks_get(
        self,
        id: Annotated[str, Field(description="An opaque search results identifier")],
        client_version: Annotated[Optional[str], Field(description="Client version number")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        device_type: Annotated[Optional[str], Field(description="The type of device making the request")],
        explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: tracks")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks")],
        system_type: Annotated[Optional[str], Field(description="The system type of the device making the request")],
    ) -> SearchResultsTracksMultiRelationshipDataDocument:
        """Retrieves tracks relationship."""
        ...


    async def search_results_id_relationships_videos_get(
        self,
        id: Annotated[str, Field(description="An opaque search results identifier")],
        client_version: Annotated[Optional[str], Field(description="Client version number")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        device_type: Annotated[Optional[str], Field(description="The type of device making the request")],
        explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: videos")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos")],
        system_type: Annotated[Optional[str], Field(description="The system type of the device making the request")],
    ) -> SearchResultsVideosMultiRelationshipDataDocument:
        """Retrieves videos relationship."""
        ...
