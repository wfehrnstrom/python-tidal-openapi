# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.models.track_manifests_read_by_id403_response_body import TrackManifestsReadById403ResponseBody
from tidal.models.track_manifests_read_by_id404_response_body import TrackManifestsReadById404ResponseBody
from tidal.models.track_manifests_single_resource_data_document import TrackManifestsSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseTrackManifestsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTrackManifestsApi.subclasses = BaseTrackManifestsApi.subclasses + (cls,)
    async def track_manifests_id_get(
        self,
        adaptive: bool,
        formats: List[str],
        id: Annotated[str, Field(description="Track manifest id")],
        manifest_type: str,
        uri_scheme: str,
        usage: str,
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TrackManifestsSingleResourceDataDocument:
        """Retrieves single trackManifest by id."""
        ...
