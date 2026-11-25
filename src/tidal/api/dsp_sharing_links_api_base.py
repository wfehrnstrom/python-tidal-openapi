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
from tidal.models.dsp_sharing_links_multi_resource_data_document import DspSharingLinksMultiResourceDataDocument
from tidal.models.dsp_sharing_links_subject_single_relationship_data_document import DspSharingLinksSubjectSingleRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseDspSharingLinksApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDspSharingLinksApi.subclasses = BaseDspSharingLinksApi.subclasses + (cls,)
    async def dsp_sharing_links_get(
        self,
        filter_subject_id: Annotated[Optional[List[str]], Field(description="Deprecated: use filter[subject]. The id of the subject resource")],
        filter_subject_type: Annotated[Optional[List[str]], Field(description="Deprecated: use filter[subject]. The type of the subject resource (e.g. `tracks`)")],
        filter_subject: Annotated[Optional[str], Field(description="The subject whose DSP sharing links to return. Use either subject or the deprecated subject.id and subject.type pair.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")],
    ) -> DspSharingLinksMultiResourceDataDocument:
        """Retrieves multiple dspSharingLinks by available filters, or without if applicable."""
        ...


    async def dsp_sharing_links_id_relationships_subject_get(
        self,
        id: Annotated[str, Field(description="DspSharingLinks Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")],
    ) -> DspSharingLinksSubjectSingleRelationshipDataDocument:
        """Retrieves subject relationship."""
        ...
