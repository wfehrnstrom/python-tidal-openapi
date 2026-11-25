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
from tidal.models.viewer_contexts_comments_multi_relationship_data_document import ViewerContextsCommentsMultiRelationshipDataDocument
from tidal.models.viewer_contexts_multi_resource_data_document import ViewerContextsMultiResourceDataDocument
from tidal.models.viewer_contexts_reactions_multi_relationship_data_document import ViewerContextsReactionsMultiRelationshipDataDocument
from tidal.models.viewer_contexts_single_resource_data_document import ViewerContextsSingleResourceDataDocument
from tidal.models.viewer_contexts_subject_single_relationship_data_document import ViewerContextsSubjectSingleRelationshipDataDocument
from tidal.models.viewer_contexts_viewer_single_relationship_data_document import ViewerContextsViewerSingleRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseViewerContextsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseViewerContextsApi.subclasses = BaseViewerContextsApi.subclasses + (cls,)
    async def viewer_contexts_get(
        self,
        filter_subject: Annotated[List[str], Field(min_length=1, max_length=20, description="Original subjects to look up. Also accepts `folders:me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: comments, reactions, subject, viewer")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: comments.author.albums")],
    ) -> ViewerContextsMultiResourceDataDocument:
        """Returns viewer contexts for up to 20 original subjects. Duplicate subjects are returned once."""
        ...


    async def viewer_contexts_id_get(
        self,
        id: Annotated[str, Field(min_length=1, max_length=256, description="Opaque identifier of one authenticated viewer and original subject pair")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: comments, reactions, subject, viewer")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: comments.author.albums")],
    ) -> ViewerContextsSingleResourceDataDocument:
        """Retrieves single viewerContext by id."""
        ...


    async def viewer_contexts_id_relationships_comments_get(
        self,
        id: Annotated[str, Field(min_length=1, max_length=256, description="Opaque identifier of one authenticated viewer and original subject pair")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: comments")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: comments.author.albums")],
    ) -> ViewerContextsCommentsMultiRelationshipDataDocument:
        """Returns the viewer&#39;s comments on the subject."""
        ...


    async def viewer_contexts_id_relationships_reactions_get(
        self,
        id: Annotated[str, Field(min_length=1, max_length=256, description="Opaque identifier of one authenticated viewer and original subject pair")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: reactions")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: reactions.author.albums")],
    ) -> ViewerContextsReactionsMultiRelationshipDataDocument:
        """Returns the viewer&#39;s reactions on the subject."""
        ...


    async def viewer_contexts_id_relationships_subject_get(
        self,
        id: Annotated[str, Field(min_length=1, max_length=256, description="Opaque identifier of one authenticated viewer and original subject pair")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")],
    ) -> ViewerContextsSubjectSingleRelationshipDataDocument:
        """Returns the subject of this viewer context."""
        ...


    async def viewer_contexts_id_relationships_viewer_get(
        self,
        id: Annotated[str, Field(min_length=1, max_length=256, description="Opaque identifier of one authenticated viewer and original subject pair")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: viewer")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: viewer.artist.albums")],
    ) -> ViewerContextsViewerSingleRelationshipDataDocument:
        """Returns the authenticated viewer of this context."""
        ...
