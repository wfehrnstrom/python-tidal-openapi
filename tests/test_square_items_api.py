# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.atomic_operations400_response_body import AtomicOperations400ResponseBody  # noqa: F401
from tidal.models.atomic_operations403_response_body import AtomicOperations403ResponseBody  # noqa: F401
from tidal.models.atomic_operations404_response_body import AtomicOperations404ResponseBody  # noqa: F401
from tidal.models.atomic_operations405_response_body import AtomicOperations405ResponseBody  # noqa: F401
from tidal.models.atomic_operations406_response_body import AtomicOperations406ResponseBody  # noqa: F401
from tidal.models.atomic_operations409_response_body import AtomicOperations409ResponseBody  # noqa: F401
from tidal.models.atomic_operations415_response_body import AtomicOperations415ResponseBody  # noqa: F401
from tidal.models.atomic_operations422_response_body import AtomicOperations422ResponseBody  # noqa: F401
from tidal.models.atomic_operations429_response_body import AtomicOperations429ResponseBody  # noqa: F401
from tidal.models.atomic_operations500_response_body import AtomicOperations500ResponseBody  # noqa: F401
from tidal.models.atomic_operations503_response_body import AtomicOperations503ResponseBody  # noqa: F401
from tidal.models.atomic_operations_request import AtomicOperationsRequest  # noqa: F401
from tidal.models.atomic_operations_response import AtomicOperationsResponse  # noqa: F401
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
from tidal.models.square_items_artworks_multi_relationship_data_document import SquareItemsArtworksMultiRelationshipDataDocument  # noqa: F401
from tidal.models.square_items_artworks_read_multi_data_relationship409_response_body import SquareItemsArtworksReadMultiDataRelationship409ResponseBody  # noqa: F401
from tidal.models.square_items_artworks_relationship_update_operation_payload import SquareItemsArtworksRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.square_items_artworks_update_multi_data_relationship403_response_body import SquareItemsArtworksUpdateMultiDataRelationship403ResponseBody  # noqa: F401
from tidal.models.square_items_artworks_update_multi_data_relationship409_response_body import SquareItemsArtworksUpdateMultiDataRelationship409ResponseBody  # noqa: F401
from tidal.models.square_items_artworks_update_multi_data_relationship413_response_body import SquareItemsArtworksUpdateMultiDataRelationship413ResponseBody  # noqa: F401
from tidal.models.square_items_artworks_update_multi_relationship_data_document import SquareItemsArtworksUpdateMultiRelationshipDataDocument  # noqa: F401
from tidal.models.square_items_delete_resource403_response_body import SquareItemsDeleteResource403ResponseBody  # noqa: F401
from tidal.models.square_items_delete_resource409_response_body import SquareItemsDeleteResource409ResponseBody  # noqa: F401
from tidal.models.square_items_multi_resource_data_document import SquareItemsMultiResourceDataDocument  # noqa: F401
from tidal.models.square_items_owners_multi_relationship_data_document import SquareItemsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.square_items_read_by_filter403_response_body import SquareItemsReadByFilter403ResponseBody  # noqa: F401
from tidal.models.square_items_read_by_filter409_response_body import SquareItemsReadByFilter409ResponseBody  # noqa: F401
from tidal.models.square_items_read_by_id403_response_body import SquareItemsReadById403ResponseBody  # noqa: F401
from tidal.models.square_items_read_by_id409_response_body import SquareItemsReadById409ResponseBody  # noqa: F401
from tidal.models.square_items_single_resource_data_document import SquareItemsSingleResourceDataDocument  # noqa: F401
from tidal.models.square_items_update_operation_payload import SquareItemsUpdateOperationPayload  # noqa: F401
from tidal.models.square_items_update_resource403_response_body import SquareItemsUpdateResource403ResponseBody  # noqa: F401
from tidal.models.square_items_update_resource409_response_body import SquareItemsUpdateResource409ResponseBody  # noqa: F401
from tidal.models.square_items_update_single_resource_data_document import SquareItemsUpdateSingleResourceDataDocument  # noqa: F401
from tidal.models.square_items_variations_multi_relationship_data_document import SquareItemsVariationsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.square_items_variations_read_multi_data_relationship403_response_body import SquareItemsVariationsReadMultiDataRelationship403ResponseBody  # noqa: F401
from tidal.models.square_items_variations_read_multi_data_relationship409_response_body import SquareItemsVariationsReadMultiDataRelationship409ResponseBody  # noqa: F401
from tidal.models.square_items_variations_relationship_update_operation_payload import SquareItemsVariationsRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.square_items_variations_update_multi_data_relationship403_response_body import SquareItemsVariationsUpdateMultiDataRelationship403ResponseBody  # noqa: F401
from tidal.models.square_items_variations_update_multi_data_relationship409_response_body import SquareItemsVariationsUpdateMultiDataRelationship409ResponseBody  # noqa: F401
from tidal.models.square_items_variations_update_multi_relationship_data_document import SquareItemsVariationsUpdateMultiRelationshipDataDocument  # noqa: F401


