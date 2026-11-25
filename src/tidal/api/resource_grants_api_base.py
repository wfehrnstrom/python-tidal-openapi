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
from tidal.models.resource_grants_create_operation_payload import ResourceGrantsCreateOperationPayload
from tidal.models.resource_grants_create_resource403_response_body import ResourceGrantsCreateResource403ResponseBody
from tidal.models.resource_grants_create_resource429_response_body import ResourceGrantsCreateResource429ResponseBody
from tidal.models.resource_grants_create_single_resource_data_document import ResourceGrantsCreateSingleResourceDataDocument
from tidal.models.resource_grants_grantee_single_relationship_data_document import ResourceGrantsGranteeSingleRelationshipDataDocument
from tidal.models.resource_grants_invitation_single_relationship_data_document import ResourceGrantsInvitationSingleRelationshipDataDocument
from tidal.models.resource_grants_multi_resource_data_document import ResourceGrantsMultiResourceDataDocument
from tidal.models.resource_grants_single_resource_data_document import ResourceGrantsSingleResourceDataDocument
from tidal.models.resource_grants_subject_single_relationship_data_document import ResourceGrantsSubjectSingleRelationshipDataDocument
from tidal.models.resource_grants_update_operation_payload import ResourceGrantsUpdateOperationPayload
from tidal.models.resource_grants_update_single_resource_data_document import ResourceGrantsUpdateSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseResourceGrantsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseResourceGrantsApi.subclasses = BaseResourceGrantsApi.subclasses + (cls,)
    async def resource_grants_get(
        self,
        filter_grantee: Annotated[Optional[str], Field(description="Filter by grantee. Use `groups:everyone` for the Everyone group. Also accepts `users:me`.")],
        filter_role: Annotated[Optional[str], Field(description="One of: VIEWER, COLLABORATOR, OWNER (e.g. `VIEWER`)")],
        filter_self_applies_to: Annotated[Optional[str], Field(description="Album, track or folder whose grants are listed, including those on its ancestor folders and albums. Each grant keeps the subject it is stored on. Also accepts `folders:me`.")],
        filter_subject: Annotated[Optional[str], Field(description="Filter by subject. Required unless `filter[self][appliesTo]` is used. The subject's owner reads all its grants; other callers read only grants made directly to them. Also accepts `folders:me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: grantee, invitation, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: grantee.artist.albums")],
    ) -> ResourceGrantsMultiResourceDataDocument:
        """Retrieves multiple resourceGrants by available filters, or without if applicable."""
        ...


    async def resource_grants_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        resource_grants_create_operation_payload: Optional[ResourceGrantsCreateOperationPayload],
    ) -> ResourceGrantsCreateSingleResourceDataDocument:
        """Create a direct grant from &#x60;role&#x60;, &#x60;subject&#x60; and &#x60;grantee&#x60;. Alternatively, redeem an invitation with only the &#x60;invitation&#x60; relationship: the caller receives the invitation&#39;s role on its subject, and the response is the caller&#39;s grant. Redeeming again returns the same grant. Every redemption, repeated ones included, needs a password-protected invitation&#39;s password and counts as a use of a limited invitation; password attempts are rate limited. The invitation&#39;s creator cannot redeem it."""
        ...


    async def resource_grants_id_get(
        self,
        id: Annotated[str, Field(description="Opaque resource grant ID")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: grantee, invitation, subject")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: grantee.artist.albums")],
    ) -> ResourceGrantsSingleResourceDataDocument:
        """Retrieves single resourceGrant by id."""
        ...


    async def resource_grants_id_delete(
        self,
        id: Annotated[str, Field(description="Opaque resource grant ID")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
    ) -> MutationResponseDocument:
        """Deletes existing resourceGrant."""
        ...


    async def resource_grants_id_patch(
        self,
        id: Annotated[str, Field(description="Opaque resource grant ID")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        resource_grants_update_operation_payload: Optional[ResourceGrantsUpdateOperationPayload],
    ) -> ResourceGrantsUpdateSingleResourceDataDocument:
        """Updates existing resourceGrant."""
        ...


    async def resource_grants_id_relationships_grantee_get(
        self,
        id: Annotated[str, Field(description="Opaque resource grant ID")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: grantee")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: grantee.artist.albums")],
    ) -> ResourceGrantsGranteeSingleRelationshipDataDocument:
        """Retrieves grantee relationship."""
        ...


    async def resource_grants_id_relationships_invitation_get(
        self,
        id: Annotated[str, Field(description="Opaque resource grant ID")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: invitation")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: invitation.subject")],
    ) -> ResourceGrantsInvitationSingleRelationshipDataDocument:
        """Retrieves invitation relationship."""
        ...


    async def resource_grants_id_relationships_subject_get(
        self,
        id: Annotated[str, Field(description="Opaque resource grant ID")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")],
    ) -> ResourceGrantsSubjectSingleRelationshipDataDocument:
        """Retrieves subject relationship."""
        ...
