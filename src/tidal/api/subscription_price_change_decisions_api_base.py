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
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.subscription_price_change_decisions_create_operation_payload import SubscriptionPriceChangeDecisionsCreateOperationPayload
from tidal.models.subscription_price_change_decisions_create_single_resource_data_document import SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument
from tidal.models.subscription_price_change_decisions_multi_resource_data_document import SubscriptionPriceChangeDecisionsMultiResourceDataDocument
from tidal.models.subscription_price_change_decisions_price_change_single_relationship_data_document import SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument
from tidal.models.subscription_price_change_decisions_update_operation_payload import SubscriptionPriceChangeDecisionsUpdateOperationPayload
from tidal.models.subscription_price_change_decisions_update_single_resource_data_document import SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseSubscriptionPriceChangeDecisionsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSubscriptionPriceChangeDecisionsApi.subclasses = BaseSubscriptionPriceChangeDecisionsApi.subclasses + (cls,)
    async def subscription_price_change_decisions_get(
        self,
        filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="User id. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: priceChange")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> SubscriptionPriceChangeDecisionsMultiResourceDataDocument:
        """Retrieves multiple subscriptionPriceChangeDecisions by available filters, or without if applicable."""
        ...


    async def subscription_price_change_decisions_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        subscription_price_change_decisions_create_operation_payload: Optional[SubscriptionPriceChangeDecisionsCreateOperationPayload],
    ) -> SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument:
        """Creates a new subscriptionPriceChangeDecision."""
        ...


    async def subscription_price_change_decisions_id_patch(
        self,
        id: Annotated[str, Field(description="Price change decision id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        subscription_price_change_decisions_update_operation_payload: Optional[SubscriptionPriceChangeDecisionsUpdateOperationPayload],
    ) -> SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument:
        """Updates existing subscriptionPriceChangeDecision."""
        ...


    async def subscription_price_change_decisions_id_relationships_price_change_get(
        self,
        id: Annotated[str, Field(description="Price change decision id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: priceChange")],
    ) -> SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument:
        """Retrieves priceChange relationship."""
        ...
