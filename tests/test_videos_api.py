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
from tidal.models.videos_albums_multi_relationship_data_document import VideosAlbumsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.videos_artists_multi_relationship_data_document import VideosArtistsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.videos_credits_multi_relationship_data_document import VideosCreditsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.videos_multi_resource_data_document import VideosMultiResourceDataDocument  # noqa: F401
from tidal.models.videos_providers_multi_relationship_data_document import VideosProvidersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.videos_replacement_single_relationship_data_document import VideosReplacementSingleRelationshipDataDocument  # noqa: F401
from tidal.models.videos_similar_videos_multi_relationship_data_document import VideosSimilarVideosMultiRelationshipDataDocument  # noqa: F401
from tidal.models.videos_single_resource_data_document import VideosSingleResourceDataDocument  # noqa: F401
from tidal.models.videos_suggested_videos_multi_relationship_data_document import VideosSuggestedVideosMultiRelationshipDataDocument  # noqa: F401
from tidal.models.videos_thumbnail_art_multi_relationship_data_document import VideosThumbnailArtMultiRelationshipDataDocument  # noqa: F401
from tidal.models.videos_usage_rules_single_relationship_data_document import VideosUsageRulesSingleRelationshipDataDocument  # noqa: F401


def test_videos_get(client: TestClient):
    """Test case for videos_get

    Get multiple videos.
    """
    params = [("country_code", 'US'),     ("filter_id", ['filter_id_example']),     ("filter_isrc", ['filter_isrc_example']),     ("include", ['albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'albums')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/videos",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_videos_id_get(client: TestClient):
    """Test case for videos_id_get

    Get single video.
    """
    params = [("country_code", 'US'),     ("include", ['albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'albums')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/videos/{id}".format(id='75623239'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_videos_id_relationships_albums_get(client: TestClient):
    """Test case for videos_id_relationships_albums_get

    Get albums relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'albums')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/videos/{id}/relationships/albums".format(id='75623239'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_videos_id_relationships_artists_get(client: TestClient):
    """Test case for videos_id_relationships_artists_get

    Get artists relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['artists.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'artists.albums')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/videos/{id}/relationships/artists".format(id='75623239'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_videos_id_relationships_credits_get(client: TestClient):
    """Test case for videos_id_relationships_credits_get

    Get credits relationship (\"to-many\").
    """
    params = [("include", ['credits.artist.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'credits.artist.albums')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/videos/{id}/relationships/credits".format(id='75623239'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_videos_id_relationships_providers_get(client: TestClient):
    """Test case for videos_id_relationships_providers_get

    Get providers relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['providers']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/videos/{id}/relationships/providers".format(id='75623239'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_videos_id_relationships_replacement_get(client: TestClient):
    """Test case for videos_id_relationships_replacement_get

    Get replacement relationship (\"to-one\").
    """
    params = [("country_code", 'US'),     ("include", ['replacement']),     ("replace_media", 'replacement')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/videos/{id}/relationships/replacement".format(id='75623239'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_videos_id_relationships_similar_videos_get(client: TestClient):
    """Test case for videos_id_relationships_similar_videos_get

    Get similarVideos relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['similarVideos']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'similarVideos')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/videos/{id}/relationships/similarVideos".format(id='75623239'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_videos_id_relationships_suggested_videos_get(client: TestClient):
    """Test case for videos_id_relationships_suggested_videos_get

    Get suggestedVideos relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['suggestedVideos']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'suggestedVideos')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/videos/{id}/relationships/suggestedVideos".format(id='75623239'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_videos_id_relationships_thumbnail_art_get(client: TestClient):
    """Test case for videos_id_relationships_thumbnail_art_get

    Get thumbnailArt relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['thumbnailArt']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/videos/{id}/relationships/thumbnailArt".format(id='75623239'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_videos_id_relationships_usage_rules_get(client: TestClient):
    """Test case for videos_id_relationships_usage_rules_get

    Get usageRules relationship (\"to-one\").
    """
    params = [("country_code", 'US'),     ("include", ['usageRules'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/videos/{id}/relationships/usageRules".format(id='75623239'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

