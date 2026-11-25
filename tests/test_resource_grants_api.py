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
from tidal.models.resource_grants_create_operation_payload import ResourceGrantsCreateOperationPayload  # noqa: F401
from tidal.models.resource_grants_create_resource403_response_body import ResourceGrantsCreateResource403ResponseBody  # noqa: F401
from tidal.models.resource_grants_create_resource429_response_body import ResourceGrantsCreateResource429ResponseBody  # noqa: F401
from tidal.models.resource_grants_create_single_resource_data_document import ResourceGrantsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.resource_grants_grantee_single_relationship_data_document import ResourceGrantsGranteeSingleRelationshipDataDocument  # noqa: F401
from tidal.models.resource_grants_invitation_single_relationship_data_document import ResourceGrantsInvitationSingleRelationshipDataDocument  # noqa: F401
from tidal.models.resource_grants_multi_resource_data_document import ResourceGrantsMultiResourceDataDocument  # noqa: F401
from tidal.models.resource_grants_single_resource_data_document import ResourceGrantsSingleResourceDataDocument  # noqa: F401
from tidal.models.resource_grants_subject_single_relationship_data_document import ResourceGrantsSubjectSingleRelationshipDataDocument  # noqa: F401
from tidal.models.resource_grants_update_operation_payload import ResourceGrantsUpdateOperationPayload  # noqa: F401
from tidal.models.resource_grants_update_single_resource_data_document import ResourceGrantsUpdateSingleResourceDataDocument  # noqa: F401


def test_resource_grants_get(client: TestClient):
    """Test case for resource_grants_get

    Get multiple resourceGrants.
    """
    params = [("filter_grantee", 'filter_grantee_example'),     ("filter_role", 'filter_role_example'),     ("filter_self_applies_to", 'filter_self_applies_to_example'),     ("filter_subject", 'filter_subject_example'),     ("include", ['grantee.artist.albums']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'grantee.artist.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/resourceGrants",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resource_grants_post(client: TestClient):
    """Test case for resource_grants_post

    Create single resourceGrant.
    """
    resource_grants_create_operation_payload = tidal.ResourceGrantsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/resourceGrants",
    #    headers=headers,
    #    json=resource_grants_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resource_grants_id_get(client: TestClient):
    """Test case for resource_grants_id_get

    Get single resourceGrant.
    """
    params = [("include", ['grantee.artist.albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'grantee.artist.albums')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/resourceGrants/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resource_grants_id_delete(client: TestClient):
    """Test case for resource_grants_id_delete

    Delete single resourceGrant.
    """

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/resourceGrants/{id}".format(id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resource_grants_id_patch(client: TestClient):
    """Test case for resource_grants_id_patch

    Update single resourceGrant.
    """
    resource_grants_update_operation_payload = tidal.ResourceGrantsUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/resourceGrants/{id}".format(id='id_example'),
    #    headers=headers,
    #    json=resource_grants_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resource_grants_id_relationships_grantee_get(client: TestClient):
    """Test case for resource_grants_id_relationships_grantee_get

    Get grantee relationship (\"to-one\").
    """
    params = [("include", ['grantee.artist.albums']),     ("replace_media", 'grantee.artist.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/resourceGrants/{id}/relationships/grantee".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resource_grants_id_relationships_invitation_get(client: TestClient):
    """Test case for resource_grants_id_relationships_invitation_get

    Get invitation relationship (\"to-one\").
    """
    params = [("include", ['invitation.subject']),     ("replace_media", 'invitation.subject')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/resourceGrants/{id}/relationships/invitation".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resource_grants_id_relationships_subject_get(client: TestClient):
    """Test case for resource_grants_id_relationships_subject_get

    Get subject relationship (\"to-one\").
    """
    params = [("include", ['subject']),     ("replace_media", 'subject')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/resourceGrants/{id}/relationships/subject".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

