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
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.saved_shares_create_operation_payload import SavedSharesCreateOperationPayload
from tidal.models.saved_shares_create_resource403_response_body import SavedSharesCreateResource403ResponseBody
from tidal.models.saved_shares_create_resource429_response_body import SavedSharesCreateResource429ResponseBody
from tidal.models.saved_shares_create_single_resource_data_document import SavedSharesCreateSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseSavedSharesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSavedSharesApi.subclasses = BaseSavedSharesApi.subclasses + (cls,)
    async def saved_shares_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        saved_shares_create_operation_payload: Optional[SavedSharesCreateOperationPayload],
    ) -> SavedSharesCreateSingleResourceDataDocument:
        """Redeem an active share with VOUCHER access mode for its offered role. A share without VOUCHER mode returns 403. Every save, repeated ones included, needs a password-protected share&#39;s password and counts as a use of a limited share; password attempts are rate limited. Deprecated for playlist shares: use &#x60;POST /resourceGrants&#x60; with an &#x60;invitation&#x60; relationship instead."""
        ...
