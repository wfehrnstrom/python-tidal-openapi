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
from tidal.models.lyrics_create_operation_payload import LyricsCreateOperationPayload
from tidal.models.lyrics_create_single_resource_data_document import LyricsCreateSingleResourceDataDocument
from tidal.models.lyrics_owners_multi_relationship_data_document import LyricsOwnersMultiRelationshipDataDocument
from tidal.models.lyrics_single_resource_data_document import LyricsSingleResourceDataDocument
from tidal.models.lyrics_track_single_relationship_data_document import LyricsTrackSingleRelationshipDataDocument
from tidal.models.lyrics_update_operation_payload import LyricsUpdateOperationPayload
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseLyricsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseLyricsApi.subclasses = BaseLyricsApi.subclasses + (cls,)
    async def lyrics_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        lyrics_create_operation_payload: Optional[LyricsCreateOperationPayload],
    ) -> LyricsCreateSingleResourceDataDocument:
        """Creates a new lyric."""
        ...


    async def lyrics_id_get(
        self,
        id: Annotated[str, Field(description="Lyrics Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, track")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: track")],
    ) -> LyricsSingleResourceDataDocument:
        """Retrieves single lyric by id."""
        ...


    async def lyrics_id_delete(
        self,
        id: Annotated[str, Field(description="Lyrics Id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
    ) -> MutationResponseDocument:
        """Deletes existing lyric."""
        ...


    async def lyrics_id_patch(
        self,
        id: Annotated[str, Field(description="Lyrics Id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        lyrics_update_operation_payload: Optional[LyricsUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Updates existing lyric."""
        ...


    async def lyrics_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Lyrics Id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> LyricsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def lyrics_id_relationships_track_get(
        self,
        id: Annotated[str, Field(description="Lyrics Id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: track")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: track")],
    ) -> LyricsTrackSingleRelationshipDataDocument:
        """Retrieves track relationship."""
        ...
