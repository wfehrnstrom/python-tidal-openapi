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
from tidal.models.search_suggestions_direct_hits_multi_relationship_data_document import SearchSuggestionsDirectHitsMultiRelationshipDataDocument
from tidal.models.search_suggestions_history_multi_relationship_data_document import SearchSuggestionsHistoryMultiRelationshipDataDocument
from tidal.models.search_suggestions_multi_resource_data_document import SearchSuggestionsMultiResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseSearchSuggestionsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSearchSuggestionsApi.subclasses = BaseSearchSuggestionsApi.subclasses + (cls,)
    async def search_suggestions_get(
        self,
        filter_query: Annotated[str, Field(min_length=1, max_length=256, description="Search query (e.g. `hello`)")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: directHits, history")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: directHits")],
    ) -> SearchSuggestionsMultiResourceDataDocument:
        """Searches for a query and returns a collection containing exactly one search suggestions resource."""
        ...


    async def search_suggestions_id_relationships_direct_hits_get(
        self,
        id: Annotated[str, Field(description="An opaque search suggestions identifier")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: directHits")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: directHits")],
    ) -> SearchSuggestionsDirectHitsMultiRelationshipDataDocument:
        """Retrieves directHits relationship."""
        ...


    async def search_suggestions_id_relationships_history_get(
        self,
        id: Annotated[str, Field(description="An opaque search suggestions identifier")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        explicit_filter: Annotated[Optional[str], Field(description="Explicit filter. Valid values: INCLUDE or EXCLUDE")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: history")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> SearchSuggestionsHistoryMultiRelationshipDataDocument:
        """Retrieves history relationship."""
        ...
