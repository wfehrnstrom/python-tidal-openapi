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
from tidal.models.offline_tasks_collection_single_relationship_data_document import OfflineTasksCollectionSingleRelationshipDataDocument  # noqa: F401
from tidal.models.offline_tasks_item_single_relationship_data_document import OfflineTasksItemSingleRelationshipDataDocument  # noqa: F401
from tidal.models.offline_tasks_multi_resource_data_document import OfflineTasksMultiResourceDataDocument  # noqa: F401
from tidal.models.offline_tasks_owners_multi_relationship_data_document import OfflineTasksOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.offline_tasks_single_resource_data_document import OfflineTasksSingleResourceDataDocument  # noqa: F401
from tidal.models.offline_tasks_update_operation_payload import OfflineTasksUpdateOperationPayload  # noqa: F401


def test_offline_tasks_get(client: TestClient):
    """Test case for offline_tasks_get

    Get multiple offlineTasks.
    """
    params = [("filter_installation_id", ['filter_installation_id_example']),     ("include", ['collection']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'collection')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/offlineTasks",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_offline_tasks_id_get(client: TestClient):
    """Test case for offline_tasks_id_get

    Get single offlineTask.
    """
    params = [("include", ['collection']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'collection')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/offlineTasks/{id}".format(id='a468bee8-8def-4a1b-8c1e-123456789abc'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_offline_tasks_id_patch(client: TestClient):
    """Test case for offline_tasks_id_patch

    Update single offlineTask.
    """
    offline_tasks_update_operation_payload = tidal.OfflineTasksUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/offlineTasks/{id}".format(id='a468bee8-8def-4a1b-8c1e-123456789abc'),
    #    headers=headers,
    #    json=offline_tasks_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_offline_tasks_id_relationships_collection_get(client: TestClient):
    """Test case for offline_tasks_id_relationships_collection_get

    Get collection relationship (\"to-one\").
    """
    params = [("include", ['collection']),     ("replace_media", 'collection')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/offlineTasks/{id}/relationships/collection".format(id='a468bee8-8def-4a1b-8c1e-123456789abc'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_offline_tasks_id_relationships_item_get(client: TestClient):
    """Test case for offline_tasks_id_relationships_item_get

    Get item relationship (\"to-one\").
    """
    params = [("include", ['item']),     ("replace_media", 'item')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/offlineTasks/{id}/relationships/item".format(id='a468bee8-8def-4a1b-8c1e-123456789abc'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_offline_tasks_id_relationships_owners_get(client: TestClient):
    """Test case for offline_tasks_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/offlineTasks/{id}/relationships/owners".format(id='a468bee8-8def-4a1b-8c1e-123456789abc'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

