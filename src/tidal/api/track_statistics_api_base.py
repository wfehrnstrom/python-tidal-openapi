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
from tidal.models.track_statistics_owners_multi_relationship_data_document import TrackStatisticsOwnersMultiRelationshipDataDocument
from tidal.models.track_statistics_single_resource_data_document import TrackStatisticsSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseTrackStatisticsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTrackStatisticsApi.subclasses = BaseTrackStatisticsApi.subclasses + (cls,)
    async def track_statistics_id_get(
        self,
        id: Annotated[str, Field(description="Track statistic id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> TrackStatisticsSingleResourceDataDocument:
        """Retrieves single trackStatistic by id."""
        ...


    async def track_statistics_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Track statistic id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> TrackStatisticsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...
