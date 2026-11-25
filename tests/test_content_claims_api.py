# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.content_claims_claimed_resource_single_relationship_data_document import ContentClaimsClaimedResourceSingleRelationshipDataDocument  # noqa: F401
from tidal.models.content_claims_claiming_artist_single_relationship_data_document import ContentClaimsClaimingArtistSingleRelationshipDataDocument  # noqa: F401
from tidal.models.content_claims_create_operation_payload import ContentClaimsCreateOperationPayload  # noqa: F401
from tidal.models.content_claims_create_single_resource_data_document import ContentClaimsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.content_claims_multi_resource_data_document import ContentClaimsMultiResourceDataDocument  # noqa: F401
from tidal.models.content_claims_owners_multi_relationship_data_document import ContentClaimsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.content_claims_single_resource_data_document import ContentClaimsSingleResourceDataDocument  # noqa: F401
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


def test_content_claims_get(client: TestClient):
    """Test case for content_claims_get

    Get multiple contentClaims.
    """
    params = [("filter_owners_id", ['filter_owners_id_example']),     ("include", ['claimedResource']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'claimedResource')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/contentClaims",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_content_claims_post(client: TestClient):
    """Test case for content_claims_post

    Create single contentClaim.
    """
    content_claims_create_operation_payload = tidal.ContentClaimsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/contentClaims",
    #    headers=headers,
    #    json=content_claims_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_content_claims_id_get(client: TestClient):
    """Test case for content_claims_id_get

    Get single contentClaim.
    """
    params = [("include", ['claimedResource']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'claimedResource')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/contentClaims/{id}".format(id='f47ac10b-58cc-4372-a567-0e02b2c3d479'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_content_claims_id_relationships_claimed_resource_get(client: TestClient):
    """Test case for content_claims_id_relationships_claimed_resource_get

    Get claimedResource relationship (\"to-one\").
    """
    params = [("include", ['claimedResource']),     ("replace_media", 'claimedResource')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/contentClaims/{id}/relationships/claimedResource".format(id='f47ac10b-58cc-4372-a567-0e02b2c3d479'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_content_claims_id_relationships_claiming_artist_get(client: TestClient):
    """Test case for content_claims_id_relationships_claiming_artist_get

    Get claimingArtist relationship (\"to-one\").
    """
    params = [("include", ['claimingArtist.albums']),     ("replace_media", 'claimingArtist.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/contentClaims/{id}/relationships/claimingArtist".format(id='f47ac10b-58cc-4372-a567-0e02b2c3d479'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_content_claims_id_relationships_owners_get(client: TestClient):
    """Test case for content_claims_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/contentClaims/{id}/relationships/owners".format(id='f47ac10b-58cc-4372-a567-0e02b2c3d479'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

