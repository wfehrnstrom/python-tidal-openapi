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
from tidal.models.user_subscription_price_changes_decision_single_relationship_data_document import UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument  # noqa: F401
from tidal.models.user_subscription_price_changes_multi_resource_data_document import UserSubscriptionPriceChangesMultiResourceDataDocument  # noqa: F401


def test_user_subscription_price_changes_get(client: TestClient):
    """Test case for user_subscription_price_changes_get

    Get multiple userSubscriptionPriceChanges.
    """
    params = [("filter_owners_id", ['filter_owners_id_example']),     ("include", ['decision']),     ("include_linkage", ['include_linkage_example'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userSubscriptionPriceChanges",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_subscription_price_changes_id_relationships_decision_get(client: TestClient):
    """Test case for user_subscription_price_changes_id_relationships_decision_get

    Get decision relationship (\"to-one\").
    """
    params = [("include", ['decision'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userSubscriptionPriceChanges/{id}/relationships/decision".format(id='1AC1yHZWFAFVjnFOn8XoXA'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

