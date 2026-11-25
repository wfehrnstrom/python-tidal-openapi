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
from tidal.models.videos_albums_multi_relationship_data_document import VideosAlbumsMultiRelationshipDataDocument
from tidal.models.videos_artists_multi_relationship_data_document import VideosArtistsMultiRelationshipDataDocument
from tidal.models.videos_credits_multi_relationship_data_document import VideosCreditsMultiRelationshipDataDocument
from tidal.models.videos_multi_resource_data_document import VideosMultiResourceDataDocument
from tidal.models.videos_providers_multi_relationship_data_document import VideosProvidersMultiRelationshipDataDocument
from tidal.models.videos_replacement_single_relationship_data_document import VideosReplacementSingleRelationshipDataDocument
from tidal.models.videos_similar_videos_multi_relationship_data_document import VideosSimilarVideosMultiRelationshipDataDocument
from tidal.models.videos_single_resource_data_document import VideosSingleResourceDataDocument
from tidal.models.videos_suggested_videos_multi_relationship_data_document import VideosSuggestedVideosMultiRelationshipDataDocument
from tidal.models.videos_thumbnail_art_multi_relationship_data_document import VideosThumbnailArtMultiRelationshipDataDocument
from tidal.models.videos_usage_rules_single_relationship_data_document import VideosUsageRulesSingleRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseVideosApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseVideosApi.subclasses = BaseVideosApi.subclasses + (cls,)
    async def videos_get(
        self,
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of video IDs (e.g. `75623239`)")],
        filter_isrc: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of ISRCs (e.g. `QMJMT1701237`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums, artists, credits, providers, replacement, similarVideos, suggestedVideos, thumbnailArt, usageRules")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")],
    ) -> VideosMultiResourceDataDocument:
        """Retrieves multiple videos by available filters, or without if applicable."""
        ...


    async def videos_id_get(
        self,
        id: Annotated[str, Field(description="Video id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums, artists, credits, providers, replacement, similarVideos, suggestedVideos, thumbnailArt, usageRules")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")],
    ) -> VideosSingleResourceDataDocument:
        """Retrieves single video by id."""
        ...


    async def videos_id_relationships_albums_get(
        self,
        id: Annotated[str, Field(description="Video id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albums")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")],
    ) -> VideosAlbumsMultiRelationshipDataDocument:
        """Retrieves albums relationship."""
        ...


    async def videos_id_relationships_artists_get(
        self,
        id: Annotated[str, Field(description="Video id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artists")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")],
    ) -> VideosArtistsMultiRelationshipDataDocument:
        """Retrieves artists relationship."""
        ...


    async def videos_id_relationships_credits_get(
        self,
        id: Annotated[str, Field(description="Video id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: credits")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: credits.artist.albums")],
    ) -> VideosCreditsMultiRelationshipDataDocument:
        """Retrieves credits relationship."""
        ...


    async def videos_id_relationships_providers_get(
        self,
        id: Annotated[str, Field(description="Video id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: providers")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> VideosProvidersMultiRelationshipDataDocument:
        """Retrieves providers relationship."""
        ...


    async def videos_id_relationships_replacement_get(
        self,
        id: Annotated[str, Field(description="Video id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: replacement")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: replacement")],
    ) -> VideosReplacementSingleRelationshipDataDocument:
        """Retrieves replacement relationship."""
        ...


    async def videos_id_relationships_similar_videos_get(
        self,
        id: Annotated[str, Field(description="Video id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: similarVideos")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarVideos")],
    ) -> VideosSimilarVideosMultiRelationshipDataDocument:
        """Retrieves similarVideos relationship."""
        ...


    async def videos_id_relationships_suggested_videos_get(
        self,
        id: Annotated[str, Field(description="Video id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: suggestedVideos")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: suggestedVideos")],
    ) -> VideosSuggestedVideosMultiRelationshipDataDocument:
        """Retrieves suggestedVideos relationship."""
        ...


    async def videos_id_relationships_thumbnail_art_get(
        self,
        id: Annotated[str, Field(description="Video id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: thumbnailArt")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> VideosThumbnailArtMultiRelationshipDataDocument:
        """Retrieves thumbnailArt relationship."""
        ...


    async def videos_id_relationships_usage_rules_get(
        self,
        id: Annotated[str, Field(description="Video id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: usageRules")],
    ) -> VideosUsageRulesSingleRelationshipDataDocument:
        """Retrieves usageRules relationship."""
        ...
