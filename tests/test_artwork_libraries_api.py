# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.artwork_libraries_artworks_multi_relationship_data_document import ArtworkLibrariesArtworksMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artwork_libraries_multi_resource_data_document import ArtworkLibrariesMultiResourceDataDocument  # noqa: F401
from tidal.models.artwork_libraries_random_artwork_single_relationship_data_document import ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument  # noqa: F401
from tidal.models.artwork_libraries_single_resource_data_document import ArtworkLibrariesSingleResourceDataDocument  # noqa: F401
from tidal.models.default400_response_body import Default400ResponseBody  # noqa: F401
from tidal.models.default404_response_body import Default404ResponseBody  # noqa: F401
from tidal.models.default405_response_body import Default405ResponseBody  # noqa: F401
from tidal.models.default406_response_body import Default406ResponseBody  # noqa: F401
from tidal.models.default415_response_body import Default415ResponseBody  # noqa: F401
from tidal.models.default429_response_body import Default429ResponseBody  # noqa: F401
from tidal.models.default500_response_body import Default500ResponseBody  # noqa: F401
from tidal.models.default503_response_body import Default503ResponseBody  # noqa: F401


def test_artwork_libraries_get(client: TestClient):
    """Test case for artwork_libraries_get

    Get multiple artworkLibraries.
    """
    params = [("filter_name", ['filter_name_example']),     ("include", ['artworks']),     ("include_linkage", ['include_linkage_example'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artworkLibraries",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artwork_libraries_id_get(client: TestClient):
    """Test case for artwork_libraries_id_get

    Get single artworkLibrarie.
    """
    params = [("include", ['artworks']),     ("include_linkage", ['include_linkage_example'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artworkLibraries/{id}".format(id='AmX9i1vQ54Db3RZwLBr'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artwork_libraries_id_relationships_artworks_get(client: TestClient):
    """Test case for artwork_libraries_id_relationships_artworks_get

    Get artworks relationship (\"to-many\").
    """
    params = [("include", ['artworks']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artworkLibraries/{id}/relationships/artworks".format(id='AmX9i1vQ54Db3RZwLBr'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artwork_libraries_id_relationships_random_artwork_get(client: TestClient):
    """Test case for artwork_libraries_id_relationships_random_artwork_get

    Get randomArtwork relationship (\"to-one\").
    """
    params = [("include", ['randomArtwork'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artworkLibraries/{id}/relationships/randomArtwork".format(id='AmX9i1vQ54Db3RZwLBr'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

