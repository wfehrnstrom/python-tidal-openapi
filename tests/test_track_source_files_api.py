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
from tidal.models.track_source_files_comment_summary_single_relationship_data_document import TrackSourceFilesCommentSummarySingleRelationshipDataDocument  # noqa: F401
from tidal.models.track_source_files_create_operation_payload import TrackSourceFilesCreateOperationPayload  # noqa: F401
from tidal.models.track_source_files_create_single_resource_data_document import TrackSourceFilesCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.track_source_files_owners_multi_relationship_data_document import TrackSourceFilesOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.track_source_files_reaction_summary_single_relationship_data_document import TrackSourceFilesReactionSummarySingleRelationshipDataDocument  # noqa: F401
from tidal.models.track_source_files_single_resource_data_document import TrackSourceFilesSingleResourceDataDocument  # noqa: F401


def test_track_source_files_post(client: TestClient):
    """Test case for track_source_files_post

    Create single trackSourceFile.
    """
    track_source_files_create_operation_payload = tidal.TrackSourceFilesCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/trackSourceFiles",
    #    headers=headers,
    #    json=track_source_files_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_track_source_files_id_get(client: TestClient):
    """Test case for track_source_files_id_get

    Get single trackSourceFile.
    """
    params = [("include", ['commentSummary']),     ("include_linkage", ['include_linkage_example']),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/trackSourceFiles/{id}".format(id='a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_track_source_files_id_relationships_comment_summary_get(client: TestClient):
    """Test case for track_source_files_id_relationships_comment_summary_get

    Get commentSummary relationship (\"to-one\").
    """
    params = [("include", ['commentSummary']),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/trackSourceFiles/{id}/relationships/commentSummary".format(id='a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_track_source_files_id_relationships_owners_get(client: TestClient):
    """Test case for track_source_files_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/trackSourceFiles/{id}/relationships/owners".format(id='a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_track_source_files_id_relationships_reaction_summary_get(client: TestClient):
    """Test case for track_source_files_id_relationships_reaction_summary_get

    Get reactionSummary relationship (\"to-one\").
    """
    params = [("include", ['reactionSummary']),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/trackSourceFiles/{id}/relationships/reactionSummary".format(id='a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

