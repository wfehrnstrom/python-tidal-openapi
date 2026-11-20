# tidal.SearchResultsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_results_get**](SearchResultsApi.md#search_results_get) | **GET** /searchResults | Get search results by query.
[**search_results_id_relationships_albums_get**](SearchResultsApi.md#search_results_id_relationships_albums_get) | **GET** /searchResults/{id}/relationships/albums | Get albums relationship (\&quot;to-many\&quot;).
[**search_results_id_relationships_artists_get**](SearchResultsApi.md#search_results_id_relationships_artists_get) | **GET** /searchResults/{id}/relationships/artists | Get artists relationship (\&quot;to-many\&quot;).
[**search_results_id_relationships_playlists_get**](SearchResultsApi.md#search_results_id_relationships_playlists_get) | **GET** /searchResults/{id}/relationships/playlists | Get playlists relationship (\&quot;to-many\&quot;).
[**search_results_id_relationships_top_hits_get**](SearchResultsApi.md#search_results_id_relationships_top_hits_get) | **GET** /searchResults/{id}/relationships/topHits | Get topHits relationship (\&quot;to-many\&quot;).
[**search_results_id_relationships_tracks_get**](SearchResultsApi.md#search_results_id_relationships_tracks_get) | **GET** /searchResults/{id}/relationships/tracks | Get tracks relationship (\&quot;to-many\&quot;).
[**search_results_id_relationships_videos_get**](SearchResultsApi.md#search_results_id_relationships_videos_get) | **GET** /searchResults/{id}/relationships/videos | Get videos relationship (\&quot;to-many\&quot;).


# **search_results_get**
> SearchResultsMultiResourceDataDocument search_results_get(filter_query, client_version=client_version, country_code=country_code, device_type=device_type, explicit_filter=explicit_filter, include=include, include_linkage=include_linkage, replace_media=replace_media, system_type=system_type)

Get search results by query.

Searches for a query and returns a collection containing exactly one search results resource.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.search_results_multi_resource_data_document import SearchResultsMultiResourceDataDocument
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
    api_instance = tidal.SearchResultsApi(api_client)
    filter_query = 'filter_query_example' # str | Search query (e.g. `hello`)
    client_version = '2026.0.1' # str | Client version number (optional)
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    device_type = 'PHONE' # str | The type of device making the request (optional)
    explicit_filter = 'INCLUDE' # str | Explicit filter. Valid values: INCLUDE or EXCLUDE (optional) (default to 'INCLUDE')
    include = ['albums'] # List[str] | Include related resources. Available relationships: albums, artists, playlists, topHits, tracks, videos (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums (optional)
    system_type = 'IOS' # str | The system type of the device making the request (optional)

    try:
        # Get search results by query.
        api_response = api_instance.search_results_get(filter_query, client_version=client_version, country_code=country_code, device_type=device_type, explicit_filter=explicit_filter, include=include, include_linkage=include_linkage, replace_media=replace_media, system_type=system_type)
        print("The response of SearchResultsApi->search_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchResultsApi->search_results_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_query** | **str**| Search query (e.g. &#x60;hello&#x60;) | 
 **client_version** | **str**| Client version number | [optional] 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **device_type** | **str**| The type of device making the request | [optional] 
 **explicit_filter** | **str**| Explicit filter. Valid values: INCLUDE or EXCLUDE | [optional] [default to &#39;INCLUDE&#39;]
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: albums, artists, playlists, topHits, tracks, videos | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums | [optional] 
 **system_type** | **str**| The system type of the device making the request | [optional] 

### Return type

[**SearchResultsMultiResourceDataDocument**](SearchResultsMultiResourceDataDocument.md)

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

# **search_results_id_relationships_albums_get**
> SearchResultsAlbumsMultiRelationshipDataDocument search_results_id_relationships_albums_get(id, client_version=client_version, country_code=country_code, device_type=device_type, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor, replace_media=replace_media, system_type=system_type)

Get albums relationship (\"to-many\").

Retrieves albums relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.search_results_albums_multi_relationship_data_document import SearchResultsAlbumsMultiRelationshipDataDocument
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
    api_instance = tidal.SearchResultsApi(api_client)
    id = 'id_example' # str | An opaque search results identifier
    client_version = '2026.0.1' # str | Client version number (optional)
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    device_type = 'PHONE' # str | The type of device making the request (optional)
    explicit_filter = 'INCLUDE' # str | Explicit filter. Valid values: INCLUDE or EXCLUDE (optional) (default to 'INCLUDE')
    include = ['albums'] # List[str] | Include related resources. Available relationships: albums (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums (optional)
    system_type = 'IOS' # str | The system type of the device making the request (optional)

    try:
        # Get albums relationship (\"to-many\").
        api_response = api_instance.search_results_id_relationships_albums_get(id, client_version=client_version, country_code=country_code, device_type=device_type, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor, replace_media=replace_media, system_type=system_type)
        print("The response of SearchResultsApi->search_results_id_relationships_albums_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchResultsApi->search_results_id_relationships_albums_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An opaque search results identifier | 
 **client_version** | **str**| Client version number | [optional] 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **device_type** | **str**| The type of device making the request | [optional] 
 **explicit_filter** | **str**| Explicit filter. Valid values: INCLUDE or EXCLUDE | [optional] [default to &#39;INCLUDE&#39;]
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: albums | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums | [optional] 
 **system_type** | **str**| The system type of the device making the request | [optional] 

### Return type

[**SearchResultsAlbumsMultiRelationshipDataDocument**](SearchResultsAlbumsMultiRelationshipDataDocument.md)

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

# **search_results_id_relationships_artists_get**
> SearchResultsArtistsMultiRelationshipDataDocument search_results_id_relationships_artists_get(id, client_version=client_version, country_code=country_code, device_type=device_type, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor, replace_media=replace_media, system_type=system_type)

Get artists relationship (\"to-many\").

Retrieves artists relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.search_results_artists_multi_relationship_data_document import SearchResultsArtistsMultiRelationshipDataDocument
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
    api_instance = tidal.SearchResultsApi(api_client)
    id = 'id_example' # str | An opaque search results identifier
    client_version = '2026.0.1' # str | Client version number (optional)
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    device_type = 'PHONE' # str | The type of device making the request (optional)
    explicit_filter = 'INCLUDE' # str | Explicit filter. Valid values: INCLUDE or EXCLUDE (optional) (default to 'INCLUDE')
    include = ['artists.albums'] # List[str] | Include related resources. Available relationships: artists (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'artists.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums (optional)
    system_type = 'IOS' # str | The system type of the device making the request (optional)

    try:
        # Get artists relationship (\"to-many\").
        api_response = api_instance.search_results_id_relationships_artists_get(id, client_version=client_version, country_code=country_code, device_type=device_type, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor, replace_media=replace_media, system_type=system_type)
        print("The response of SearchResultsApi->search_results_id_relationships_artists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchResultsApi->search_results_id_relationships_artists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An opaque search results identifier | 
 **client_version** | **str**| Client version number | [optional] 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **device_type** | **str**| The type of device making the request | [optional] 
 **explicit_filter** | **str**| Explicit filter. Valid values: INCLUDE or EXCLUDE | [optional] [default to &#39;INCLUDE&#39;]
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artists | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums | [optional] 
 **system_type** | **str**| The system type of the device making the request | [optional] 

### Return type

[**SearchResultsArtistsMultiRelationshipDataDocument**](SearchResultsArtistsMultiRelationshipDataDocument.md)

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

# **search_results_id_relationships_playlists_get**
> SearchResultsPlaylistsMultiRelationshipDataDocument search_results_id_relationships_playlists_get(id, client_version=client_version, country_code=country_code, device_type=device_type, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor, replace_media=replace_media, system_type=system_type)

Get playlists relationship (\"to-many\").

Retrieves playlists relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.search_results_playlists_multi_relationship_data_document import SearchResultsPlaylistsMultiRelationshipDataDocument
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
    api_instance = tidal.SearchResultsApi(api_client)
    id = 'id_example' # str | An opaque search results identifier
    client_version = '2026.0.1' # str | Client version number (optional)
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    device_type = 'PHONE' # str | The type of device making the request (optional)
    explicit_filter = 'INCLUDE' # str | Explicit filter. Valid values: INCLUDE or EXCLUDE (optional) (default to 'INCLUDE')
    include = ['playlists.items'] # List[str] | Include related resources. Available relationships: playlists (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'playlists.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlists.items (optional)
    system_type = 'IOS' # str | The system type of the device making the request (optional)

    try:
        # Get playlists relationship (\"to-many\").
        api_response = api_instance.search_results_id_relationships_playlists_get(id, client_version=client_version, country_code=country_code, device_type=device_type, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor, replace_media=replace_media, system_type=system_type)
        print("The response of SearchResultsApi->search_results_id_relationships_playlists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchResultsApi->search_results_id_relationships_playlists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An opaque search results identifier | 
 **client_version** | **str**| Client version number | [optional] 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **device_type** | **str**| The type of device making the request | [optional] 
 **explicit_filter** | **str**| Explicit filter. Valid values: INCLUDE or EXCLUDE | [optional] [default to &#39;INCLUDE&#39;]
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: playlists | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: playlists.items | [optional] 
 **system_type** | **str**| The system type of the device making the request | [optional] 

### Return type

[**SearchResultsPlaylistsMultiRelationshipDataDocument**](SearchResultsPlaylistsMultiRelationshipDataDocument.md)

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

# **search_results_id_relationships_top_hits_get**
> SearchResultsTopHitsMultiRelationshipDataDocument search_results_id_relationships_top_hits_get(id, client_version=client_version, country_code=country_code, device_type=device_type, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor, replace_media=replace_media, system_type=system_type)

Get topHits relationship (\"to-many\").

Retrieves topHits relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.search_results_top_hits_multi_relationship_data_document import SearchResultsTopHitsMultiRelationshipDataDocument
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
    api_instance = tidal.SearchResultsApi(api_client)
    id = 'id_example' # str | An opaque search results identifier
    client_version = '2026.0.1' # str | Client version number (optional)
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    device_type = 'PHONE' # str | The type of device making the request (optional)
    explicit_filter = 'INCLUDE' # str | Explicit filter. Valid values: INCLUDE or EXCLUDE (optional) (default to 'INCLUDE')
    include = ['topHits'] # List[str] | Include related resources. Available relationships: topHits (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'topHits' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: topHits (optional)
    system_type = 'IOS' # str | The system type of the device making the request (optional)

    try:
        # Get topHits relationship (\"to-many\").
        api_response = api_instance.search_results_id_relationships_top_hits_get(id, client_version=client_version, country_code=country_code, device_type=device_type, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor, replace_media=replace_media, system_type=system_type)
        print("The response of SearchResultsApi->search_results_id_relationships_top_hits_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchResultsApi->search_results_id_relationships_top_hits_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An opaque search results identifier | 
 **client_version** | **str**| Client version number | [optional] 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **device_type** | **str**| The type of device making the request | [optional] 
 **explicit_filter** | **str**| Explicit filter. Valid values: INCLUDE or EXCLUDE | [optional] [default to &#39;INCLUDE&#39;]
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: topHits | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: topHits | [optional] 
 **system_type** | **str**| The system type of the device making the request | [optional] 

### Return type

[**SearchResultsTopHitsMultiRelationshipDataDocument**](SearchResultsTopHitsMultiRelationshipDataDocument.md)

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

# **search_results_id_relationships_tracks_get**
> SearchResultsTracksMultiRelationshipDataDocument search_results_id_relationships_tracks_get(id, client_version=client_version, country_code=country_code, device_type=device_type, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor, replace_media=replace_media, system_type=system_type)

Get tracks relationship (\"to-many\").

Retrieves tracks relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.search_results_tracks_multi_relationship_data_document import SearchResultsTracksMultiRelationshipDataDocument
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
    api_instance = tidal.SearchResultsApi(api_client)
    id = 'id_example' # str | An opaque search results identifier
    client_version = '2026.0.1' # str | Client version number (optional)
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    device_type = 'PHONE' # str | The type of device making the request (optional)
    explicit_filter = 'INCLUDE' # str | Explicit filter. Valid values: INCLUDE or EXCLUDE (optional) (default to 'INCLUDE')
    include = ['tracks'] # List[str] | Include related resources. Available relationships: tracks (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'tracks' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks (optional)
    system_type = 'IOS' # str | The system type of the device making the request (optional)

    try:
        # Get tracks relationship (\"to-many\").
        api_response = api_instance.search_results_id_relationships_tracks_get(id, client_version=client_version, country_code=country_code, device_type=device_type, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor, replace_media=replace_media, system_type=system_type)
        print("The response of SearchResultsApi->search_results_id_relationships_tracks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchResultsApi->search_results_id_relationships_tracks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An opaque search results identifier | 
 **client_version** | **str**| Client version number | [optional] 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **device_type** | **str**| The type of device making the request | [optional] 
 **explicit_filter** | **str**| Explicit filter. Valid values: INCLUDE or EXCLUDE | [optional] [default to &#39;INCLUDE&#39;]
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: tracks | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: tracks | [optional] 
 **system_type** | **str**| The system type of the device making the request | [optional] 

### Return type

[**SearchResultsTracksMultiRelationshipDataDocument**](SearchResultsTracksMultiRelationshipDataDocument.md)

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

# **search_results_id_relationships_videos_get**
> SearchResultsVideosMultiRelationshipDataDocument search_results_id_relationships_videos_get(id, client_version=client_version, country_code=country_code, device_type=device_type, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor, replace_media=replace_media, system_type=system_type)

Get videos relationship (\"to-many\").

Retrieves videos relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.search_results_videos_multi_relationship_data_document import SearchResultsVideosMultiRelationshipDataDocument
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
    api_instance = tidal.SearchResultsApi(api_client)
    id = 'id_example' # str | An opaque search results identifier
    client_version = '2026.0.1' # str | Client version number (optional)
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    device_type = 'PHONE' # str | The type of device making the request (optional)
    explicit_filter = 'INCLUDE' # str | Explicit filter. Valid values: INCLUDE or EXCLUDE (optional) (default to 'INCLUDE')
    include = ['videos'] # List[str] | Include related resources. Available relationships: videos (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'videos' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos (optional)
    system_type = 'IOS' # str | The system type of the device making the request (optional)

    try:
        # Get videos relationship (\"to-many\").
        api_response = api_instance.search_results_id_relationships_videos_get(id, client_version=client_version, country_code=country_code, device_type=device_type, explicit_filter=explicit_filter, include=include, page_cursor=page_cursor, replace_media=replace_media, system_type=system_type)
        print("The response of SearchResultsApi->search_results_id_relationships_videos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchResultsApi->search_results_id_relationships_videos_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An opaque search results identifier | 
 **client_version** | **str**| Client version number | [optional] 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **device_type** | **str**| The type of device making the request | [optional] 
 **explicit_filter** | **str**| Explicit filter. Valid values: INCLUDE or EXCLUDE | [optional] [default to &#39;INCLUDE&#39;]
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: videos | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: videos | [optional] 
 **system_type** | **str**| The system type of the device making the request | [optional] 

### Return type

[**SearchResultsVideosMultiRelationshipDataDocument**](SearchResultsVideosMultiRelationshipDataDocument.md)

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

