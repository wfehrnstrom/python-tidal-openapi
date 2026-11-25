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
from tidal.models.dynamic_modules_items_multi_relationship_data_document import DynamicModulesItemsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.dynamic_modules_multi_resource_data_document import DynamicModulesMultiResourceDataDocument  # noqa: F401
from tidal.models.dynamic_modules_seed_item_single_relationship_data_document import DynamicModulesSeedItemSingleRelationshipDataDocument  # noqa: F401
from tidal.models.dynamic_modules_single_resource_data_document import DynamicModulesSingleResourceDataDocument  # noqa: F401


def test_dynamic_modules_get(client: TestClient):
    """Test case for dynamic_modules_get

    Get multiple dynamicModules.
    """
    params = [("client_version", '2026.0.1'),     ("device_type", 'PHONE'),     ("filter_id", ['filter_id_example']),     ("system_type", 'IOS'),     ("country_code", 'US'),     ("include", ['items']),     ("include_linkage", ['include_linkage_example']),     ("locale", 'en-US'),     ("refresh_seed", 'refresh_seed_example'),     ("replace_media", 'items')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/dynamicModules",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_dynamic_modules_id_get(client: TestClient):
    """Test case for dynamic_modules_id_get

    Get single dynamicModule.
    """
    params = [("client_version", '2026.0.1'),     ("device_type", 'PHONE'),     ("system_type", 'IOS'),     ("country_code", 'US'),     ("include", ['items']),     ("include_linkage", ['include_linkage_example']),     ("locale", 'en-US'),     ("refresh_seed", 'refresh_seed_example'),     ("replace_media", 'items')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/dynamicModules/{id}".format(id='nejMcAhh5N8S3EQ4LaqysVdI0cZZ'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_dynamic_modules_id_relationships_items_get(client: TestClient):
    """Test case for dynamic_modules_id_relationships_items_get

    Get items relationship (\"to-many\").
    """
    params = [("client_version", '2026.0.1'),     ("device_type", 'PHONE'),     ("system_type", 'IOS'),     ("country_code", 'US'),     ("include", ['items']),     ("locale", 'en-US'),     ("page_cursor", 'page_cursor_example'),     ("refresh_seed", 'refresh_seed_example'),     ("replace_media", 'items')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/dynamicModules/{id}/relationships/items".format(id='nejMcAhh5N8S3EQ4LaqysVdI0cZZ'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_dynamic_modules_id_relationships_seed_item_get(client: TestClient):
    """Test case for dynamic_modules_id_relationships_seed_item_get

    Get seedItem relationship (\"to-one\").
    """
    params = [("client_version", '2026.0.1'),     ("device_type", 'PHONE'),     ("system_type", 'IOS'),     ("country_code", 'US'),     ("include", ['seedItem']),     ("locale", 'en-US'),     ("refresh_seed", 'refresh_seed_example'),     ("replace_media", 'seedItem')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/dynamicModules/{id}/relationships/seedItem".format(id='nejMcAhh5N8S3EQ4LaqysVdI0cZZ'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

