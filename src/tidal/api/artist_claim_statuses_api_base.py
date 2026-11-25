# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field
from typing import List
from typing_extensions import Annotated
from tidal.models.artist_claim_statuses_multi_resource_data_document import ArtistClaimStatusesMultiResourceDataDocument
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseArtistClaimStatusesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseArtistClaimStatusesApi.subclasses = BaseArtistClaimStatusesApi.subclasses + (cls,)
    async def artist_claim_statuses_get(
        self,
        filter_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20, description="List of artist claim status IDs (e.g. `QVJUSVNUUzoxNTY2`)")],
    ) -> ArtistClaimStatusesMultiResourceDataDocument:
        """Retrieves multiple artistClaimStatuses by available filters, or without if applicable."""
        ...
