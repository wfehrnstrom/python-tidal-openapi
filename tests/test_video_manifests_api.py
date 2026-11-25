# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.default400_response_body import Default400ResponseBody  # noqa: F401
from tidal.models.default405_response_body import Default405ResponseBody  # noqa: F401
from tidal.models.default406_response_body import Default406ResponseBody  # noqa: F401
from tidal.models.default415_response_body import Default415ResponseBody  # noqa: F401
from tidal.models.default429_response_body import Default429ResponseBody  # noqa: F401
from tidal.models.default500_response_body import Default500ResponseBody  # noqa: F401
from tidal.models.default503_response_body import Default503ResponseBody  # noqa: F401
from tidal.models.video_manifests_read_by_id403_response_body import VideoManifestsReadById403ResponseBody  # noqa: F401
from tidal.models.video_manifests_read_by_id404_response_body import VideoManifestsReadById404ResponseBody  # noqa: F401
from tidal.models.video_manifests_single_resource_data_document import VideoManifestsSingleResourceDataDocument  # noqa: F401


def test_video_manifests_id_get(client: TestClient):
    """Test case for video_manifests_id_get

    Get single videoManifest.
    """
    params = [("uri_scheme", 'uri_scheme_example'),     ("usage", 'usage_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/videoManifests/{id}".format(id='75623239'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

