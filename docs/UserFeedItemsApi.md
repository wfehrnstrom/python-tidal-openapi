# tidal.UserFeedItemsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_feed_items_get**](UserFeedItemsApi.md#user_feed_items_get) | **GET** /userFeedItems | Get multiple userFeedItems.
[**user_feed_items_id_relationships_actors_get**](UserFeedItemsApi.md#user_feed_items_id_relationships_actors_get) | **GET** /userFeedItems/{id}/relationships/actors | Get actors relationship (\&quot;to-many\&quot;).
[**user_feed_items_id_relationships_subject_get**](UserFeedItemsApi.md#user_feed_items_id_relationships_subject_get) | **GET** /userFeedItems/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).


# **user_feed_items_get**
> UserFeedItemsMultiResourceDataDocument user_feed_items_get(filter_owners_id, filter_surface, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media)

Get multiple userFeedItems.

The authenticated user's activity on the selected feed surface.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_feed_items_multi_resource_data_document import UserFeedItemsMultiResourceDataDocument
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
    api_instance = tidal.UserFeedItemsApi(api_client)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`.
    filter_surface = 'filter_surface_example' # str | Feed surface to read (e.g. `INBOX`)
    include = ['actors.albums'] # List[str] | Include related resources. Available relationships: actors, subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'actors.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: actors.albums (optional)

    try:
        # Get multiple userFeedItems.
        api_response = api_instance.user_feed_items_get(filter_owners_id, filter_surface, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of UserFeedItemsApi->user_feed_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFeedItemsApi->user_feed_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_owners_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | 
 **filter_surface** | **str**| Feed surface to read (e.g. &#x60;INBOX&#x60;) | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: actors, subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: actors.albums | [optional] 

### Return type

[**UserFeedItemsMultiResourceDataDocument**](UserFeedItemsMultiResourceDataDocument.md)

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

# **user_feed_items_id_relationships_actors_get**
> UserFeedItemsActorsMultiRelationshipDataDocument user_feed_items_id_relationships_actors_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get actors relationship (\"to-many\").

Artists attributed to the activity. Always empty for `ALBUM_FAVOURITED`, `TRACK_FAVOURITED` and `TRACK_PLAYLISTED`, which are counts only, and for `HISTORY_MIX_READY` and `TRACK_PLAY_MILESTONE`, which nobody else acted on.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_feed_items_actors_multi_relationship_data_document import UserFeedItemsActorsMultiRelationshipDataDocument
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
    api_instance = tidal.UserFeedItemsApi(api_client)
    id = '49XlsRIbQZSrRDe0QZhJ0y9nGzecOTVBOUN8MUUeD1iEbppZTWCgdLaxmzUvtk0K0JodRqxYgJrDQ5DAfi16j2ICfJGJ9MH9S6IvYuKzQAn1UWWSCdMA' # str | Opaque identifier of a user feed item.
    include = ['actors.albums'] # List[str] | Include related resources. Available relationships: actors (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'actors.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: actors.albums (optional)

    try:
        # Get actors relationship (\"to-many\").
        api_response = api_instance.user_feed_items_id_relationships_actors_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of UserFeedItemsApi->user_feed_items_id_relationships_actors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFeedItemsApi->user_feed_items_id_relationships_actors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque identifier of a user feed item. | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: actors | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: actors.albums | [optional] 

### Return type

[**UserFeedItemsActorsMultiRelationshipDataDocument**](UserFeedItemsActorsMultiRelationshipDataDocument.md)

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

# **user_feed_items_id_relationships_subject_get**
> UserFeedItemsSubjectSingleRelationshipDataDocument user_feed_items_id_relationships_subject_get(id, include=include, replace_media=replace_media)

Get subject relationship (\"to-one\").

The resource the activity concerns. For `HISTORY_MIX_READY`, the viewer's history mix as a playlist.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_feed_items_subject_single_relationship_data_document import UserFeedItemsSubjectSingleRelationshipDataDocument
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
    api_instance = tidal.UserFeedItemsApi(api_client)
    id = '49XlsRIbQZSrRDe0QZhJ0y9nGzecOTVBOUN8MUUeD1iEbppZTWCgdLaxmzUvtk0K0JodRqxYgJrDQ5DAfi16j2ICfJGJ9MH9S6IvYuKzQAn1UWWSCdMA' # str | Opaque identifier of a user feed item.
    include = ['subject'] # List[str] | Include related resources. Available relationships: subject (optional)
    replace_media = 'subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject (optional)

    try:
        # Get subject relationship (\"to-one\").
        api_response = api_instance.user_feed_items_id_relationships_subject_get(id, include=include, replace_media=replace_media)
        print("The response of UserFeedItemsApi->user_feed_items_id_relationships_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFeedItemsApi->user_feed_items_id_relationships_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque identifier of a user feed item. | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject | [optional] 

### Return type

[**UserFeedItemsSubjectSingleRelationshipDataDocument**](UserFeedItemsSubjectSingleRelationshipDataDocument.md)

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

