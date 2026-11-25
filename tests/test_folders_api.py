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
from tidal.models.folders_children_multi_relationship_data_document import FoldersChildrenMultiRelationshipDataDocument  # noqa: F401
from tidal.models.folders_create_operation_payload import FoldersCreateOperationPayload  # noqa: F401
from tidal.models.folders_create_single_resource_data_document import FoldersCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.folders_delete_resource400_response_body import FoldersDeleteResource400ResponseBody  # noqa: F401
from tidal.models.folders_multi_resource_data_document import FoldersMultiResourceDataDocument  # noqa: F401
from tidal.models.folders_owners_multi_relationship_data_document import FoldersOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.folders_parent_single_relationship_data_document import FoldersParentSingleRelationshipDataDocument  # noqa: F401
from tidal.models.folders_preview_multi_relationship_data_document import FoldersPreviewMultiRelationshipDataDocument  # noqa: F401
from tidal.models.folders_single_resource_data_document import FoldersSingleResourceDataDocument  # noqa: F401
from tidal.models.folders_update_operation_payload import FoldersUpdateOperationPayload  # noqa: F401
from tidal.models.folders_update_resource400_response_body import FoldersUpdateResource400ResponseBody  # noqa: F401
from tidal.models.folders_update_single_resource_data_document import FoldersUpdateSingleResourceDataDocument  # noqa: F401
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody  # noqa: F401
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody  # noqa: F401
from tidal.models.mutation_response_document import MutationResponseDocument  # noqa: F401


def test_folders_get(client: TestClient):
    """Test case for folders_get

    Get multiple folders.
    """
    params = [("filter_id", ['filter_id_example']),     ("include", ['children.subject']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'children.subject'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folders",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folders_post(client: TestClient):
    """Test case for folders_post

    Create single folder.
    """
    folders_create_operation_payload = tidal.FoldersCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/folders",
    #    headers=headers,
    #    json=folders_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folders_id_get(client: TestClient):
    """Test case for folders_id_get

    Get single folder.
    """
    params = [("include", ['children.subject']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'children.subject'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folders/{id}".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folders_id_delete(client: TestClient):
    """Test case for folders_id_delete

    Delete single folder.
    """
    params = [("share_code", 'xyz')]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/folders/{id}".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folders_id_patch(client: TestClient):
    """Test case for folders_id_patch

    Update single folder.
    """
    folders_update_operation_payload = tidal.FoldersUpdateOperationPayload()
    params = [("share_code", 'xyz')]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/folders/{id}".format(id='me'),
    #    headers=headers,
    #    json=folders_update_operation_payload,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folders_id_relationships_children_get(client: TestClient):
    """Test case for folders_id_relationships_children_get

    Get children relationship (\"to-many\").
    """
    params = [("include", ['children.subject']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'children.subject'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folders/{id}/relationships/children".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folders_id_relationships_owners_get(client: TestClient):
    """Test case for folders_id_relationships_owners_get

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
    #    "/folders/{id}/relationships/owners".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folders_id_relationships_parent_get(client: TestClient):
    """Test case for folders_id_relationships_parent_get

    Get parent relationship (\"to-one\").
    """
    params = [("include", ['parent.children.subject']),     ("replace_media", 'parent.children.subject'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folders/{id}/relationships/parent".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folders_id_relationships_preview_get(client: TestClient):
    """Test case for folders_id_relationships_preview_get

    Get preview relationship (\"to-many\").
    """
    params = [("include", ['preview.subject']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'preview.subject'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folders/{id}/relationships/preview".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

