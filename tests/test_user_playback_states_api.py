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
from tidal.models.user_playback_states_active_player_relationship_update_operation_payload import UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.user_playback_states_active_player_single_relationship_data_document import UserPlaybackStatesActivePlayerSingleRelationshipDataDocument  # noqa: F401
from tidal.models.user_playback_states_active_player_update_single_relationship_data_document import UserPlaybackStatesActivePlayerUpdateSingleRelationshipDataDocument  # noqa: F401
from tidal.models.user_playback_states_available_players_add_multi_relationship_data_document import UserPlaybackStatesAvailablePlayersAddMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_playback_states_available_players_multi_relationship_data_document import UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_playback_states_available_players_relationship_add_operation_payload import UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload  # noqa: F401
from tidal.models.user_playback_states_available_players_relationship_remove_operation_payload import UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload  # noqa: F401
from tidal.models.user_playback_states_change_event_stream_single_relationship_data_document import UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument  # noqa: F401
from tidal.models.user_playback_states_play_queue_relationship_update_operation_payload import UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.user_playback_states_play_queue_single_relationship_data_document import UserPlaybackStatesPlayQueueSingleRelationshipDataDocument  # noqa: F401
from tidal.models.user_playback_states_play_queue_update_single_relationship_data_document import UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument  # noqa: F401
from tidal.models.user_playback_states_single_resource_data_document import UserPlaybackStatesSingleResourceDataDocument  # noqa: F401
from tidal.models.user_playback_states_update_operation_payload import UserPlaybackStatesUpdateOperationPayload  # noqa: F401
from tidal.models.user_playback_states_update_single_resource_data_document import UserPlaybackStatesUpdateSingleResourceDataDocument  # noqa: F401


def test_user_playback_states_id_get(client: TestClient):
    """Test case for user_playback_states_id_get

    Get single userPlaybackState.
    """
    params = [("include", ['activePlayer.offlineInventory']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'activePlayer.offlineInventory')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userPlaybackStates/{id}".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_playback_states_id_patch(client: TestClient):
    """Test case for user_playback_states_id_patch

    Update single userPlaybackState.
    """
    user_playback_states_update_operation_payload = tidal.UserPlaybackStatesUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/userPlaybackStates/{id}".format(id='me'),
    #    headers=headers,
    #    json=user_playback_states_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_playback_states_id_relationships_active_player_get(client: TestClient):
    """Test case for user_playback_states_id_relationships_active_player_get

    Get activePlayer relationship (\"to-one\").
    """
    params = [("include", ['activePlayer.offlineInventory']),     ("replace_media", 'activePlayer.offlineInventory')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userPlaybackStates/{id}/relationships/activePlayer".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_playback_states_id_relationships_active_player_patch(client: TestClient):
    """Test case for user_playback_states_id_relationships_active_player_patch

    Update activePlayer relationship (\"to-one\").
    """
    user_playback_states_active_player_relationship_update_operation_payload = tidal.UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/userPlaybackStates/{id}/relationships/activePlayer".format(id='me'),
    #    headers=headers,
    #    json=user_playback_states_active_player_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_playback_states_id_relationships_available_players_get(client: TestClient):
    """Test case for user_playback_states_id_relationships_available_players_get

    Get availablePlayers relationship (\"to-many\").
    """
    params = [("include", ['availablePlayers.offlineInventory']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'availablePlayers.offlineInventory')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userPlaybackStates/{id}/relationships/availablePlayers".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_playback_states_id_relationships_available_players_post(client: TestClient):
    """Test case for user_playback_states_id_relationships_available_players_post

    Add to availablePlayers relationship (\"to-many\").
    """
    user_playback_states_available_players_relationship_add_operation_payload = tidal.UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/userPlaybackStates/{id}/relationships/availablePlayers".format(id='me'),
    #    headers=headers,
    #    json=user_playback_states_available_players_relationship_add_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_playback_states_id_relationships_available_players_delete(client: TestClient):
    """Test case for user_playback_states_id_relationships_available_players_delete

    Delete from availablePlayers relationship (\"to-many\").
    """
    user_playback_states_available_players_relationship_remove_operation_payload = tidal.UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/userPlaybackStates/{id}/relationships/availablePlayers".format(id='me'),
    #    headers=headers,
    #    json=user_playback_states_available_players_relationship_remove_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_playback_states_id_relationships_change_event_stream_get(client: TestClient):
    """Test case for user_playback_states_id_relationships_change_event_stream_get

    Get changeEventStream relationship (\"to-one\").
    """
    params = [("include", ['changeEventStream'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userPlaybackStates/{id}/relationships/changeEventStream".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_playback_states_id_relationships_play_queue_get(client: TestClient):
    """Test case for user_playback_states_id_relationships_play_queue_get

    Get playQueue relationship (\"to-one\").
    """
    params = [("include", ['playQueue.current']),     ("replace_media", 'playQueue.current')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userPlaybackStates/{id}/relationships/playQueue".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_playback_states_id_relationships_play_queue_patch(client: TestClient):
    """Test case for user_playback_states_id_relationships_play_queue_patch

    Update playQueue relationship (\"to-one\").
    """
    user_playback_states_play_queue_relationship_update_operation_payload = tidal.UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/userPlaybackStates/{id}/relationships/playQueue".format(id='me'),
    #    headers=headers,
    #    json=user_playback_states_play_queue_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

