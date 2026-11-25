# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field  # noqa: F401
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
from tidal.models.square_sites_items_add_multi_data_relationship403_response_body import SquareSitesItemsAddMultiDataRelationship403ResponseBody  # noqa: F401
from tidal.models.square_sites_items_add_multi_data_relationship409_response_body import SquareSitesItemsAddMultiDataRelationship409ResponseBody  # noqa: F401
from tidal.models.square_sites_items_multi_relationship_data_document import SquareSitesItemsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.square_sites_items_read_multi_data_relationship403_response_body import SquareSitesItemsReadMultiDataRelationship403ResponseBody  # noqa: F401
from tidal.models.square_sites_items_read_multi_data_relationship409_response_body import SquareSitesItemsReadMultiDataRelationship409ResponseBody  # noqa: F401
from tidal.models.square_sites_items_relationship_add_operation_payload import SquareSitesItemsRelationshipAddOperationPayload  # noqa: F401
from tidal.models.square_sites_items_relationship_remove_operation_payload import SquareSitesItemsRelationshipRemoveOperationPayload  # noqa: F401
from tidal.models.square_sites_items_remove_multi_data_relationship403_response_body import SquareSitesItemsRemoveMultiDataRelationship403ResponseBody  # noqa: F401
from tidal.models.square_sites_items_remove_multi_data_relationship409_response_body import SquareSitesItemsRemoveMultiDataRelationship409ResponseBody  # noqa: F401


def test_square_sites_id_relationships_items_get(client: TestClient):
    """Test case for square_sites_id_relationships_items_get

    Get items relationship (\"to-many\").
    """
    params = [("include", ['items']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/squareSites/{id}/relationships/items".format(id='IhETt7taHSVV2MUu9kqjMDengjnhVZa'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_sites_id_relationships_items_post(client: TestClient):
    """Test case for square_sites_id_relationships_items_post

    Add to items relationship (\"to-many\").
    """
    square_sites_items_relationship_add_operation_payload = tidal.SquareSitesItemsRelationshipAddOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/squareSites/{id}/relationships/items".format(id='IhETt7taHSVV2MUu9kqjMDengjnhVZa'),
    #    headers=headers,
    #    json=square_sites_items_relationship_add_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_sites_id_relationships_items_delete(client: TestClient):
    """Test case for square_sites_id_relationships_items_delete

    Delete from items relationship (\"to-many\").
    """
    square_sites_items_relationship_remove_operation_payload = tidal.SquareSitesItemsRelationshipRemoveOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/squareSites/{id}/relationships/items".format(id='IhETt7taHSVV2MUu9kqjMDengjnhVZa'),
    #    headers=headers,
    #    json=square_sites_items_relationship_remove_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

