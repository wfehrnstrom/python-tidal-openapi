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
from tidal.models.dynamic_modules_items_multi_relationship_data_document import DynamicModulesItemsMultiRelationshipDataDocument
from tidal.models.dynamic_modules_multi_resource_data_document import DynamicModulesMultiResourceDataDocument
from tidal.models.dynamic_modules_seed_item_single_relationship_data_document import DynamicModulesSeedItemSingleRelationshipDataDocument
from tidal.models.dynamic_modules_single_resource_data_document import DynamicModulesSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseDynamicModulesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDynamicModulesApi.subclasses = BaseDynamicModulesApi.subclasses + (cls,)
    async def dynamic_modules_get(
        self,
        client_version: Annotated[str, Field(description="Client version number")],
        device_type: Annotated[str, Field(description="The type of device making the request")],
        filter_id: Annotated[List[str], Field(min_length=1, max_length=20, description="DynamicModules Id (e.g. `nejMcAhh5N8S3EQ4LaqysVdI0cZZ`)")],
        system_type: Annotated[str, Field(description="The system type of the device making the request")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items, seedItem")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")],
        refresh_seed: Annotated[Optional[str], Field(description="Stable seed used to keep dynamic page and module results consistent across a client session.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")],
    ) -> DynamicModulesMultiResourceDataDocument:
        """Retrieves multiple dynamicModules by available filters, or without if applicable."""
        ...


    async def dynamic_modules_id_get(
        self,
        client_version: Annotated[str, Field(description="Client version number")],
        device_type: Annotated[str, Field(description="The type of device making the request")],
        id: Annotated[str, Field(description="DynamicModules Id")],
        system_type: Annotated[str, Field(description="The system type of the device making the request")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items, seedItem")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")],
        refresh_seed: Annotated[Optional[str], Field(description="Stable seed used to keep dynamic page and module results consistent across a client session.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")],
    ) -> DynamicModulesSingleResourceDataDocument:
        """Retrieves single dynamicModule by id."""
        ...


    async def dynamic_modules_id_relationships_items_get(
        self,
        client_version: Annotated[str, Field(description="Client version number")],
        device_type: Annotated[str, Field(description="The type of device making the request")],
        id: Annotated[str, Field(description="DynamicModules Id")],
        system_type: Annotated[str, Field(description="The system type of the device making the request")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")],
        locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        refresh_seed: Annotated[Optional[str], Field(description="Stable seed used to keep dynamic page and module results consistent across a client session.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")],
    ) -> DynamicModulesItemsMultiRelationshipDataDocument:
        """The module&#39;s items, in order — one stable collection per module, consistent for a given refreshSeed. Reads without a cursor return the first page (the slice a page shelf renders, sized for the module&#39;s previewLayout and device) with a continuation cursor; passing the cursor returns subsequent pages."""
        ...


    async def dynamic_modules_id_relationships_seed_item_get(
        self,
        client_version: Annotated[str, Field(description="Client version number")],
        device_type: Annotated[str, Field(description="The type of device making the request")],
        id: Annotated[str, Field(description="DynamicModules Id")],
        system_type: Annotated[str, Field(description="The system type of the device making the request")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: seedItem")],
        locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")],
        refresh_seed: Annotated[Optional[str], Field(description="Stable seed used to keep dynamic page and module results consistent across a client session.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: seedItem")],
    ) -> DynamicModulesSeedItemSingleRelationshipDataDocument:
        """The item whose listen or add event seeded this module&#39;s collection (e.g. the album a BECAUSE_YOU_* module is based on); null for modules that are not seeded by an item."""
        ...
