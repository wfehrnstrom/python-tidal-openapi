# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.comment_summaries_multi_resource_data_document import CommentSummariesMultiResourceDataDocument
from tidal.models.comment_summaries_subject_single_relationship_data_document import CommentSummariesSubjectSingleRelationshipDataDocument
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseCommentSummariesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCommentSummariesApi.subclasses = BaseCommentSummariesApi.subclasses + (cls,)
    async def comment_summaries_get(
        self,
        filter_subject: Annotated[List[str], Field(min_length=1, max_length=20, description="Subjects whose counts to return.")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.author.albums")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> CommentSummariesMultiResourceDataDocument:
        """Returns one current summary per accessible subject, for up to 20 subjects. Duplicates are returned once. Inaccessible or missing subjects are omitted. Empty supported subjects still have a summary. IDs remain stable as counts change. Counts include root comments on source files and direct replies on comments."""
        ...


    async def comment_summaries_id_relationships_subject_get(
        self,
        id: Annotated[str, Field(description="Opaque identifier of one subject's current summary")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.author.albums")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> CommentSummariesSubjectSingleRelationshipDataDocument:
        """Retrieves subject relationship."""
        ...
