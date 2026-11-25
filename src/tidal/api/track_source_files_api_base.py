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
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.track_source_files_comment_summary_single_relationship_data_document import TrackSourceFilesCommentSummarySingleRelationshipDataDocument
from tidal.models.track_source_files_create_operation_payload import TrackSourceFilesCreateOperationPayload
from tidal.models.track_source_files_create_single_resource_data_document import TrackSourceFilesCreateSingleResourceDataDocument
from tidal.models.track_source_files_owners_multi_relationship_data_document import TrackSourceFilesOwnersMultiRelationshipDataDocument
from tidal.models.track_source_files_reaction_summary_single_relationship_data_document import TrackSourceFilesReactionSummarySingleRelationshipDataDocument
from tidal.models.track_source_files_single_resource_data_document import TrackSourceFilesSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseTrackSourceFilesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTrackSourceFilesApi.subclasses = BaseTrackSourceFilesApi.subclasses + (cls,)
    async def track_source_files_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        track_source_files_create_operation_payload: Optional[TrackSourceFilesCreateOperationPayload],
    ) -> TrackSourceFilesCreateSingleResourceDataDocument:
        """Create a track source file. &lt;p/&gt; The response contains a upload link that must be used to upload the actual content.&lt;p/&gt; The headers in the upload link response must be sent doing the actual upload. """
        ...


    async def track_source_files_id_get(
        self,
        id: Annotated[str, Field(description="Track source file id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: commentSummary, owners, reactionSummary")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TrackSourceFilesSingleResourceDataDocument:
        """Retrieves single trackSourceFile by id."""
        ...


    async def track_source_files_id_relationships_comment_summary_get(
        self,
        id: Annotated[str, Field(description="Track source file id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: commentSummary")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TrackSourceFilesCommentSummarySingleRelationshipDataDocument:
        """Retrieves commentSummary relationship."""
        ...


    async def track_source_files_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Track source file id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TrackSourceFilesOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def track_source_files_id_relationships_reaction_summary_get(
        self,
        id: Annotated[str, Field(description="Track source file id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: reactionSummary")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> TrackSourceFilesReactionSummarySingleRelationshipDataDocument:
        """Retrieves reactionSummary relationship."""
        ...
