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
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.usage_rules_create_operation_payload import UsageRulesCreateOperationPayload
from tidal.models.usage_rules_create_resource403_response_body import UsageRulesCreateResource403ResponseBody
from tidal.models.usage_rules_create_single_resource_data_document import UsageRulesCreateSingleResourceDataDocument
from tidal.models.usage_rules_single_resource_data_document import UsageRulesSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseUsageRulesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUsageRulesApi.subclasses = BaseUsageRulesApi.subclasses + (cls,)
    async def usage_rules_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        usage_rules_create_operation_payload: Optional[UsageRulesCreateOperationPayload],
    ) -> UsageRulesCreateSingleResourceDataDocument:
        """Creates a new usageRule."""
        ...


    async def usage_rules_id_get(
        self,
        id: Annotated[str, Field(description="Usage rules id")],
    ) -> UsageRulesSingleResourceDataDocument:
        """Retrieves single usageRule by id."""
        ...
