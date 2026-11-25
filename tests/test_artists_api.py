# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.artists_albums_multi_relationship_data_document import ArtistsAlbumsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artists_banner_art_multi_relationship_data_document import ArtistsBannerArtMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artists_banner_art_relationship_update_operation_payload import ArtistsBannerArtRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.artists_biography_single_relationship_data_document import ArtistsBiographySingleRelationshipDataDocument  # noqa: F401
from tidal.models.artists_claim_status_single_relationship_data_document import ArtistsClaimStatusSingleRelationshipDataDocument  # noqa: F401
from tidal.models.artists_create_operation_payload import ArtistsCreateOperationPayload  # noqa: F401
from tidal.models.artists_create_single_resource_data_document import ArtistsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.artists_followers_multi_relationship_data_document import ArtistsFollowersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artists_following_multi_relationship_data_document import ArtistsFollowingMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artists_following_relationship_add_operation_payload import ArtistsFollowingRelationshipAddOperationPayload  # noqa: F401
from tidal.models.artists_following_relationship_remove_operation_payload import ArtistsFollowingRelationshipRemoveOperationPayload  # noqa: F401
from tidal.models.artists_logo_art_multi_relationship_data_document import ArtistsLogoArtMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artists_logo_art_relationship_update_operation_payload import ArtistsLogoArtRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.artists_multi_resource_data_document import ArtistsMultiResourceDataDocument  # noqa: F401
from tidal.models.artists_owners_multi_relationship_data_document import ArtistsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artists_profile_art_multi_relationship_data_document import ArtistsProfileArtMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artists_profile_art_relationship_update_operation_payload import ArtistsProfileArtRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.artists_radio_multi_relationship_data_document import ArtistsRadioMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artists_roles_multi_relationship_data_document import ArtistsRolesMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artists_similar_artists_multi_relationship_data_document import ArtistsSimilarArtistsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artists_single_resource_data_document import ArtistsSingleResourceDataDocument  # noqa: F401
from tidal.models.artists_track_providers_multi_relationship_data_document import ArtistsTrackProvidersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artists_tracks_multi_relationship_data_document import ArtistsTracksMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artists_update_operation_payload import ArtistsUpdateOperationPayload  # noqa: F401
from tidal.models.artists_videos_multi_relationship_data_document import ArtistsVideosMultiRelationshipDataDocument  # noqa: F401
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


