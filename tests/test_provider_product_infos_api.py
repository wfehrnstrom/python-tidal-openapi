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
from tidal.models.provider_product_infos_multi_resource_data_document import ProviderProductInfosMultiResourceDataDocument  # noqa: F401
from tidal.models.provider_product_infos_provider_single_relationship_data_document import ProviderProductInfosProviderSingleRelationshipDataDocument  # noqa: F401
from tidal.models.provider_product_infos_subject_single_relationship_data_document import ProviderProductInfosSubjectSingleRelationshipDataDocument  # noqa: F401


def test_provider_product_infos_get(client: TestClient):
    """Test case for provider_product_infos_get

    Get multiple providerProductInfos.
    """
    params = [("filter_provider_id", ['filter_provider_id_example']),     ("country_code", 'US'),     ("filter_barcode_id", ['filter_barcode_id_example']),     ("filter_grid", ['filter_grid_example']),     ("include", ['subject']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'subject')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/providerProductInfos",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_provider_product_infos_id_relationships_provider_get(client: TestClient):
    """Test case for provider_product_infos_id_relationships_provider_get

    Get provider relationship (\"to-one\").
    """
    params = [("include", ['provider'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/providerProductInfos/{id}/relationships/provider".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_provider_product_infos_id_relationships_subject_get(client: TestClient):
    """Test case for provider_product_infos_id_relationships_subject_get

    Get subject relationship (\"to-one\").
    """
    params = [("country_code", 'US'),     ("include", ['subject']),     ("replace_media", 'subject')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/providerProductInfos/{id}/relationships/subject".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

