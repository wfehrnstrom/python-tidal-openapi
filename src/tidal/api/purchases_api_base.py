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
from tidal.models.purchases_multi_resource_data_document import PurchasesMultiResourceDataDocument
from tidal.models.purchases_owners_multi_relationship_data_document import PurchasesOwnersMultiRelationshipDataDocument
from tidal.models.purchases_subject_single_relationship_data_document import PurchasesSubjectSingleRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BasePurchasesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePurchasesApi.subclasses = BasePurchasesApi.subclasses + (cls,)
    async def purchases_get(
        self,
        filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="User id. Also accepts `me`.")],
        filter_subject_type: Annotated[List[str], Field(description="The type of purchased content (e.g. `albums`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")],
    ) -> PurchasesMultiResourceDataDocument:
        """Retrieves multiple purchases by available filters, or without if applicable."""
        ...


    async def purchases_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Purchase id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> PurchasesOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def purchases_id_relationships_subject_get(
        self,
        id: Annotated[str, Field(description="Purchase id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")],
    ) -> PurchasesSubjectSingleRelationshipDataDocument:
        """Retrieves subject relationship."""
        ...
