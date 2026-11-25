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
from tidal.models.user_subscription_price_changes_decision_single_relationship_data_document import UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument
from tidal.models.user_subscription_price_changes_multi_resource_data_document import UserSubscriptionPriceChangesMultiResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseUserSubscriptionPriceChangesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUserSubscriptionPriceChangesApi.subclasses = BaseUserSubscriptionPriceChangesApi.subclasses + (cls,)
    async def user_subscription_price_changes_get(
        self,
        filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="User id. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: decision")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> UserSubscriptionPriceChangesMultiResourceDataDocument:
        """Retrieves multiple userSubscriptionPriceChanges by available filters, or without if applicable."""
        ...


    async def user_subscription_price_changes_id_relationships_decision_get(
        self,
        id: Annotated[str, Field(description="Price change id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: decision")],
    ) -> UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument:
        """Retrieves decision relationship."""
        ...
