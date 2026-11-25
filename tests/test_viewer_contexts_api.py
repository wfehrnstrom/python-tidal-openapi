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
from tidal.models.viewer_contexts_comments_multi_relationship_data_document import ViewerContextsCommentsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.viewer_contexts_multi_resource_data_document import ViewerContextsMultiResourceDataDocument  # noqa: F401
from tidal.models.viewer_contexts_reactions_multi_relationship_data_document import ViewerContextsReactionsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.viewer_contexts_single_resource_data_document import ViewerContextsSingleResourceDataDocument  # noqa: F401
from tidal.models.viewer_contexts_subject_single_relationship_data_document import ViewerContextsSubjectSingleRelationshipDataDocument  # noqa: F401
from tidal.models.viewer_contexts_viewer_single_relationship_data_document import ViewerContextsViewerSingleRelationshipDataDocument  # noqa: F401


def test_viewer_contexts_get(client: TestClient):
    """Test case for viewer_contexts_get

    Get multiple viewerContexts.
    """
    params = [("filter_subject", ['filter_subject_example']),     ("include", ['comments.author.albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'comments.author.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/viewerContexts",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_viewer_contexts_id_get(client: TestClient):
    """Test case for viewer_contexts_id_get

    Get single viewerContext.
    """
    params = [("include", ['comments.author.albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'comments.author.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/viewerContexts/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_viewer_contexts_id_relationships_comments_get(client: TestClient):
    """Test case for viewer_contexts_id_relationships_comments_get

    Get comments relationship (\"to-many\").
    """
    params = [("include", ['comments.author.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'comments.author.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/viewerContexts/{id}/relationships/comments".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_viewer_contexts_id_relationships_reactions_get(client: TestClient):
    """Test case for viewer_contexts_id_relationships_reactions_get

    Get reactions relationship (\"to-many\").
    """
    params = [("include", ['reactions.author.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'reactions.author.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/viewerContexts/{id}/relationships/reactions".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_viewer_contexts_id_relationships_subject_get(client: TestClient):
    """Test case for viewer_contexts_id_relationships_subject_get

    Get subject relationship (\"to-one\").
    """
    params = [("include", ['subject']),     ("replace_media", 'subject')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/viewerContexts/{id}/relationships/subject".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_viewer_contexts_id_relationships_viewer_get(client: TestClient):
    """Test case for viewer_contexts_id_relationships_viewer_get

    Get viewer relationship (\"to-one\").
    """
    params = [("include", ['viewer.artist.albums']),     ("replace_media", 'viewer.artist.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/viewerContexts/{id}/relationships/viewer".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

