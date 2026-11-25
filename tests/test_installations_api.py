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
from tidal.models.installations_create_operation_payload import InstallationsCreateOperationPayload  # noqa: F401
from tidal.models.installations_create_single_resource_data_document import InstallationsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.installations_multi_resource_data_document import InstallationsMultiResourceDataDocument  # noqa: F401
from tidal.models.installations_offline_inventory_multi_relationship_data_document import InstallationsOfflineInventoryMultiRelationshipDataDocument  # noqa: F401
from tidal.models.installations_offline_inventory_relationship_add_operation_payload import InstallationsOfflineInventoryRelationshipAddOperationPayload  # noqa: F401
from tidal.models.installations_offline_inventory_relationship_remove_operation_payload import InstallationsOfflineInventoryRelationshipRemoveOperationPayload  # noqa: F401
from tidal.models.installations_owners_multi_relationship_data_document import InstallationsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.installations_single_resource_data_document import InstallationsSingleResourceDataDocument  # noqa: F401
from tidal.models.mutation_response_document import MutationResponseDocument  # noqa: F401


def test_installations_get(client: TestClient):
    """Test case for installations_get

    Get multiple installations.
    """
    params = [("filter_client_provided_installation_id", ['filter_client_provided_installation_id_example']),     ("filter_owners_id", ['filter_owners_id_example']),     ("include", ['offlineInventory']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'offlineInventory')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/installations",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_installations_post(client: TestClient):
    """Test case for installations_post

    Create single installation.
    """
    installations_create_operation_payload = tidal.InstallationsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/installations",
    #    headers=headers,
    #    json=installations_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_installations_id_get(client: TestClient):
    """Test case for installations_id_get

    Get single installation.
    """
    params = [("include", ['offlineInventory']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'offlineInventory')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/installations/{id}".format(id='a468bee88def'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_installations_id_relationships_offline_inventory_get(client: TestClient):
    """Test case for installations_id_relationships_offline_inventory_get

    Get offlineInventory relationship (\"to-many\").
    """
    params = [("filter_type", ['filter_type_example']),     ("filter_client_storage_state", ['filter_client_storage_state_example']),     ("filter_id", ['filter_id_example']),     ("include", ['offlineInventory']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'offlineInventory')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/installations/{id}/relationships/offlineInventory".format(id='a468bee88def'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_installations_id_relationships_offline_inventory_post(client: TestClient):
    """Test case for installations_id_relationships_offline_inventory_post

    Add to offlineInventory relationship (\"to-many\").
    """
    installations_offline_inventory_relationship_add_operation_payload = tidal.InstallationsOfflineInventoryRelationshipAddOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/installations/{id}/relationships/offlineInventory".format(id='a468bee88def'),
    #    headers=headers,
    #    json=installations_offline_inventory_relationship_add_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_installations_id_relationships_offline_inventory_delete(client: TestClient):
    """Test case for installations_id_relationships_offline_inventory_delete

    Delete from offlineInventory relationship (\"to-many\").
    """
    installations_offline_inventory_relationship_remove_operation_payload = tidal.InstallationsOfflineInventoryRelationshipRemoveOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/installations/{id}/relationships/offlineInventory".format(id='a468bee88def'),
    #    headers=headers,
    #    json=installations_offline_inventory_relationship_remove_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_installations_id_relationships_owners_get(client: TestClient):
    """Test case for installations_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/installations/{id}/relationships/owners".format(id='a468bee88def'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

