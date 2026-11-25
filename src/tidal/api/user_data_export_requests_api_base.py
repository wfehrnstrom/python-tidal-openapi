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
from tidal.models.user_data_export_requests_create_operation_payload import UserDataExportRequestsCreateOperationPayload
from tidal.models.user_data_export_requests_create_single_resource_data_document import UserDataExportRequestsCreateSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseUserDataExportRequestsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUserDataExportRequestsApi.subclasses = BaseUserDataExportRequestsApi.subclasses + (cls,)
    async def user_data_export_requests_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_data_export_requests_create_operation_payload: Optional[UserDataExportRequestsCreateOperationPayload],
    ) -> UserDataExportRequestsCreateSingleResourceDataDocument:
        """Creates a new userDataExportRequest."""
        ...
