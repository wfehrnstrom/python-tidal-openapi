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
from tidal.models.dynamic_pages_modules_multi_relationship_data_document import DynamicPagesModulesMultiRelationshipDataDocument
from tidal.models.dynamic_pages_multi_resource_data_document import DynamicPagesMultiResourceDataDocument
from tidal.models.dynamic_pages_subject_single_relationship_data_document import DynamicPagesSubjectSingleRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseDynamicPagesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDynamicPagesApi.subclasses = BaseDynamicPagesApi.subclasses + (cls,)
    async def dynamic_pages_get(
        self,
        client_version: Annotated[str, Field(description="Client version number")],
        device_type: Annotated[str, Field(description="The type of device making the request")],
        filter_page_type: Annotated[List[str], Field(description="Type of the page (e.g. `ARTIST`)")],
        system_type: Annotated[str, Field(description="The system type of the device making the request")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        filter_subject: Annotated[Optional[str], Field(description="The page subject. Its type must match pageType. Required except for HOME_FREE, where it must be omitted. Also accepts `users:me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: modules, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")],
        refresh_seed: Annotated[Optional[str], Field(description="Stable seed used to keep dynamic page and module results consistent across a client session.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: modules.items")],
    ) -> DynamicPagesMultiResourceDataDocument:
        """Retrieves multiple dynamicPages by available filters, or without if applicable."""
        ...


    async def dynamic_pages_id_relationships_modules_get(
        self,
        client_version: Annotated[str, Field(description="Client version number")],
        device_type: Annotated[str, Field(description="The type of device making the request")],
        id: Annotated[str, Field(description="DynamicPages Id")],
        system_type: Annotated[str, Field(description="The system type of the device making the request")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: modules")],
        locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        refresh_seed: Annotated[Optional[str], Field(description="Stable seed used to keep dynamic page and module results consistent across a client session.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: modules.items")],
    ) -> DynamicPagesModulesMultiRelationshipDataDocument:
        """The page&#39;s modules, in display order."""
        ...


    async def dynamic_pages_id_relationships_subject_get(
        self,
        id: Annotated[str, Field(description="DynamicPages Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")],
    ) -> DynamicPagesSubjectSingleRelationshipDataDocument:
        """Retrieves subject relationship."""
        ...
