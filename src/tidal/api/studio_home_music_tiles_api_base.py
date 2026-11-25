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
from tidal.models.studio_home_music_tiles_items_multi_relationship_data_document import StudioHomeMusicTilesItemsMultiRelationshipDataDocument
from tidal.models.studio_home_music_tiles_single_resource_data_document import StudioHomeMusicTilesSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseStudioHomeMusicTilesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseStudioHomeMusicTilesApi.subclasses = BaseStudioHomeMusicTilesApi.subclasses + (cls,)
    async def studio_home_music_tiles_id_get(
        self,
        id: Annotated[str, Field(description="Studio Home music tile id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")],
    ) -> StudioHomeMusicTilesSingleResourceDataDocument:
        """Retrieves single studioHomeMusicTile by id."""
        ...


    async def studio_home_music_tiles_id_relationships_items_get(
        self,
        id: Annotated[str, Field(description="Studio Home music tile id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")],
    ) -> StudioHomeMusicTilesItemsMultiRelationshipDataDocument:
        """The user&#39;s uploaded albums, newest first."""
        ...
