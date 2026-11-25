# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.default400_response_body import Default400ResponseBody  # noqa: F401
from tidal.models.default404_response_body import Default404ResponseBody  # noqa: F401
from tidal.models.default405_response_body import Default405ResponseBody  # noqa: F401
from tidal.models.default406_response_body import Default406ResponseBody  # noqa: F401
from tidal.models.default415_response_body import Default415ResponseBody  # noqa: F401
from tidal.models.default429_response_body import Default429ResponseBody  # noqa: F401
from tidal.models.default500_response_body import Default500ResponseBody  # noqa: F401
from tidal.models.default503_response_body import Default503ResponseBody  # noqa: F401
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody  # noqa: F401
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody  # noqa: F401
from tidal.models.mutation_response_document import MutationResponseDocument  # noqa: F401
from tidal.models.playlist_generation_schedules_create_operation_payload import PlaylistGenerationSchedulesCreateOperationPayload  # noqa: F401
from tidal.models.playlist_generation_schedules_create_resource403_response_body import PlaylistGenerationSchedulesCreateResource403ResponseBody  # noqa: F401
from tidal.models.playlist_generation_schedules_create_single_resource_data_document import PlaylistGenerationSchedulesCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.playlist_generation_schedules_multi_resource_data_document import PlaylistGenerationSchedulesMultiResourceDataDocument  # noqa: F401
from tidal.models.playlist_generation_schedules_playlist_single_relationship_data_document import PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument  # noqa: F401
from tidal.models.playlist_generation_schedules_single_resource_data_document import PlaylistGenerationSchedulesSingleResourceDataDocument  # noqa: F401
from tidal.models.playlist_generation_schedules_update_operation_payload import PlaylistGenerationSchedulesUpdateOperationPayload  # noqa: F401
from tidal.models.playlist_generation_schedules_update_single_resource_data_document import PlaylistGenerationSchedulesUpdateSingleResourceDataDocument  # noqa: F401


def test_playlist_generation_schedules_get(client: TestClient):
    """Test case for playlist_generation_schedules_get

    Get multiple playlistGenerationSchedules.
    """
    params = [("filter_playlist_id", ['filter_playlist_id_example']),     ("include", ['playlist.items']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'playlist.items')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlistGenerationSchedules",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_generation_schedules_post(client: TestClient):
    """Test case for playlist_generation_schedules_post

    Create single playlistGenerationSchedule.
    """
    playlist_generation_schedules_create_operation_payload = tidal.PlaylistGenerationSchedulesCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/playlistGenerationSchedules",
    #    headers=headers,
    #    json=playlist_generation_schedules_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_generation_schedules_id_get(client: TestClient):
    """Test case for playlist_generation_schedules_id_get

    Get single playlistGenerationSchedule.
    """
    params = [("include", ['playlist.items']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'playlist.items')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlistGenerationSchedules/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_generation_schedules_id_delete(client: TestClient):
    """Test case for playlist_generation_schedules_id_delete

    Delete single playlistGenerationSchedule.
    """

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/playlistGenerationSchedules/{id}".format(id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_generation_schedules_id_patch(client: TestClient):
    """Test case for playlist_generation_schedules_id_patch

    Update single playlistGenerationSchedule.
    """
    playlist_generation_schedules_update_operation_payload = tidal.PlaylistGenerationSchedulesUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/playlistGenerationSchedules/{id}".format(id='id_example'),
    #    headers=headers,
    #    json=playlist_generation_schedules_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_generation_schedules_id_relationships_playlist_get(client: TestClient):
    """Test case for playlist_generation_schedules_id_relationships_playlist_get

    Get playlist relationship (\"to-one\").
    """
    params = [("include", ['playlist.items']),     ("replace_media", 'playlist.items')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlistGenerationSchedules/{id}/relationships/playlist".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

