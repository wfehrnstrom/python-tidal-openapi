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
from tidal.models.reactions_author_single_relationship_data_document import ReactionsAuthorSingleRelationshipDataDocument  # noqa: F401
from tidal.models.reactions_create_operation_payload import ReactionsCreateOperationPayload  # noqa: F401
from tidal.models.reactions_create_single_resource_data_document import ReactionsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.reactions_multi_resource_data_document import ReactionsMultiResourceDataDocument  # noqa: F401
from tidal.models.reactions_owners_multi_relationship_data_document import ReactionsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.reactions_subject_single_relationship_data_document import ReactionsSubjectSingleRelationshipDataDocument  # noqa: F401


def test_reactions_get(client: TestClient):
    """Test case for reactions_get

    Get multiple reactions.
    """
    params = [("filter_subject", 'filter_subject_example'),     ("filter_emoji", ['filter_emoji_example']),     ("include", ['author.albums']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'author.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/reactions",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_reactions_post(client: TestClient):
    """Test case for reactions_post

    Create single reaction.
    """
    reactions_create_operation_payload = tidal.ReactionsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/reactions",
    #    headers=headers,
    #    json=reactions_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_reactions_id_delete(client: TestClient):
    """Test case for reactions_id_delete

    Delete single reaction.
    """

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/reactions/{id}".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_reactions_id_relationships_author_get(client: TestClient):
    """Test case for reactions_id_relationships_author_get

    Get author relationship (\"to-one\").
    """
    params = [("include", ['author.albums']),     ("replace_media", 'author.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/reactions/{id}/relationships/author".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_reactions_id_relationships_owners_get(client: TestClient):
    """Test case for reactions_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/reactions/{id}/relationships/owners".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_reactions_id_relationships_subject_get(client: TestClient):
    """Test case for reactions_id_relationships_subject_get

    Get subject relationship (\"to-one\").
    """
    params = [("include", ['subject.author.albums']),     ("replace_media", 'subject.author.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/reactions/{id}/relationships/subject".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

