# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field
from typing_extensions import Annotated
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.models.studio_home_event_tiles_single_resource_data_document import StudioHomeEventTilesSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseStudioHomeEventTilesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseStudioHomeEventTilesApi.subclasses = BaseStudioHomeEventTilesApi.subclasses + (cls,)
    async def studio_home_event_tiles_id_get(
        self,
        id: Annotated[str, Field(description="Studio Home event tile id. Use `me` for the authenticated user's resource")],
    ) -> StudioHomeEventTilesSingleResourceDataDocument:
        """Retrieves single studioHomeEventTile by id."""
        ...
