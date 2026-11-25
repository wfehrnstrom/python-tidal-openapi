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
from tidal.models.user_collection_folders_create_operation_payload import UserCollectionFoldersCreateOperationPayload  # noqa: F401
from tidal.models.user_collection_folders_create_single_resource_data_document import UserCollectionFoldersCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.user_collection_folders_delete_resource400_response_body import UserCollectionFoldersDeleteResource400ResponseBody  # noqa: F401
from tidal.models.user_collection_folders_items_multi_relationship_data_document import UserCollectionFoldersItemsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_collection_folders_items_relationship_add_operation_payload import UserCollectionFoldersItemsRelationshipAddOperationPayload  # noqa: F401
from tidal.models.user_collection_folders_items_relationship_remove_operation_payload import UserCollectionFoldersItemsRelationshipRemoveOperationPayload  # noqa: F401
from tidal.models.user_collection_folders_multi_resource_data_document import UserCollectionFoldersMultiResourceDataDocument  # noqa: F401
from tidal.models.user_collection_folders_owners_multi_relationship_data_document import UserCollectionFoldersOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_collection_folders_single_resource_data_document import UserCollectionFoldersSingleResourceDataDocument  # noqa: F401
from tidal.models.user_collection_folders_update_operation_payload import UserCollectionFoldersUpdateOperationPayload  # noqa: F401
from tidal.models.user_collection_folders_user_collection_single_relationship_data_document import UserCollectionFoldersUserCollectionSingleRelationshipDataDocument  # noqa: F401


def test_user_collection_folders_get(client: TestClient):
    """Test case for user_collection_folders_get

    Get multiple userCollectionFolders.
    """
    params = [("filter_id", ['filter_id_example']),     ("include", ['items.items']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'items.items')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userCollectionFolders",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_folders_post(client: TestClient):
    """Test case for user_collection_folders_post

    Create single userCollectionFolder.
    """
    user_collection_folders_create_operation_payload = tidal.UserCollectionFoldersCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/userCollectionFolders",
    #    headers=headers,
    #    json=user_collection_folders_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_folders_id_get(client: TestClient):
    """Test case for user_collection_folders_id_get

    Get single userCollectionFolder.
    """
    params = [("include", ['items.items']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'items.items')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userCollectionFolders/{id}".format(id='CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_folders_id_delete(client: TestClient):
    """Test case for user_collection_folders_id_delete

    Delete single userCollectionFolder.
    """

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/userCollectionFolders/{id}".format(id='CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_folders_id_patch(client: TestClient):
    """Test case for user_collection_folders_id_patch

    Update single userCollectionFolder.
    """
    user_collection_folders_update_operation_payload = tidal.UserCollectionFoldersUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/userCollectionFolders/{id}".format(id='CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX'),
    #    headers=headers,
    #    json=user_collection_folders_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_folders_id_relationships_items_get(client: TestClient):
    """Test case for user_collection_folders_id_relationships_items_get

    Get items relationship (\"to-many\").
    """
    params = [("include", ['items.items']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'items.items'),     ("sort", ['sort_example'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userCollectionFolders/{id}/relationships/items".format(id='CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_folders_id_relationships_items_post(client: TestClient):
    """Test case for user_collection_folders_id_relationships_items_post

    Add to items relationship (\"to-many\").
    """
    user_collection_folders_items_relationship_add_operation_payload = tidal.UserCollectionFoldersItemsRelationshipAddOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/userCollectionFolders/{id}/relationships/items".format(id='CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX'),
    #    headers=headers,
    #    json=user_collection_folders_items_relationship_add_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_folders_id_relationships_items_delete(client: TestClient):
    """Test case for user_collection_folders_id_relationships_items_delete

    Delete from items relationship (\"to-many\").
    """
    user_collection_folders_items_relationship_remove_operation_payload = tidal.UserCollectionFoldersItemsRelationshipRemoveOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/userCollectionFolders/{id}/relationships/items".format(id='CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX'),
    #    headers=headers,
    #    json=user_collection_folders_items_relationship_remove_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_folders_id_relationships_owners_get(client: TestClient):
    """Test case for user_collection_folders_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userCollectionFolders/{id}/relationships/owners".format(id='CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_folders_id_relationships_user_collection_get(client: TestClient):
    """Test case for user_collection_folders_id_relationships_user_collection_get

    Get userCollection relationship (\"to-one\").
    """
    params = [("include", ['userCollection.items.items']),     ("replace_media", 'userCollection.items.items')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userCollectionFolders/{id}/relationships/userCollection".format(id='CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

