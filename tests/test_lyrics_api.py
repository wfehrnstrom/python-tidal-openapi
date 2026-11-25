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
from tidal.models.lyrics_create_operation_payload import LyricsCreateOperationPayload  # noqa: F401
from tidal.models.lyrics_create_single_resource_data_document import LyricsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.lyrics_owners_multi_relationship_data_document import LyricsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.lyrics_single_resource_data_document import LyricsSingleResourceDataDocument  # noqa: F401
from tidal.models.lyrics_track_single_relationship_data_document import LyricsTrackSingleRelationshipDataDocument  # noqa: F401
from tidal.models.lyrics_update_operation_payload import LyricsUpdateOperationPayload  # noqa: F401
from tidal.models.mutation_response_document import MutationResponseDocument  # noqa: F401


def test_lyrics_post(client: TestClient):
    """Test case for lyrics_post

    Create single lyric.
    """
    lyrics_create_operation_payload = tidal.LyricsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/lyrics",
    #    headers=headers,
    #    json=lyrics_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_lyrics_id_get(client: TestClient):
    """Test case for lyrics_id_get

    Get single lyric.
    """
    params = [("include", ['track']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'track')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/lyrics/{id}".format(id='nejMcAhh5N8S3EQ4LaqysVdI0cZZ'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_lyrics_id_delete(client: TestClient):
    """Test case for lyrics_id_delete

    Delete single lyric.
    """

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/lyrics/{id}".format(id='nejMcAhh5N8S3EQ4LaqysVdI0cZZ'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_lyrics_id_patch(client: TestClient):
    """Test case for lyrics_id_patch

    Update single lyric.
    """
    lyrics_update_operation_payload = tidal.LyricsUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/lyrics/{id}".format(id='nejMcAhh5N8S3EQ4LaqysVdI0cZZ'),
    #    headers=headers,
    #    json=lyrics_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_lyrics_id_relationships_owners_get(client: TestClient):
    """Test case for lyrics_id_relationships_owners_get

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
    #    "/lyrics/{id}/relationships/owners".format(id='nejMcAhh5N8S3EQ4LaqysVdI0cZZ'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_lyrics_id_relationships_track_get(client: TestClient):
    """Test case for lyrics_id_relationships_track_get

    Get track relationship (\"to-one\").
    """
    params = [("country_code", 'US'),     ("include", ['track']),     ("replace_media", 'track')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/lyrics/{id}/relationships/track".format(id='nejMcAhh5N8S3EQ4LaqysVdI0cZZ'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

