# tidal.DynamicModulesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dynamic_modules_get**](DynamicModulesApi.md#dynamic_modules_get) | **GET** /dynamicModules | Get multiple dynamicModules.
[**dynamic_modules_id_get**](DynamicModulesApi.md#dynamic_modules_id_get) | **GET** /dynamicModules/{id} | Get single dynamicModule.
[**dynamic_modules_id_relationships_items_get**](DynamicModulesApi.md#dynamic_modules_id_relationships_items_get) | **GET** /dynamicModules/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
[**dynamic_modules_id_relationships_seed_item_get**](DynamicModulesApi.md#dynamic_modules_id_relationships_seed_item_get) | **GET** /dynamicModules/{id}/relationships/seedItem | Get seedItem relationship (\&quot;to-one\&quot;).


# **dynamic_modules_get**
> DynamicModulesMultiResourceDataDocument dynamic_modules_get(client_version, device_type, filter_id, system_type, country_code=country_code, include=include, include_linkage=include_linkage, locale=locale, refresh_seed=refresh_seed, replace_media=replace_media)

Get multiple dynamicModules.

Retrieves multiple dynamicModules by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.dynamic_modules_multi_resource_data_document import DynamicModulesMultiResourceDataDocument
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
    api_instance = tidal.DynamicModulesApi(api_client)
    client_version = '2026.0.1' # str | Client version number
    device_type = 'PHONE' # str | The type of device making the request
    filter_id = ['filter_id_example'] # List[str] | DynamicModules Id (e.g. `nejMcAhh5N8S3EQ4LaqysVdI0cZZ`)
    system_type = 'IOS' # str | The system type of the device making the request
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['items'] # List[str] | Include related resources. Available relationships: items, seedItem (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    locale = 'en-US' # str | BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. (optional) (default to 'en-US')
    refresh_seed = 'refresh_seed_example' # str | Stable seed used to keep dynamic page and module results consistent across a client session. (optional)
    replace_media = 'items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items (optional)

    try:
        # Get multiple dynamicModules.
        api_response = api_instance.dynamic_modules_get(client_version, device_type, filter_id, system_type, country_code=country_code, include=include, include_linkage=include_linkage, locale=locale, refresh_seed=refresh_seed, replace_media=replace_media)
        print("The response of DynamicModulesApi->dynamic_modules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicModulesApi->dynamic_modules_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | **str**| Client version number | 
 **device_type** | **str**| The type of device making the request | 
 **filter_id** | [**List[str]**](str.md)| DynamicModules Id (e.g. &#x60;nejMcAhh5N8S3EQ4LaqysVdI0cZZ&#x60;) | 
 **system_type** | **str**| The system type of the device making the request | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items, seedItem | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **locale** | **str**| BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. | [optional] [default to &#39;en-US&#39;]
 **refresh_seed** | **str**| Stable seed used to keep dynamic page and module results consistent across a client session. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items | [optional] 

### Return type

[**DynamicModulesMultiResourceDataDocument**](DynamicModulesMultiResourceDataDocument.md)

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

# **dynamic_modules_id_get**
> DynamicModulesSingleResourceDataDocument dynamic_modules_id_get(client_version, device_type, id, system_type, country_code=country_code, include=include, include_linkage=include_linkage, locale=locale, refresh_seed=refresh_seed, replace_media=replace_media)

Get single dynamicModule.

Retrieves single dynamicModule by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.dynamic_modules_single_resource_data_document import DynamicModulesSingleResourceDataDocument
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
    api_instance = tidal.DynamicModulesApi(api_client)
    client_version = '2026.0.1' # str | Client version number
    device_type = 'PHONE' # str | The type of device making the request
    id = 'nejMcAhh5N8S3EQ4LaqysVdI0cZZ' # str | DynamicModules Id
    system_type = 'IOS' # str | The system type of the device making the request
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['items'] # List[str] | Include related resources. Available relationships: items, seedItem (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    locale = 'en-US' # str | BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. (optional) (default to 'en-US')
    refresh_seed = 'refresh_seed_example' # str | Stable seed used to keep dynamic page and module results consistent across a client session. (optional)
    replace_media = 'items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items (optional)

    try:
        # Get single dynamicModule.
        api_response = api_instance.dynamic_modules_id_get(client_version, device_type, id, system_type, country_code=country_code, include=include, include_linkage=include_linkage, locale=locale, refresh_seed=refresh_seed, replace_media=replace_media)
        print("The response of DynamicModulesApi->dynamic_modules_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicModulesApi->dynamic_modules_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | **str**| Client version number | 
 **device_type** | **str**| The type of device making the request | 
 **id** | **str**| DynamicModules Id | 
 **system_type** | **str**| The system type of the device making the request | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items, seedItem | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **locale** | **str**| BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. | [optional] [default to &#39;en-US&#39;]
 **refresh_seed** | **str**| Stable seed used to keep dynamic page and module results consistent across a client session. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items | [optional] 

### Return type

[**DynamicModulesSingleResourceDataDocument**](DynamicModulesSingleResourceDataDocument.md)

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

# **dynamic_modules_id_relationships_items_get**
> DynamicModulesItemsMultiRelationshipDataDocument dynamic_modules_id_relationships_items_get(client_version, device_type, id, system_type, country_code=country_code, include=include, locale=locale, page_cursor=page_cursor, refresh_seed=refresh_seed, replace_media=replace_media)

Get items relationship (\"to-many\").

The module's items, in order — one stable collection per module, consistent for a given refreshSeed. Reads without a cursor return the first page (the slice a page shelf renders, sized for the module's previewLayout and device) with a continuation cursor; passing the cursor returns subsequent pages.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.dynamic_modules_items_multi_relationship_data_document import DynamicModulesItemsMultiRelationshipDataDocument
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
    api_instance = tidal.DynamicModulesApi(api_client)
    client_version = '2026.0.1' # str | Client version number
    device_type = 'PHONE' # str | The type of device making the request
    id = 'nejMcAhh5N8S3EQ4LaqysVdI0cZZ' # str | DynamicModules Id
    system_type = 'IOS' # str | The system type of the device making the request
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['items'] # List[str] | Include related resources. Available relationships: items (optional)
    locale = 'en-US' # str | BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. (optional) (default to 'en-US')
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    refresh_seed = 'refresh_seed_example' # str | Stable seed used to keep dynamic page and module results consistent across a client session. (optional)
    replace_media = 'items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items (optional)

    try:
        # Get items relationship (\"to-many\").
        api_response = api_instance.dynamic_modules_id_relationships_items_get(client_version, device_type, id, system_type, country_code=country_code, include=include, locale=locale, page_cursor=page_cursor, refresh_seed=refresh_seed, replace_media=replace_media)
        print("The response of DynamicModulesApi->dynamic_modules_id_relationships_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicModulesApi->dynamic_modules_id_relationships_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | **str**| Client version number | 
 **device_type** | **str**| The type of device making the request | 
 **id** | **str**| DynamicModules Id | 
 **system_type** | **str**| The system type of the device making the request | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items | [optional] 
 **locale** | **str**| BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. | [optional] [default to &#39;en-US&#39;]
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **refresh_seed** | **str**| Stable seed used to keep dynamic page and module results consistent across a client session. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items | [optional] 

### Return type

[**DynamicModulesItemsMultiRelationshipDataDocument**](DynamicModulesItemsMultiRelationshipDataDocument.md)

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

# **dynamic_modules_id_relationships_seed_item_get**
> DynamicModulesSeedItemSingleRelationshipDataDocument dynamic_modules_id_relationships_seed_item_get(client_version, device_type, id, system_type, country_code=country_code, include=include, locale=locale, refresh_seed=refresh_seed, replace_media=replace_media)

Get seedItem relationship (\"to-one\").

The item whose listen or add event seeded this module's collection (e.g. the album a BECAUSE_YOU_* module is based on); null for modules that are not seeded by an item.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.dynamic_modules_seed_item_single_relationship_data_document import DynamicModulesSeedItemSingleRelationshipDataDocument
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
    api_instance = tidal.DynamicModulesApi(api_client)
    client_version = '2026.0.1' # str | Client version number
    device_type = 'PHONE' # str | The type of device making the request
    id = 'nejMcAhh5N8S3EQ4LaqysVdI0cZZ' # str | DynamicModules Id
    system_type = 'IOS' # str | The system type of the device making the request
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['seedItem'] # List[str] | Include related resources. Available relationships: seedItem (optional)
    locale = 'en-US' # str | BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. (optional) (default to 'en-US')
    refresh_seed = 'refresh_seed_example' # str | Stable seed used to keep dynamic page and module results consistent across a client session. (optional)
    replace_media = 'seedItem' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: seedItem (optional)

    try:
        # Get seedItem relationship (\"to-one\").
        api_response = api_instance.dynamic_modules_id_relationships_seed_item_get(client_version, device_type, id, system_type, country_code=country_code, include=include, locale=locale, refresh_seed=refresh_seed, replace_media=replace_media)
        print("The response of DynamicModulesApi->dynamic_modules_id_relationships_seed_item_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicModulesApi->dynamic_modules_id_relationships_seed_item_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | **str**| Client version number | 
 **device_type** | **str**| The type of device making the request | 
 **id** | **str**| DynamicModules Id | 
 **system_type** | **str**| The system type of the device making the request | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: seedItem | [optional] 
 **locale** | **str**| BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. | [optional] [default to &#39;en-US&#39;]
 **refresh_seed** | **str**| Stable seed used to keep dynamic page and module results consistent across a client session. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: seedItem | [optional] 

### Return type

[**DynamicModulesSeedItemSingleRelationshipDataDocument**](DynamicModulesSeedItemSingleRelationshipDataDocument.md)

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

