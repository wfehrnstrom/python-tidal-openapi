# tidal.ProviderProductInfosApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**provider_product_infos_get**](ProviderProductInfosApi.md#provider_product_infos_get) | **GET** /providerProductInfos | Get multiple providerProductInfos.
[**provider_product_infos_id_relationships_provider_get**](ProviderProductInfosApi.md#provider_product_infos_id_relationships_provider_get) | **GET** /providerProductInfos/{id}/relationships/provider | Get provider relationship (\&quot;to-one\&quot;).
[**provider_product_infos_id_relationships_subject_get**](ProviderProductInfosApi.md#provider_product_infos_id_relationships_subject_get) | **GET** /providerProductInfos/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).


# **provider_product_infos_get**
> ProviderProductInfosMultiResourceDataDocument provider_product_infos_get(filter_provider_id, country_code=country_code, filter_barcode_id=filter_barcode_id, filter_grid=filter_grid, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get multiple providerProductInfos.

Retrieves multiple providerProductInfos by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.provider_product_infos_multi_resource_data_document import ProviderProductInfosMultiResourceDataDocument
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
    api_instance = tidal.ProviderProductInfosApi(api_client)
    filter_provider_id = ['filter_provider_id_example'] # List[str] | Content provider ID (e.g. `50`)
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    filter_barcode_id = ['filter_barcode_id_example'] # List[str] | List of barcode IDs (EAN-13 or UPC-A) (e.g. `00602527336510`) (optional)
    filter_grid = ['filter_grid_example'] # List[str] | List of GRIDs (Global Release Identifier, ISO 7064) (e.g. `A10302B0013941653J`) (optional)
    include = ['subject'] # List[str] | Include related resources. Available relationships: provider, subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject (optional)

    try:
        # Get multiple providerProductInfos.
        api_response = api_instance.provider_product_infos_get(filter_provider_id, country_code=country_code, filter_barcode_id=filter_barcode_id, filter_grid=filter_grid, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of ProviderProductInfosApi->provider_product_infos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderProductInfosApi->provider_product_infos_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_provider_id** | [**List[str]**](str.md)| Content provider ID (e.g. &#x60;50&#x60;) | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **filter_barcode_id** | [**List[str]**](str.md)| List of barcode IDs (EAN-13 or UPC-A) (e.g. &#x60;00602527336510&#x60;) | [optional] 
 **filter_grid** | [**List[str]**](str.md)| List of GRIDs (Global Release Identifier, ISO 7064) (e.g. &#x60;A10302B0013941653J&#x60;) | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: provider, subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject | [optional] 

### Return type

[**ProviderProductInfosMultiResourceDataDocument**](ProviderProductInfosMultiResourceDataDocument.md)

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

# **provider_product_infos_id_relationships_provider_get**
> ProviderProductInfosProviderSingleRelationshipDataDocument provider_product_infos_id_relationships_provider_get(id, include=include)

Get provider relationship (\"to-one\").

Retrieves provider relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.provider_product_infos_provider_single_relationship_data_document import ProviderProductInfosProviderSingleRelationshipDataDocument
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
    api_instance = tidal.ProviderProductInfosApi(api_client)
    id = 'id_example' # str | Provider product info id
    include = ['provider'] # List[str] | Include related resources. Available relationships: provider (optional)

    try:
        # Get provider relationship (\"to-one\").
        api_response = api_instance.provider_product_infos_id_relationships_provider_get(id, include=include)
        print("The response of ProviderProductInfosApi->provider_product_infos_id_relationships_provider_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderProductInfosApi->provider_product_infos_id_relationships_provider_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider product info id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: provider | [optional] 

### Return type

[**ProviderProductInfosProviderSingleRelationshipDataDocument**](ProviderProductInfosProviderSingleRelationshipDataDocument.md)

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

# **provider_product_infos_id_relationships_subject_get**
> ProviderProductInfosSubjectSingleRelationshipDataDocument provider_product_infos_id_relationships_subject_get(id, country_code=country_code, include=include, replace_media=replace_media)

Get subject relationship (\"to-one\").

Retrieves subject relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.provider_product_infos_subject_single_relationship_data_document import ProviderProductInfosSubjectSingleRelationshipDataDocument
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
    api_instance = tidal.ProviderProductInfosApi(api_client)
    id = 'id_example' # str | Provider product info id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['subject'] # List[str] | Include related resources. Available relationships: subject (optional)
    replace_media = 'subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject (optional)

    try:
        # Get subject relationship (\"to-one\").
        api_response = api_instance.provider_product_infos_id_relationships_subject_get(id, country_code=country_code, include=include, replace_media=replace_media)
        print("The response of ProviderProductInfosApi->provider_product_infos_id_relationships_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderProductInfosApi->provider_product_infos_id_relationships_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider product info id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject | [optional] 

### Return type

[**ProviderProductInfosSubjectSingleRelationshipDataDocument**](ProviderProductInfosSubjectSingleRelationshipDataDocument.md)

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

