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
from tidal.models.square_connections_create_operation_payload import SquareConnectionsCreateOperationPayload  # noqa: F401
from tidal.models.square_connections_create_single_resource_data_document import SquareConnectionsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.square_connections_read_by_id403_response_body import SquareConnectionsReadById403ResponseBody  # noqa: F401
from tidal.models.square_connections_selected_site_read_single_data_relationship403_response_body import SquareConnectionsSelectedSiteReadSingleDataRelationship403ResponseBody  # noqa: F401
from tidal.models.square_connections_selected_site_relationship_update_operation_payload import SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.square_connections_selected_site_single_relationship_data_document import SquareConnectionsSelectedSiteSingleRelationshipDataDocument  # noqa: F401
from tidal.models.square_connections_selected_site_update_single_data_relationship403_response_body import SquareConnectionsSelectedSiteUpdateSingleDataRelationship403ResponseBody  # noqa: F401
from tidal.models.square_connections_selected_site_update_single_data_relationship409_response_body import SquareConnectionsSelectedSiteUpdateSingleDataRelationship409ResponseBody  # noqa: F401
from tidal.models.square_connections_selected_site_update_single_relationship_data_document import SquareConnectionsSelectedSiteUpdateSingleRelationshipDataDocument  # noqa: F401
from tidal.models.square_connections_single_resource_data_document import SquareConnectionsSingleResourceDataDocument  # noqa: F401
from tidal.models.square_connections_sites_multi_relationship_data_document import SquareConnectionsSitesMultiRelationshipDataDocument  # noqa: F401
from tidal.models.square_connections_sites_read_multi_data_relationship403_response_body import SquareConnectionsSitesReadMultiDataRelationship403ResponseBody  # noqa: F401


def test_square_connections_post(client: TestClient):
    """Test case for square_connections_post

    Create single squareConnection.
    """
    square_connections_create_operation_payload = tidal.SquareConnectionsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/squareConnections",
    #    headers=headers,
    #    json=square_connections_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_connections_id_get(client: TestClient):
    """Test case for square_connections_id_get

    Get single squareConnection.
    """
    params = [("include", ['selectedSite']),     ("include_linkage", ['include_linkage_example'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/squareConnections/{id}".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_connections_id_relationships_selected_site_get(client: TestClient):
    """Test case for square_connections_id_relationships_selected_site_get

    Get selectedSite relationship (\"to-one\").
    """
    params = [("include", ['selectedSite'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/squareConnections/{id}/relationships/selectedSite".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_connections_id_relationships_selected_site_patch(client: TestClient):
    """Test case for square_connections_id_relationships_selected_site_patch

    Update selectedSite relationship (\"to-one\").
    """
    square_connections_selected_site_relationship_update_operation_payload = tidal.SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/squareConnections/{id}/relationships/selectedSite".format(id='me'),
    #    headers=headers,
    #    json=square_connections_selected_site_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_square_connections_id_relationships_sites_get(client: TestClient):
    """Test case for square_connections_id_relationships_sites_get

    Get sites relationship (\"to-many\").
    """
    params = [("include", ['sites']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/squareConnections/{id}/relationships/sites".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

