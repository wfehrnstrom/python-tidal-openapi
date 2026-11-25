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
from tidal.models.play_queues_change_event_stream_single_relationship_data_document import PlayQueuesChangeEventStreamSingleRelationshipDataDocument  # noqa: F401
from tidal.models.play_queues_create_operation_payload import PlayQueuesCreateOperationPayload  # noqa: F401
from tidal.models.play_queues_create_single_resource_data_document import PlayQueuesCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.play_queues_current_relationship_update_operation_payload import PlayQueuesCurrentRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.play_queues_current_single_relationship_data_document import PlayQueuesCurrentSingleRelationshipDataDocument  # noqa: F401
from tidal.models.play_queues_current_update_single_relationship_data_document import PlayQueuesCurrentUpdateSingleRelationshipDataDocument  # noqa: F401
from tidal.models.play_queues_future_add_multi_relationship_data_document import PlayQueuesFutureAddMultiRelationshipDataDocument  # noqa: F401
from tidal.models.play_queues_future_multi_relationship_data_document import PlayQueuesFutureMultiRelationshipDataDocument  # noqa: F401
from tidal.models.play_queues_future_relationship_add_operation_payload import PlayQueuesFutureRelationshipAddOperationPayload  # noqa: F401
from tidal.models.play_queues_future_relationship_remove_operation_payload import PlayQueuesFutureRelationshipRemoveOperationPayload  # noqa: F401
from tidal.models.play_queues_future_relationship_update_operation_payload import PlayQueuesFutureRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.play_queues_future_update_multi_relationship_data_document import PlayQueuesFutureUpdateMultiRelationshipDataDocument  # noqa: F401
from tidal.models.play_queues_multi_resource_data_document import PlayQueuesMultiResourceDataDocument  # noqa: F401
from tidal.models.play_queues_owners_multi_relationship_data_document import PlayQueuesOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.play_queues_past_multi_relationship_data_document import PlayQueuesPastMultiRelationshipDataDocument  # noqa: F401
from tidal.models.play_queues_single_resource_data_document import PlayQueuesSingleResourceDataDocument  # noqa: F401
from tidal.models.play_queues_update_operation_payload import PlayQueuesUpdateOperationPayload  # noqa: F401
from tidal.models.play_queues_update_single_resource_data_document import PlayQueuesUpdateSingleResourceDataDocument  # noqa: F401


def test_play_queues_get(client: TestClient):
    """Test case for play_queues_get

    Get multiple playQueues.
    """
    params = [("filter_owners_id", ['filter_owners_id_example']),     ("include", ['current']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'current')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playQueues",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_play_queues_post(client: TestClient):
    """Test case for play_queues_post

    Create single playQueue.
    """
    play_queues_create_operation_payload = tidal.PlayQueuesCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/playQueues",
    #    headers=headers,
    #    json=play_queues_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_play_queues_id_get(client: TestClient):
    """Test case for play_queues_id_get

    Get single playQueue.
    """
    params = [("include", ['current']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'current')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playQueues/{id}".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_play_queues_id_delete(client: TestClient):
    """Test case for play_queues_id_delete

    Delete single playQueue.
    """

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/playQueues/{id}".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_play_queues_id_patch(client: TestClient):
    """Test case for play_queues_id_patch

    Update single playQueue.
    """
    play_queues_update_operation_payload = tidal.PlayQueuesUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/playQueues/{id}".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    json=play_queues_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_play_queues_id_relationships_change_event_stream_get(client: TestClient):
    """Test case for play_queues_id_relationships_change_event_stream_get

    Get changeEventStream relationship (\"to-one\").
    """
    params = [("include", ['changeEventStream'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playQueues/{id}/relationships/changeEventStream".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_play_queues_id_relationships_current_get(client: TestClient):
    """Test case for play_queues_id_relationships_current_get

    Get current relationship (\"to-one\").
    """
    params = [("include", ['current']),     ("replace_media", 'current')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playQueues/{id}/relationships/current".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_play_queues_id_relationships_current_patch(client: TestClient):
    """Test case for play_queues_id_relationships_current_patch

    Update current relationship (\"to-one\").
    """
    play_queues_current_relationship_update_operation_payload = tidal.PlayQueuesCurrentRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/playQueues/{id}/relationships/current".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    json=play_queues_current_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_play_queues_id_relationships_future_get(client: TestClient):
    """Test case for play_queues_id_relationships_future_get

    Get future relationship (\"to-many\").
    """
    params = [("include", ['future']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'future')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playQueues/{id}/relationships/future".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_play_queues_id_relationships_future_post(client: TestClient):
    """Test case for play_queues_id_relationships_future_post

    Add to future relationship (\"to-many\").
    """
    play_queues_future_relationship_add_operation_payload = tidal.PlayQueuesFutureRelationshipAddOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/playQueues/{id}/relationships/future".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    json=play_queues_future_relationship_add_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_play_queues_id_relationships_future_delete(client: TestClient):
    """Test case for play_queues_id_relationships_future_delete

    Delete from future relationship (\"to-many\").
    """
    play_queues_future_relationship_remove_operation_payload = tidal.PlayQueuesFutureRelationshipRemoveOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/playQueues/{id}/relationships/future".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    json=play_queues_future_relationship_remove_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_play_queues_id_relationships_future_patch(client: TestClient):
    """Test case for play_queues_id_relationships_future_patch

    Update future relationship (\"to-many\").
    """
    play_queues_future_relationship_update_operation_payload = tidal.PlayQueuesFutureRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/playQueues/{id}/relationships/future".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    json=play_queues_future_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_play_queues_id_relationships_owners_get(client: TestClient):
    """Test case for play_queues_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playQueues/{id}/relationships/owners".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_play_queues_id_relationships_past_get(client: TestClient):
    """Test case for play_queues_id_relationships_past_get

    Get past relationship (\"to-many\").
    """
    params = [("include", ['past']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'past')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playQueues/{id}/relationships/past".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

