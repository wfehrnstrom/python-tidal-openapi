# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.track_manifests_api_base import BaseTrackManifestsApi
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
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.models.track_manifests_read_by_id403_response_body import TrackManifestsReadById403ResponseBody
from tidal.models.track_manifests_read_by_id404_response_body import TrackManifestsReadById404ResponseBody
from tidal.models.track_manifests_single_resource_data_document import TrackManifestsSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/trackManifests/{id}",
    responses={
        200: {"model": TrackManifestsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": TrackManifestsReadById403ResponseBody, "description": "Required playback prerequisites are missing; Content is unavailable in your location; Content must be purchased before playback; Client cannot access this content; Account is playing on another app or device"},
        404: {"model": TrackManifestsReadById404ResponseBody, "description": "Content does not exist or is no longer available"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["trackManifests"],
    summary="Get single trackManifest.",
    response_model_by_alias=True,
)
async def track_manifests_id_get(
    adaptive: bool = Query(..., description="", alias="adaptive"),
    formats: List[str] = Query(..., description="", alias="formats"),
    id: Annotated[str, Field(description="Track manifest id")] = Path(..., description="Track manifest id", examples=["123456"]),
    manifest_type: str = Query(..., description="", alias="manifestType"),
    uri_scheme: str = Query(..., description="", alias="uriScheme"),
    usage: str = Query(..., description="", alias="usage"),
    share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")] = Query(None, description="Share code used as a bearer credential for the resource.", alias="shareCode", examples=["xyz"]),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playback", "r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> TrackManifestsSingleResourceDataDocument:
    """Retrieves single trackManifest by id."""
    if not BaseTrackManifestsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTrackManifestsApi.subclasses[0]().track_manifests_id_get(adaptive, formats, id, manifest_type, uri_scheme, usage, share_code)
