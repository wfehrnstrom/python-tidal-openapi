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
from tidal.models.downloads_multi_resource_data_document import DownloadsMultiResourceDataDocument
from tidal.models.downloads_owners_multi_relationship_data_document import DownloadsOwnersMultiRelationshipDataDocument
from tidal.models.downloads_single_resource_data_document import DownloadsSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseDownloadsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDownloadsApi.subclasses = BaseDownloadsApi.subclasses + (cls,)
    async def downloads_get(
        self,
        filter_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="Download id (e.g. `VFJBQ0tTOjEyMzQ1`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> DownloadsMultiResourceDataDocument:
        """Retrieves multiple downloads by available filters, or without if applicable."""
        ...


    async def downloads_id_get(
        self,
        id: Annotated[str, Field(description="Download id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> DownloadsSingleResourceDataDocument:
        """Retrieves single download by id."""
        ...


    async def downloads_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Download id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> DownloadsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...
