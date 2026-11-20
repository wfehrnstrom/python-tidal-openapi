# tidal.UserDiscoveryMixesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_discovery_mixes_id_get**](UserDiscoveryMixesApi.md#user_discovery_mixes_id_get) | **GET** /userDiscoveryMixes/{id} | Get single userDiscoveryMixe.
[**user_discovery_mixes_id_relationships_items_get**](UserDiscoveryMixesApi.md#user_discovery_mixes_id_relationships_items_get) | **GET** /userDiscoveryMixes/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).


# **user_discovery_mixes_id_get**
> UserDiscoveryMixesSingleResourceDataDocument user_discovery_mixes_id_get(id, include=include, include_linkage=include_linkage, locale=locale, replace_media=replace_media)

Get single userDiscoveryMixe.

Retrieves single userDiscoveryMixe by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_discovery_mixes_single_resource_data_document import UserDiscoveryMixesSingleResourceDataDocument
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
    api_instance = tidal.UserDiscoveryMixesApi(api_client)
    id = 'me' # str | User discovery mixes id. Use `me` for the authenticated user's resource
    include = ['items.items'] # List[str] | Include related resources. Available relationships: items (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    locale = 'en-US' # str | BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. (optional) (default to 'en-US')
    replace_media = 'items.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items (optional)

    try:
        # Get single userDiscoveryMixe.
        api_response = api_instance.user_discovery_mixes_id_get(id, include=include, include_linkage=include_linkage, locale=locale, replace_media=replace_media)
        print("The response of UserDiscoveryMixesApi->user_discovery_mixes_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDiscoveryMixesApi->user_discovery_mixes_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User discovery mixes id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **locale** | **str**| BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. | [optional] [default to &#39;en-US&#39;]
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items.items | [optional] 

### Return type

[**UserDiscoveryMixesSingleResourceDataDocument**](UserDiscoveryMixesSingleResourceDataDocument.md)

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

# **user_discovery_mixes_id_relationships_items_get**
> UserDiscoveryMixesItemsMultiRelationshipDataDocument user_discovery_mixes_id_relationships_items_get(id, include=include, locale=locale, page_cursor=page_cursor, replace_media=replace_media)

Get items relationship (\"to-many\").

Retrieves items relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_discovery_mixes_items_multi_relationship_data_document import UserDiscoveryMixesItemsMultiRelationshipDataDocument
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
    api_instance = tidal.UserDiscoveryMixesApi(api_client)
    id = 'me' # str | User discovery mixes id. Use `me` for the authenticated user's resource
    include = ['items.items'] # List[str] | Include related resources. Available relationships: items (optional)
    locale = 'en-US' # str | BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. (optional) (default to 'en-US')
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'items.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items (optional)

    try:
        # Get items relationship (\"to-many\").
        api_response = api_instance.user_discovery_mixes_id_relationships_items_get(id, include=include, locale=locale, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of UserDiscoveryMixesApi->user_discovery_mixes_id_relationships_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDiscoveryMixesApi->user_discovery_mixes_id_relationships_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User discovery mixes id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items | [optional] 
 **locale** | **str**| BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. | [optional] [default to &#39;en-US&#39;]
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items.items | [optional] 

### Return type

[**UserDiscoveryMixesItemsMultiRelationshipDataDocument**](UserDiscoveryMixesItemsMultiRelationshipDataDocument.md)

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