def test_artists_get(client: TestClient):
    """Test case for artists_get

    Get multiple artists.
    """
    params = [("country_code", 'US'),     ("filter_handle", ['filter_handle_example']),     ("filter_id", ['filter_id_example']),     ("filter_owners_id", ['filter_owners_id_example']),     ("include", ['albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'albums')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_post(client: TestClient):
    """Test case for artists_post

    Create single artist.
    """
    artists_create_operation_payload = tidal.ArtistsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/artists",
    #    headers=headers,
    #    json=artists_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_get(client: TestClient):
    """Test case for artists_id_get

    Get single artist.
    """
    params = [("country_code", 'US'),     ("include", ['albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'albums')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists/{id}".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_patch(client: TestClient):
    """Test case for artists_id_patch

    Update single artist.
    """
    artists_update_operation_payload = tidal.ArtistsUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/artists/{id}".format(id='1566'),
    #    headers=headers,
    #    json=artists_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_albums_get(client: TestClient):
    """Test case for artists_id_relationships_albums_get

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
    #    "/artists/{id}/relationships/albums".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_banner_art_get(client: TestClient):
    """Test case for artists_id_relationships_banner_art_get

    Get bannerArt relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['bannerArt']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists/{id}/relationships/bannerArt".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_banner_art_patch(client: TestClient):
    """Test case for artists_id_relationships_banner_art_patch

    Update bannerArt relationship (\"to-many\").
    """
    artists_banner_art_relationship_update_operation_payload = tidal.ArtistsBannerArtRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/artists/{id}/relationships/bannerArt".format(id='1566'),
    #    headers=headers,
    #    json=artists_banner_art_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_biography_get(client: TestClient):
    """Test case for artists_id_relationships_biography_get

    Get biography relationship (\"to-one\").
    """
    params = [("country_code", 'US'),     ("include", ['biography'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists/{id}/relationships/biography".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_claim_status_get(client: TestClient):
    """Test case for artists_id_relationships_claim_status_get

    Get claimStatus relationship (\"to-one\").
    """
    params = [("include", ['claimStatus'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists/{id}/relationships/claimStatus".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_followers_get(client: TestClient):
    """Test case for artists_id_relationships_followers_get

    Get followers relationship (\"to-many\").
    """
    params = [("include", ['followers.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'followers.albums'),     ("viewer_context", 'viewer_context_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists/{id}/relationships/followers".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_following_get(client: TestClient):
    """Test case for artists_id_relationships_following_get

    Get following relationship (\"to-many\").
    """
    params = [("include", ['following.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'following.albums'),     ("viewer_context", 'viewer_context_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists/{id}/relationships/following".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_following_post(client: TestClient):
    """Test case for artists_id_relationships_following_post

    Add to following relationship (\"to-many\").
    """
    artists_following_relationship_add_operation_payload = tidal.ArtistsFollowingRelationshipAddOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/artists/{id}/relationships/following".format(id='1566'),
    #    headers=headers,
    #    json=artists_following_relationship_add_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_following_delete(client: TestClient):
    """Test case for artists_id_relationships_following_delete

    Delete from following relationship (\"to-many\").
    """
    artists_following_relationship_remove_operation_payload = tidal.ArtistsFollowingRelationshipRemoveOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/artists/{id}/relationships/following".format(id='1566'),
    #    headers=headers,
    #    json=artists_following_relationship_remove_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_logo_art_get(client: TestClient):
    """Test case for artists_id_relationships_logo_art_get

    Get logoArt relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['logoArt']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists/{id}/relationships/logoArt".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_logo_art_patch(client: TestClient):
    """Test case for artists_id_relationships_logo_art_patch

    Update logoArt relationship (\"to-many\").
    """
    artists_logo_art_relationship_update_operation_payload = tidal.ArtistsLogoArtRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/artists/{id}/relationships/logoArt".format(id='1566'),
    #    headers=headers,
    #    json=artists_logo_art_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_owners_get(client: TestClient):
    """Test case for artists_id_relationships_owners_get

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
    #    "/artists/{id}/relationships/owners".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_profile_art_get(client: TestClient):
    """Test case for artists_id_relationships_profile_art_get

    Get profileArt relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['profileArt']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists/{id}/relationships/profileArt".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_profile_art_patch(client: TestClient):
    """Test case for artists_id_relationships_profile_art_patch

    Update profileArt relationship (\"to-many\").
    """
    artists_profile_art_relationship_update_operation_payload = tidal.ArtistsProfileArtRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/artists/{id}/relationships/profileArt".format(id='1566'),
    #    headers=headers,
    #    json=artists_profile_art_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_radio_get(client: TestClient):
    """Test case for artists_id_relationships_radio_get

    Get radio relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['radio.items']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'radio.items')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists/{id}/relationships/radio".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_roles_get(client: TestClient):
    """Test case for artists_id_relationships_roles_get

    Get roles relationship (\"to-many\").
    """
    params = [("include", ['roles']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists/{id}/relationships/roles".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_similar_artists_get(client: TestClient):
    """Test case for artists_id_relationships_similar_artists_get

    Get similarArtists relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['similarArtists.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'similarArtists.albums')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists/{id}/relationships/similarArtists".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_track_providers_get(client: TestClient):
    """Test case for artists_id_relationships_track_providers_get

    Get trackProviders relationship (\"to-many\").
    """
    params = [("include", ['trackProviders']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists/{id}/relationships/trackProviders".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_tracks_get(client: TestClient):
    """Test case for artists_id_relationships_tracks_get

    Get tracks relationship (\"to-many\").
    """
    params = [("collapse_by", 'FINGERPRINT'),     ("country_code", 'US'),     ("include", ['tracks']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'tracks')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists/{id}/relationships/tracks".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artists_id_relationships_videos_get(client: TestClient):
    """Test case for artists_id_relationships_videos_get

    Get videos relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['videos']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'videos')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artists/{id}/relationships/videos".format(id='1566'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

