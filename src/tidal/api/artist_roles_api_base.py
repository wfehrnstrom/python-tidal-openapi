# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field
from typing_extensions import Annotated
from tidal.models.artist_roles_single_resource_data_document import ArtistRolesSingleResourceDataDocument
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseArtistRolesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseArtistRolesApi.subclasses = BaseArtistRolesApi.subclasses + (cls,)
    async def artist_roles_id_get(
        self,
        id: Annotated[str, Field(description="Artist role id")],
    ) -> ArtistRolesSingleResourceDataDocument:
        """Retrieves single artistRole by id."""
        ...
