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
from tidal.models.user_collection_save_for_laters_items_add_multi_data_relationship_with_response409_response_body import UserCollectionSaveForLatersItemsAddMultiDataRelationshipWithResponse409ResponseBody  # noqa: F401
from tidal.models.user_collection_save_for_laters_items_add_multi_relationship_data_document import UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_collection_save_for_laters_items_multi_relationship_data_document import UserCollectionSaveForLatersItemsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_collection_save_for_laters_items_relationship_add_operation_payload import UserCollectionSaveForLatersItemsRelationshipAddOperationPayload  # noqa: F401
from tidal.models.user_collection_save_for_laters_items_relationship_remove_operation_payload import UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayload  # noqa: F401
from tidal.models.user_collection_save_for_laters_owners_multi_relationship_data_document import UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_collection_save_for_laters_single_resource_data_document import UserCollectionSaveForLatersSingleResourceDataDocument  # noqa: F401


def test_user_collection_save_for_laters_id_get(client: TestClient):
    """Test case for user_collection_save_for_laters_id_get

    Get single userCollectionSaveForLater.
    """
    params = [("include", ['items']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'items')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userCollectionSaveForLaters/{id}".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_save_for_laters_id_relationships_items_get(client: TestClient):
    """Test case for user_collection_save_for_laters_id_relationships_items_get

    Get items relationship (\"to-many\").
    """
    params = [("include", ['items']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'items')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userCollectionSaveForLaters/{id}/relationships/items".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_save_for_laters_id_relationships_items_post(client: TestClient):
    """Test case for user_collection_save_for_laters_id_relationships_items_post

    Add to items relationship (\"to-many\").
    """
    user_collection_save_for_laters_items_relationship_add_operation_payload = tidal.UserCollectionSaveForLatersItemsRelationshipAddOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/userCollectionSaveForLaters/{id}/relationships/items".format(id='me'),
    #    headers=headers,
    #    json=user_collection_save_for_laters_items_relationship_add_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_save_for_laters_id_relationships_items_delete(client: TestClient):
    """Test case for user_collection_save_for_laters_id_relationships_items_delete

    Delete from items relationship (\"to-many\").
    """
    user_collection_save_for_laters_items_relationship_remove_operation_payload = tidal.UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/userCollectionSaveForLaters/{id}/relationships/items".format(id='me'),
    #    headers=headers,
    #    json=user_collection_save_for_laters_items_relationship_remove_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_save_for_laters_id_relationships_owners_get(client: TestClient):
    """Test case for user_collection_save_for_laters_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userCollectionSaveForLaters/{id}/relationships/owners".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

