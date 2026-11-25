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
from tidal.models.provider_product_infos_multi_resource_data_document import ProviderProductInfosMultiResourceDataDocument
from tidal.models.provider_product_infos_provider_single_relationship_data_document import ProviderProductInfosProviderSingleRelationshipDataDocument
from tidal.models.provider_product_infos_subject_single_relationship_data_document import ProviderProductInfosSubjectSingleRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseProviderProductInfosApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseProviderProductInfosApi.subclasses = BaseProviderProductInfosApi.subclasses + (cls,)
    async def provider_product_infos_get(
        self,
        filter_provider_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="Content provider ID (e.g. `50`)")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        filter_barcode_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of barcode IDs (EAN-13 or UPC-A) (e.g. `00602527336510`)")],
        filter_grid: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of GRIDs (Global Release Identifier, ISO 7064) (e.g. `A10302B0013941653J`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: provider, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")],
    ) -> ProviderProductInfosMultiResourceDataDocument:
        """Retrieves multiple providerProductInfos by available filters, or without if applicable."""
        ...


    async def provider_product_infos_id_relationships_provider_get(
        self,
        id: Annotated[str, Field(description="Provider product info id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: provider")],
    ) -> ProviderProductInfosProviderSingleRelationshipDataDocument:
        """Retrieves provider relationship."""
        ...


    async def provider_product_infos_id_relationships_subject_get(
        self,
        id: Annotated[str, Field(description="Provider product info id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")],
    ) -> ProviderProductInfosSubjectSingleRelationshipDataDocument:
        """Retrieves subject relationship."""
        ...
