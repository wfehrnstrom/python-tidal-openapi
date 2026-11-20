# tidal.DynamicPagesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dynamic_pages_get**](DynamicPagesApi.md#dynamic_pages_get) | **GET** /dynamicPages | Get multiple dynamicPages.
[**dynamic_pages_id_relationships_modules_get**](DynamicPagesApi.md#dynamic_pages_id_relationships_modules_get) | **GET** /dynamicPages/{id}/relationships/modules | Get modules relationship (\&quot;to-many\&quot;).
[**dynamic_pages_id_relationships_subject_get**](DynamicPagesApi.md#dynamic_pages_id_relationships_subject_get) | **GET** /dynamicPages/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).


# **dynamic_pages_get**
> DynamicPagesMultiResourceDataDocument dynamic_pages_get(client_version, device_type, filter_page_type, system_type, country_code=country_code, filter_subject=filter_subject, include=include, include_linkage=include_linkage, locale=locale, refresh_seed=refresh_seed, replace_media=replace_media)

Get multiple dynamicPages.

Retrieves multiple dynamicPages by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.dynamic_pages_multi_resource_data_document import DynamicPagesMultiResourceDataDocument
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
    api_instance = tidal.DynamicPagesApi(api_client)
    client_version = '2026.0.1' # str | Client version number
    device_type = 'PHONE' # str | The type of device making the request
    filter_page_type = ['filter_page_type_example'] # List[str] | Type of the page (e.g. `ARTIST`)
    system_type = 'IOS' # str | The system type of the device making the request
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    filter_subject = 'filter_subject_example' # str | The page subject. Its type must match pageType. Required except for HOME_FREE, where it must be omitted. Also accepts `users:me`. (optional)
    include = ['modules.items'] # List[str] | Include related resources. Available relationships: modules, subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    locale = 'en-US' # str | BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. (optional) (default to 'en-US')
    refresh_seed = 'refresh_seed_example' # str | Stable seed used to keep dynamic page and module results consistent across a client session. (optional)
    replace_media = 'modules.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: modules.items (optional)

    try:
        # Get multiple dynamicPages.
        api_response = api_instance.dynamic_pages_get(client_version, device_type, filter_page_type, system_type, country_code=country_code, filter_subject=filter_subject, include=include, include_linkage=include_linkage, locale=locale, refresh_seed=refresh_seed, replace_media=replace_media)
        print("The response of DynamicPagesApi->dynamic_pages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicPagesApi->dynamic_pages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | **str**| Client version number | 
 **device_type** | **str**| The type of device making the request | 
 **filter_page_type** | [**List[str]**](str.md)| Type of the page (e.g. &#x60;ARTIST&#x60;) | 
 **system_type** | **str**| The system type of the device making the request | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **filter_subject** | **str**| The page subject. Its type must match pageType. Required except for HOME_FREE, where it must be omitted. Also accepts &#x60;users:me&#x60;. | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: modules, subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **locale** | **str**| BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. | [optional] [default to &#39;en-US&#39;]
 **refresh_seed** | **str**| Stable seed used to keep dynamic page and module results consistent across a client session. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: modules.items | [optional] 

### Return type

[**DynamicPagesMultiResourceDataDocument**](DynamicPagesMultiResourceDataDocument.md)

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

# **dynamic_pages_id_relationships_modules_get**
> DynamicPagesModulesMultiRelationshipDataDocument dynamic_pages_id_relationships_modules_get(client_version, device_type, id, system_type, country_code=country_code, include=include, locale=locale, page_cursor=page_cursor, refresh_seed=refresh_seed, replace_media=replace_media)

Get modules relationship (\"to-many\").

The page's modules, in display order.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.dynamic_pages_modules_multi_relationship_data_document import DynamicPagesModulesMultiRelationshipDataDocument
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
    api_instance = tidal.DynamicPagesApi(api_client)
    client_version = '2026.0.1' # str | Client version number
    device_type = 'PHONE' # str | The type of device making the request
    id = 'nejMcAhh5N8S3EQ4LaqysVdI0cZZ' # str | DynamicPages Id
    system_type = 'IOS' # str | The system type of the device making the request
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['modules.items'] # List[str] | Include related resources. Available relationships: modules (optional)
    locale = 'en-US' # str | BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. (optional) (default to 'en-US')
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    refresh_seed = 'refresh_seed_example' # str | Stable seed used to keep dynamic page and module results consistent across a client session. (optional)
    replace_media = 'modules.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: modules.items (optional)

    try:
        # Get modules relationship (\"to-many\").
        api_response = api_instance.dynamic_pages_id_relationships_modules_get(client_version, device_type, id, system_type, country_code=country_code, include=include, locale=locale, page_cursor=page_cursor, refresh_seed=refresh_seed, replace_media=replace_media)
        print("The response of DynamicPagesApi->dynamic_pages_id_relationships_modules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicPagesApi->dynamic_pages_id_relationships_modules_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_version** | **str**| Client version number | 
 **device_type** | **str**| The type of device making the request | 
 **id** | **str**| DynamicPages Id | 
 **system_type** | **str**| The system type of the device making the request | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: modules | [optional] 
 **locale** | **str**| BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. | [optional] [default to &#39;en-US&#39;]
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **refresh_seed** | **str**| Stable seed used to keep dynamic page and module results consistent across a client session. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: modules.items | [optional] 

### Return type

[**DynamicPagesModulesMultiRelationshipDataDocument**](DynamicPagesModulesMultiRelationshipDataDocument.md)

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

# **dynamic_pages_id_relationships_subject_get**
> DynamicPagesSubjectSingleRelationshipDataDocument dynamic_pages_id_relationships_subject_get(id, include=include, replace_media=replace_media)

Get subject relationship (\"to-one\").

Retrieves subject relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.dynamic_pages_subject_single_relationship_data_document import DynamicPagesSubjectSingleRelationshipDataDocument
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
    api_instance = tidal.DynamicPagesApi(api_client)
    id = 'nejMcAhh5N8S3EQ4LaqysVdI0cZZ' # str | DynamicPages Id
    include = ['subject'] # List[str] | Include related resources. Available relationships: subject (optional)
    replace_media = 'subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject (optional)

    try:
        # Get subject relationship (\"to-one\").
        api_response = api_instance.dynamic_pages_id_relationships_subject_get(id, include=include, replace_media=replace_media)
        print("The response of DynamicPagesApi->dynamic_pages_id_relationships_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicPagesApi->dynamic_pages_id_relationships_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicPages Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject | [optional] 

### Return type

[**DynamicPagesSubjectSingleRelationshipDataDocument**](DynamicPagesSubjectSingleRelationshipDataDocument.md)

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

