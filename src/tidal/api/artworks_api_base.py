# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.artworks_create_operation_payload import ArtworksCreateOperationPayload
from tidal.models.artworks_create_single_resource_data_document import ArtworksCreateSingleResourceDataDocument
from tidal.models.artworks_multi_resource_data_document import ArtworksMultiResourceDataDocument
from tidal.models.artworks_owners_multi_relationship_data_document import ArtworksOwnersMultiRelationshipDataDocument
from tidal.models.artworks_single_resource_data_document import ArtworksSingleResourceDataDocument
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
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseArtworksApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseArtworksApi.subclasses = BaseArtworksApi.subclasses + (cls,)
    async def artworks_get(
        self,
        filter_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="Artwork id (e.g. `a468bee88def`)")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> ArtworksMultiResourceDataDocument:
        """Retrieves multiple artworks by available filters, or without if applicable."""
        ...


    async def artworks_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        artworks_create_operation_payload: Optional[ArtworksCreateOperationPayload],
    ) -> ArtworksCreateSingleResourceDataDocument:
        """Creates a new artwork."""
        ...


    async def artworks_id_get(
        self,
        id: Annotated[str, Field(description="Artwork id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
    ) -> ArtworksSingleResourceDataDocument:
        """Retrieves single artwork by id."""
        ...


    async def artworks_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Artwork id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> ArtworksOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...
