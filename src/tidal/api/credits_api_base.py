# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.credits_artist_single_relationship_data_document import CreditsArtistSingleRelationshipDataDocument
from tidal.models.credits_category_single_relationship_data_document import CreditsCategorySingleRelationshipDataDocument
from tidal.models.credits_single_resource_data_document import CreditsSingleResourceDataDocument
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseCreditsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCreditsApi.subclasses = BaseCreditsApi.subclasses + (cls,)
    async def credits_id_get(
        self,
        id: Annotated[str, Field(description="Credit id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artist, category")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artist.albums")],
    ) -> CreditsSingleResourceDataDocument:
        """Retrieves single credit by id."""
        ...


    async def credits_id_relationships_artist_get(
        self,
        id: Annotated[str, Field(description="Credit id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artist")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artist.albums")],
    ) -> CreditsArtistSingleRelationshipDataDocument:
        """Retrieves artist relationship."""
        ...


    async def credits_id_relationships_category_get(
        self,
        id: Annotated[str, Field(description="Credit id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: category")],
    ) -> CreditsCategorySingleRelationshipDataDocument:
        """Retrieves category relationship."""
        ...
