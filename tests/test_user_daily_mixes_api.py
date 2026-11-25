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
from tidal.models.user_daily_mixes_items_multi_relationship_data_document import UserDailyMixesItemsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_daily_mixes_single_resource_data_document import UserDailyMixesSingleResourceDataDocument  # noqa: F401


def test_user_daily_mixes_id_get(client: TestClient):
    """Test case for user_daily_mixes_id_get

    Get single userDailyMixe.
    """
    params = [("include", ['items.items']),     ("include_linkage", ['include_linkage_example']),     ("locale", 'en-US'),     ("replace_media", 'items.items')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userDailyMixes/{id}".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_daily_mixes_id_relationships_items_get(client: TestClient):
    """Test case for user_daily_mixes_id_relationships_items_get

    Get items relationship (\"to-many\").
    """
    params = [("include", ['items.items']),     ("locale", 'en-US'),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'items.items')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userDailyMixes/{id}/relationships/items".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

