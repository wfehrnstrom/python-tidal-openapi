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
from tidal.models.stripe_dashboard_links_multi_resource_data_document import StripeDashboardLinksMultiResourceDataDocument
from tidal.models.stripe_dashboard_links_owners_multi_relationship_data_document import StripeDashboardLinksOwnersMultiRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseStripeDashboardLinksApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseStripeDashboardLinksApi.subclasses = BaseStripeDashboardLinksApi.subclasses + (cls,)
    async def stripe_dashboard_links_get(
        self,
        filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="User id. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> StripeDashboardLinksMultiResourceDataDocument:
        """Retrieves multiple stripeDashboardLinks by available filters, or without if applicable."""
        ...


    async def stripe_dashboard_links_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Stripe dashboard link id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> StripeDashboardLinksOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...
