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
from tidal.models.user_recommendation_blocks_artists_add_multi_data_relationship_with_response409_response_body import UserRecommendationBlocksArtistsAddMultiDataRelationshipWithResponse409ResponseBody  # noqa: F401
from tidal.models.user_recommendation_blocks_artists_add_multi_relationship_data_document import UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_recommendation_blocks_artists_multi_relationship_data_document import UserRecommendationBlocksArtistsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_recommendation_blocks_artists_relationship_add_operation_payload import UserRecommendationBlocksArtistsRelationshipAddOperationPayload  # noqa: F401
from tidal.models.user_recommendation_blocks_artists_relationship_remove_operation_payload import UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload  # noqa: F401
from tidal.models.user_recommendation_blocks_owners_multi_relationship_data_document import UserRecommendationBlocksOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_recommendation_blocks_single_resource_data_document import UserRecommendationBlocksSingleResourceDataDocument  # noqa: F401
from tidal.models.user_recommendation_blocks_tracks_add_multi_data_relationship_with_response409_response_body import UserRecommendationBlocksTracksAddMultiDataRelationshipWithResponse409ResponseBody  # noqa: F401
from tidal.models.user_recommendation_blocks_tracks_add_multi_relationship_data_document import UserRecommendationBlocksTracksAddMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_recommendation_blocks_tracks_multi_relationship_data_document import UserRecommendationBlocksTracksMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_recommendation_blocks_tracks_relationship_add_operation_payload import UserRecommendationBlocksTracksRelationshipAddOperationPayload  # noqa: F401
from tidal.models.user_recommendation_blocks_tracks_relationship_remove_operation_payload import UserRecommendationBlocksTracksRelationshipRemoveOperationPayload  # noqa: F401
from tidal.models.user_recommendation_blocks_videos_add_multi_data_relationship_with_response409_response_body import UserRecommendationBlocksVideosAddMultiDataRelationshipWithResponse409ResponseBody  # noqa: F401
from tidal.models.user_recommendation_blocks_videos_add_multi_relationship_data_document import UserRecommendationBlocksVideosAddMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_recommendation_blocks_videos_multi_relationship_data_document import UserRecommendationBlocksVideosMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_recommendation_blocks_videos_relationship_add_operation_payload import UserRecommendationBlocksVideosRelationshipAddOperationPayload  # noqa: F401
from tidal.models.user_recommendation_blocks_videos_relationship_remove_operation_payload import UserRecommendationBlocksVideosRelationshipRemoveOperationPayload  # noqa: F401


def test_user_recommendation_blocks_id_get(client: TestClient):
    """Test case for user_recommendation_blocks_id_get

    Get single userRecommendationBlock.
    """
    params = [("include", ['artists.albums']),     ("include_linkage", ['include_linkage_example']),     ("locale", 'en-US'),     ("replace_media", 'artists.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userRecommendationBlocks/{id}".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_recommendation_blocks_id_relationships_artists_get(client: TestClient):
    """Test case for user_recommendation_blocks_id_relationships_artists_get

    Get artists relationship (\"to-many\").
    """
    params = [("include", ['artists.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'artists.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userRecommendationBlocks/{id}/relationships/artists".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_recommendation_blocks_id_relationships_artists_post(client: TestClient):
    """Test case for user_recommendation_blocks_id_relationships_artists_post

    Add to artists relationship (\"to-many\").
    """
    user_recommendation_blocks_artists_relationship_add_operation_payload = tidal.UserRecommendationBlocksArtistsRelationshipAddOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/userRecommendationBlocks/{id}/relationships/artists".format(id='me'),
    #    headers=headers,
    #    json=user_recommendation_blocks_artists_relationship_add_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_recommendation_blocks_id_relationships_artists_delete(client: TestClient):
    """Test case for user_recommendation_blocks_id_relationships_artists_delete

    Delete from artists relationship (\"to-many\").
    """
    user_recommendation_blocks_artists_relationship_remove_operation_payload = tidal.UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/userRecommendationBlocks/{id}/relationships/artists".format(id='me'),
    #    headers=headers,
    #    json=user_recommendation_blocks_artists_relationship_remove_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_recommendation_blocks_id_relationships_owners_get(client: TestClient):
    """Test case for user_recommendation_blocks_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userRecommendationBlocks/{id}/relationships/owners".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_recommendation_blocks_id_relationships_tracks_get(client: TestClient):
    """Test case for user_recommendation_blocks_id_relationships_tracks_get

    Get tracks relationship (\"to-many\").
    """
    params = [("include", ['tracks']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'tracks')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userRecommendationBlocks/{id}/relationships/tracks".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_recommendation_blocks_id_relationships_tracks_post(client: TestClient):
    """Test case for user_recommendation_blocks_id_relationships_tracks_post

    Add to tracks relationship (\"to-many\").
    """
    user_recommendation_blocks_tracks_relationship_add_operation_payload = tidal.UserRecommendationBlocksTracksRelationshipAddOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/userRecommendationBlocks/{id}/relationships/tracks".format(id='me'),
    #    headers=headers,
    #    json=user_recommendation_blocks_tracks_relationship_add_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_recommendation_blocks_id_relationships_tracks_delete(client: TestClient):
    """Test case for user_recommendation_blocks_id_relationships_tracks_delete

    Delete from tracks relationship (\"to-many\").
    """
    user_recommendation_blocks_tracks_relationship_remove_operation_payload = tidal.UserRecommendationBlocksTracksRelationshipRemoveOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/userRecommendationBlocks/{id}/relationships/tracks".format(id='me'),
    #    headers=headers,
    #    json=user_recommendation_blocks_tracks_relationship_remove_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_recommendation_blocks_id_relationships_videos_get(client: TestClient):
    """Test case for user_recommendation_blocks_id_relationships_videos_get

    Get videos relationship (\"to-many\").
    """
    params = [("include", ['videos']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'videos')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userRecommendationBlocks/{id}/relationships/videos".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_recommendation_blocks_id_relationships_videos_post(client: TestClient):
    """Test case for user_recommendation_blocks_id_relationships_videos_post

    Add to videos relationship (\"to-many\").
    """
    user_recommendation_blocks_videos_relationship_add_operation_payload = tidal.UserRecommendationBlocksVideosRelationshipAddOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/userRecommendationBlocks/{id}/relationships/videos".format(id='me'),
    #    headers=headers,
    #    json=user_recommendation_blocks_videos_relationship_add_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_recommendation_blocks_id_relationships_videos_delete(client: TestClient):
    """Test case for user_recommendation_blocks_id_relationships_videos_delete

    Delete from videos relationship (\"to-many\").
    """
    user_recommendation_blocks_videos_relationship_remove_operation_payload = tidal.UserRecommendationBlocksVideosRelationshipRemoveOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/userRecommendationBlocks/{id}/relationships/videos".format(id='me'),
    #    headers=headers,
    #    json=user_recommendation_blocks_videos_relationship_remove_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

