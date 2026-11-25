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
from tidal.models.user_feed_items_actors_multi_relationship_data_document import UserFeedItemsActorsMultiRelationshipDataDocument
from tidal.models.user_feed_items_multi_resource_data_document import UserFeedItemsMultiResourceDataDocument
from tidal.models.user_feed_items_subject_single_relationship_data_document import UserFeedItemsSubjectSingleRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseUserFeedItemsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUserFeedItemsApi.subclasses = BaseUserFeedItemsApi.subclasses + (cls,)
    async def user_feed_items_get(
        self,
        filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="User id. Also accepts `me`.")],
        filter_surface: Annotated[str, Field(description="Feed surface to read (e.g. `INBOX`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: actors, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: actors.albums")],
    ) -> UserFeedItemsMultiResourceDataDocument:
        """The authenticated user&#39;s activity on the selected feed surface."""
        ...


    async def user_feed_items_id_relationships_actors_get(
        self,
        id: Annotated[str, Field(min_length=1, max_length=432, description="Opaque identifier of a user feed item.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: actors")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: actors.albums")],
    ) -> UserFeedItemsActorsMultiRelationshipDataDocument:
        """Artists attributed to the activity. Always empty for &#x60;ALBUM_FAVOURITED&#x60;, &#x60;TRACK_FAVOURITED&#x60; and &#x60;TRACK_PLAYLISTED&#x60;, which are counts only, and for &#x60;HISTORY_MIX_READY&#x60; and &#x60;TRACK_PLAY_MILESTONE&#x60;, which nobody else acted on."""
        ...


    async def user_feed_items_id_relationships_subject_get(
        self,
        id: Annotated[str, Field(min_length=1, max_length=432, description="Opaque identifier of a user feed item.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")],
    ) -> UserFeedItemsSubjectSingleRelationshipDataDocument:
        """The resource the activity concerns. For &#x60;HISTORY_MIX_READY&#x60;, the viewer&#39;s history mix as a playlist."""
        ...
