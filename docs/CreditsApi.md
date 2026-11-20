# tidal.CreditsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credits_id_get**](CreditsApi.md#credits_id_get) | **GET** /credits/{id} | Get single credit.
[**credits_id_relationships_artist_get**](CreditsApi.md#credits_id_relationships_artist_get) | **GET** /credits/{id}/relationships/artist | Get artist relationship (\&quot;to-one\&quot;).
[**credits_id_relationships_category_get**](CreditsApi.md#credits_id_relationships_category_get) | **GET** /credits/{id}/relationships/category | Get category relationship (\&quot;to-one\&quot;).


# **credits_id_get**
> CreditsSingleResourceDataDocument credits_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single credit.

Retrieves single credit by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.credits_single_resource_data_document import CreditsSingleResourceDataDocument
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
    api_instance = tidal.CreditsApi(api_client)
    id = '3fG7kLmN2pQrStUv' # str | Credit id
    include = ['artist.albums'] # List[str] | Include related resources. Available relationships: artist, category (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'artist.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artist.albums (optional)

    try:
        # Get single credit.
        api_response = api_instance.credits_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of CreditsApi->credits_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->credits_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Credit id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artist, category | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artist.albums | [optional] 

### Return type

[**CreditsSingleResourceDataDocument**](CreditsSingleResourceDataDocument.md)

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

# **credits_id_relationships_artist_get**
> CreditsArtistSingleRelationshipDataDocument credits_id_relationships_artist_get(id, include=include, replace_media=replace_media)

Get artist relationship (\"to-one\").

Retrieves artist relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.credits_artist_single_relationship_data_document import CreditsArtistSingleRelationshipDataDocument
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
    api_instance = tidal.CreditsApi(api_client)
    id = '3fG7kLmN2pQrStUv' # str | Credit id
    include = ['artist.albums'] # List[str] | Include related resources. Available relationships: artist (optional)
    replace_media = 'artist.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artist.albums (optional)

    try:
        # Get artist relationship (\"to-one\").
        api_response = api_instance.credits_id_relationships_artist_get(id, include=include, replace_media=replace_media)
        print("The response of CreditsApi->credits_id_relationships_artist_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->credits_id_relationships_artist_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Credit id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artist | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artist.albums | [optional] 

### Return type

[**CreditsArtistSingleRelationshipDataDocument**](CreditsArtistSingleRelationshipDataDocument.md)

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

# **credits_id_relationships_category_get**
> CreditsCategorySingleRelationshipDataDocument credits_id_relationships_category_get(id, include=include)

Get category relationship (\"to-one\").

Retrieves category relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.credits_category_single_relationship_data_document import CreditsCategorySingleRelationshipDataDocument
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
    api_instance = tidal.CreditsApi(api_client)
    id = '3fG7kLmN2pQrStUv' # str | Credit id
    include = ['category'] # List[str] | Include related resources. Available relationships: category (optional)

    try:
        # Get category relationship (\"to-one\").
        api_response = api_instance.credits_id_relationships_category_get(id, include=include)
        print("The response of CreditsApi->credits_id_relationships_category_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->credits_id_relationships_category_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Credit id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: category | [optional] 

### Return type

[**CreditsCategorySingleRelationshipDataDocument**](CreditsCategorySingleRelationshipDataDocument.md)

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

