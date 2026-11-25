# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.artist_streams_statistics_artist_single_relationship_data_document import ArtistStreamsStatisticsArtistSingleRelationshipDataDocument
from tidal.models.artist_streams_statistics_multi_resource_data_document import ArtistStreamsStatisticsMultiResourceDataDocument
from tidal.models.artist_streams_statistics_top_tracks_multi_relationship_data_document import ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseArtistStreamsStatisticsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseArtistStreamsStatisticsApi.subclasses = BaseArtistStreamsStatisticsApi.subclasses + (cls,)
    async def artist_streams_statistics_get(
        self,
        filter_artist_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="Artist ID. Every published range of the artist is returned (e.g. `1566`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artist, topTracks")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artist.albums")],
    ) -> ArtistStreamsStatisticsMultiResourceDataDocument:
        """Retrieves multiple artistStreamsStatistics by available filters, or without if applicable."""
        ...


    async def artist_streams_statistics_id_relationships_artist_get(
        self,
        id: Annotated[str, Field(description="Artist streams statistics id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artist")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artist.albums")],
    ) -> ArtistStreamsStatisticsArtistSingleRelationshipDataDocument:
        """Retrieves artist relationship."""
        ...


    async def artist_streams_statistics_id_relationships_top_tracks_get(
        self,
        id: Annotated[str, Field(description="Artist streams statistics id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: topTracks")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: topTracks")],
    ) -> ArtistStreamsStatisticsTopTracksMultiRelationshipDataDocument:
        """Retrieves topTracks relationship."""
        ...
