# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing import List  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.default400_response_body import Default400ResponseBody  # noqa: F401
from tidal.models.default405_response_body import Default405ResponseBody  # noqa: F401
from tidal.models.default406_response_body import Default406ResponseBody  # noqa: F401
from tidal.models.default415_response_body import Default415ResponseBody  # noqa: F401
from tidal.models.default429_response_body import Default429ResponseBody  # noqa: F401
from tidal.models.default500_response_body import Default500ResponseBody  # noqa: F401
from tidal.models.default503_response_body import Default503ResponseBody  # noqa: F401
from tidal.models.track_files_read_by_id403_response_body import TrackFilesReadById403ResponseBody  # noqa: F401
from tidal.models.track_files_read_by_id404_response_body import TrackFilesReadById404ResponseBody  # noqa: F401
from tidal.models.track_files_single_resource_data_document import TrackFilesSingleResourceDataDocument  # noqa: F401


def test_track_files_id_get(client: TestClient):
    """Test case for track_files_id_get

    Get single trackFile.
    """
    params = [("formats", ['formats_example']),     ("usage", 'usage_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/trackFiles/{id}".format(id='123456'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

