# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.purchases_api_base import BasePurchasesApi
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
from tidal.models.purchases_multi_resource_data_document import PurchasesMultiResourceDataDocument
from tidal.models.purchases_owners_multi_relationship_data_document import PurchasesOwnersMultiRelationshipDataDocument
from tidal.models.purchases_subject_single_relationship_data_document import PurchasesSubjectSingleRelationshipDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/purchases",
    responses={
        200: {"model": PurchasesMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["purchases"],
    summary="Get multiple purchases.",
    response_model_by_alias=True,
)
async def purchases_get(
    filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1, description="User id. Also accepts `me`.")] = Query(..., description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    filter_subject_type: Annotated[List[str], Field(description="The type of purchased content (e.g. `albums`)")] = Query(..., description="The type of purchased content (e.g. &#x60;albums&#x60;)", alias="filter[subject.type]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, subject")] = Query(None, description="Include related resources. Available relationships: owners, subject", alias="include", examples=["subject"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject", alias="replaceMedia", examples=["subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> PurchasesMultiResourceDataDocument:
    """Retrieves multiple purchases by available filters, or without if applicable."""
    if not BasePurchasesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePurchasesApi.subclasses[0]().purchases_get(filter_owners_id, filter_subject_type, include, include_linkage, page_cursor, replace_media)


@router.get(
    "/purchases/{id}/relationships/owners",
    responses={
        200: {"model": PurchasesOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["purchases"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def purchases_id_relationships_owners_get(
    id: Annotated[str, Field(description="Purchase id")] = Path(..., description="Purchase id", examples=["3fG7kLmN2pQrStUv"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> PurchasesOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BasePurchasesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePurchasesApi.subclasses[0]().purchases_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/purchases/{id}/relationships/subject",
    responses={
        200: {"model": PurchasesSubjectSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["purchases"],
    summary="Get subject relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def purchases_id_relationships_subject_get(
    id: Annotated[str, Field(description="Purchase id")] = Path(..., description="Purchase id", examples=["3fG7kLmN2pQrStUv"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject", alias="replaceMedia", examples=["subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> PurchasesSubjectSingleRelationshipDataDocument:
    """Retrieves subject relationship."""
    if not BasePurchasesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePurchasesApi.subclasses[0]().purchases_id_relationships_subject_get(id, include, replace_media)
