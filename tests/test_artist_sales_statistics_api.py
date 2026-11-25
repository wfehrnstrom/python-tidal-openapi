# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.artist_sales_statistics_artist_single_relationship_data_document import ArtistSalesStatisticsArtistSingleRelationshipDataDocument  # noqa: F401
from tidal.models.artist_sales_statistics_multi_resource_data_document import ArtistSalesStatisticsMultiResourceDataDocument  # noqa: F401
from tidal.models.artist_sales_statistics_top_sellers_multi_relationship_data_document import ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.default400_response_body import Default400ResponseBody  # noqa: F401
from tidal.models.default404_response_body import Default404ResponseBody  # noqa: F401
from tidal.models.default405_response_body import Default405ResponseBody  # noqa: F401
from tidal.models.default406_response_body import Default406ResponseBody  # noqa: F401
from tidal.models.default415_response_body import Default415ResponseBody  # noqa: F401
from tidal.models.default429_response_body import Default429ResponseBody  # noqa: F401
from tidal.models.default500_response_body import Default500ResponseBody  # noqa: F401
from tidal.models.default503_response_body import Default503ResponseBody  # noqa: F401


def test_artist_sales_statistics_get(client: TestClient):
    """Test case for artist_sales_statistics_get

    Get multiple artistSalesStatistics.
    """
    params = [("filter_artist_id", ['filter_artist_id_example']),     ("include", ['artist.albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'artist.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artistSalesStatistics",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_sales_statistics_id_relationships_artist_get(client: TestClient):
    """Test case for artist_sales_statistics_id_relationships_artist_get

    Get artist relationship (\"to-one\").
    """
    params = [("include", ['artist.albums']),     ("replace_media", 'artist.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artistSalesStatistics/{id}/relationships/artist".format(id='LPtReLsCUO7kRhYq'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_sales_statistics_id_relationships_top_sellers_get(client: TestClient):
    """Test case for artist_sales_statistics_id_relationships_top_sellers_get

    Get topSellers relationship (\"to-many\").
    """
    params = [("include", ['topSellers']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'topSellers')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artistSalesStatistics/{id}/relationships/topSellers".format(id='LPtReLsCUO7kRhYq'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

