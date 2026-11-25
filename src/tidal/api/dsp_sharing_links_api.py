# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.dsp_sharing_links_api_base import BaseDspSharingLinksApi
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
from tidal.models.dsp_sharing_links_multi_resource_data_document import DspSharingLinksMultiResourceDataDocument
from tidal.models.dsp_sharing_links_subject_single_relationship_data_document import DspSharingLinksSubjectSingleRelationshipDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/dspSharingLinks",
    responses={
        200: {"model": DspSharingLinksMultiResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["dspSharingLinks"],
    summary="Get multiple dspSharingLinks.",
    response_model_by_alias=True,
)
async def dsp_sharing_links_get(
    filter_subject_id: Annotated[Optional[List[str]], Field(description="Deprecated: use filter[subject]. The id of the subject resource")] = Query(None, description="Deprecated: use filter[subject]. The id of the subject resource", alias="filter[subject.id]"),
    filter_subject_type: Annotated[Optional[List[str]], Field(description="Deprecated: use filter[subject]. The type of the subject resource (e.g. `tracks`)")] = Query(None, description="Deprecated: use filter[subject]. The type of the subject resource (e.g. &#x60;tracks&#x60;)", alias="filter[subject.type]"),
    filter_subject: Annotated[Optional[str], Field(description="The subject whose DSP sharing links to return. Use either subject or the deprecated subject.id and subject.type pair.")] = Query(None, description="The subject whose DSP sharing links to return. Use either subject or the deprecated subject.id and subject.type pair.", alias="filter[subject]", regex=r"^(?:tracks|albums|artists):[^,]+$"),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject"]),
    include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = Query(None, description="Comma-separated direct relationships to return as linkage only, without related content.", alias="includeLinkage"),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject", alias="replaceMedia", examples=["subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> DspSharingLinksMultiResourceDataDocument:
    """Retrieves multiple dspSharingLinks by available filters, or without if applicable."""
    if not BaseDspSharingLinksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDspSharingLinksApi.subclasses[0]().dsp_sharing_links_get(filter_subject_id, filter_subject_type, filter_subject, include, include_linkage, replace_media)


@router.get(
    "/dspSharingLinks/{id}/relationships/subject",
    responses={
        200: {"model": DspSharingLinksSubjectSingleRelationshipDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        404: {"model": Default404ResponseBody, "description": "Resource not found"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["dspSharingLinks"],
    summary="Get subject relationship (\&quot;to-one\&quot;).",
    response_model_by_alias=True,
)
async def dsp_sharing_links_id_relationships_subject_get(
    id: Annotated[str, Field(description="DspSharingLinks Id")] = Path(..., description="DspSharingLinks Id", examples=["QUxCVU1TOjEyMzQ1"]),
    include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: subject")] = Query(None, description="Include related resources. Available relationships: subject", alias="include", examples=["subject"]),
    replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject")] = Query(None, description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject", alias="replaceMedia", examples=["subject"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=[]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> DspSharingLinksSubjectSingleRelationshipDataDocument:
    """Retrieves subject relationship."""
    if not BaseDspSharingLinksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDspSharingLinksApi.subclasses[0]().dsp_sharing_links_id_relationships_subject_get(id, include, replace_media)
