# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.accepted_terms_api_base import BaseAcceptedTermsApi
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
from tidal.models.accepted_terms_create_operation_payload import AcceptedTermsCreateOperationPayload
from tidal.models.accepted_terms_create_single_resource_data_document import AcceptedTermsCreateSingleResourceDataDocument
from tidal.models.accepted_terms_multi_resource_data_document import AcceptedTermsMultiResourceDataDocument
from tidal.models.accepted_terms_owners_multi_relationship_data_document import AcceptedTermsOwnersMultiRelationshipDataDocument
from tidal.models.accepted_terms_terms_single_relationship_data_document import AcceptedTermsTermsSingleRelationshipDataDocument
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
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/acceptedTerms",
    responses={
        200: {"model": AcceptedTermsMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["acceptedTerms"],
    summary="Get multiple acceptedTerms.",
    response_model_by_alias=True,
)
async def accepted_terms_get(
    filter_owners_id: Annotated[List[Annotated[str, Field(min_length=1)]], Field(description="User id. Also accepts `me`.")] = Query(..., description="User id. Also accepts &#x60;me&#x60;.", alias="filter[owners.id]"),
    filter_terms_terms_type: Annotated[List[str], Field(description="One of: DEVELOPER, UPLOAD_MARKETPLACE, MERCH_GUIDELINES, TIDAL_CONNECT_DEVELOPER (e.g. `DEVELOPER`)")] = Query(..., description="One of: DEVELOPER, UPLOAD_MARKETPLACE, MERCH_GUIDELINES, TIDAL_CONNECT_DEVELOPER (e.g. &#x60;DEVELOPER&#x60;)", alias="filter[terms.termsType]"),
    filter_terms_is_latest_version: Annotated[Optional[List[str]], Field(description="Filter by terms.isLatestVersion")] = Query(None, description="Filter by terms.isLatestVersion", alias="filter[terms.isLatestVersion]"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners, terms")] = Query(None, description="Include related resources. Available relationships: owners, terms", alias="include", examples=["terms"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> AcceptedTermsMultiResourceDataDocument:
    """Retrieves multiple acceptedTerms by available filters, or without if applicable."""
    if not BaseAcceptedTermsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAcceptedTermsApi.subclasses[0]().accepted_terms_get(filter_owners_id, filter_terms_terms_type, filter_terms_is_latest_version, include, include_linkage)


@router.post(
    "/acceptedTerms",
    responses={
        201: {"model": AcceptedTermsCreateSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        409: {"model": Idempotency409ResponseBody, "description": "Request already in progress for this idempotency key"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        422: {"model": Idempotency422ResponseBody, "description": "Idempotency key reused for a different request"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["acceptedTerms"],
    summary="Create single acceptedTerm.",
    response_model_by_alias=True,
)
async def accepted_terms_post(
    idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = Header(None, description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.", max_length=128, examples=["79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d"]),
    accepted_terms_create_operation_payload: Optional[AcceptedTermsCreateOperationPayload] = Body(None, description=""),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["w_usr"]
    ),
) -> AcceptedTermsCreateSingleResourceDataDocument:
    """Creates a new acceptedTerm."""
    if not BaseAcceptedTermsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAcceptedTermsApi.subclasses[0]().accepted_terms_post(idempotency_key, accepted_terms_create_operation_payload)


@router.get(
    "/acceptedTerms/{id}/relationships/owners",
    responses={
        200: {"model": AcceptedTermsOwnersMultiRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["acceptedTerms"],
    summary="Get owners relationship (\&quot;to-many\&quot;).",
    response_model_by_alias=True,
)
async def accepted_terms_id_relationships_owners_get(
    id: Annotated[str, Field(description="Accepted terms id")] = Path(..., description="Accepted terms id", examples=["a468bee88def"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")] = Query(None, description="Include related resources. Available relationships: owners", alias="include", examples=["owners"]),
    page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = Query(None, description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified", alias="page[cursor]"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> AcceptedTermsOwnersMultiRelationshipDataDocument:
    """Retrieves owners relationship."""
    if not BaseAcceptedTermsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAcceptedTermsApi.subclasses[0]().accepted_terms_id_relationships_owners_get(id, include, page_cursor)


@router.get(
    "/acceptedTerms/{id}/relationships/terms",
    responses={
        200: {"model": AcceptedTermsTermsSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["acceptedTerms"],
    summary="Get terms relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def accepted_terms_id_relationships_terms_get(
    id: Annotated[str, Field(description="Accepted terms id")] = Path(..., description="Accepted terms id", examples=["a468bee88def"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: terms")] = Query(None, description="Include related resources. Available relationships: terms", alias="include", examples=["terms"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["r_usr"]
    ),
) -> AcceptedTermsTermsSingleRelationshipDataDocument:
    """Retrieves terms relationship."""
    if not BaseAcceptedTermsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAcceptedTermsApi.subclasses[0]().accepted_terms_id_relationships_terms_get(id, include)
