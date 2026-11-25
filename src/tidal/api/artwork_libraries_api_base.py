# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.artwork_libraries_artworks_multi_relationship_data_document import ArtworkLibrariesArtworksMultiRelationshipDataDocument
from tidal.models.artwork_libraries_multi_resource_data_document import ArtworkLibrariesMultiResourceDataDocument
from tidal.models.artwork_libraries_random_artwork_single_relationship_data_document import ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument
from tidal.models.artwork_libraries_single_resource_data_document import ArtworkLibrariesSingleResourceDataDocument
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseArtworkLibrariesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseArtworkLibrariesApi.subclasses = BaseArtworkLibrariesApi.subclasses + (cls,)
    async def artwork_libraries_get(
        self,
        filter_name: Annotated[List[str], Field(min_length=1, max_length=20, description="Library names (e.g. `album-defaults`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks, randomArtwork")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> ArtworkLibrariesMultiResourceDataDocument:
        """Retrieves multiple artworkLibraries by available filters, or without if applicable."""
        ...


    async def artwork_libraries_id_get(
        self,
        id: Annotated[str, Field(description="Artwork library ID")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks, randomArtwork")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> ArtworkLibrariesSingleResourceDataDocument:
        """Retrieves single artworkLibrarie by id."""
        ...


    async def artwork_libraries_id_relationships_artworks_get(
        self,
        id: Annotated[str, Field(description="Artwork library ID")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artworks")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ArtworkLibrariesArtworksMultiRelationshipDataDocument:
        """Artworks in the library that have finished processing and are not flagged or taken down, newest first"""
        ...


    async def artwork_libraries_id_relationships_random_artwork_get(
        self,
        id: Annotated[str, Field(description="Artwork library ID")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: randomArtwork")],
    ) -> ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument:
        """A random artwork from the library, used by clients to supply a default artwork, for example for albums without cover art. Picked per request from the artworks that have finished processing and are not flagged or taken down, and not stored; empty when there are none"""
        ...
