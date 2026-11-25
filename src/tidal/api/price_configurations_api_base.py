# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field
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
from tidal.models.price_configurations_create_operation_payload import PriceConfigurationsCreateOperationPayload
from tidal.models.price_configurations_create_single_resource_data_document import PriceConfigurationsCreateSingleResourceDataDocument
from tidal.models.price_configurations_multi_resource_data_document import PriceConfigurationsMultiResourceDataDocument
from tidal.models.price_configurations_single_resource_data_document import PriceConfigurationsSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BasePriceConfigurationsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePriceConfigurationsApi.subclasses = BasePriceConfigurationsApi.subclasses + (cls,)
    async def price_configurations_get(
        self,
        filter_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20, description="List of price configurations IDs (e.g. `cHJpY2UtY29uZmlnLTEyMzpVUw`)")],
    ) -> PriceConfigurationsMultiResourceDataDocument:
        """Retrieves multiple priceConfigurations by available filters, or without if applicable."""
        ...


    async def price_configurations_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        price_configurations_create_operation_payload: Optional[PriceConfigurationsCreateOperationPayload],
    ) -> PriceConfigurationsCreateSingleResourceDataDocument:
        """Creates a new priceConfiguration."""
        ...


    async def price_configurations_id_get(
        self,
        id: Annotated[str, Field(description="Price configuration id")],
    ) -> PriceConfigurationsSingleResourceDataDocument:
        """Retrieves single priceConfiguration by id."""
        ...
