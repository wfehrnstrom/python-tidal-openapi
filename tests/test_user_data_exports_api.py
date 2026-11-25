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
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody  # noqa: F401
from tidal.models.user_data_exports_create_operation_payload import UserDataExportsCreateOperationPayload  # noqa: F401
from tidal.models.user_data_exports_create_resource400_response_body import UserDataExportsCreateResource400ResponseBody  # noqa: F401
from tidal.models.user_data_exports_create_resource409_response_body import UserDataExportsCreateResource409ResponseBody  # noqa: F401
from tidal.models.user_data_exports_create_single_resource_data_document import UserDataExportsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.user_data_exports_multi_resource_data_document import UserDataExportsMultiResourceDataDocument  # noqa: F401
from tidal.models.user_data_exports_owners_multi_relationship_data_document import UserDataExportsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_data_exports_single_resource_data_document import UserDataExportsSingleResourceDataDocument  # noqa: F401


def test_user_data_exports_get(client: TestClient):
    """Test case for user_data_exports_get

    Get multiple userDataExports.
    """
    params = [("filter_owners_id", ['filter_owners_id_example']),     ("include", ['include_example']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userDataExports",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_data_exports_post(client: TestClient):
    """Test case for user_data_exports_post

    Create single userDataExport.
    """
    user_data_exports_create_operation_payload = tidal.UserDataExportsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/userDataExports",
    #    headers=headers,
    #    json=user_data_exports_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_data_exports_id_get(client: TestClient):
    """Test case for user_data_exports_id_get

    Get single userDataExport.
    """
    params = [("include", ['include_example']),     ("include_linkage", ['include_linkage_example'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userDataExports/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_data_exports_id_relationships_owners_get(client: TestClient):
    """Test case for user_data_exports_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userDataExports/{id}/relationships/owners".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

