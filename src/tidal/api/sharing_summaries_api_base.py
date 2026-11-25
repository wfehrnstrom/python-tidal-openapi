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
from tidal.models.sharing_summaries_multi_resource_data_document import SharingSummariesMultiResourceDataDocument
from tidal.models.sharing_summaries_subject_single_relationship_data_document import SharingSummariesSubjectSingleRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseSharingSummariesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSharingSummariesApi.subclasses = BaseSharingSummariesApi.subclasses + (cls,)
    async def sharing_summaries_get(
        self,
        filter_subject: Annotated[List[str], Field(min_length=1, max_length=20, description="Filter by subject. Also accepts `folders:me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")],
    ) -> SharingSummariesMultiResourceDataDocument:
        """Returns one current summary per distinct owned subject, for up to 20 subjects. Live subjects with no sharing return false flags. Missing or inaccessible subjects are omitted. IDs remain stable as sharing changes."""
        ...


    async def sharing_summaries_id_relationships_subject_get(
        self,
        id: Annotated[str, Field(description="Opaque sharing summary ID")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")],
    ) -> SharingSummariesSubjectSingleRelationshipDataDocument:
        """Retrieves subject relationship."""
        ...
