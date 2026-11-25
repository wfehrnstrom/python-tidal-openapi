# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List
from typing_extensions import Annotated
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.models.track_files_read_by_id403_response_body import TrackFilesReadById403ResponseBody
from tidal.models.track_files_read_by_id404_response_body import TrackFilesReadById404ResponseBody
from tidal.models.track_files_single_resource_data_document import TrackFilesSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseTrackFilesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTrackFilesApi.subclasses = BaseTrackFilesApi.subclasses + (cls,)
    async def track_files_id_get(
        self,
        formats: List[str],
        id: Annotated[str, Field(description="Track file id")],
        usage: str,
    ) -> TrackFilesSingleResourceDataDocument:
        """Retrieves single trackFile by id."""
        ...
