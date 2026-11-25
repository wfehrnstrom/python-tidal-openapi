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
from tidal.models.tracks_albums_multi_relationship_data_document import TracksAlbumsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_albums_relationship_update_operation_payload import TracksAlbumsRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.tracks_artists_multi_relationship_data_document import TracksArtistsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_artists_relationship_update_operation_payload import TracksArtistsRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.tracks_create_operation_payload import TracksCreateOperationPayload  # noqa: F401
from tidal.models.tracks_create_single_resource_data_document import TracksCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.tracks_credits_multi_relationship_data_document import TracksCreditsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_download_single_relationship_data_document import TracksDownloadSingleRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_genres_multi_relationship_data_document import TracksGenresMultiRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_lyrics_multi_relationship_data_document import TracksLyricsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_metadata_status_single_relationship_data_document import TracksMetadataStatusSingleRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_multi_resource_data_document import TracksMultiResourceDataDocument  # noqa: F401
from tidal.models.tracks_owners_multi_relationship_data_document import TracksOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_price_config_single_relationship_data_document import TracksPriceConfigSingleRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_providers_multi_relationship_data_document import TracksProvidersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_radio_multi_relationship_data_document import TracksRadioMultiRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_replacement_single_relationship_data_document import TracksReplacementSingleRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_shares_multi_relationship_data_document import TracksSharesMultiRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_similar_tracks_multi_relationship_data_document import TracksSimilarTracksMultiRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_single_resource_data_document import TracksSingleResourceDataDocument  # noqa: F401
from tidal.models.tracks_source_file_single_relationship_data_document import TracksSourceFileSingleRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_suggested_tracks_multi_relationship_data_document import TracksSuggestedTracksMultiRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_track_statistics_single_relationship_data_document import TracksTrackStatisticsSingleRelationshipDataDocument  # noqa: F401
from tidal.models.tracks_update_operation_payload import TracksUpdateOperationPayload  # noqa: F401
from tidal.models.tracks_usage_rules_single_relationship_data_document import TracksUsageRulesSingleRelationshipDataDocument  # noqa: F401


