# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.credits_artist_single_relationship_data_document import CreditsArtistSingleRelationshipDataDocument  # noqa: F401
from tidal.models.credits_category_single_relationship_data_document import CreditsCategorySingleRelationshipDataDocument  # noqa: F401
from tidal.models.credits_single_resource_data_document import CreditsSingleResourceDataDocument  # noqa: F401
from tidal.models.default400_response_body import Default400ResponseBody  # noqa: F401
from tidal.models.default404_response_body import Default404ResponseBody  # noqa: F401
from tidal.models.default405_response_body import Default405ResponseBody  # noqa: F401
from tidal.models.default406_response_body import Default406ResponseBody  # noqa: F401
from tidal.models.default415_response_body import Default415ResponseBody  # noqa: F401
from tidal.models.default429_response_body import Default429ResponseBody  # noqa: F401
from tidal.models.default500_response_body import Default500ResponseBody  # noqa: F401
from tidal.models.default503_response_body import Default503ResponseBody  # noqa: F401


def test_credits_id_get(client: TestClient):
    """Test case for credits_id_get

    Get single credit.
    """
    params = [("include", ['artist.albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'artist.albums')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/credits/{id}".format(id='3fG7kLmN2pQrStUv'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_credits_id_relationships_artist_get(client: TestClient):
    """Test case for credits_id_relationships_artist_get

    Get artist relationship (\"to-one\").
    """
    params = [("include", ['artist.albums']),     ("replace_media", 'artist.albums')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/credits/{id}/relationships/artist".format(id='3fG7kLmN2pQrStUv'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_credits_id_relationships_category_get(client: TestClient):
    """Test case for credits_id_relationships_category_get

    Get category relationship (\"to-one\").
    """
    params = [("include", ['category'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/credits/{id}/relationships/category".format(id='3fG7kLmN2pQrStUv'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

