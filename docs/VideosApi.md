# tidal.VideosApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**videos_get**](VideosApi.md#videos_get) | **GET** /videos | Get multiple videos.
[**videos_id_get**](VideosApi.md#videos_id_get) | **GET** /videos/{id} | Get single video.
[**videos_id_relationships_albums_get**](VideosApi.md#videos_id_relationships_albums_get) | **GET** /videos/{id}/relationships/albums | Get albums relationship (\&quot;to-many\&quot;).
[**videos_id_relationships_artists_get**](VideosApi.md#videos_id_relationships_artists_get) | **GET** /videos/{id}/relationships/artists | Get artists relationship (\&quot;to-many\&quot;).
[**videos_id_relationships_credits_get**](VideosApi.md#videos_id_relationships_credits_get) | **GET** /videos/{id}/relationships/credits | Get credits relationship (\&quot;to-many\&quot;).
[**videos_id_relationships_providers_get**](VideosApi.md#videos_id_relationships_providers_get) | **GET** /videos/{id}/relationships/providers | Get providers relationship (\&quot;to-many\&quot;).
[**videos_id_relationships_replacement_get**](VideosApi.md#videos_id_relationships_replacement_get) | **GET** /videos/{id}/relationships/replacement | Get replacement relationship (\&quot;to-one\&quot;).
[**videos_id_relationships_similar_videos_get**](VideosApi.md#videos_id_relationships_similar_videos_get) | **GET** /videos/{id}/relationships/similarVideos | Get similarVideos relationship (\&quot;to-many\&quot;).
[**videos_id_relationships_suggested_videos_get**](VideosApi.md#videos_id_relationships_suggested_videos_get) | **GET** /videos/{id}/relationships/suggestedVideos | Get suggestedVideos relationship (\&quot;to-many\&quot;).
[**videos_id_relationships_thumbnail_art_get**](VideosApi.md#videos_id_relationships_thumbnail_art_get) | **GET** /videos/{id}/relationships/thumbnailArt | Get thumbnailArt relationship (\&quot;to-many\&quot;).
[**videos_id_relationships_usage_rules_get**](VideosApi.md#videos_id_relationships_usage_rules_get) | **GET** /videos/{id}/relationships/usageRules | Get usageRules relationship (\&quot;to-one\&quot;).


# **videos_get**
> VideosMultiResourceDataDocument videos_get(country_code=country_code, filter_id=filter_id, filter_isrc=filter_isrc, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get multiple videos.

Retrieves multiple videos by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.videos_multi_resource_data_document import VideosMultiResourceDataDocument
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
    api_instance = tidal.VideosApi(api_client)
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    filter_id = ['filter_id_example'] # List[str] | List of video IDs (e.g. `75623239`) (optional)
    filter_isrc = ['filter_isrc_example'] # List[str] | List of ISRCs (e.g. `QMJMT1701237`) (optional)
    include = ['albums'] # List[str] | Include related resources. Available relationships: albums, artists, credits, providers, replacement, similarVideos, suggestedVideos, thumbnailArt, usageRules (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums (optional)

    try:
        # Get multiple videos.
        api_response = api_instance.videos_get(country_code=country_code, filter_id=filter_id, filter_isrc=filter_isrc, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of VideosApi->videos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->videos_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **filter_id** | [**List[str]**](str.md)| List of video IDs (e.g. &#x60;75623239&#x60;) | [optional] 
 **filter_isrc** | [**List[str]**](str.md)| List of ISRCs (e.g. &#x60;QMJMT1701237&#x60;) | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: albums, artists, credits, providers, replacement, similarVideos, suggestedVideos, thumbnailArt, usageRules | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums | [optional] 

### Return type

[**VideosMultiResourceDataDocument**](VideosMultiResourceDataDocument.md)

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

# **videos_id_get**
> VideosSingleResourceDataDocument videos_id_get(id, country_code=country_code, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single video.

Retrieves single video by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.videos_single_resource_data_document import VideosSingleResourceDataDocument
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
    api_instance = tidal.VideosApi(api_client)
    id = '75623239' # str | Video id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['albums'] # List[str] | Include related resources. Available relationships: albums, artists, credits, providers, replacement, similarVideos, suggestedVideos, thumbnailArt, usageRules (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums (optional)

    try:
        # Get single video.
        api_response = api_instance.videos_id_get(id, country_code=country_code, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of VideosApi->videos_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->videos_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Video id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: albums, artists, credits, providers, replacement, similarVideos, suggestedVideos, thumbnailArt, usageRules | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums | [optional] 

### Return type

[**VideosSingleResourceDataDocument**](VideosSingleResourceDataDocument.md)

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

# **videos_id_relationships_albums_get**
> VideosAlbumsMultiRelationshipDataDocument videos_id_relationships_albums_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get albums relationship (\"to-many\").

Retrieves albums relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.videos_albums_multi_relationship_data_document import VideosAlbumsMultiRelationshipDataDocument
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
    api_instance = tidal.VideosApi(api_client)
    id = '75623239' # str | Video id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['albums'] # List[str] | Include related resources. Available relationships: albums (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums (optional)

    try:
        # Get albums relationship (\"to-many\").
        api_response = api_instance.videos_id_relationships_albums_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of VideosApi->videos_id_relationships_albums_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->videos_id_relationships_albums_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Video id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: albums | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums | [optional] 

### Return type

[**VideosAlbumsMultiRelationshipDataDocument**](VideosAlbumsMultiRelationshipDataDocument.md)

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

# **videos_id_relationships_artists_get**
> VideosArtistsMultiRelationshipDataDocument videos_id_relationships_artists_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get artists relationship (\"to-many\").

Retrieves artists relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.videos_artists_multi_relationship_data_document import VideosArtistsMultiRelationshipDataDocument
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
    api_instance = tidal.VideosApi(api_client)
    id = '75623239' # str | Video id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['artists.albums'] # List[str] | Include related resources. Available relationships: artists (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'artists.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums (optional)

    try:
        # Get artists relationship (\"to-many\").
        api_response = api_instance.videos_id_relationships_artists_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of VideosApi->videos_id_relationships_artists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->videos_id_relationships_artists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Video id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artists | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums | [optional] 

### Return type

[**VideosArtistsMultiRelationshipDataDocument**](VideosArtistsMultiRelationshipDataDocument.md)

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

# **videos_id_relationships_credits_get**
> VideosCreditsMultiRelationshipDataDocument videos_id_relationships_credits_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get credits relationship (\"to-many\").

Retrieves credits relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.videos_credits_multi_relationship_data_document import VideosCreditsMultiRelationshipDataDocument
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
    api_instance = tidal.VideosApi(api_client)
    id = '75623239' # str | Video id
    include = ['credits.artist.albums'] # List[str] | Include related resources. Available relationships: credits (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'credits.artist.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: credits.artist.albums (optional)

    try:
        # Get credits relationship (\"to-many\").
        api_response = api_instance.videos_id_relationships_credits_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of VideosApi->videos_id_relationships_credits_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->videos_id_relationships_credits_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Video id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: credits | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: credits.artist.albums | [optional] 

### Return type

[**VideosCreditsMultiRelationshipDataDocument**](VideosCreditsMultiRelationshipDataDocument.md)

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

# **videos_id_relationships_providers_get**
> VideosProvidersMultiRelationshipDataDocument videos_id_relationships_providers_get(id, country_code=country_code, include=include, page_cursor=page_cursor)

Get providers relationship (\"to-many\").

Retrieves providers relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.videos_providers_multi_relationship_data_document import VideosProvidersMultiRelationshipDataDocument
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
    api_instance = tidal.VideosApi(api_client)
    id = '75623239' # str | Video id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['providers'] # List[str] | Include related resources. Available relationships: providers (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get providers relationship (\"to-many\").
        api_response = api_instance.videos_id_relationships_providers_get(id, country_code=country_code, include=include, page_cursor=page_cursor)
        print("The response of VideosApi->videos_id_relationships_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->videos_id_relationships_providers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Video id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: providers | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**VideosProvidersMultiRelationshipDataDocument**](VideosProvidersMultiRelationshipDataDocument.md)

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

# **videos_id_relationships_replacement_get**
> VideosReplacementSingleRelationshipDataDocument videos_id_relationships_replacement_get(id, country_code=country_code, include=include, replace_media=replace_media)

Get replacement relationship (\"to-one\").

Retrieves replacement relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.videos_replacement_single_relationship_data_document import VideosReplacementSingleRelationshipDataDocument
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
    api_instance = tidal.VideosApi(api_client)
    id = '75623239' # str | Video id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['replacement'] # List[str] | Include related resources. Available relationships: replacement (optional)
    replace_media = 'replacement' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: replacement (optional)

    try:
        # Get replacement relationship (\"to-one\").
        api_response = api_instance.videos_id_relationships_replacement_get(id, country_code=country_code, include=include, replace_media=replace_media)
        print("The response of VideosApi->videos_id_relationships_replacement_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->videos_id_relationships_replacement_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Video id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: replacement | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: replacement | [optional] 

### Return type

[**VideosReplacementSingleRelationshipDataDocument**](VideosReplacementSingleRelationshipDataDocument.md)

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

# **videos_id_relationships_similar_videos_get**
> VideosSimilarVideosMultiRelationshipDataDocument videos_id_relationships_similar_videos_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get similarVideos relationship (\"to-many\").

Retrieves similarVideos relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.videos_similar_videos_multi_relationship_data_document import VideosSimilarVideosMultiRelationshipDataDocument
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
    api_instance = tidal.VideosApi(api_client)
    id = '75623239' # str | Video id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['similarVideos'] # List[str] | Include related resources. Available relationships: similarVideos (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'similarVideos' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarVideos (optional)

    try:
        # Get similarVideos relationship (\"to-many\").
        api_response = api_instance.videos_id_relationships_similar_videos_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of VideosApi->videos_id_relationships_similar_videos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->videos_id_relationships_similar_videos_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Video id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: similarVideos | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: similarVideos | [optional] 

### Return type

[**VideosSimilarVideosMultiRelationshipDataDocument**](VideosSimilarVideosMultiRelationshipDataDocument.md)

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

# **videos_id_relationships_suggested_videos_get**
> VideosSuggestedVideosMultiRelationshipDataDocument videos_id_relationships_suggested_videos_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get suggestedVideos relationship (\"to-many\").

Retrieves suggestedVideos relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.videos_suggested_videos_multi_relationship_data_document import VideosSuggestedVideosMultiRelationshipDataDocument
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
    api_instance = tidal.VideosApi(api_client)
    id = '75623239' # str | Video id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['suggestedVideos'] # List[str] | Include related resources. Available relationships: suggestedVideos (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'suggestedVideos' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: suggestedVideos (optional)

    try:
        # Get suggestedVideos relationship (\"to-many\").
        api_response = api_instance.videos_id_relationships_suggested_videos_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of VideosApi->videos_id_relationships_suggested_videos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->videos_id_relationships_suggested_videos_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Video id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: suggestedVideos | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: suggestedVideos | [optional] 

### Return type

[**VideosSuggestedVideosMultiRelationshipDataDocument**](VideosSuggestedVideosMultiRelationshipDataDocument.md)

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

# **videos_id_relationships_thumbnail_art_get**
> VideosThumbnailArtMultiRelationshipDataDocument videos_id_relationships_thumbnail_art_get(id, country_code=country_code, include=include, page_cursor=page_cursor)

Get thumbnailArt relationship (\"to-many\").

Retrieves thumbnailArt relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.videos_thumbnail_art_multi_relationship_data_document import VideosThumbnailArtMultiRelationshipDataDocument
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
    api_instance = tidal.VideosApi(api_client)
    id = '75623239' # str | Video id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['thumbnailArt'] # List[str] | Include related resources. Available relationships: thumbnailArt (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get thumbnailArt relationship (\"to-many\").
        api_response = api_instance.videos_id_relationships_thumbnail_art_get(id, country_code=country_code, include=include, page_cursor=page_cursor)
        print("The response of VideosApi->videos_id_relationships_thumbnail_art_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->videos_id_relationships_thumbnail_art_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Video id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: thumbnailArt | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**VideosThumbnailArtMultiRelationshipDataDocument**](VideosThumbnailArtMultiRelationshipDataDocument.md)

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

# **videos_id_relationships_usage_rules_get**
> VideosUsageRulesSingleRelationshipDataDocument videos_id_relationships_usage_rules_get(id, country_code=country_code, include=include)

Get usageRules relationship (\"to-one\").

Retrieves usageRules relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.videos_usage_rules_single_relationship_data_document import VideosUsageRulesSingleRelationshipDataDocument
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
    api_instance = tidal.VideosApi(api_client)
    id = '75623239' # str | Video id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['usageRules'] # List[str] | Include related resources. Available relationships: usageRules (optional)

    try:
        # Get usageRules relationship (\"to-one\").
        api_response = api_instance.videos_id_relationships_usage_rules_get(id, country_code=country_code, include=include)
        print("The response of VideosApi->videos_id_relationships_usage_rules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->videos_id_relationships_usage_rules_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Video id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: usageRules | [optional] 

### Return type

[**VideosUsageRulesSingleRelationshipDataDocument**](VideosUsageRulesSingleRelationshipDataDocument.md)

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

