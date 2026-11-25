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
from tidal.models.user_feed_items_actors_multi_relationship_data_document import UserFeedItemsActorsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_feed_items_multi_resource_data_document import UserFeedItemsMultiResourceDataDocument  # noqa: F401
from tidal.models.user_feed_items_subject_single_relationship_data_document import UserFeedItemsSubjectSingleRelationshipDataDocument  # noqa: F401


def test_user_feed_items_get(client: TestClient):
    """Test case for user_feed_items_get

    Get multiple userFeedItems.
    """
    params = [("filter_owners_id", ['filter_owners_id_example']),     ("filter_surface", 'filter_surface_example'),     ("include", ['actors.albums']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'actors.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userFeedItems",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_feed_items_id_relationships_actors_get(client: TestClient):
    """Test case for user_feed_items_id_relationships_actors_get

    Get actors relationship (\"to-many\").
    """
    params = [("include", ['actors.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'actors.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userFeedItems/{id}/relationships/actors".format(id='49XlsRIbQZSrRDe0QZhJ0y9nGzecOTVBOUN8MUUeD1iEbppZTWCgdLaxmzUvtk0K0JodRqxYgJrDQ5DAfi16j2ICfJGJ9MH9S6IvYuKzQAn1UWWSCdMA'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_feed_items_id_relationships_subject_get(client: TestClient):
    """Test case for user_feed_items_id_relationships_subject_get

    Get subject relationship (\"to-one\").
    """
    params = [("include", ['subject']),     ("replace_media", 'subject')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userFeedItems/{id}/relationships/subject".format(id='49XlsRIbQZSrRDe0QZhJ0y9nGzecOTVBOUN8MUUeD1iEbppZTWCgdLaxmzUvtk0K0JodRqxYgJrDQ5DAfi16j2ICfJGJ9MH9S6IvYuKzQAn1UWWSCdMA'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

