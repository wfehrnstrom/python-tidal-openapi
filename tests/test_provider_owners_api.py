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
from tidal.models.provider_owners_multi_resource_data_document import ProviderOwnersMultiResourceDataDocument  # noqa: F401
from tidal.models.provider_owners_owners_multi_relationship_data_document import ProviderOwnersOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.provider_owners_provider_single_relationship_data_document import ProviderOwnersProviderSingleRelationshipDataDocument  # noqa: F401


def test_provider_owners_get(client: TestClient):
    """Test case for provider_owners_get

    Get multiple providerOwners.
    """
    params = [("filter_owners_id", ['filter_owners_id_example']),     ("include", ['provider']),     ("include_linkage", ['include_linkage_example'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/providerOwners",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_provider_owners_id_relationships_owners_get(client: TestClient):
    """Test case for provider_owners_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/providerOwners/{id}/relationships/owners".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_provider_owners_id_relationships_provider_get(client: TestClient):
    """Test case for provider_owners_id_relationships_provider_get

    Get provider relationship (\"to-one\").
    """
    params = [("include", ['provider'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/providerOwners/{id}/relationships/provider".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

