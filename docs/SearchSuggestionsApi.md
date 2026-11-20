# tidal.SearchSuggestionsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_suggestions_get**](SearchSuggestionsApi.md#search_suggestions_get) | **GET** /searchSuggestions | Get search suggestions by query.
[**search_suggestions_id_relationships_direct_hits_get**](SearchSuggestionsApi.md#search_suggestions_id_relationships_direct_hits_get) | **GET** /searchSuggestions/{id}/relationships/directHits | Get directHits relationship (\&quot;to-many\&quot;).
[**search_suggestions_id_relationships_history_get**](SearchSuggestionsApi.md#search_suggestions_id_relationships_history_get) | **GET** /searchSuggestions/{id}/relationships/history | Get history relationship (\&quot;to-many\&quot;).


# **search_suggestions_get**
> SearchSuggestionsMultiResourceDataDocument search_suggestions_get(filter_query, country_code=country_code, explicit_filter=explicit_filter, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get search suggestions by query.

Searches for a query and returns a collection containing exactly one search suggestions resource.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.search_suggestions_multi_resource_data_document import SearchSuggestionsMultiResourceDataDocument
from tidal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi.tidal.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = tidal.Configuration(
    host = "https://openapi.tidal.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tidal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tidal.SearchSuggestionsApi(api_client)
    filter_query = 'filter_query_example' # str | Search query (e.g. `hello`)
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    explicit_filter = 'INCLUDE' # str | Explicit filter. Valid values: INCLUDE or EXCLUDE (optional) (default to 'INCLUDE')
    include = ['directHits'] # List[str] | Include related resources. Available relationships: directHits, history (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'directHits' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: directHits (optional)

    try:
        # Get search suggestions by query.
        api_response = api_instance.search_suggestions_get(filter_query, country_code=country_code, explicit_filter=explicit_filter, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of SearchSuggestionsApi->search_suggestions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchSuggestionsApi->search_suggestions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_query** | **str**| Search query (e.g. &#x60;hello&#x60;) | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **explicit_filter** | **str**| Explicit filter. Valid values: INCLUDE or EXCLUDE | [optional] [default to &#39;INCLUDE&#39;]
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: directHits, history | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: directHits | [optional] 

### Return type

[**SearchSuggestionsMultiResourceDataDocument**](SearchSuggestionsMultiResourceDataDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE), [Client_Credentials](../README.md#Client_Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**415** | Unsupported request media type or encoding |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_suggestions_id_relationships_direct_hits_get**
> SearchSuggestionsDirectHitsMultiRelationshipDataDocument search_suggestions_id_relationships_direct_hits_get(id, country_code=country_code, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get directHits relationship (\"to-many\").

Retrieves directHits relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.search_suggestions_direct_hits_multi_relationship_data_document import SearchSuggestionsDirectHitsMultiRelationshipDataDocument
from tidal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi.tidal.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = tidal.Configuration(
    host = "https://openapi.tidal.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tidal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tidal.SearchSuggestionsApi(api_client)
    id = 'id_example' # str | An opaque search suggestions identifier
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    explicit_filter = 'INCLUDE' # str | Explicit filter. Valid values: INCLUDE or EXCLUDE (optional) (default to 'INCLUDE')
    include = ['directHits'] # List[str] | Include related resources. Available relationships: directHits (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'directHits' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: directHits (optional)

    try:
        # Get directHits relationship (\"to-many\").
        api_response = api_instance.search_suggestions_id_relationships_direct_hits_get(id, country_code=country_code, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of SearchSuggestionsApi->search_suggestions_id_relationships_direct_hits_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchSuggestionsApi->search_suggestions_id_relationships_direct_hits_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An opaque search suggestions identifier | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **explicit_filter** | **str**| Explicit filter. Valid values: INCLUDE or EXCLUDE | [optional] [default to &#39;INCLUDE&#39;]
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: directHits | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: directHits | [optional] 

### Return type

[**SearchSuggestionsDirectHitsMultiRelationshipDataDocument**](SearchSuggestionsDirectHitsMultiRelationshipDataDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE), [Client_Credentials](../README.md#Client_Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**415** | Unsupported request media type or encoding |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_suggestions_id_relationships_history_get**
> SearchSuggestionsHistoryMultiRelationshipDataDocument search_suggestions_id_relationships_history_get(id, country_code=country_code, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor)

Get history relationship (\"to-many\").

Retrieves history relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.search_suggestions_history_multi_relationship_data_document import SearchSuggestionsHistoryMultiRelationshipDataDocument
from tidal.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi.tidal.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = tidal.Configuration(
    host = "https://openapi.tidal.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tidal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tidal.SearchSuggestionsApi(api_client)
    id = 'id_example' # str | An opaque search suggestions identifier
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    explicit_filter = 'INCLUDE' # str | Explicit filter. Valid values: INCLUDE or EXCLUDE (optional) (default to 'INCLUDE')
    include = ['history'] # List[str] | Include related resources. Available relationships: history (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get history relationship (\"to-many\").
        api_response = api_instance.search_suggestions_id_relationships_history_get(id, country_code=country_code, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor)
        print("The response of SearchSuggestionsApi->search_suggestions_id_relationships_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchSuggestionsApi->search_suggestions_id_relationships_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An opaque search suggestions identifier | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **explicit_filter** | **str**| Explicit filter. Valid values: INCLUDE or EXCLUDE | [optional] [default to &#39;INCLUDE&#39;]
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: history | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**SearchSuggestionsHistoryMultiRelationshipDataDocument**](SearchSuggestionsHistoryMultiRelationshipDataDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**415** | Unsupported request media type or encoding |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

