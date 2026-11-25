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
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.user_data_exports_create_operation_payload import UserDataExportsCreateOperationPayload
from tidal.models.user_data_exports_create_resource400_response_body import UserDataExportsCreateResource400ResponseBody
from tidal.models.user_data_exports_create_resource409_response_body import UserDataExportsCreateResource409ResponseBody
from tidal.models.user_data_exports_create_single_resource_data_document import UserDataExportsCreateSingleResourceDataDocument
from tidal.models.user_data_exports_multi_resource_data_document import UserDataExportsMultiResourceDataDocument
from tidal.models.user_data_exports_owners_multi_relationship_data_document import UserDataExportsOwnersMultiRelationshipDataDocument
from tidal.models.user_data_exports_single_resource_data_document import UserDataExportsSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseUserDataExportsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUserDataExportsApi.subclasses = BaseUserDataExportsApi.subclasses + (cls,)
    async def user_data_exports_get(
        self,
        filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="The authenticated user; exports of other users are never listed. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> UserDataExportsMultiResourceDataDocument:
        """Lists the authenticated user&#39;s exports, newest first."""
        ...


    async def user_data_exports_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        user_data_exports_create_operation_payload: Optional[UserDataExportsCreateOperationPayload],
    ) -> UserDataExportsCreateSingleResourceDataDocument:
        """Requests an export of the selected data types of the authenticated user&#39;s data, or returns the export already in progress as it was requested."""
        ...


    async def user_data_exports_id_get(
        self,
        id: Annotated[str, Field(max_length=64)],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> UserDataExportsSingleResourceDataDocument:
        """Retrieves single userDataExport by id."""
        ...


    async def user_data_exports_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(max_length=64)],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> UserDataExportsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...
