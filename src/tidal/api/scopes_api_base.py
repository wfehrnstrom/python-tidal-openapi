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
from tidal.models.scopes_multi_resource_data_document import ScopesMultiResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseScopesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseScopesApi.subclasses = BaseScopesApi.subclasses + (cls,)
    async def scopes_get(
        self,
        filter_required_access_tier: Annotated[Optional[Annotated[List[str], Field(min_length=1, max_length=20)]], Field(description="Filters scopes by their required client access tier. (e.g. `THIRD_PARTY`)")],
        filter_required_access_tier_satisfied_by: Annotated[Optional[str], Field(description="Selects scopes whose required access tier is satisfied by the client tier. (e.g. `PARTNER`)")],
    ) -> ScopesMultiResourceDataDocument:
        """Retrieves multiple scopes by available filters, or without if applicable."""
        ...
