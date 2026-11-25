# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.content_claims_claimed_resource_single_relationship_data_document import ContentClaimsClaimedResourceSingleRelationshipDataDocument
from tidal.models.content_claims_claiming_artist_single_relationship_data_document import ContentClaimsClaimingArtistSingleRelationshipDataDocument
from tidal.models.content_claims_create_operation_payload import ContentClaimsCreateOperationPayload
from tidal.models.content_claims_create_single_resource_data_document import ContentClaimsCreateSingleResourceDataDocument
from tidal.models.content_claims_multi_resource_data_document import ContentClaimsMultiResourceDataDocument
from tidal.models.content_claims_owners_multi_relationship_data_document import ContentClaimsOwnersMultiRelationshipDataDocument
from tidal.models.content_claims_single_resource_data_document import ContentClaimsSingleResourceDataDocument
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
from tidal.security_api import get_token_Authorization_Code_PKCE

class BaseContentClaimsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseContentClaimsApi.subclasses = BaseContentClaimsApi.subclasses + (cls,)
    async def content_claims_get(
        self,
        filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="User id. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: claimedResource, claimingArtist, owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: claimedResource")],
    ) -> ContentClaimsMultiResourceDataDocument:
        """Retrieves multiple contentClaims by available filters, or without if applicable."""
        ...


    async def content_claims_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        content_claims_create_operation_payload: Optional[ContentClaimsCreateOperationPayload],
    ) -> ContentClaimsCreateSingleResourceDataDocument:
        """Creates a new contentClaim."""
        ...


    async def content_claims_id_get(
        self,
        id: Annotated[str, Field(description="Content claim id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: claimedResource, claimingArtist, owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: claimedResource")],
    ) -> ContentClaimsSingleResourceDataDocument:
        """Retrieves single contentClaim by id."""
        ...


    async def content_claims_id_relationships_claimed_resource_get(
        self,
        id: Annotated[str, Field(description="Content claim id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: claimedResource")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: claimedResource")],
    ) -> ContentClaimsClaimedResourceSingleRelationshipDataDocument:
        """Retrieves claimedResource relationship."""
        ...


    async def content_claims_id_relationships_claiming_artist_get(
        self,
        id: Annotated[str, Field(description="Content claim id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: claimingArtist")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: claimingArtist.albums")],
    ) -> ContentClaimsClaimingArtistSingleRelationshipDataDocument:
        """Retrieves claimingArtist relationship."""
        ...


    async def content_claims_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Content claim id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ContentClaimsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...
