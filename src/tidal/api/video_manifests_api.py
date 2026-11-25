# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from api.video_manifests_api_base import BaseVideoManifestsApi
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
from typing_extensions import Annotated
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.models.video_manifests_read_by_id403_response_body import VideoManifestsReadById403ResponseBody
from tidal.models.video_manifests_read_by_id404_response_body import VideoManifestsReadById404ResponseBody
from tidal.models.video_manifests_single_resource_data_document import VideoManifestsSingleResourceDataDocument
from models.extra_models import TokenModel  # noqa: F401
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

router = APIRouter()

ns_pkg = tidal.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/videoManifests/{id}",
    responses={
        200: {"model": VideoManifestsSingleResourceDataDocument, "description": "Successful response"},
        400: {"model": Default400ResponseBody, "description": "Invalid request"},
        403: {"model": VideoManifestsReadById403ResponseBody, "description": "Required playback prerequisites are missing; Content is unavailable in your location; Content must be purchased before playback; Client cannot access this content; Account is playing on another app or device"},
        404: {"model": VideoManifestsReadById404ResponseBody, "description": "Content does not exist or is no longer available"},
        405: {"model": Default405ResponseBody, "description": "HTTP method not allowed"},
        406: {"model": Default406ResponseBody, "description": "No acceptable response media type"},
        415: {"model": Default415ResponseBody, "description": "Unsupported request media type or encoding"},
        429: {"model": Default429ResponseBody, "description": "Rate limit exceeded"},
        500: {"model": Default500ResponseBody, "description": "Internal server error"},
        503: {"model": Default503ResponseBody, "description": "Service temporarily unavailable"},
    },
    tags=["videoManifests"],
    summary="Get single videoManifest.",
    response_model_by_alias=True,
)
async def video_manifests_id_get(
    id: Annotated[str, Field(description="Video manifest id")] = Path(..., description="Video manifest id", examples=["75623239"]),
    uri_scheme: str = Query(..., description="", alias="uriScheme"),
    usage: str = Query(..., description="", alias="usage"),
    token_Authorization_Code_PKCE: TokenModel = Security(
        get_token_Authorization_Code_PKCE, scopes=["playback", "r_usr"]
    ),
    token_Client_Credentials: TokenModel = Security(
        get_token_Client_Credentials, scopes=[]
    ),
) -> VideoManifestsSingleResourceDataDocument:
    """Retrieves single videoManifest by id."""
    if not BaseVideoManifestsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseVideoManifestsApi.subclasses[0]().video_manifests_id_get(id, uri_scheme, usage)
