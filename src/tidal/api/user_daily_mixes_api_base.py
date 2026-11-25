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
from tidal.models.user_daily_mixes_items_multi_relationship_data_document import UserDailyMixesItemsMultiRelationshipDataDocument
from tidal.models.user_daily_mixes_single_resource_data_document import UserDailyMixesSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseUserDailyMixesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUserDailyMixesApi.subclasses = BaseUserDailyMixesApi.subclasses + (cls,)
    async def user_daily_mixes_id_get(
        self,
        id: Annotated[str, Field(description="User daily mixes id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items")],
    ) -> UserDailyMixesSingleResourceDataDocument:
        """Retrieves single userDailyMixe by id."""
        ...


    async def user_daily_mixes_id_relationships_items_get(
        self,
        id: Annotated[str, Field(description="User daily mixes id. Use `me` for the authenticated user's resource")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")],
        locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items")],
    ) -> UserDailyMixesItemsMultiRelationshipDataDocument:
        """Retrieves items relationship."""
        ...
