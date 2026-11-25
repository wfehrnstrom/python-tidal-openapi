# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.clients_certificates_multi_relationship_data_document import ClientsCertificatesMultiRelationshipDataDocument  # noqa: F401
from tidal.models.clients_create_operation_payload import ClientsCreateOperationPayload  # noqa: F401
from tidal.models.clients_create_single_resource_data_document import ClientsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.clients_multi_resource_data_document import ClientsMultiResourceDataDocument  # noqa: F401
from tidal.models.clients_owners_multi_relationship_data_document import ClientsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.clients_single_resource_data_document import ClientsSingleResourceDataDocument  # noqa: F401
from tidal.models.clients_update_operation_payload import ClientsUpdateOperationPayload  # noqa: F401
from tidal.models.clients_update_single_resource_data_document import ClientsUpdateSingleResourceDataDocument  # noqa: F401
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


def test_clients_get(client: TestClient):
    """Test case for clients_get

    Get multiple clients.
    """
    params = [("filter_owners_id", ['filter_owners_id_example']),     ("include", ['certificates']),     ("include_linkage", ['include_linkage_example'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/clients",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_clients_post(client: TestClient):
    """Test case for clients_post

    Create single client.
    """
    clients_create_operation_payload = tidal.ClientsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/clients",
    #    headers=headers,
    #    json=clients_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_clients_id_get(client: TestClient):
    """Test case for clients_id_get

    Get single client.
    """
    params = [("include", ['certificates']),     ("include_linkage", ['include_linkage_example'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/clients/{id}".format(id='a468bee88def'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_clients_id_delete(client: TestClient):
    """Test case for clients_id_delete

    Delete single client.
    """

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/clients/{id}".format(id='a468bee88def'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_clients_id_patch(client: TestClient):
    """Test case for clients_id_patch

    Update single client.
    """
    clients_update_operation_payload = tidal.ClientsUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/clients/{id}".format(id='a468bee88def'),
    #    headers=headers,
    #    json=clients_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_clients_id_relationships_certificates_get(client: TestClient):
    """Test case for clients_id_relationships_certificates_get

    Get certificates relationship (\"to-many\").
    """
    params = [("include", ['certificates']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/clients/{id}/relationships/certificates".format(id='a468bee88def'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_clients_id_relationships_owners_get(client: TestClient):
    """Test case for clients_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/clients/{id}/relationships/owners".format(id='a468bee88def'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