def test_operations_post(client: TestClient):
    """Test case for operations_post

    Commit atomic resource operations
    """
    atomic_operations_request = tidal.AtomicOperationsRequest()

    headers = {
        "idempotency_key": 'idempotency_key_example',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/operations",
    #    headers=headers,
    #    json=atomic_operations_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_items_get(client: TestClient):
    """Test case for square_items_get

    Get multiple squareItems.
    """
    params = [("filter_owners_id", ['filter_owners_id_example']),     ("filter_origin", 'filter_origin_example'),     ("filter_self_matches_query", 'filter_self_matches_query_example'),     ("include", ['artworks']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/squareItems",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_items_id_get(client: TestClient):
    """Test case for square_items_id_get

    Get single squareItem.
    """
    params = [("include", ['artworks']),     ("include_linkage", ['include_linkage_example'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/squareItems/{id}".format(id='p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_items_id_delete(client: TestClient):
    """Test case for square_items_id_delete

    Delete single squareItem.
    """

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/squareItems/{id}".format(id='p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_items_id_patch(client: TestClient):
    """Test case for square_items_id_patch

    Update single squareItem.
    """
    square_items_update_operation_payload = tidal.SquareItemsUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/squareItems/{id}".format(id='p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay'),
    #    headers=headers,
    #    json=square_items_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_items_id_relationships_artworks_get(client: TestClient):
    """Test case for square_items_id_relationships_artworks_get

    Get artworks relationship (\"to-many\").
    """
    params = [("include", ['artworks']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/squareItems/{id}/relationships/artworks".format(id='p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_items_id_relationships_artworks_patch(client: TestClient):
    """Test case for square_items_id_relationships_artworks_patch

    Update artworks relationship (\"to-many\").
    """
    square_items_artworks_relationship_update_operation_payload = tidal.SquareItemsArtworksRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/squareItems/{id}/relationships/artworks".format(id='p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay'),
    #    headers=headers,
    #    json=square_items_artworks_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_items_id_relationships_owners_get(client: TestClient):
    """Test case for square_items_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/squareItems/{id}/relationships/owners".format(id='p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_items_id_relationships_variations_get(client: TestClient):
    """Test case for square_items_id_relationships_variations_get

    Get variations relationship (\"to-many\").
    """
    params = [("include", ['variations']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/squareItems/{id}/relationships/variations".format(id='p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_items_id_relationships_variations_patch(client: TestClient):
    """Test case for square_items_id_relationships_variations_patch

    Update variations relationship (\"to-many\").
    """
    square_items_variations_relationship_update_operation_payload = tidal.SquareItemsVariationsRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/squareItems/{id}/relationships/variations".format(id='p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay'),
    #    headers=headers,
    #    json=square_items_variations_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

