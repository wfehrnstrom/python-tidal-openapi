# tidal.ArtworkLibrariesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artwork_libraries_get**](ArtworkLibrariesApi.md#artwork_libraries_get) | **GET** /artworkLibraries | Get multiple artworkLibraries.
[**artwork_libraries_id_get**](ArtworkLibrariesApi.md#artwork_libraries_id_get) | **GET** /artworkLibraries/{id} | Get single artworkLibrarie.
[**artwork_libraries_id_relationships_artworks_get**](ArtworkLibrariesApi.md#artwork_libraries_id_relationships_artworks_get) | **GET** /artworkLibraries/{id}/relationships/artworks | Get artworks relationship (\&quot;to-many\&quot;).
[**artwork_libraries_id_relationships_random_artwork_get**](ArtworkLibrariesApi.md#artwork_libraries_id_relationships_random_artwork_get) | **GET** /artworkLibraries/{id}/relationships/randomArtwork | Get randomArtwork relationship (\&quot;to-one\&quot;).


# **artwork_libraries_get**
> ArtworkLibrariesMultiResourceDataDocument artwork_libraries_get(filter_name, include=include, include_linkage=include_linkage)

Get multiple artworkLibraries.

Retrieves multiple artworkLibraries by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artwork_libraries_multi_resource_data_document import ArtworkLibrariesMultiResourceDataDocument
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
    api_instance = tidal.ArtworkLibrariesApi(api_client)
    filter_name = ['filter_name_example'] # List[str] | Library names (e.g. `album-defaults`)
    include = ['artworks'] # List[str] | Include related resources. Available relationships: artworks, randomArtwork (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get multiple artworkLibraries.
        api_response = api_instance.artwork_libraries_get(filter_name, include=include, include_linkage=include_linkage)
        print("The response of ArtworkLibrariesApi->artwork_libraries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtworkLibrariesApi->artwork_libraries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_name** | [**List[str]**](str.md)| Library names (e.g. &#x60;album-defaults&#x60;) | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artworks, randomArtwork | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 

### Return type

[**ArtworkLibrariesMultiResourceDataDocument**](ArtworkLibrariesMultiResourceDataDocument.md)

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

# **artwork_libraries_id_get**
> ArtworkLibrariesSingleResourceDataDocument artwork_libraries_id_get(id, include=include, include_linkage=include_linkage)

Get single artworkLibrarie.

Retrieves single artworkLibrarie by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artwork_libraries_single_resource_data_document import ArtworkLibrariesSingleResourceDataDocument
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
    api_instance = tidal.ArtworkLibrariesApi(api_client)
    id = 'AmX9i1vQ54Db3RZwLBr' # str | Artwork library ID
    include = ['artworks'] # List[str] | Include related resources. Available relationships: artworks, randomArtwork (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get single artworkLibrarie.
        api_response = api_instance.artwork_libraries_id_get(id, include=include, include_linkage=include_linkage)
        print("The response of ArtworkLibrariesApi->artwork_libraries_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtworkLibrariesApi->artwork_libraries_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artwork library ID | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artworks, randomArtwork | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 

### Return type

[**ArtworkLibrariesSingleResourceDataDocument**](ArtworkLibrariesSingleResourceDataDocument.md)

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

# **artwork_libraries_id_relationships_artworks_get**
> ArtworkLibrariesArtworksMultiRelationshipDataDocument artwork_libraries_id_relationships_artworks_get(id, include=include, page_cursor=page_cursor)

Get artworks relationship (\"to-many\").

Artworks in the library that have finished processing and are not flagged or taken down, newest first

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artwork_libraries_artworks_multi_relationship_data_document import ArtworkLibrariesArtworksMultiRelationshipDataDocument
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
    api_instance = tidal.ArtworkLibrariesApi(api_client)
    id = 'AmX9i1vQ54Db3RZwLBr' # str | Artwork library ID
    include = ['artworks'] # List[str] | Include related resources. Available relationships: artworks (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get artworks relationship (\"to-many\").
        api_response = api_instance.artwork_libraries_id_relationships_artworks_get(id, include=include, page_cursor=page_cursor)
        print("The response of ArtworkLibrariesApi->artwork_libraries_id_relationships_artworks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtworkLibrariesApi->artwork_libraries_id_relationships_artworks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artwork library ID | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artworks | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**ArtworkLibrariesArtworksMultiRelationshipDataDocument**](ArtworkLibrariesArtworksMultiRelationshipDataDocument.md)

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

# **artwork_libraries_id_relationships_random_artwork_get**
> ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument artwork_libraries_id_relationships_random_artwork_get(id, include=include)

Get randomArtwork relationship (\"to-one\").

A random artwork from the library, used by clients to supply a default artwork, for example for albums without cover art. Picked per request from the artworks that have finished processing and are not flagged or taken down, and not stored; empty when there are none

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artwork_libraries_random_artwork_single_relationship_data_document import ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument
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
    api_instance = tidal.ArtworkLibrariesApi(api_client)
    id = 'AmX9i1vQ54Db3RZwLBr' # str | Artwork library ID
    include = ['randomArtwork'] # List[str] | Include related resources. Available relationships: randomArtwork (optional)

    try:
        # Get randomArtwork relationship (\"to-one\").
        api_response = api_instance.artwork_libraries_id_relationships_random_artwork_get(id, include=include)
        print("The response of ArtworkLibrariesApi->artwork_libraries_id_relationships_random_artwork_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtworkLibrariesApi->artwork_libraries_id_relationships_random_artwork_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artwork library ID | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: randomArtwork | [optional] 

### Return type

[**ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument**](ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument.md)

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

