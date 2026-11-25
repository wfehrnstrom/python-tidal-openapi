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
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody  # noqa: F401
from tidal.models.mutation_response_document import MutationResponseDocument  # noqa: F401
from tidal.models.playlist_generations_base_generation_single_relationship_data_document import PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument  # noqa: F401
from tidal.models.playlist_generations_create_operation_payload import PlaylistGenerationsCreateOperationPayload  # noqa: F401
from tidal.models.playlist_generations_create_resource409_response_body import PlaylistGenerationsCreateResource409ResponseBody  # noqa: F401
from tidal.models.playlist_generations_create_single_resource_data_document import PlaylistGenerationsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.playlist_generations_multi_resource_data_document import PlaylistGenerationsMultiResourceDataDocument  # noqa: F401
from tidal.models.playlist_generations_playlist_single_relationship_data_document import PlaylistGenerationsPlaylistSingleRelationshipDataDocument  # noqa: F401
from tidal.models.playlist_generations_single_resource_data_document import PlaylistGenerationsSingleResourceDataDocument  # noqa: F401
from tidal.models.playlist_generations_track_preferences_add_multi_data_relationship_with_response409_response_body import PlaylistGenerationsTrackPreferencesAddMultiDataRelationshipWithResponse409ResponseBody  # noqa: F401
from tidal.models.playlist_generations_track_preferences_add_multi_relationship_data_document import PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocument  # noqa: F401
from tidal.models.playlist_generations_track_preferences_multi_relationship_data_document import PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument  # noqa: F401
from tidal.models.playlist_generations_track_preferences_relationship_add_operation_payload import PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload  # noqa: F401
from tidal.models.playlist_generations_track_preferences_relationship_remove_operation_payload import PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload  # noqa: F401
from tidal.models.playlist_generations_track_preferences_relationship_update_operation_payload import PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.playlist_generations_track_preferences_remove_multi_data_relationship409_response_body import PlaylistGenerationsTrackPreferencesRemoveMultiDataRelationship409ResponseBody  # noqa: F401
from tidal.models.playlist_generations_track_preferences_update_multi_data_relationship409_response_body import PlaylistGenerationsTrackPreferencesUpdateMultiDataRelationship409ResponseBody  # noqa: F401
from tidal.models.playlist_generations_track_preferences_update_multi_relationship_data_document import PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocument  # noqa: F401


def test_playlist_generations_get(client: TestClient):
    """Test case for playlist_generations_get

    Get multiple playlistGenerations.
    """
    params = [("filter_playlist_id", ['filter_playlist_id_example']),     ("generation_view", 'CURRENT'),     ("include", ['baseGeneration.trackPreferences']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'baseGeneration.trackPreferences')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlistGenerations",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_generations_post(client: TestClient):
    """Test case for playlist_generations_post

    Create single playlistGeneration.
    """
    playlist_generations_create_operation_payload = tidal.PlaylistGenerationsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/playlistGenerations",
    #    headers=headers,
    #    json=playlist_generations_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_generations_id_get(client: TestClient):
    """Test case for playlist_generations_id_get

    Get single playlistGeneration.
    """
    params = [("include", ['baseGeneration.trackPreferences']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'baseGeneration.trackPreferences')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlistGenerations/{id}".format(id='10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_generations_id_relationships_base_generation_get(client: TestClient):
    """Test case for playlist_generations_id_relationships_base_generation_get

    Get baseGeneration relationship (\"to-one\").
    """
    params = [("include", ['baseGeneration.trackPreferences']),     ("replace_media", 'baseGeneration.trackPreferences')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlistGenerations/{id}/relationships/baseGeneration".format(id='10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_generations_id_relationships_playlist_get(client: TestClient):
    """Test case for playlist_generations_id_relationships_playlist_get

    Get playlist relationship (\"to-one\").
    """
    params = [("include", ['playlist.items']),     ("replace_media", 'playlist.items')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlistGenerations/{id}/relationships/playlist".format(id='10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_generations_id_relationships_track_preferences_get(client: TestClient):
    """Test case for playlist_generations_id_relationships_track_preferences_get

    Get trackPreferences relationship (\"to-many\").
    """
    params = [("include", ['trackPreferences']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'trackPreferences')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlistGenerations/{id}/relationships/trackPreferences".format(id='10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_generations_id_relationships_track_preferences_post(client: TestClient):
    """Test case for playlist_generations_id_relationships_track_preferences_post

    Add to trackPreferences relationship (\"to-many\").
    """
    playlist_generations_track_preferences_relationship_add_operation_payload = tidal.PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/playlistGenerations/{id}/relationships/trackPreferences".format(id='10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg'),
    #    headers=headers,
    #    json=playlist_generations_track_preferences_relationship_add_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_generations_id_relationships_track_preferences_delete(client: TestClient):
    """Test case for playlist_generations_id_relationships_track_preferences_delete

    Delete from trackPreferences relationship (\"to-many\").
    """
    playlist_generations_track_preferences_relationship_remove_operation_payload = tidal.PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/playlistGenerations/{id}/relationships/trackPreferences".format(id='10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg'),
    #    headers=headers,
    #    json=playlist_generations_track_preferences_relationship_remove_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_generations_id_relationships_track_preferences_patch(client: TestClient):
    """Test case for playlist_generations_id_relationships_track_preferences_patch

    Update trackPreferences relationship (\"to-many\").
    """
    playlist_generations_track_preferences_relationship_update_operation_payload = tidal.PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/playlistGenerations/{id}/relationships/trackPreferences".format(id='10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg'),
    #    headers=headers,
    #    json=playlist_generations_track_preferences_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

