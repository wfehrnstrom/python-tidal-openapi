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
from tidal.models.resource_grant_invitations_create_operation_payload import ResourceGrantInvitationsCreateOperationPayload
from tidal.models.resource_grant_invitations_create_single_resource_data_document import ResourceGrantInvitationsCreateSingleResourceDataDocument
from tidal.models.resource_grant_invitations_multi_resource_data_document import ResourceGrantInvitationsMultiResourceDataDocument
from tidal.models.resource_grant_invitations_owners_multi_relationship_data_document import ResourceGrantInvitationsOwnersMultiRelationshipDataDocument
from tidal.models.resource_grant_invitations_preview_grant_single_relationship_data_document import ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument
from tidal.models.resource_grant_invitations_single_resource_data_document import ResourceGrantInvitationsSingleResourceDataDocument
from tidal.models.resource_grant_invitations_subject_single_relationship_data_document import ResourceGrantInvitationsSubjectSingleRelationshipDataDocument
from tidal.models.resource_grant_invitations_update_operation_payload import ResourceGrantInvitationsUpdateOperationPayload
from tidal.models.resource_grant_invitations_update_single_resource_data_document import ResourceGrantInvitationsUpdateSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseResourceGrantInvitationsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseResourceGrantInvitationsApi.subclasses = BaseResourceGrantInvitationsApi.subclasses + (cls,)
    async def resource_grant_invitations_get(
        self,
        filter_code: Annotated[Optional[Annotated[str, Field(min_length=1)]], Field(description="Invitation code (e.g. `42179b73-6f0c-405c-b926-2fdb45363c44`)")],
        filter_self_applies_to: Annotated[Optional[str], Field(description="Album, track or folder owned by the caller. Selects undeleted, unexpired invitations on the resource or its ancestors; used-up ones are included. Each keeps its own subject. Cannot be combined with other filters. Missing or non-owned resources and subjects without a live access node return no records. Ordered by expiry then ID; at most 20 invitations per page. Also accepts `folders:me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, previewGrant, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: previewGrant.subject")],
    ) -> ResourceGrantInvitationsMultiResourceDataDocument:
        """Retrieves multiple resourceGrantInvitations by available filters, or without if applicable."""
        ...


    async def resource_grant_invitations_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        resource_grant_invitations_create_operation_payload: Optional[ResourceGrantInvitationsCreateOperationPayload],
    ) -> ResourceGrantInvitationsCreateSingleResourceDataDocument:
        """Creates a new resourceGrantInvitation."""
        ...


    async def resource_grant_invitations_id_get(
        self,
        id: Annotated[str, Field(description="Invitation id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, previewGrant, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: previewGrant.subject")],
    ) -> ResourceGrantInvitationsSingleResourceDataDocument:
        """Retrieves single resourceGrantInvitation by id."""
        ...


    async def resource_grant_invitations_id_delete(
        self,
        id: Annotated[str, Field(description="Invitation id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        revoke_grants: Annotated[Optional[bool], Field(description="Also revoke the grants redemptions issued; access from other sources stays. Defaults to false.")],
    ) -> MutationResponseDocument:
        """Delete the invitation, ending redemption and its preview."""
        ...


    async def resource_grant_invitations_id_patch(
        self,
        id: Annotated[str, Field(description="Invitation id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        resource_grant_invitations_update_operation_payload: Optional[ResourceGrantInvitationsUpdateOperationPayload],
    ) -> ResourceGrantInvitationsUpdateSingleResourceDataDocument:
        """Set, change or remove the password, or turn the preview on or off. Users who redeemed keep their grants."""
        ...


    async def resource_grant_invitations_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Invitation id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ResourceGrantInvitationsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def resource_grant_invitations_id_relationships_preview_grant_get(
        self,
        id: Annotated[str, Field(description="Invitation id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: previewGrant")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: previewGrant.subject")],
    ) -> ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument:
        """Retrieves previewGrant relationship."""
        ...


    async def resource_grant_invitations_id_relationships_subject_get(
        self,
        id: Annotated[str, Field(description="Invitation id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")],
    ) -> ResourceGrantInvitationsSubjectSingleRelationshipDataDocument:
        """Retrieves subject relationship."""
        ...
