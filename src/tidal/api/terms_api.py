# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.terms_api_base import BaseTermsApi
import tidal.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

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
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/terms",
    responses={
        200: {"model": TermsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["terms"],
    summary="Get multiple terms.",
    response_model_by_alias=True,
)
async def terms_get(
    filter_terms_type: Annotated[List[str], Field(description="One of: DEVELOPER, UPLOAD_MARKETPLACE, MERCH_GUIDELINES, TIDAL_CONNECT_DEVELOPER (e.g. `DEVELOPER`)")] = Query(..., description="One of: DEVELOPER, UPLOAD_MARKETPLACE, MERCH_GUIDELINES, TIDAL_CONNECT_DEVELOPER (e.g. &#x60;DEVELOPER&#x60;)", alias="filter[termsType]"),
    filter_country_code: Annotated[Optional[List[Annotated[str, Field(min_length=1)]]], Field(description="Selects the country-specific terms variant when it has an effective version; otherwise falls back to the worldwide (WW) variant. Combine with `filter[isLatestVersion]=true` to return the currently acceptable terms. (e.g. `US`)")] = Query(None, description="Selects the country-specific terms variant when it has an effective version; otherwise falls back to the worldwide (WW) variant. Combine with &#x60;filter[isLatestVersion]&#x3D;true&#x60; to return the currently acceptable terms. (e.g. &#x60;US&#x60;)", alias="filter[countryCode]"),
    filter_is_latest_version: Annotated[Optional[List[str]], Field(description="Filter by isLatestVersion")] = Query(None, description="Filter by isLatestVersion", alias="filter[isLatestVersion]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TermsMultiResourceDataDocument:
    """Retrieves multiple terms by available filters, or without if applicable."""
    if not BaseTermsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTermsApi.subclasses[0]().terms_get(filter_terms_type, filter_country_code, filter_is_latest_version)


@router.get(
    "/terms/{id}",
    responses={
        200: {"model": TermsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["terms"],
    summary="Get single term.",
    response_model_by_alias=True,
)
async def terms_id_get(
    id: Annotated[str, Field(description="Terms id")] = Path(..., description="Terms id", examples=["a468bee88def"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TermsSingleResourceDataDocument:
    """Retrieves single term by id."""
    if not BaseTermsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTermsApi.subclasses[0]().terms_id_get(id)
