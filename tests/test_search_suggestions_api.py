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
from tidal.models.search_suggestions_direct_hits_multi_relationship_data_document import SearchSuggestionsDirectHitsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.search_suggestions_history_multi_relationship_data_document import SearchSuggestionsHistoryMultiRelationshipDataDocument  # noqa: F401
from tidal.models.search_suggestions_multi_resource_data_document import SearchSuggestionsMultiResourceDataDocument  # noqa: F401


def test_search_suggestions_get(client: TestClient):
    """Test case for search_suggestions_get

    Get search suggestions by query.
    """
    params = [("filter_query", 'filter_query_example'),     ("country_code", 'US'),     ("explicit_filter", 'INCLUDE'),     ("include", ['directHits']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'directHits')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/searchSuggestions",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_search_suggestions_id_relationships_direct_hits_get(client: TestClient):
    """Test case for search_suggestions_id_relationships_direct_hits_get

    Get directHits relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("explicit_filter", 'INCLUDE'),     ("include", ['directHits']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'directHits')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/searchSuggestions/{id}/relationships/directHits".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_search_suggestions_id_relationships_history_get(client: TestClient):
    """Test case for search_suggestions_id_relationships_history_get

    Get history relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("explicit_filter", 'INCLUDE'),     ("include", ['history']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/searchSuggestions/{id}/relationships/history".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

