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
from tidal.models.purchases_multi_resource_data_document import PurchasesMultiResourceDataDocument  # noqa: F401
from tidal.models.purchases_owners_multi_relationship_data_document import PurchasesOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.purchases_subject_single_relationship_data_document import PurchasesSubjectSingleRelationshipDataDocument  # noqa: F401


def test_purchases_get(client: TestClient):
    """Test case for purchases_get

    Get multiple purchases.
    """
    params = [("filter_owners_id", ['filter_owners_id_example']),     ("filter_subject_type", ['filter_subject_type_example']),     ("include", ['subject']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'subject')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/purchases",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_purchases_id_relationships_owners_get(client: TestClient):
    """Test case for purchases_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/purchases/{id}/relationships/owners".format(id='3fG7kLmN2pQrStUv'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_purchases_id_relationships_subject_get(client: TestClient):
    """Test case for purchases_id_relationships_subject_get

    Get subject relationship (\"to-one\").
    """
    params = [("include", ['subject']),     ("replace_media", 'subject')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/purchases/{id}/relationships/subject".format(id='3fG7kLmN2pQrStUv'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

