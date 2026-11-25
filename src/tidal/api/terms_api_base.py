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
from tidal.models.terms_multi_resource_data_document import TermsMultiResourceDataDocument
from tidal.models.terms_single_resource_data_document import TermsSingleResourceDataDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseTermsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTermsApi.subclasses = BaseTermsApi.subclasses + (cls,)
    async def terms_get(
        self,
        filter_terms_type: Annotated[List[str], Field(description="One of: DEVELOPER, UPLOAD_MARKETPLACE, MERCH_GUIDELINES, TIDAL_CONNECT_DEVELOPER (e.g. `DEVELOPER`)")],
        filter_country_code: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="Selects the country-specific terms variant when it has an effective version; otherwise falls back to the worldwide (WW) variant. Combine with `filter[isLatestVersion]=true` to return the currently acceptable terms. (e.g. `US`)")],
        filter_is_latest_version: Annotated[Optional[List[str]], Field(description="Filter by isLatestVersion")],
    ) -> TermsMultiResourceDataDocument:
        """Retrieves multiple terms by available filters, or without if applicable."""
        ...


    async def terms_id_get(
        self,
        id: Annotated[str, Field(description="Terms id")],
    ) -> TermsSingleResourceDataDocument:
        """Retrieves single term by id."""
        ...
