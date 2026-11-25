# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.comments_author_single_relationship_data_document import CommentsAuthorSingleRelationshipDataDocument
from tidal.models.comments_comment_summary_single_relationship_data_document import CommentsCommentSummarySingleRelationshipDataDocument
from tidal.models.comments_create_operation_payload import CommentsCreateOperationPayload
from tidal.models.comments_create_single_resource_data_document import CommentsCreateSingleResourceDataDocument
from tidal.models.comments_multi_resource_data_document import CommentsMultiResourceDataDocument
from tidal.models.comments_owners_multi_relationship_data_document import CommentsOwnersMultiRelationshipDataDocument
from tidal.models.comments_reaction_summary_single_relationship_data_document import CommentsReactionSummarySingleRelationshipDataDocument
from tidal.models.comments_root_subject_single_relationship_data_document import CommentsRootSubjectSingleRelationshipDataDocument
from tidal.models.comments_single_resource_data_document import CommentsSingleResourceDataDocument
from tidal.models.comments_subject_single_relationship_data_document import CommentsSubjectSingleRelationshipDataDocument
from tidal.models.comments_update_operation_payload import CommentsUpdateOperationPayload
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
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseCommentsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCommentsApi.subclasses = BaseCommentsApi.subclasses + (cls,)
    async def comments_get(
        self,
        filter_subject: Annotated[str, Field(description="The immediate subject whose comments to return.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: author, commentSummary, owners, reactionSummary, rootSubject, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums")],
        sort: Annotated[Optional[List[str]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")],
    ) -> CommentsMultiResourceDataDocument:
        """Returns root comments on a resource, or replies to a comment. Both support createdAt in either direction, newest first by default."""
        ...


    async def comments_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        comments_create_operation_payload: Optional[CommentsCreateOperationPayload],
    ) -> CommentsCreateSingleResourceDataDocument:
        """Creates a root comment on a resource or a reply whose subject is a root comment. Replies to replies are rejected."""
        ...


    async def comments_id_get(
        self,
        id: Annotated[str, Field(description="Comment Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: author, commentSummary, owners, reactionSummary, rootSubject, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums")],
    ) -> CommentsSingleResourceDataDocument:
        """Retrieves single comment by id."""
        ...


    async def comments_id_delete(
        self,
        id: Annotated[str, Field(description="Comment Id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
    ) -> MutationResponseDocument:
        """Deletes existing comment."""
        ...


    async def comments_id_patch(
        self,
        id: Annotated[str, Field(description="Comment Id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        comments_update_operation_payload: Optional[CommentsUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Updates existing comment."""
        ...


    async def comments_id_relationships_author_get(
        self,
        id: Annotated[str, Field(description="Comment Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: author")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums")],
    ) -> CommentsAuthorSingleRelationshipDataDocument:
        """The artist who wrote the comment."""
        ...


    async def comments_id_relationships_comment_summary_get(
        self,
        id: Annotated[str, Field(description="Comment Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: commentSummary")],
    ) -> CommentsCommentSummarySingleRelationshipDataDocument:
        """Retrieves commentSummary relationship."""
        ...


    async def comments_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Comment Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> CommentsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def comments_id_relationships_reaction_summary_get(
        self,
        id: Annotated[str, Field(description="Comment Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: reactionSummary")],
    ) -> CommentsReactionSummarySingleRelationshipDataDocument:
        """Retrieves reactionSummary relationship."""
        ...


    async def comments_id_relationships_root_subject_get(
        self,
        id: Annotated[str, Field(description="Comment Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: rootSubject")],
    ) -> CommentsRootSubjectSingleRelationshipDataDocument:
        """Retrieves rootSubject relationship."""
        ...


    async def comments_id_relationships_subject_get(
        self,
        id: Annotated[str, Field(description="Comment Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.author.albums")],
    ) -> CommentsSubjectSingleRelationshipDataDocument:
        """Retrieves subject relationship."""
        ...
