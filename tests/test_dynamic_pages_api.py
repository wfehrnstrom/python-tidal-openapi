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
from tidal.models.dynamic_pages_modules_multi_relationship_data_document import DynamicPagesModulesMultiRelationshipDataDocument  # noqa: F401
from tidal.models.dynamic_pages_multi_resource_data_document import DynamicPagesMultiResourceDataDocument  # noqa: F401
from tidal.models.dynamic_pages_subject_single_relationship_data_document import DynamicPagesSubjectSingleRelationshipDataDocument  # noqa: F401


def test_dynamic_pages_get(client: TestClient):
    """Test case for dynamic_pages_get

    Get multiple dynamicPages.
    """
    params = [("client_version", '2026.0.1'),     ("device_type", 'PHONE'),     ("filter_page_type", ['filter_page_type_example']),     ("system_type", 'IOS'),     ("country_code", 'US'),     ("filter_subject", 'filter_subject_example'),     ("include", ['modules.items']),     ("include_linkage", ['include_linkage_example']),     ("locale", 'en-US'),     ("refresh_seed", 'refresh_seed_example'),     ("replace_media", 'modules.items')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/dynamicPages",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_dynamic_pages_id_relationships_modules_get(client: TestClient):
    """Test case for dynamic_pages_id_relationships_modules_get

    Get modules relationship (\"to-many\").
    """
    params = [("client_version", '2026.0.1'),     ("device_type", 'PHONE'),     ("system_type", 'IOS'),     ("country_code", 'US'),     ("include", ['modules.items']),     ("locale", 'en-US'),     ("page_cursor", 'page_cursor_example'),     ("refresh_seed", 'refresh_seed_example'),     ("replace_media", 'modules.items')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/dynamicPages/{id}/relationships/modules".format(id='nejMcAhh5N8S3EQ4LaqysVdI0cZZ'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_dynamic_pages_id_relationships_subject_get(client: TestClient):
    """Test case for dynamic_pages_id_relationships_subject_get

    Get subject relationship (\"to-one\").
    """
    params = [("include", ['subject']),     ("replace_media", 'subject')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/dynamicPages/{id}/relationships/subject".format(id='nejMcAhh5N8S3EQ4LaqysVdI0cZZ'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

