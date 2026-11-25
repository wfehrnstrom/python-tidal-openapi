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
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody  # noqa: F401
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody  # noqa: F401
from tidal.models.subscription_price_change_decisions_create_operation_payload import SubscriptionPriceChangeDecisionsCreateOperationPayload  # noqa: F401
from tidal.models.subscription_price_change_decisions_create_single_resource_data_document import SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.subscription_price_change_decisions_multi_resource_data_document import SubscriptionPriceChangeDecisionsMultiResourceDataDocument  # noqa: F401
from tidal.models.subscription_price_change_decisions_price_change_single_relationship_data_document import SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument  # noqa: F401
from tidal.models.subscription_price_change_decisions_update_operation_payload import SubscriptionPriceChangeDecisionsUpdateOperationPayload  # noqa: F401
from tidal.models.subscription_price_change_decisions_update_single_resource_data_document import SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument  # noqa: F401


def test_subscription_price_change_decisions_get(client: TestClient):
    """Test case for subscription_price_change_decisions_get

    Get multiple subscriptionPriceChangeDecisions.
    """
    params = [("filter_owners_id", ['filter_owners_id_example']),     ("include", ['priceChange']),     ("include_linkage", ['include_linkage_example'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/subscriptionPriceChangeDecisions",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_subscription_price_change_decisions_post(client: TestClient):
    """Test case for subscription_price_change_decisions_post

    Create single subscriptionPriceChangeDecision.
    """
    subscription_price_change_decisions_create_operation_payload = tidal.SubscriptionPriceChangeDecisionsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/subscriptionPriceChangeDecisions",
    #    headers=headers,
    #    json=subscription_price_change_decisions_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_subscription_price_change_decisions_id_patch(client: TestClient):
    """Test case for subscription_price_change_decisions_id_patch

    Update single subscriptionPriceChangeDecision.
    """
    subscription_price_change_decisions_update_operation_payload = tidal.SubscriptionPriceChangeDecisionsUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/subscriptionPriceChangeDecisions/{id}".format(id='1AC1yHZWFAFVjnFOn8XoXA'),
    #    headers=headers,
    #    json=subscription_price_change_decisions_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_subscription_price_change_decisions_id_relationships_price_change_get(client: TestClient):
    """Test case for subscription_price_change_decisions_id_relationships_price_change_get

    Get priceChange relationship (\"to-one\").
    """
    params = [("include", ['priceChange'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/subscriptionPriceChangeDecisions/{id}/relationships/priceChange".format(id='1AC1yHZWFAFVjnFOn8XoXA'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

