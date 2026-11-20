# tidal.PlaylistGenerationSchedulesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playlist_generation_schedules_get**](PlaylistGenerationSchedulesApi.md#playlist_generation_schedules_get) | **GET** /playlistGenerationSchedules | Get multiple playlistGenerationSchedules.
[**playlist_generation_schedules_id_delete**](PlaylistGenerationSchedulesApi.md#playlist_generation_schedules_id_delete) | **DELETE** /playlistGenerationSchedules/{id} | Delete single playlistGenerationSchedule.
[**playlist_generation_schedules_id_get**](PlaylistGenerationSchedulesApi.md#playlist_generation_schedules_id_get) | **GET** /playlistGenerationSchedules/{id} | Get single playlistGenerationSchedule.
[**playlist_generation_schedules_id_patch**](PlaylistGenerationSchedulesApi.md#playlist_generation_schedules_id_patch) | **PATCH** /playlistGenerationSchedules/{id} | Update single playlistGenerationSchedule.
[**playlist_generation_schedules_id_relationships_playlist_get**](PlaylistGenerationSchedulesApi.md#playlist_generation_schedules_id_relationships_playlist_get) | **GET** /playlistGenerationSchedules/{id}/relationships/playlist | Get playlist relationship (\&quot;to-one\&quot;).
[**playlist_generation_schedules_post**](PlaylistGenerationSchedulesApi.md#playlist_generation_schedules_post) | **POST** /playlistGenerationSchedules | Create single playlistGenerationSchedule.


# **playlist_generation_schedules_get**
> PlaylistGenerationSchedulesMultiResourceDataDocument playlist_generation_schedules_get(filter_playlist_id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get multiple playlistGenerationSchedules.

Retrieves multiple playlistGenerationSchedules by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlist_generation_schedules_multi_resource_data_document import PlaylistGenerationSchedulesMultiResourceDataDocument
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
    api_instance = tidal.PlaylistGenerationSchedulesApi(api_client)
    filter_playlist_id = ['filter_playlist_id_example'] # List[str] | Playlist id (e.g. `550e8400-e29b-41d4-a716-446655440000`)
    include = ['playlist.items'] # List[str] | Include related resources. Available relationships: playlist (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'playlist.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlist.items (optional)

    try:
        # Get multiple playlistGenerationSchedules.
        api_response = api_instance.playlist_generation_schedules_get(filter_playlist_id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of PlaylistGenerationSchedulesApi->playlist_generation_schedules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationSchedulesApi->playlist_generation_schedules_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_playlist_id** | [**List[str]**](str.md)| Playlist id (e.g. &#x60;550e8400-e29b-41d4-a716-446655440000&#x60;) | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: playlist | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: playlist.items | [optional] 

### Return type

[**PlaylistGenerationSchedulesMultiResourceDataDocument**](PlaylistGenerationSchedulesMultiResourceDataDocument.md)

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

# **playlist_generation_schedules_id_delete**
> MutationResponseDocument playlist_generation_schedules_id_delete(id, idempotency_key=idempotency_key)

Delete single playlistGenerationSchedule.

Deletes existing playlistGenerationSchedule.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
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
    api_instance = tidal.PlaylistGenerationSchedulesApi(api_client)
    id = 'id_example' # str | 
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)

    try:
        # Delete single playlistGenerationSchedule.
        api_response = api_instance.playlist_generation_schedules_id_delete(id, idempotency_key=idempotency_key)
        print("The response of PlaylistGenerationSchedulesApi->playlist_generation_schedules_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationSchedulesApi->playlist_generation_schedules_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 

### Return type

[**MutationResponseDocument**](MutationResponseDocument.md)

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
**409** | Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlist_generation_schedules_id_get**
> PlaylistGenerationSchedulesSingleResourceDataDocument playlist_generation_schedules_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single playlistGenerationSchedule.

Retrieves single playlistGenerationSchedule by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlist_generation_schedules_single_resource_data_document import PlaylistGenerationSchedulesSingleResourceDataDocument
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
    api_instance = tidal.PlaylistGenerationSchedulesApi(api_client)
    id = 'id_example' # str | 
    include = ['playlist.items'] # List[str] | Include related resources. Available relationships: playlist (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'playlist.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlist.items (optional)

    try:
        # Get single playlistGenerationSchedule.
        api_response = api_instance.playlist_generation_schedules_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of PlaylistGenerationSchedulesApi->playlist_generation_schedules_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationSchedulesApi->playlist_generation_schedules_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: playlist | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: playlist.items | [optional] 

### Return type

[**PlaylistGenerationSchedulesSingleResourceDataDocument**](PlaylistGenerationSchedulesSingleResourceDataDocument.md)

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

# **playlist_generation_schedules_id_patch**
> PlaylistGenerationSchedulesUpdateSingleResourceDataDocument playlist_generation_schedules_id_patch(id, idempotency_key=idempotency_key, playlist_generation_schedules_update_operation_payload=playlist_generation_schedules_update_operation_payload)

Update single playlistGenerationSchedule.

Updates existing playlistGenerationSchedule.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlist_generation_schedules_update_operation_payload import PlaylistGenerationSchedulesUpdateOperationPayload
from tidal.models.playlist_generation_schedules_update_single_resource_data_document import PlaylistGenerationSchedulesUpdateSingleResourceDataDocument
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
    api_instance = tidal.PlaylistGenerationSchedulesApi(api_client)
    id = 'id_example' # str | 
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    playlist_generation_schedules_update_operation_payload = tidal.PlaylistGenerationSchedulesUpdateOperationPayload() # PlaylistGenerationSchedulesUpdateOperationPayload |  (optional)

    try:
        # Update single playlistGenerationSchedule.
        api_response = api_instance.playlist_generation_schedules_id_patch(id, idempotency_key=idempotency_key, playlist_generation_schedules_update_operation_payload=playlist_generation_schedules_update_operation_payload)
        print("The response of PlaylistGenerationSchedulesApi->playlist_generation_schedules_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationSchedulesApi->playlist_generation_schedules_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **playlist_generation_schedules_update_operation_payload** | [**PlaylistGenerationSchedulesUpdateOperationPayload**](PlaylistGenerationSchedulesUpdateOperationPayload.md)|  | [optional] 

### Return type

[**PlaylistGenerationSchedulesUpdateSingleResourceDataDocument**](PlaylistGenerationSchedulesUpdateSingleResourceDataDocument.md)

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
**409** | Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlist_generation_schedules_id_relationships_playlist_get**
> PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument playlist_generation_schedules_id_relationships_playlist_get(id, include=include, replace_media=replace_media)

Get playlist relationship (\"to-one\").

Retrieves playlist relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlist_generation_schedules_playlist_single_relationship_data_document import PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument
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
    api_instance = tidal.PlaylistGenerationSchedulesApi(api_client)
    id = 'id_example' # str | 
    include = ['playlist.items'] # List[str] | Include related resources. Available relationships: playlist (optional)
    replace_media = 'playlist.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playlist.items (optional)

    try:
        # Get playlist relationship (\"to-one\").
        api_response = api_instance.playlist_generation_schedules_id_relationships_playlist_get(id, include=include, replace_media=replace_media)
        print("The response of PlaylistGenerationSchedulesApi->playlist_generation_schedules_id_relationships_playlist_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationSchedulesApi->playlist_generation_schedules_id_relationships_playlist_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: playlist | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: playlist.items | [optional] 

### Return type

[**PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument**](PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument.md)

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

# **playlist_generation_schedules_post**
> PlaylistGenerationSchedulesCreateSingleResourceDataDocument playlist_generation_schedules_post(idempotency_key=idempotency_key, playlist_generation_schedules_create_operation_payload=playlist_generation_schedules_create_operation_payload)

Create single playlistGenerationSchedule.

Creates a new playlistGenerationSchedule.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlist_generation_schedules_create_operation_payload import PlaylistGenerationSchedulesCreateOperationPayload
from tidal.models.playlist_generation_schedules_create_single_resource_data_document import PlaylistGenerationSchedulesCreateSingleResourceDataDocument
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
    api_instance = tidal.PlaylistGenerationSchedulesApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    playlist_generation_schedules_create_operation_payload = tidal.PlaylistGenerationSchedulesCreateOperationPayload() # PlaylistGenerationSchedulesCreateOperationPayload |  (optional)

    try:
        # Create single playlistGenerationSchedule.
        api_response = api_instance.playlist_generation_schedules_post(idempotency_key=idempotency_key, playlist_generation_schedules_create_operation_payload=playlist_generation_schedules_create_operation_payload)
        print("The response of PlaylistGenerationSchedulesApi->playlist_generation_schedules_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistGenerationSchedulesApi->playlist_generation_schedules_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **playlist_generation_schedules_create_operation_payload** | [**PlaylistGenerationSchedulesCreateOperationPayload**](PlaylistGenerationSchedulesCreateOperationPayload.md)|  | [optional] 

### Return type

[**PlaylistGenerationSchedulesCreateSingleResourceDataDocument**](PlaylistGenerationSchedulesCreateSingleResourceDataDocument.md)

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
**403** | Active playlist schedule limit reached |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

