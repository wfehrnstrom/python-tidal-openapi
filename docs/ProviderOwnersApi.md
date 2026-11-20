# tidal.ProviderOwnersApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**provider_owners_get**](ProviderOwnersApi.md#provider_owners_get) | **GET** /providerOwners | Get multiple providerOwners.
[**provider_owners_id_relationships_owners_get**](ProviderOwnersApi.md#provider_owners_id_relationships_owners_get) | **GET** /providerOwners/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**provider_owners_id_relationships_provider_get**](ProviderOwnersApi.md#provider_owners_id_relationships_provider_get) | **GET** /providerOwners/{id}/relationships/provider | Get provider relationship (\&quot;to-one\&quot;).


# **provider_owners_get**
> ProviderOwnersMultiResourceDataDocument provider_owners_get(filter_owners_id, include=include, include_linkage=include_linkage)

Get multiple providerOwners.

Retrieves multiple providerOwners by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.provider_owners_multi_resource_data_document import ProviderOwnersMultiResourceDataDocument
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
    api_instance = tidal.ProviderOwnersApi(api_client)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`.
    include = ['provider'] # List[str] | Include related resources. Available relationships: owners, provider (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get multiple providerOwners.
        api_response = api_instance.provider_owners_get(filter_owners_id, include=include, include_linkage=include_linkage)
        print("The response of ProviderOwnersApi->provider_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderOwnersApi->provider_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_owners_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners, provider | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 

### Return type

[**ProviderOwnersMultiResourceDataDocument**](ProviderOwnersMultiResourceDataDocument.md)

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

# **provider_owners_id_relationships_owners_get**
> ProviderOwnersOwnersMultiRelationshipDataDocument provider_owners_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.provider_owners_owners_multi_relationship_data_document import ProviderOwnersOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.ProviderOwnersApi(api_client)
    id = 'id_example' # str | Provider owner id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.provider_owners_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of ProviderOwnersApi->provider_owners_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderOwnersApi->provider_owners_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider owner id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**ProviderOwnersOwnersMultiRelationshipDataDocument**](ProviderOwnersOwnersMultiRelationshipDataDocument.md)

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

# **provider_owners_id_relationships_provider_get**
> ProviderOwnersProviderSingleRelationshipDataDocument provider_owners_id_relationships_provider_get(id, include=include)

Get provider relationship (\"to-one\").

Retrieves provider relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.provider_owners_provider_single_relationship_data_document import ProviderOwnersProviderSingleRelationshipDataDocument
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
    api_instance = tidal.ProviderOwnersApi(api_client)
    id = 'id_example' # str | Provider owner id
    include = ['provider'] # List[str] | Include related resources. Available relationships: provider (optional)

    try:
        # Get provider relationship (\"to-one\").
        api_response = api_instance.provider_owners_id_relationships_provider_get(id, include=include)
        print("The response of ProviderOwnersApi->provider_owners_id_relationships_provider_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderOwnersApi->provider_owners_id_relationships_provider_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider owner id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: provider | [optional] 

### Return type

[**ProviderOwnersProviderSingleRelationshipDataDocument**](ProviderOwnersProviderSingleRelationshipDataDocument.md)

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

