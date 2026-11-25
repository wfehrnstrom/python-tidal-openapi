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
from tidal.models.search_results_albums_multi_relationship_data_document import SearchResultsAlbumsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.search_results_artists_multi_relationship_data_document import SearchResultsArtistsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.search_results_multi_resource_data_document import SearchResultsMultiResourceDataDocument  # noqa: F401
from tidal.models.search_results_playlists_multi_relationship_data_document import SearchResultsPlaylistsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.search_results_top_hits_multi_relationship_data_document import SearchResultsTopHitsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.search_results_tracks_multi_relationship_data_document import SearchResultsTracksMultiRelationshipDataDocument  # noqa: F401
from tidal.models.search_results_videos_multi_relationship_data_document import SearchResultsVideosMultiRelationshipDataDocument  # noqa: F401


def test_search_results_get(client: TestClient):
    """Test case for search_results_get

    Get search results by query.
    """
    params = [("filter_query", 'filter_query_example'),     ("client_version", '2026.0.1'),     ("country_code", 'US'),     ("device_type", 'PHONE'),     ("explicit_filter", 'INCLUDE'),     ("include", ['albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'albums'),     ("system_type", 'IOS')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/searchResults",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_search_results_id_relationships_albums_get(client: TestClient):
    """Test case for search_results_id_relationships_albums_get

    Get albums relationship (\"to-many\").
    """
    params = [("client_version", '2026.0.1'),     ("country_code", 'US'),     ("device_type", 'PHONE'),     ("explicit_filter", 'INCLUDE'),     ("include", ['albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'albums'),     ("system_type", 'IOS')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/searchResults/{id}/relationships/albums".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_search_results_id_relationships_artists_get(client: TestClient):
    """Test case for search_results_id_relationships_artists_get

    Get artists relationship (\"to-many\").
    """
    params = [("client_version", '2026.0.1'),     ("country_code", 'US'),     ("device_type", 'PHONE'),     ("explicit_filter", 'INCLUDE'),     ("include", ['artists.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'artists.albums'),     ("system_type", 'IOS')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/searchResults/{id}/relationships/artists".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_search_results_id_relationships_playlists_get(client: TestClient):
    """Test case for search_results_id_relationships_playlists_get

    Get playlists relationship (\"to-many\").
    """
    params = [("client_version", '2026.0.1'),     ("country_code", 'US'),     ("device_type", 'PHONE'),     ("explicit_filter", 'INCLUDE'),     ("include", ['playlists.items']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'playlists.items'),     ("system_type", 'IOS')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/searchResults/{id}/relationships/playlists".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_search_results_id_relationships_top_hits_get(client: TestClient):
    """Test case for search_results_id_relationships_top_hits_get

    Get topHits relationship (\"to-many\").
    """
    params = [("client_version", '2026.0.1'),     ("country_code", 'US'),     ("device_type", 'PHONE'),     ("explicit_filter", 'INCLUDE'),     ("include", ['topHits']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'topHits'),     ("system_type", 'IOS')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/searchResults/{id}/relationships/topHits".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_search_results_id_relationships_tracks_get(client: TestClient):
    """Test case for search_results_id_relationships_tracks_get

    Get tracks relationship (\"to-many\").
    """
    params = [("client_version", '2026.0.1'),     ("country_code", 'US'),     ("device_type", 'PHONE'),     ("explicit_filter", 'INCLUDE'),     ("include", ['tracks']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'tracks'),     ("system_type", 'IOS')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/searchResults/{id}/relationships/tracks".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_search_results_id_relationships_videos_get(client: TestClient):
    """Test case for search_results_id_relationships_videos_get

    Get videos relationship (\"to-many\").
    """
    params = [("client_version", '2026.0.1'),     ("country_code", 'US'),     ("device_type", 'PHONE'),     ("explicit_filter", 'INCLUDE'),     ("include", ['videos']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'videos'),     ("system_type", 'IOS')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/searchResults/{id}/relationships/videos".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

