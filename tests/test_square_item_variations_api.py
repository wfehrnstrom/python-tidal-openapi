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
from tidal.models.square_item_variations_artworks_multi_relationship_data_document import SquareItemVariationsArtworksMultiRelationshipDataDocument  # noqa: F401
from tidal.models.square_item_variations_artworks_read_multi_data_relationship403_response_body import SquareItemVariationsArtworksReadMultiDataRelationship403ResponseBody  # noqa: F401
from tidal.models.square_item_variations_artworks_read_multi_data_relationship409_response_body import SquareItemVariationsArtworksReadMultiDataRelationship409ResponseBody  # noqa: F401
from tidal.models.square_item_variations_artworks_relationship_update_operation_payload import SquareItemVariationsArtworksRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.square_item_variations_artworks_update_multi_data_relationship403_response_body import SquareItemVariationsArtworksUpdateMultiDataRelationship403ResponseBody  # noqa: F401
from tidal.models.square_item_variations_artworks_update_multi_data_relationship409_response_body import SquareItemVariationsArtworksUpdateMultiDataRelationship409ResponseBody  # noqa: F401
from tidal.models.square_item_variations_artworks_update_multi_data_relationship413_response_body import SquareItemVariationsArtworksUpdateMultiDataRelationship413ResponseBody  # noqa: F401
from tidal.models.square_item_variations_artworks_update_multi_relationship_data_document import SquareItemVariationsArtworksUpdateMultiRelationshipDataDocument  # noqa: F401
from tidal.models.square_item_variations_create_operation_payload import SquareItemVariationsCreateOperationPayload  # noqa: F401
from tidal.models.square_item_variations_create_resource403_response_body import SquareItemVariationsCreateResource403ResponseBody  # noqa: F401
from tidal.models.square_item_variations_create_resource409_response_body import SquareItemVariationsCreateResource409ResponseBody  # noqa: F401
from tidal.models.square_item_variations_create_single_resource_data_document import SquareItemVariationsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.square_item_variations_delete_resource403_response_body import SquareItemVariationsDeleteResource403ResponseBody  # noqa: F401
from tidal.models.square_item_variations_delete_resource409_response_body import SquareItemVariationsDeleteResource409ResponseBody  # noqa: F401
from tidal.models.square_item_variations_owners_multi_relationship_data_document import SquareItemVariationsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.square_item_variations_read_by_id403_response_body import SquareItemVariationsReadById403ResponseBody  # noqa: F401
from tidal.models.square_item_variations_read_by_id409_response_body import SquareItemVariationsReadById409ResponseBody  # noqa: F401
from tidal.models.square_item_variations_single_resource_data_document import SquareItemVariationsSingleResourceDataDocument  # noqa: F401
from tidal.models.square_item_variations_update_operation_payload import SquareItemVariationsUpdateOperationPayload  # noqa: F401
from tidal.models.square_item_variations_update_resource403_response_body import SquareItemVariationsUpdateResource403ResponseBody  # noqa: F401
from tidal.models.square_item_variations_update_resource409_response_body import SquareItemVariationsUpdateResource409ResponseBody  # noqa: F401
from tidal.models.square_item_variations_update_single_resource_data_document import SquareItemVariationsUpdateSingleResourceDataDocument  # noqa: F401


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


def test_square_item_variations_post(client: TestClient):
    """Test case for square_item_variations_post

    Create single squareItemVariation.
    """
    square_item_variations_create_operation_payload = tidal.SquareItemVariationsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/squareItemVariations",
    #    headers=headers,
    #    json=square_item_variations_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_item_variations_id_get(client: TestClient):
    """Test case for square_item_variations_id_get

    Get single squareItemVariation.
    """
    params = [("include", ['artworks']),     ("include_linkage", ['include_linkage_example'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/squareItemVariations/{id}".format(id='p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_item_variations_id_delete(client: TestClient):
    """Test case for square_item_variations_id_delete

    Delete single squareItemVariation.
    """

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/squareItemVariations/{id}".format(id='p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_item_variations_id_patch(client: TestClient):
    """Test case for square_item_variations_id_patch

    Update single squareItemVariation.
    """
    square_item_variations_update_operation_payload = tidal.SquareItemVariationsUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/squareItemVariations/{id}".format(id='p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm'),
    #    headers=headers,
    #    json=square_item_variations_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_item_variations_id_relationships_artworks_get(client: TestClient):
    """Test case for square_item_variations_id_relationships_artworks_get

    Get artworks relationship (\"to-many\").
    """
    params = [("include", ['artworks']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/squareItemVariations/{id}/relationships/artworks".format(id='p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_item_variations_id_relationships_artworks_patch(client: TestClient):
    """Test case for square_item_variations_id_relationships_artworks_patch

    Update artworks relationship (\"to-many\").
    """
    square_item_variations_artworks_relationship_update_operation_payload = tidal.SquareItemVariationsArtworksRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/squareItemVariations/{id}/relationships/artworks".format(id='p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm'),
    #    headers=headers,
    #    json=square_item_variations_artworks_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_item_variations_id_relationships_owners_get(client: TestClient):
    """Test case for square_item_variations_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/squareItemVariations/{id}/relationships/owners".format(id='p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

