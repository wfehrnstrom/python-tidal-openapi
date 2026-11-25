# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field
from typing import List
from typing_extensions import Annotated
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.models.groups_multi_resource_data_document import GroupsMultiResourceDataDocument
from tidal.models.groups_single_resource_data_document import GroupsSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseGroupsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseGroupsApi.subclasses = BaseGroupsApi.subclasses + (cls,)
    async def groups_get(
        self,
        filter_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20, description="Group ID. The built-in Everyone group has the case-sensitive ID `everyone`.")],
    ) -> GroupsMultiResourceDataDocument:
        """Retrieves multiple groups by available filters, or without if applicable."""
        ...


    async def groups_id_get(
        self,
        id: Annotated[str, Field(description="Group ID. The built-in Everyone group has the case-sensitive ID `everyone`.")],
    ) -> GroupsSingleResourceDataDocument:
        """Retrieves single group by id."""
        ...
