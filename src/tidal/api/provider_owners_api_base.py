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
from tidal.models.provider_owners_multi_resource_data_document import ProviderOwnersMultiResourceDataDocument
from tidal.models.provider_owners_owners_multi_relationship_data_document import ProviderOwnersOwnersMultiRelationshipDataDocument
from tidal.models.provider_owners_provider_single_relationship_data_document import ProviderOwnersProviderSingleRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseProviderOwnersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseProviderOwnersApi.subclasses = BaseProviderOwnersApi.subclasses + (cls,)
    async def provider_owners_get(
        self,
        filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="User id. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, provider")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> ProviderOwnersMultiResourceDataDocument:
        """Retrieves multiple providerOwners by available filters, or without if applicable."""
        ...


    async def provider_owners_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Provider owner id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ProviderOwnersOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def provider_owners_id_relationships_provider_get(
        self,
        id: Annotated[str, Field(description="Provider owner id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: provider")],
    ) -> ProviderOwnersProviderSingleRelationshipDataDocument:
        """Retrieves provider relationship."""
        ...
