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
from tidal.models.resource_grant_invitations_create_operation_payload import ResourceGrantInvitationsCreateOperationPayload  # noqa: F401
from tidal.models.resource_grant_invitations_create_single_resource_data_document import ResourceGrantInvitationsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.resource_grant_invitations_multi_resource_data_document import ResourceGrantInvitationsMultiResourceDataDocument  # noqa: F401
from tidal.models.resource_grant_invitations_owners_multi_relationship_data_document import ResourceGrantInvitationsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.resource_grant_invitations_preview_grant_single_relationship_data_document import ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument  # noqa: F401
from tidal.models.resource_grant_invitations_single_resource_data_document import ResourceGrantInvitationsSingleResourceDataDocument  # noqa: F401
from tidal.models.resource_grant_invitations_subject_single_relationship_data_document import ResourceGrantInvitationsSubjectSingleRelationshipDataDocument  # noqa: F401
from tidal.models.resource_grant_invitations_update_operation_payload import ResourceGrantInvitationsUpdateOperationPayload  # noqa: F401
from tidal.models.resource_grant_invitations_update_single_resource_data_document import ResourceGrantInvitationsUpdateSingleResourceDataDocument  # noqa: F401


def test_resource_grant_invitations_get(client: TestClient):
    """Test case for resource_grant_invitations_get

    Get multiple resourceGrantInvitations.
    """
    params = [("filter_code", 'filter_code_example'),     ("filter_self_applies_to", 'filter_self_applies_to_example'),     ("include", ['previewGrant.subject']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'previewGrant.subject')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/resourceGrantInvitations",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resource_grant_invitations_post(client: TestClient):
    """Test case for resource_grant_invitations_post

    Create single resourceGrantInvitation.
    """
    resource_grant_invitations_create_operation_payload = tidal.ResourceGrantInvitationsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/resourceGrantInvitations",
    #    headers=headers,
    #    json=resource_grant_invitations_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resource_grant_invitations_id_get(client: TestClient):
    """Test case for resource_grant_invitations_id_get

    Get single resourceGrantInvitation.
    """
    params = [("include", ['previewGrant.subject']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'previewGrant.subject')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/resourceGrantInvitations/{id}".format(id='e0163a07-8eee-4d30-ae44-75d44b1e47b0'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resource_grant_invitations_id_delete(client: TestClient):
    """Test case for resource_grant_invitations_id_delete

    Delete single resourceGrantInvitation.
    """
    params = [("revoke_grants", True)]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/resourceGrantInvitations/{id}".format(id='e0163a07-8eee-4d30-ae44-75d44b1e47b0'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resource_grant_invitations_id_patch(client: TestClient):
    """Test case for resource_grant_invitations_id_patch

    Update single resourceGrantInvitation.
    """
    resource_grant_invitations_update_operation_payload = tidal.ResourceGrantInvitationsUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/resourceGrantInvitations/{id}".format(id='e0163a07-8eee-4d30-ae44-75d44b1e47b0'),
    #    headers=headers,
    #    json=resource_grant_invitations_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resource_grant_invitations_id_relationships_owners_get(client: TestClient):
    """Test case for resource_grant_invitations_id_relationships_owners_get

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
    #    "/resourceGrantInvitations/{id}/relationships/owners".format(id='e0163a07-8eee-4d30-ae44-75d44b1e47b0'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resource_grant_invitations_id_relationships_preview_grant_get(client: TestClient):
    """Test case for resource_grant_invitations_id_relationships_preview_grant_get

    Get previewGrant relationship (\"to-one\").
    """
    params = [("include", ['previewGrant.subject']),     ("replace_media", 'previewGrant.subject')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/resourceGrantInvitations/{id}/relationships/previewGrant".format(id='e0163a07-8eee-4d30-ae44-75d44b1e47b0'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_resource_grant_invitations_id_relationships_subject_get(client: TestClient):
    """Test case for resource_grant_invitations_id_relationships_subject_get

    Get subject relationship (\"to-one\").
    """
    params = [("include", ['subject']),     ("replace_media", 'subject')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/resourceGrantInvitations/{id}/relationships/subject".format(id='e0163a07-8eee-4d30-ae44-75d44b1e47b0'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

