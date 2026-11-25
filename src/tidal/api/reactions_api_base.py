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
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.reactions_author_single_relationship_data_document import ReactionsAuthorSingleRelationshipDataDocument
from tidal.models.reactions_create_operation_payload import ReactionsCreateOperationPayload
from tidal.models.reactions_create_single_resource_data_document import ReactionsCreateSingleResourceDataDocument
from tidal.models.reactions_multi_resource_data_document import ReactionsMultiResourceDataDocument
from tidal.models.reactions_owners_multi_relationship_data_document import ReactionsOwnersMultiRelationshipDataDocument
from tidal.models.reactions_subject_single_relationship_data_document import ReactionsSubjectSingleRelationshipDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseReactionsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseReactionsApi.subclasses = BaseReactionsApi.subclasses + (cls,)
    async def reactions_get(
        self,
        filter_subject: Annotated[str, Field(description="The subject whose reactions to return.")],
        filter_emoji: Annotated[Optional[List[Annotated[str, Field(min_length=1, max_length=32)]]], Field(description="Filter by emoji (e.g. `👍`)")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: author, owners, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums")],
    ) -> ReactionsMultiResourceDataDocument:
        """Lists reactions on a source file or comment, newest first."""
        ...


    async def reactions_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        reactions_create_operation_payload: Optional[ReactionsCreateOperationPayload],
    ) -> ReactionsCreateSingleResourceDataDocument:
        """Adds the caller&#39;s emoji reaction on a subject and exact time offsets. Omit both offsets for the whole subject, provide startOffset for a point, or both for a section. Offsets are supported only on source files and must be nonnegative, with endOffset at or after startOffset. Each user can add different emojis at the same position or section. Repeating the same emoji returns the existing reaction with its UUID and creation time unchanged."""
        ...


    async def reactions_id_delete(
        self,
        id: Annotated[str, Field(description="Reaction Id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
    ) -> MutationResponseDocument:
        """Deletes existing reaction."""
        ...


    async def reactions_id_relationships_author_get(
        self,
        id: Annotated[str, Field(description="Reaction Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: author")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums")],
    ) -> ReactionsAuthorSingleRelationshipDataDocument:
        """The artist who left the reaction."""
        ...


    async def reactions_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Reaction Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ReactionsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def reactions_id_relationships_subject_get(
        self,
        id: Annotated[str, Field(description="Reaction Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.author.albums")],
    ) -> ReactionsSubjectSingleRelationshipDataDocument:
        """Retrieves subject relationship."""
        ...
