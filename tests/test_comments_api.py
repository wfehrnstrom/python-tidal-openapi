# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.comments_author_single_relationship_data_document import CommentsAuthorSingleRelationshipDataDocument  # noqa: F401
from tidal.models.comments_comment_summary_single_relationship_data_document import CommentsCommentSummarySingleRelationshipDataDocument  # noqa: F401
from tidal.models.comments_create_operation_payload import CommentsCreateOperationPayload  # noqa: F401
from tidal.models.comments_create_single_resource_data_document import CommentsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.comments_multi_resource_data_document import CommentsMultiResourceDataDocument  # noqa: F401
from tidal.models.comments_owners_multi_relationship_data_document import CommentsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.comments_reaction_summary_single_relationship_data_document import CommentsReactionSummarySingleRelationshipDataDocument  # noqa: F401
from tidal.models.comments_root_subject_single_relationship_data_document import CommentsRootSubjectSingleRelationshipDataDocument  # noqa: F401
from tidal.models.comments_single_resource_data_document import CommentsSingleResourceDataDocument  # noqa: F401
from tidal.models.comments_subject_single_relationship_data_document import CommentsSubjectSingleRelationshipDataDocument  # noqa: F401
from tidal.models.comments_update_operation_payload import CommentsUpdateOperationPayload  # noqa: F401
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


def test_comments_get(client: TestClient):
    """Test case for comments_get

    Get multiple comments.
    """
    params = [("filter_subject", 'filter_subject_example'),     ("include", ['author.albums']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'author.albums'),     ("sort", ['sort_example'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/comments",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_comments_post(client: TestClient):
    """Test case for comments_post

    Create single comment.
    """
    comments_create_operation_payload = tidal.CommentsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/comments",
    #    headers=headers,
    #    json=comments_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_comments_id_get(client: TestClient):
    """Test case for comments_id_get

    Get single comment.
    """
    params = [("include", ['author.albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'author.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/comments/{id}".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_comments_id_delete(client: TestClient):
    """Test case for comments_id_delete

    Delete single comment.
    """

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/comments/{id}".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_comments_id_patch(client: TestClient):
    """Test case for comments_id_patch

    Update single comment.
    """
    comments_update_operation_payload = tidal.CommentsUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/comments/{id}".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    json=comments_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_comments_id_relationships_author_get(client: TestClient):
    """Test case for comments_id_relationships_author_get

    Get author relationship (\"to-one\").
    """
    params = [("include", ['author.albums']),     ("replace_media", 'author.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/comments/{id}/relationships/author".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_comments_id_relationships_comment_summary_get(client: TestClient):
    """Test case for comments_id_relationships_comment_summary_get

    Get commentSummary relationship (\"to-one\").
    """
    params = [("include", ['commentSummary'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/comments/{id}/relationships/commentSummary".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_comments_id_relationships_owners_get(client: TestClient):
    """Test case for comments_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/comments/{id}/relationships/owners".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_comments_id_relationships_reaction_summary_get(client: TestClient):
    """Test case for comments_id_relationships_reaction_summary_get

    Get reactionSummary relationship (\"to-one\").
    """
    params = [("include", ['reactionSummary'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/comments/{id}/relationships/reactionSummary".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_comments_id_relationships_root_subject_get(client: TestClient):
    """Test case for comments_id_relationships_root_subject_get

    Get rootSubject relationship (\"to-one\").
    """
    params = [("include", ['rootSubject'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/comments/{id}/relationships/rootSubject".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_comments_id_relationships_subject_get(client: TestClient):
    """Test case for comments_id_relationships_subject_get

    Get subject relationship (\"to-one\").
    """
    params = [("include", ['subject.author.albums']),     ("replace_media", 'subject.author.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/comments/{id}/relationships/subject".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

