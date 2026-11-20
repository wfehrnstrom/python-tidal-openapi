# tidal.PlaylistGenerationsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playlist_generations_get**](PlaylistGenerationsApi.md#playlist_generations_get) | **GET** /playlistGenerations | Get multiple playlistGenerations.
[**playlist_generations_id_get**](PlaylistGenerationsApi.md#playlist_generations_id_get) | **GET** /playlistGenerations/{id} | Get single playlistGeneration.
[**playlist_generations_id_relationships_base_generation_get**](PlaylistGenerationsApi.md#playlist_generations_id_relationships_base_generation_get) | **GET** /playlistGenerations/{id}/relationships/baseGeneration | Get baseGeneration relationship (\&quot;to-one\&quot;).
[**playlist_generations_id_relationships_playlist_get**](PlaylistGenerationsApi.md#playlist_generations_id_relationships_playlist_get) | **GET** /playlistGenerations/{id}/relationships/playlist | Get playlist relationship (\&quot;to-one\&quot;).
[**playlist_generations_id_relationships_track_preferences_delete**](PlaylistGenerationsApi.md#playlist_generations_id_relationships_track_preferences_delete) | **DELETE** /playlistGenerations/{id}/relationships/trackPreferences | Delete from trackPreferences relationship (\&quot;to-many\&quot;).
[**playlist_generations_id_relationships_track_preferences_get**](PlaylistGenerationsApi.md#playlist_generations_id_relationships_track_preferences_get) | **GET** /playlistGenerations/{id}/relationships/trackPreferences | Get trackPreferences relationship (\&quot;to-many\&quot;).
[**playlist_generations_id_relationships_track_preferences_patch**](PlaylistGenerationsApi.md#playlist_generations_id_relationships_track_preferences_patch) | **PATCH** /playlistGenerations/{id}/relationships/trackPreferences | Update trackPreferences relationship (\&quot;to-many\&quot;).
[**playlist_generations_id_relationships_track_preferences_post**](PlaylistGenerationsApi.md#playlist_generations_id_relationships_track_preferences_post) | **POST** /playlistGenerations/{id}/relationships/trackPreferences | Add to trackPreferences relationship (\&quot;to-many\&quot;).
[**playlist_generations_post**](PlaylistGenerationsApi.md#playlist_generations_post) | **POST** /playlistGenerations | Create single playlistGeneration.


# **playlist_generations_get**
> PlaylistGenerationsMultiResourceDataDocument playlist_generations_get(filter_playlist_id, generation_view=generation_view, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get multiple playlistGenerations.

Retrieves multiple playlistGenerations by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlist_generations_multi_resource_data_document import PlaylistGenerationsMultiResourceDataDocument
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
    api_instance = tidal.PlaylistGenerationsApi(api_client)
    filter_playlist_id = ['filter_playlist_id_example'] # List[str] | Playlist id (e.g. `550e8400-e29b-41d4-a716-446655440000`)
    generation_view = 'CURRENT' # str | CURRENT selects the committed generation. LATEST selects the newest accepted attempt, regardless of status. New values may be added at any time. (optional) (default to 'CURRENT')
    include = ['baseGeneration.trackPreferences'] # List[str] | Include related resources. Available relationships: baseGeneration, playlist, trackPreferences (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'baseGeneration.trackPreferences' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: baseGeneration.trackPreferences (optional)

    try:
        # Get multiple playlistGenerations.
        api_response = api_instance.playlist_generations_get(filter_playlist_id, generation_view=generation_view, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of PlaylistGenerationsApi->playlist_generations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationsApi->playlist_generations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_playlist_id** | [**List[str]**](str.md)| Playlist id (e.g. &#x60;550e8400-e29b-41d4-a716-446655440000&#x60;) | 
 **generation_view** | **str**| CURRENT selects the committed generation. LATEST selects the newest accepted attempt, regardless of status. New values may be added at any time. | [optional] [default to &#39;CURRENT&#39;]
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: baseGeneration, playlist, trackPreferences | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: baseGeneration.trackPreferences | [optional] 

### Return type

[**PlaylistGenerationsMultiResourceDataDocument**](PlaylistGenerationsMultiResourceDataDocument.md)

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

# **playlist_generations_id_get**
> PlaylistGenerationsSingleResourceDataDocument playlist_generations_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single playlistGeneration.

Retrieves single playlistGeneration by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlist_generations_single_resource_data_document import PlaylistGenerationsSingleResourceDataDocument
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
    api_instance = tidal.PlaylistGenerationsApi(api_client)
    id = '10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg' # str | Playlist generation id
    include = ['baseGeneration.trackPreferences'] # List[str] | Include related resources. Available relationships: baseGeneration, playlist, trackPreferences (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'baseGeneration.trackPreferences' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: baseGeneration.trackPreferences (optional)

    try:
        # Get single playlistGeneration.
        api_response = api_instance.playlist_generations_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of PlaylistGenerationsApi->playlist_generations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationsApi->playlist_generations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist generation id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: baseGeneration, playlist, trackPreferences | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: baseGeneration.trackPreferences | [optional] 

### Return type

[**PlaylistGenerationsSingleResourceDataDocument**](PlaylistGenerationsSingleResourceDataDocument.md)

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

# **playlist_generations_id_relationships_base_generation_get**
> PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument playlist_generations_id_relationships_base_generation_get(id, include=include, replace_media=replace_media)

Get baseGeneration relationship (\"to-one\").

Retrieves baseGeneration relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlist_generations_base_generation_single_relationship_data_document import PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument
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
    api_instance = tidal.PlaylistGenerationsApi(api_client)
    id = '10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg' # str | Playlist generation id
    include = ['baseGeneration.trackPreferences'] # List[str] | Include related resources. Available relationships: baseGeneration (optional)
    replace_media = 'baseGeneration.trackPreferences' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: baseGeneration.trackPreferences (optional)

    try:
        # Get baseGeneration relationship (\"to-one\").
        api_response = api_instance.playlist_generations_id_relationships_base_generation_get(id, include=include, replace_media=replace_media)
        print("The response of PlaylistGenerationsApi->playlist_generations_id_relationships_base_generation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationsApi->playlist_generations_id_relationships_base_generation_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist generation id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: baseGeneration | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: baseGeneration.trackPreferences | [optional] 

### Return type

[**PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument**](PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument.md)

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

# **playlist_generations_id_relationships_playlist_get**
> PlaylistGenerationsPlaylistSingleRelationshipDataDocument playlist_generations_id_relationships_playlist_get(id, include=include, replace_media=replace_media)

Get playlist relationship (\"to-one\").

Retrieves playlist relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlist_generations_playlist_single_relationship_data_document import PlaylistGenerationsPlaylistSingleRelationshipDataDocument
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
    api_instance = tidal.PlaylistGenerationsApi(api_client)
    id = '10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg' # str | Playlist generation id
    include = ['playlist.items'] # List[str] | Include related resources. Available relationships: playlist (optional)
    replace_media = 'playlist.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlist.items (optional)

    try:
        # Get playlist relationship (\"to-one\").
        api_response = api_instance.playlist_generations_id_relationships_playlist_get(id, include=include, replace_media=replace_media)
        print("The response of PlaylistGenerationsApi->playlist_generations_id_relationships_playlist_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationsApi->playlist_generations_id_relationships_playlist_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist generation id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: playlist | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: playlist.items | [optional] 

### Return type

[**PlaylistGenerationsPlaylistSingleRelationshipDataDocument**](PlaylistGenerationsPlaylistSingleRelationshipDataDocument.md)

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

# **playlist_generations_id_relationships_track_preferences_delete**
> MutationResponseDocument playlist_generations_id_relationships_track_preferences_delete(id, idempotency_key=idempotency_key, playlist_generations_track_preferences_relationship_remove_operation_payload=playlist_generations_track_preferences_relationship_remove_operation_payload)

Delete from trackPreferences relationship (\"to-many\").

Removes feedback for one track without removing the track from the playlist. An absent entry is unchanged. Returns an acknowledgement; read the relationship again for its current preference version. Requires the current meta.preferenceVersion as meta.expectedPreferenceVersion; stale versions return 409.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.playlist_generations_track_preferences_relationship_remove_operation_payload import PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload
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
    api_instance = tidal.PlaylistGenerationsApi(api_client)
    id = '10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg' # str | Playlist generation id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    playlist_generations_track_preferences_relationship_remove_operation_payload = tidal.PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload() # PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload |  (optional)

    try:
        # Delete from trackPreferences relationship (\"to-many\").
        api_response = api_instance.playlist_generations_id_relationships_track_preferences_delete(id, idempotency_key=idempotency_key, playlist_generations_track_preferences_relationship_remove_operation_payload=playlist_generations_track_preferences_relationship_remove_operation_payload)
        print("The response of PlaylistGenerationsApi->playlist_generations_id_relationships_track_preferences_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationsApi->playlist_generations_id_relationships_track_preferences_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist generation id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **playlist_generations_track_preferences_relationship_remove_operation_payload** | [**PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload**](PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload.md)|  | [optional] 

### Return type

[**MutationResponseDocument**](MutationResponseDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | The playlist state conflicts with the request: the preference version or base generation is stale, or the track preference selected for update does not exist. Refresh the current generation and track preferences before retrying.; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlist_generations_id_relationships_track_preferences_get**
> PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument playlist_generations_id_relationships_track_preferences_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get trackPreferences relationship (\"to-many\").

Retrieves trackPreferences relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlist_generations_track_preferences_multi_relationship_data_document import PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument
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
    api_instance = tidal.PlaylistGenerationsApi(api_client)
    id = '10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg' # str | Playlist generation id
    include = ['trackPreferences'] # List[str] | Include related resources. Available relationships: trackPreferences (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'trackPreferences' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: trackPreferences (optional)

    try:
        # Get trackPreferences relationship (\"to-many\").
        api_response = api_instance.playlist_generations_id_relationships_track_preferences_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of PlaylistGenerationsApi->playlist_generations_id_relationships_track_preferences_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationsApi->playlist_generations_id_relationships_track_preferences_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist generation id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: trackPreferences | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: trackPreferences | [optional] 

### Return type

[**PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument**](PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument.md)

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

# **playlist_generations_id_relationships_track_preferences_patch**
> PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocument playlist_generations_id_relationships_track_preferences_patch(id, idempotency_key=idempotency_key, playlist_generations_track_preferences_relationship_update_operation_payload=playlist_generations_track_preferences_relationship_update_operation_payload)

Update trackPreferences relationship (\"to-many\").

Incrementally updates feedback for one existing track preference, leaving other entries unchanged. Empty data is rejected; a missing entry returns 409. Returns the complete preference snapshot. Requires the current meta.preferenceVersion as meta.expectedPreferenceVersion; stale versions return 409.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlist_generations_track_preferences_relationship_update_operation_payload import PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload
from tidal.models.playlist_generations_track_preferences_update_multi_relationship_data_document import PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocument
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
    api_instance = tidal.PlaylistGenerationsApi(api_client)
    id = '10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg' # str | Playlist generation id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    playlist_generations_track_preferences_relationship_update_operation_payload = tidal.PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload() # PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update trackPreferences relationship (\"to-many\").
        api_response = api_instance.playlist_generations_id_relationships_track_preferences_patch(id, idempotency_key=idempotency_key, playlist_generations_track_preferences_relationship_update_operation_payload=playlist_generations_track_preferences_relationship_update_operation_payload)
        print("The response of PlaylistGenerationsApi->playlist_generations_id_relationships_track_preferences_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationsApi->playlist_generations_id_relationships_track_preferences_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist generation id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **playlist_generations_track_preferences_relationship_update_operation_payload** | [**PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload**](PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayload.md)|  | [optional] 

### Return type

[**PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocument**](PlaylistGenerationsTrackPreferencesUpdateMultiRelationshipDataDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | The playlist state conflicts with the request: the preference version or base generation is stale, or the track preference selected for update does not exist. Refresh the current generation and track preferences before retrying.; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlist_generations_id_relationships_track_preferences_post**
> PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocument playlist_generations_id_relationships_track_preferences_post(id, idempotency_key=idempotency_key, playlist_generations_track_preferences_relationship_add_operation_payload=playlist_generations_track_preferences_relationship_add_operation_payload)

Add to trackPreferences relationship (\"to-many\").

Adds feedback for one track. An existing entry is unchanged, including its preference. Returns the complete preference snapshot. All writes require the current meta.preferenceVersion as meta.expectedPreferenceVersion; stale versions return 409.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlist_generations_track_preferences_add_multi_relationship_data_document import PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocument
from tidal.models.playlist_generations_track_preferences_relationship_add_operation_payload import PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload
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
    api_instance = tidal.PlaylistGenerationsApi(api_client)
    id = '10TwTjJ5EVfyMaTFh1evzyxi0cuSjcbzClSQBtDDX4CXQ7GVg' # str | Playlist generation id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    playlist_generations_track_preferences_relationship_add_operation_payload = tidal.PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload() # PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload |  (optional)

    try:
        # Add to trackPreferences relationship (\"to-many\").
        api_response = api_instance.playlist_generations_id_relationships_track_preferences_post(id, idempotency_key=idempotency_key, playlist_generations_track_preferences_relationship_add_operation_payload=playlist_generations_track_preferences_relationship_add_operation_payload)
        print("The response of PlaylistGenerationsApi->playlist_generations_id_relationships_track_preferences_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationsApi->playlist_generations_id_relationships_track_preferences_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist generation id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **playlist_generations_track_preferences_relationship_add_operation_payload** | [**PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload**](PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload.md)|  | [optional] 

### Return type

[**PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocument**](PlaylistGenerationsTrackPreferencesAddMultiRelationshipDataDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | The playlist state conflicts with the request: the preference version or base generation is stale, or the track preference selected for update does not exist. Refresh the current generation and track preferences before retrying.; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlist_generations_post**
> PlaylistGenerationsCreateSingleResourceDataDocument playlist_generations_post(idempotency_key=idempotency_key, playlist_generations_create_operation_payload=playlist_generations_create_operation_payload)

Create single playlistGeneration.

Creates a new playlistGeneration.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlist_generations_create_operation_payload import PlaylistGenerationsCreateOperationPayload
from tidal.models.playlist_generations_create_single_resource_data_document import PlaylistGenerationsCreateSingleResourceDataDocument
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
    api_instance = tidal.PlaylistGenerationsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    playlist_generations_create_operation_payload = tidal.PlaylistGenerationsCreateOperationPayload() # PlaylistGenerationsCreateOperationPayload |  (optional)

    try:
        # Create single playlistGeneration.
        api_response = api_instance.playlist_generations_post(idempotency_key=idempotency_key, playlist_generations_create_operation_payload=playlist_generations_create_operation_payload)
        print("The response of PlaylistGenerationsApi->playlist_generations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationsApi->playlist_generations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **playlist_generations_create_operation_payload** | [**PlaylistGenerationsCreateOperationPayload**](PlaylistGenerationsCreateOperationPayload.md)|  | [optional] 

### Return type

[**PlaylistGenerationsCreateSingleResourceDataDocument**](PlaylistGenerationsCreateSingleResourceDataDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | Invalid request |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | The playlist state conflicts with the request: the preference version or base generation is stale, or the track preference selected for update does not exist. Refresh the current generation and track preferences before retrying.; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

