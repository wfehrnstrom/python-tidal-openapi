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
from tidal.models.folder_items_breadcrumb_multi_relationship_data_document import FolderItemsBreadcrumbMultiRelationshipDataDocument  # noqa: F401
from tidal.models.folder_items_create_operation_payload import FolderItemsCreateOperationPayload  # noqa: F401
from tidal.models.folder_items_create_resource400_response_body import FolderItemsCreateResource400ResponseBody  # noqa: F401
from tidal.models.folder_items_create_single_resource_data_document import FolderItemsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.folder_items_multi_resource_data_document import FolderItemsMultiResourceDataDocument  # noqa: F401
from tidal.models.folder_items_owners_multi_relationship_data_document import FolderItemsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.folder_items_parent_relationship_update_operation_payload import FolderItemsParentRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.folder_items_parent_single_relationship_data_document import FolderItemsParentSingleRelationshipDataDocument  # noqa: F401
from tidal.models.folder_items_parent_update_single_data_relationship400_response_body import FolderItemsParentUpdateSingleDataRelationship400ResponseBody  # noqa: F401
from tidal.models.folder_items_parent_update_single_relationship_data_document import FolderItemsParentUpdateSingleRelationshipDataDocument  # noqa: F401
from tidal.models.folder_items_sharing_summary_single_relationship_data_document import FolderItemsSharingSummarySingleRelationshipDataDocument  # noqa: F401
from tidal.models.folder_items_single_resource_data_document import FolderItemsSingleResourceDataDocument  # noqa: F401
from tidal.models.folder_items_subject_single_relationship_data_document import FolderItemsSubjectSingleRelationshipDataDocument  # noqa: F401
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody  # noqa: F401
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody  # noqa: F401
from tidal.models.mutation_response_document import MutationResponseDocument  # noqa: F401


def test_folder_items_get(client: TestClient):
    """Test case for folder_items_get

    Get multiple folderItems.
    """
    params = [("filter_parent_id", 'filter_parent_id_example'),     ("filter_parent_is_root", 'filter_parent_is_root_example'),     ("filter_parent_owners_id", 'filter_parent_owners_id_example'),     ("filter_self_matches_query", 'filter_self_matches_query_example'),     ("filter_subject_albums_published", 'filter_subject_albums_published_example'),     ("filter_subject_owners_id", 'filter_subject_owners_id_example'),     ("filter_subject_owners_id_ne", 'filter_subject_owners_id_ne_example'),     ("include", ['breadcrumb.children.subject']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'breadcrumb.children.subject'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folderItems",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_items_post(client: TestClient):
    """Test case for folder_items_post

    Create single folderItem.
    """
    folder_items_create_operation_payload = tidal.FolderItemsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/folderItems",
    #    headers=headers,
    #    json=folder_items_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_items_id_get(client: TestClient):
    """Test case for folder_items_id_get

    Get single folderItem.
    """
    params = [("include", ['breadcrumb.children.subject']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'breadcrumb.children.subject'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folderItems/{id}".format(id='e3226624-355b-48f8-aa93-db42532caa66'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_items_id_delete(client: TestClient):
    """Test case for folder_items_id_delete

    Delete single folderItem.
    """
    params = [("share_code", 'xyz')]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/folderItems/{id}".format(id='e3226624-355b-48f8-aa93-db42532caa66'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_items_id_relationships_breadcrumb_get(client: TestClient):
    """Test case for folder_items_id_relationships_breadcrumb_get

    Get breadcrumb relationship (\"to-many\").
    """
    params = [("include", ['breadcrumb.children.subject']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'breadcrumb.children.subject'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folderItems/{id}/relationships/breadcrumb".format(id='e3226624-355b-48f8-aa93-db42532caa66'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_items_id_relationships_owners_get(client: TestClient):
    """Test case for folder_items_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folderItems/{id}/relationships/owners".format(id='e3226624-355b-48f8-aa93-db42532caa66'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_items_id_relationships_parent_get(client: TestClient):
    """Test case for folder_items_id_relationships_parent_get

    Get parent relationship (\"to-one\").
    """
    params = [("include", ['parent.children.subject']),     ("replace_media", 'parent.children.subject'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folderItems/{id}/relationships/parent".format(id='e3226624-355b-48f8-aa93-db42532caa66'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_items_id_relationships_parent_patch(client: TestClient):
    """Test case for folder_items_id_relationships_parent_patch

    Update parent relationship (\"to-one\").
    """
    folder_items_parent_relationship_update_operation_payload = tidal.FolderItemsParentRelationshipUpdateOperationPayload()
    params = [("share_code", 'xyz')]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/folderItems/{id}/relationships/parent".format(id='e3226624-355b-48f8-aa93-db42532caa66'),
    #    headers=headers,
    #    json=folder_items_parent_relationship_update_operation_payload,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_items_id_relationships_sharing_summary_get(client: TestClient):
    """Test case for folder_items_id_relationships_sharing_summary_get

    Get sharingSummary relationship (\"to-one\").
    """
    params = [("include", ['sharingSummary.subject']),     ("replace_media", 'sharingSummary.subject'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folderItems/{id}/relationships/sharingSummary".format(id='e3226624-355b-48f8-aa93-db42532caa66'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_items_id_relationships_subject_get(client: TestClient):
    """Test case for folder_items_id_relationships_subject_get

    Get subject relationship (\"to-one\").
    """
    params = [("include", ['subject']),     ("replace_media", 'subject'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folderItems/{id}/relationships/subject".format(id='e3226624-355b-48f8-aa93-db42532caa66'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

