# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.artist_claims_accepted_artists_multi_relationship_data_document import ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument
from tidal.models.artist_claims_accepted_artists_relationship_update_operation_payload import ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload
from tidal.models.artist_claims_create_operation_payload import ArtistClaimsCreateOperationPayload
from tidal.models.artist_claims_create_single_resource_data_document import ArtistClaimsCreateSingleResourceDataDocument
from tidal.models.artist_claims_multi_resource_data_document import ArtistClaimsMultiResourceDataDocument
from tidal.models.artist_claims_owners_multi_relationship_data_document import ArtistClaimsOwnersMultiRelationshipDataDocument
from tidal.models.artist_claims_recommended_artists_multi_relationship_data_document import ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument
from tidal.models.artist_claims_single_resource_data_document import ArtistClaimsSingleResourceDataDocument
from tidal.models.artist_claims_update_operation_payload import ArtistClaimsUpdateOperationPayload
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

class BaseArtistClaimsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseArtistClaimsApi.subclasses = BaseArtistClaimsApi.subclasses + (cls,)
    async def artist_claims_get(
        self,
        filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="User id. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: acceptedArtists, owners, recommendedArtists")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: acceptedArtists.albums")],
    ) -> ArtistClaimsMultiResourceDataDocument:
        """Retrieves multiple artistClaims by available filters, or without if applicable."""
        ...


    async def artist_claims_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        artist_claims_create_operation_payload: Optional[ArtistClaimsCreateOperationPayload],
    ) -> ArtistClaimsCreateSingleResourceDataDocument:
        """Creates a new artistClaim."""
        ...


    async def artist_claims_id_get(
        self,
        id: Annotated[str, Field(description="Artist claim id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: acceptedArtists, owners, recommendedArtists")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: acceptedArtists.albums")],
    ) -> ArtistClaimsSingleResourceDataDocument:
        """Retrieves single artistClaim by id."""
        ...


    async def artist_claims_id_delete(
        self,
        id: Annotated[str, Field(description="Artist claim id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
    ) -> MutationResponseDocument:
        """Deletes existing artistClaim."""
        ...


    async def artist_claims_id_patch(
        self,
        id: Annotated[str, Field(description="Artist claim id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        artist_claims_update_operation_payload: Optional[ArtistClaimsUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Updates existing artistClaim."""
        ...


    async def artist_claims_id_relationships_accepted_artists_get(
        self,
        id: Annotated[str, Field(description="Artist claim id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: acceptedArtists")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: acceptedArtists.albums")],
    ) -> ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument:
        """Retrieves acceptedArtists relationship."""
        ...


    async def artist_claims_id_relationships_accepted_artists_patch(
        self,
        id: Annotated[str, Field(description="Artist claim id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        artist_claims_accepted_artists_relationship_update_operation_payload: Optional[ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Accepts one recommended artist and processes the claim, merging profile metadata or moving claimed albums according to the recommendation. Empty data cancels the claim; it does not delete any artist. Returns an acknowledgement."""
        ...


    async def artist_claims_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Artist claim id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ArtistClaimsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def artist_claims_id_relationships_recommended_artists_get(
        self,
        id: Annotated[str, Field(description="Artist claim id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: recommendedArtists")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: recommendedArtists.albums")],
    ) -> ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument:
        """Retrieves recommendedArtists relationship."""
        ...
