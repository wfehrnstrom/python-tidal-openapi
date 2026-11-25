# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.artist_claims_accepted_artists_multi_relationship_data_document import ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artist_claims_accepted_artists_relationship_update_operation_payload import ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.artist_claims_create_operation_payload import ArtistClaimsCreateOperationPayload  # noqa: F401
from tidal.models.artist_claims_create_single_resource_data_document import ArtistClaimsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.artist_claims_multi_resource_data_document import ArtistClaimsMultiResourceDataDocument  # noqa: F401
from tidal.models.artist_claims_owners_multi_relationship_data_document import ArtistClaimsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artist_claims_recommended_artists_multi_relationship_data_document import ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artist_claims_single_resource_data_document import ArtistClaimsSingleResourceDataDocument  # noqa: F401
from tidal.models.artist_claims_update_operation_payload import ArtistClaimsUpdateOperationPayload  # noqa: F401
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


def test_artist_claims_get(client: TestClient):
    """Test case for artist_claims_get

    Get multiple artistClaims.
    """
    params = [("filter_owners_id", ['filter_owners_id_example']),     ("include", ['acceptedArtists.albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'acceptedArtists.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artistClaims",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_claims_post(client: TestClient):
    """Test case for artist_claims_post

    Create single artistClaim.
    """
    artist_claims_create_operation_payload = tidal.ArtistClaimsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/artistClaims",
    #    headers=headers,
    #    json=artist_claims_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_claims_id_get(client: TestClient):
    """Test case for artist_claims_id_get

    Get single artistClaim.
    """
    params = [("include", ['acceptedArtists.albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'acceptedArtists.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artistClaims/{id}".format(id='f47ac10b-58cc-4372-a567-0e02b2c3d479'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_claims_id_delete(client: TestClient):
    """Test case for artist_claims_id_delete

    Delete single artistClaim.
    """

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/artistClaims/{id}".format(id='f47ac10b-58cc-4372-a567-0e02b2c3d479'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_claims_id_patch(client: TestClient):
    """Test case for artist_claims_id_patch

    Update single artistClaim.
    """
    artist_claims_update_operation_payload = tidal.ArtistClaimsUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/artistClaims/{id}".format(id='f47ac10b-58cc-4372-a567-0e02b2c3d479'),
    #    headers=headers,
    #    json=artist_claims_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_claims_id_relationships_accepted_artists_get(client: TestClient):
    """Test case for artist_claims_id_relationships_accepted_artists_get

    Get acceptedArtists relationship (\"to-many\").
    """
    params = [("include", ['acceptedArtists.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'acceptedArtists.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artistClaims/{id}/relationships/acceptedArtists".format(id='f47ac10b-58cc-4372-a567-0e02b2c3d479'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_claims_id_relationships_accepted_artists_patch(client: TestClient):
    """Test case for artist_claims_id_relationships_accepted_artists_patch

    Update acceptedArtists relationship (\"to-many\").
    """
    artist_claims_accepted_artists_relationship_update_operation_payload = tidal.ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/artistClaims/{id}/relationships/acceptedArtists".format(id='f47ac10b-58cc-4372-a567-0e02b2c3d479'),
    #    headers=headers,
    #    json=artist_claims_accepted_artists_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_claims_id_relationships_owners_get(client: TestClient):
    """Test case for artist_claims_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artistClaims/{id}/relationships/owners".format(id='f47ac10b-58cc-4372-a567-0e02b2c3d479'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_claims_id_relationships_recommended_artists_get(client: TestClient):
    """Test case for artist_claims_id_relationships_recommended_artists_get

    Get recommendedArtists relationship (\"to-many\").
    """
    params = [("include", ['recommendedArtists.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'recommendedArtists.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artistClaims/{id}/relationships/recommendedArtists".format(id='f47ac10b-58cc-4372-a567-0e02b2c3d479'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

