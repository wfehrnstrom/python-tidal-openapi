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
from tidal.models.shares_create_operation_payload import SharesCreateOperationPayload  # noqa: F401
from tidal.models.shares_create_single_resource_data_document import SharesCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.shares_multi_resource_data_document import SharesMultiResourceDataDocument  # noqa: F401
from tidal.models.shares_owners_multi_relationship_data_document import SharesOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.shares_shared_resources_multi_relationship_data_document import SharesSharedResourcesMultiRelationshipDataDocument  # noqa: F401
from tidal.models.shares_single_resource_data_document import SharesSingleResourceDataDocument  # noqa: F401
from tidal.models.shares_update_operation_payload import SharesUpdateOperationPayload  # noqa: F401
from tidal.models.shares_update_single_resource_data_document import SharesUpdateSingleResourceDataDocument  # noqa: F401


def test_shares_get(client: TestClient):
    """Test case for shares_get

    Get multiple shares.
    """
    params = [("filter_code", ['filter_code_example']),     ("filter_self_applies_to", 'filter_self_applies_to_example'),     ("include", ['sharedResources']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'sharedResources')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/shares",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_shares_post(client: TestClient):
    """Test case for shares_post

    Create single share.
    """
    shares_create_operation_payload = tidal.SharesCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/shares",
    #    headers=headers,
    #    json=shares_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_shares_id_get(client: TestClient):
    """Test case for shares_id_get

    Get single share.
    """
    params = [("include", ['sharedResources']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'sharedResources')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/shares/{id}".format(id='a468bee88def'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_shares_id_delete(client: TestClient):
    """Test case for shares_id_delete

    Delete single share.
    """
    params = [("revoke_grants", True)]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/shares/{id}".format(id='a468bee88def'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_shares_id_patch(client: TestClient):
    """Test case for shares_id_patch

    Update single share.
    """
    shares_update_operation_payload = tidal.SharesUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/shares/{id}".format(id='a468bee88def'),
    #    headers=headers,
    #    json=shares_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_shares_id_relationships_owners_get(client: TestClient):
    """Test case for shares_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/shares/{id}/relationships/owners".format(id='a468bee88def'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_shares_id_relationships_shared_resources_get(client: TestClient):
    """Test case for shares_id_relationships_shared_resources_get

    Get sharedResources relationship (\"to-many\").
    """
    params = [("include", ['sharedResources']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'sharedResources')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/shares/{id}/relationships/sharedResources".format(id='a468bee88def'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