def test_tracks_get(client: TestClient):
    """Test case for tracks_get

    Get multiple tracks.
    """
    params = [("country_code", 'US'),     ("filter_id", ['filter_id_example']),     ("filter_isrc", ['filter_isrc_example']),     ("filter_owners_id", ['filter_owners_id_example']),     ("include", ['albums']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'albums'),     ("share_code", 'xyz'),     ("sort", ['sort_example'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_post(client: TestClient):
    """Test case for tracks_post

    Create single track.
    """
    tracks_create_operation_payload = tidal.TracksCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/tracks",
    #    headers=headers,
    #    json=tracks_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_get(client: TestClient):
    """Test case for tracks_id_get

    Get single track.
    """
    params = [("country_code", 'US'),     ("include", ['albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'albums'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_delete(client: TestClient):
    """Test case for tracks_id_delete

    Delete single track.
    """
    params = [("share_code", 'xyz')]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/tracks/{id}".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_patch(client: TestClient):
    """Test case for tracks_id_patch

    Update single track.
    """
    tracks_update_operation_payload = tidal.TracksUpdateOperationPayload()
    params = [("share_code", 'xyz')]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/tracks/{id}".format(id='75413016'),
    #    headers=headers,
    #    json=tracks_update_operation_payload,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_albums_get(client: TestClient):
    """Test case for tracks_id_relationships_albums_get

    Get albums relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'albums'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/albums".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_albums_patch(client: TestClient):
    """Test case for tracks_id_relationships_albums_patch

    Update albums relationship (\"to-many\").
    """
    tracks_albums_relationship_update_operation_payload = tidal.TracksAlbumsRelationshipUpdateOperationPayload()
    params = [("share_code", 'xyz')]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/tracks/{id}/relationships/albums".format(id='75413016'),
    #    headers=headers,
    #    json=tracks_albums_relationship_update_operation_payload,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_artists_get(client: TestClient):
    """Test case for tracks_id_relationships_artists_get

    Get artists relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['artists.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'artists.albums'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/artists".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_artists_patch(client: TestClient):
    """Test case for tracks_id_relationships_artists_patch

    Update artists relationship (\"to-many\").
    """
    tracks_artists_relationship_update_operation_payload = tidal.TracksArtistsRelationshipUpdateOperationPayload()
    params = [("share_code", 'xyz')]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/tracks/{id}/relationships/artists".format(id='75413016'),
    #    headers=headers,
    #    json=tracks_artists_relationship_update_operation_payload,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_credits_get(client: TestClient):
    """Test case for tracks_id_relationships_credits_get

    Get credits relationship (\"to-many\").
    """
    params = [("include", ['credits.artist.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'credits.artist.albums'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/credits".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_download_get(client: TestClient):
    """Test case for tracks_id_relationships_download_get

    Get download relationship (\"to-one\").
    """
    params = [("include", ['download']),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/download".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_genres_get(client: TestClient):
    """Test case for tracks_id_relationships_genres_get

    Get genres relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['genres']),     ("page_cursor", 'page_cursor_example'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/genres".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_lyrics_get(client: TestClient):
    """Test case for tracks_id_relationships_lyrics_get

    Get lyrics relationship (\"to-many\").
    """
    params = [("include", ['lyrics.track']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'lyrics.track'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/lyrics".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_metadata_status_get(client: TestClient):
    """Test case for tracks_id_relationships_metadata_status_get

    Get metadataStatus relationship (\"to-one\").
    """
    params = [("include", ['metadataStatus']),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/metadataStatus".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_owners_get(client: TestClient):
    """Test case for tracks_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/owners".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_price_config_get(client: TestClient):
    """Test case for tracks_id_relationships_price_config_get

    Get priceConfig relationship (\"to-one\").
    """
    params = [("country_code", 'US'),     ("include", ['priceConfig']),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/priceConfig".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_providers_get(client: TestClient):
    """Test case for tracks_id_relationships_providers_get

    Get providers relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['providers']),     ("page_cursor", 'page_cursor_example'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/providers".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_radio_get(client: TestClient):
    """Test case for tracks_id_relationships_radio_get

    Get radio relationship (\"to-many\").
    """
    params = [("include", ['radio.items']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'radio.items'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/radio".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_replacement_get(client: TestClient):
    """Test case for tracks_id_relationships_replacement_get

    Get replacement relationship (\"to-one\").
    """
    params = [("country_code", 'US'),     ("include", ['replacement']),     ("replace_media", 'replacement'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/replacement".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_shares_get(client: TestClient):
    """Test case for tracks_id_relationships_shares_get

    Get shares relationship (\"to-many\").
    """
    params = [("include", ['shares.sharedResources']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'shares.sharedResources'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/shares".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_similar_tracks_get(client: TestClient):
    """Test case for tracks_id_relationships_similar_tracks_get

    Get similarTracks relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['similarTracks']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'similarTracks'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/similarTracks".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_source_file_get(client: TestClient):
    """Test case for tracks_id_relationships_source_file_get

    Get sourceFile relationship (\"to-one\").
    """
    params = [("include", ['sourceFile']),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/sourceFile".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_suggested_tracks_get(client: TestClient):
    """Test case for tracks_id_relationships_suggested_tracks_get

    Get suggestedTracks relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['suggestedTracks']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'suggestedTracks'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/suggestedTracks".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_track_statistics_get(client: TestClient):
    """Test case for tracks_id_relationships_track_statistics_get

    Get trackStatistics relationship (\"to-one\").
    """
    params = [("include", ['trackStatistics']),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/trackStatistics".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tracks_id_relationships_usage_rules_get(client: TestClient):
    """Test case for tracks_id_relationships_usage_rules_get

    Get usageRules relationship (\"to-one\").
    """
    params = [("country_code", 'US'),     ("include", ['usageRules']),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tracks/{id}/relationships/usageRules".format(id='75413016'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

