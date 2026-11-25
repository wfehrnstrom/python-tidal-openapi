# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field
from typing import Optional
from typing_extensions import Annotated
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.square_item_variation_physical_counts_create_operation_payload import SquareItemVariationPhysicalCountsCreateOperationPayload
from tidal.models.square_item_variation_physical_counts_create_resource403_response_body import SquareItemVariationPhysicalCountsCreateResource403ResponseBody
from tidal.models.square_item_variation_physical_counts_create_resource409_response_body import SquareItemVariationPhysicalCountsCreateResource409ResponseBody
from tidal.models.square_item_variation_physical_counts_create_single_resource_data_document import SquareItemVariationPhysicalCountsCreateSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseSquareItemVariationPhysicalCountsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSquareItemVariationPhysicalCountsApi.subclasses = BaseSquareItemVariationPhysicalCountsApi.subclasses + (cls,)
    async def square_item_variation_physical_counts_post(
        self,
        idempotency_key: Annotated[str, Field(max_length=128, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        square_item_variation_physical_counts_create_operation_payload: Optional[SquareItemVariationPhysicalCountsCreateOperationPayload],
    ) -> SquareItemVariationPhysicalCountsCreateSingleResourceDataDocument:
        """Records a whole-unit physical stock count at occurredAt. Requires stock tracking at the selected site&#39;s shipping location (merchant-main fallback). While its replay receipt remains available, exact retries retain the original location and event time. Catalog revisions do not guard inventory counts."""
        ...
