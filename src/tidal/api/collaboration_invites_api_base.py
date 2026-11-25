# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.collaboration_invites_create_operation_payload import CollaborationInvitesCreateOperationPayload
from tidal.models.collaboration_invites_create_single_resource_data_document import CollaborationInvitesCreateSingleResourceDataDocument
from tidal.models.collaboration_invites_multi_resource_data_document import CollaborationInvitesMultiResourceDataDocument
from tidal.models.collaboration_invites_owners_multi_relationship_data_document import CollaborationInvitesOwnersMultiRelationshipDataDocument
from tidal.models.collaboration_invites_single_resource_data_document import CollaborationInvitesSingleResourceDataDocument
from tidal.models.collaboration_invites_subject_single_relationship_data_document import CollaborationInvitesSubjectSingleRelationshipDataDocument
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

class BaseCollaborationInvitesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCollaborationInvitesApi.subclasses = BaseCollaborationInvitesApi.subclasses + (cls,)
    async def collaboration_invites_get(
        self,
        filter_code: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="Invite code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.items")],
    ) -> CollaborationInvitesMultiResourceDataDocument:
        """Retrieves multiple collaborationInvites by available filters, or without if applicable."""
        ...


    async def collaboration_invites_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        collaboration_invites_create_operation_payload: Optional[CollaborationInvitesCreateOperationPayload],
    ) -> CollaborationInvitesCreateSingleResourceDataDocument:
        """Creates a new collaborationInvite."""
        ...


    async def collaboration_invites_id_get(
        self,
        id: Annotated[str, Field(description="Collaboration invite id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.items")],
    ) -> CollaborationInvitesSingleResourceDataDocument:
        """Retrieves single collaborationInvite by id."""
        ...


    async def collaboration_invites_id_delete(
        self,
        id: Annotated[str, Field(description="Collaboration invite id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
    ) -> MutationResponseDocument:
        """Deletes existing collaborationInvite."""
        ...


    async def collaboration_invites_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Collaboration invite id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> CollaborationInvitesOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def collaboration_invites_id_relationships_subject_get(
        self,
        id: Annotated[str, Field(description="Collaboration invite id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.items")],
    ) -> CollaborationInvitesSubjectSingleRelationshipDataDocument:
        """Retrieves subject relationship."""
        ...
