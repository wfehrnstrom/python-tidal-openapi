# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field
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
from tidal.models.genres_multi_resource_data_document import GenresMultiResourceDataDocument
from tidal.models.genres_single_resource_data_document import GenresSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseGenresApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseGenresApi.subclasses = BaseGenresApi.subclasses + (cls,)
    async def genres_get(
        self,
        filter_id: Annotated[List[str], Field(description="Allows filtering by genre id(s). USER_SELECTABLE is special value used to return specific genres which users can select from (e.g. `'1,2,3' or 'USER_SELECTABLE'`)")],
        locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
    ) -> GenresMultiResourceDataDocument:
        """Retrieves multiple genres by available filters, or without if applicable."""
        ...


    async def genres_id_get(
        self,
        id: Annotated[str, Field(description="Genre id")],
        locale: Annotated[Optional[str], Field(description="BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported.")],
    ) -> GenresSingleResourceDataDocument:
        """Retrieves single genre by id."""
        ...
