# tidal.UserPlaybackStatesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_playback_states_id_get**](UserPlaybackStatesApi.md#user_playback_states_id_get) | **GET** /userPlaybackStates/{id} | Get single userPlaybackState.
[**user_playback_states_id_patch**](UserPlaybackStatesApi.md#user_playback_states_id_patch) | **PATCH** /userPlaybackStates/{id} | Update single userPlaybackState.
[**user_playback_states_id_relationships_active_player_get**](UserPlaybackStatesApi.md#user_playback_states_id_relationships_active_player_get) | **GET** /userPlaybackStates/{id}/relationships/activePlayer | Get activePlayer relationship (\&quot;to-one\&quot;).
[**user_playback_states_id_relationships_active_player_patch**](UserPlaybackStatesApi.md#user_playback_states_id_relationships_active_player_patch) | **PATCH** /userPlaybackStates/{id}/relationships/activePlayer | Update activePlayer relationship (\&quot;to-one\&quot;).
[**user_playback_states_id_relationships_available_players_delete**](UserPlaybackStatesApi.md#user_playback_states_id_relationships_available_players_delete) | **DELETE** /userPlaybackStates/{id}/relationships/availablePlayers | Delete from availablePlayers relationship (\&quot;to-many\&quot;).
[**user_playback_states_id_relationships_available_players_get**](UserPlaybackStatesApi.md#user_playback_states_id_relationships_available_players_get) | **GET** /userPlaybackStates/{id}/relationships/availablePlayers | Get availablePlayers relationship (\&quot;to-many\&quot;).
[**user_playback_states_id_relationships_available_players_post**](UserPlaybackStatesApi.md#user_playback_states_id_relationships_available_players_post) | **POST** /userPlaybackStates/{id}/relationships/availablePlayers | Add to availablePlayers relationship (\&quot;to-many\&quot;).
[**user_playback_states_id_relationships_change_event_stream_get**](UserPlaybackStatesApi.md#user_playback_states_id_relationships_change_event_stream_get) | **GET** /userPlaybackStates/{id}/relationships/changeEventStream | Get changeEventStream relationship (\&quot;to-one\&quot;).
[**user_playback_states_id_relationships_play_queue_get**](UserPlaybackStatesApi.md#user_playback_states_id_relationships_play_queue_get) | **GET** /userPlaybackStates/{id}/relationships/playQueue | Get playQueue relationship (\&quot;to-one\&quot;).
[**user_playback_states_id_relationships_play_queue_patch**](UserPlaybackStatesApi.md#user_playback_states_id_relationships_play_queue_patch) | **PATCH** /userPlaybackStates/{id}/relationships/playQueue | Update playQueue relationship (\&quot;to-one\&quot;).


# **user_playback_states_id_get**
> UserPlaybackStatesSingleResourceDataDocument user_playback_states_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single userPlaybackState.

Retrieves single userPlaybackState by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_playback_states_single_resource_data_document import UserPlaybackStatesSingleResourceDataDocument
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
    api_instance = tidal.UserPlaybackStatesApi(api_client)
    id = 'me' # str | User playback session id. Use `me` for the authenticated user's resource
    include = ['activePlayer.offlineInventory'] # List[str] | Include related resources. Available relationships: activePlayer, availablePlayers, changeEventStream, playQueue (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'activePlayer.offlineInventory' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: activePlayer.offlineInventory (optional)

    try:
        # Get single userPlaybackState.
        api_response = api_instance.user_playback_states_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of UserPlaybackStatesApi->user_playback_states_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserPlaybackStatesApi->user_playback_states_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: activePlayer, availablePlayers, changeEventStream, playQueue | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: activePlayer.offlineInventory | [optional] 

### Return type

[**UserPlaybackStatesSingleResourceDataDocument**](UserPlaybackStatesSingleResourceDataDocument.md)

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

# **user_playback_states_id_patch**
> UserPlaybackStatesUpdateSingleResourceDataDocument user_playback_states_id_patch(id, idempotency_key=idempotency_key, user_playback_states_update_operation_payload=user_playback_states_update_operation_payload)

Update single userPlaybackState.

Updates existing userPlaybackState.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_playback_states_update_operation_payload import UserPlaybackStatesUpdateOperationPayload
from tidal.models.user_playback_states_update_single_resource_data_document import UserPlaybackStatesUpdateSingleResourceDataDocument
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
    api_instance = tidal.UserPlaybackStatesApi(api_client)
    id = 'me' # str | User playback session id. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_playback_states_update_operation_payload = tidal.UserPlaybackStatesUpdateOperationPayload() # UserPlaybackStatesUpdateOperationPayload |  (optional)

    try:
        # Update single userPlaybackState.
        api_response = api_instance.user_playback_states_id_patch(id, idempotency_key=idempotency_key, user_playback_states_update_operation_payload=user_playback_states_update_operation_payload)
        print("The response of UserPlaybackStatesApi->user_playback_states_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserPlaybackStatesApi->user_playback_states_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_playback_states_update_operation_payload** | [**UserPlaybackStatesUpdateOperationPayload**](UserPlaybackStatesUpdateOperationPayload.md)|  | [optional] 

### Return type

[**UserPlaybackStatesUpdateSingleResourceDataDocument**](UserPlaybackStatesUpdateSingleResourceDataDocument.md)

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

# **user_playback_states_id_relationships_active_player_get**
> UserPlaybackStatesActivePlayerSingleRelationshipDataDocument user_playback_states_id_relationships_active_player_get(id, include=include, replace_media=replace_media)

Get activePlayer relationship (\"to-one\").

Retrieves activePlayer relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_playback_states_active_player_single_relationship_data_document import UserPlaybackStatesActivePlayerSingleRelationshipDataDocument
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
    api_instance = tidal.UserPlaybackStatesApi(api_client)
    id = 'me' # str | User playback session id. Use `me` for the authenticated user's resource
    include = ['activePlayer.offlineInventory'] # List[str] | Include related resources. Available relationships: activePlayer (optional)
    replace_media = 'activePlayer.offlineInventory' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: activePlayer.offlineInventory (optional)

    try:
        # Get activePlayer relationship (\"to-one\").
        api_response = api_instance.user_playback_states_id_relationships_active_player_get(id, include=include, replace_media=replace_media)
        print("The response of UserPlaybackStatesApi->user_playback_states_id_relationships_active_player_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserPlaybackStatesApi->user_playback_states_id_relationships_active_player_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: activePlayer | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: activePlayer.offlineInventory | [optional] 

### Return type

[**UserPlaybackStatesActivePlayerSingleRelationshipDataDocument**](UserPlaybackStatesActivePlayerSingleRelationshipDataDocument.md)

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

# **user_playback_states_id_relationships_active_player_patch**
> UserPlaybackStatesActivePlayerUpdateSingleRelationshipDataDocument user_playback_states_id_relationships_active_player_patch(id, idempotency_key=idempotency_key, user_playback_states_active_player_relationship_update_operation_payload=user_playback_states_active_player_relationship_update_operation_payload)

Update activePlayer relationship (\"to-one\").

Replaces the active-player selection with the supplied owned installation. Explicit null data releases the player without deleting the installation. Returns null linkage when released or when the selected installation has no live attachment. An unavailable selection is retained and becomes visible again when its attachment is refreshed.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_playback_states_active_player_relationship_update_operation_payload import UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload
from tidal.models.user_playback_states_active_player_update_single_relationship_data_document import UserPlaybackStatesActivePlayerUpdateSingleRelationshipDataDocument
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
    api_instance = tidal.UserPlaybackStatesApi(api_client)
    id = 'me' # str | User playback session id. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_playback_states_active_player_relationship_update_operation_payload = tidal.UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload() # UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update activePlayer relationship (\"to-one\").
        api_response = api_instance.user_playback_states_id_relationships_active_player_patch(id, idempotency_key=idempotency_key, user_playback_states_active_player_relationship_update_operation_payload=user_playback_states_active_player_relationship_update_operation_payload)
        print("The response of UserPlaybackStatesApi->user_playback_states_id_relationships_active_player_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserPlaybackStatesApi->user_playback_states_id_relationships_active_player_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_playback_states_active_player_relationship_update_operation_payload** | [**UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload**](UserPlaybackStatesActivePlayerRelationshipUpdateOperationPayload.md)|  | [optional] 

### Return type

[**UserPlaybackStatesActivePlayerUpdateSingleRelationshipDataDocument**](UserPlaybackStatesActivePlayerUpdateSingleRelationshipDataDocument.md)

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

# **user_playback_states_id_relationships_available_players_delete**
> MutationResponseDocument user_playback_states_id_relationships_available_players_delete(id, idempotency_key=idempotency_key, user_playback_states_available_players_relationship_remove_operation_payload=user_playback_states_available_players_relationship_remove_operation_payload)

Delete from availablePlayers relationship (\"to-many\").

Detaches one installation without deleting it. Also releases the active player when it is that installation. Returns an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.user_playback_states_available_players_relationship_remove_operation_payload import UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload
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
    api_instance = tidal.UserPlaybackStatesApi(api_client)
    id = 'me' # str | User playback session id. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_playback_states_available_players_relationship_remove_operation_payload = tidal.UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload() # UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload |  (optional)

    try:
        # Delete from availablePlayers relationship (\"to-many\").
        api_response = api_instance.user_playback_states_id_relationships_available_players_delete(id, idempotency_key=idempotency_key, user_playback_states_available_players_relationship_remove_operation_payload=user_playback_states_available_players_relationship_remove_operation_payload)
        print("The response of UserPlaybackStatesApi->user_playback_states_id_relationships_available_players_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserPlaybackStatesApi->user_playback_states_id_relationships_available_players_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_playback_states_available_players_relationship_remove_operation_payload** | [**UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload**](UserPlaybackStatesAvailablePlayersRelationshipRemoveOperationPayload.md)|  | [optional] 

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
**409** | Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_playback_states_id_relationships_available_players_get**
> UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument user_playback_states_id_relationships_available_players_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get availablePlayers relationship (\"to-many\").

Retrieves availablePlayers relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_playback_states_available_players_multi_relationship_data_document import UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument
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
    api_instance = tidal.UserPlaybackStatesApi(api_client)
    id = 'me' # str | User playback session id. Use `me` for the authenticated user's resource
    include = ['availablePlayers.offlineInventory'] # List[str] | Include related resources. Available relationships: availablePlayers (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'availablePlayers.offlineInventory' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: availablePlayers.offlineInventory (optional)

    try:
        # Get availablePlayers relationship (\"to-many\").
        api_response = api_instance.user_playback_states_id_relationships_available_players_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of UserPlaybackStatesApi->user_playback_states_id_relationships_available_players_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserPlaybackStatesApi->user_playback_states_id_relationships_available_players_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: availablePlayers | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: availablePlayers.offlineInventory | [optional] 

### Return type

[**UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument**](UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument.md)

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

# **user_playback_states_id_relationships_available_players_post**
> UserPlaybackStatesAvailablePlayersAddMultiRelationshipDataDocument user_playback_states_id_relationships_available_players_post(id, idempotency_key=idempotency_key, user_playback_states_available_players_relationship_add_operation_payload=user_playback_states_available_players_relationship_add_operation_payload)

Add to availablePlayers relationship (\"to-many\").

Attaches or refreshes one owned installation as an available player, preserving other attachments. Returns all currently available player linkage.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_playback_states_available_players_add_multi_relationship_data_document import UserPlaybackStatesAvailablePlayersAddMultiRelationshipDataDocument
from tidal.models.user_playback_states_available_players_relationship_add_operation_payload import UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload
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
    api_instance = tidal.UserPlaybackStatesApi(api_client)
    id = 'me' # str | User playback session id. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_playback_states_available_players_relationship_add_operation_payload = tidal.UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload() # UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload |  (optional)

    try:
        # Add to availablePlayers relationship (\"to-many\").
        api_response = api_instance.user_playback_states_id_relationships_available_players_post(id, idempotency_key=idempotency_key, user_playback_states_available_players_relationship_add_operation_payload=user_playback_states_available_players_relationship_add_operation_payload)
        print("The response of UserPlaybackStatesApi->user_playback_states_id_relationships_available_players_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserPlaybackStatesApi->user_playback_states_id_relationships_available_players_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_playback_states_available_players_relationship_add_operation_payload** | [**UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload**](UserPlaybackStatesAvailablePlayersRelationshipAddOperationPayload.md)|  | [optional] 

### Return type

[**UserPlaybackStatesAvailablePlayersAddMultiRelationshipDataDocument**](UserPlaybackStatesAvailablePlayersAddMultiRelationshipDataDocument.md)

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

# **user_playback_states_id_relationships_change_event_stream_get**
> UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument user_playback_states_id_relationships_change_event_stream_get(id, include=include)

Get changeEventStream relationship (\"to-one\").

Retrieves changeEventStream relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_playback_states_change_event_stream_single_relationship_data_document import UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument
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
    api_instance = tidal.UserPlaybackStatesApi(api_client)
    id = 'id_example' # str | 
    include = ['changeEventStream'] # List[str] | Include related resources. Available relationships: changeEventStream (optional)

    try:
        # Get changeEventStream relationship (\"to-one\").
        api_response = api_instance.user_playback_states_id_relationships_change_event_stream_get(id, include=include)
        print("The response of UserPlaybackStatesApi->user_playback_states_id_relationships_change_event_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserPlaybackStatesApi->user_playback_states_id_relationships_change_event_stream_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: changeEventStream | [optional] 

### Return type

[**UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument**](UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument.md)

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

# **user_playback_states_id_relationships_play_queue_get**
> UserPlaybackStatesPlayQueueSingleRelationshipDataDocument user_playback_states_id_relationships_play_queue_get(id, include=include, replace_media=replace_media)

Get playQueue relationship (\"to-one\").

Retrieves playQueue relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_playback_states_play_queue_single_relationship_data_document import UserPlaybackStatesPlayQueueSingleRelationshipDataDocument
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
    api_instance = tidal.UserPlaybackStatesApi(api_client)
    id = 'me' # str | User playback session id. Use `me` for the authenticated user's resource
    include = ['playQueue.current'] # List[str] | Include related resources. Available relationships: playQueue (optional)
    replace_media = 'playQueue.current' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: playQueue.current (optional)

    try:
        # Get playQueue relationship (\"to-one\").
        api_response = api_instance.user_playback_states_id_relationships_play_queue_get(id, include=include, replace_media=replace_media)
        print("The response of UserPlaybackStatesApi->user_playback_states_id_relationships_play_queue_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserPlaybackStatesApi->user_playback_states_id_relationships_play_queue_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: playQueue | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: playQueue.current | [optional] 

### Return type

[**UserPlaybackStatesPlayQueueSingleRelationshipDataDocument**](UserPlaybackStatesPlayQueueSingleRelationshipDataDocument.md)

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

# **user_playback_states_id_relationships_play_queue_patch**
> UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument user_playback_states_id_relationships_play_queue_patch(id, idempotency_key=idempotency_key, user_playback_states_play_queue_relationship_update_operation_payload=user_playback_states_play_queue_relationship_update_operation_payload)

Update playQueue relationship (\"to-one\").

Replaces the selected play queue. Explicit null data clears the selection without deleting the queue. Returns the selected queue linkage, or null data when cleared.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_playback_states_play_queue_relationship_update_operation_payload import UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload
from tidal.models.user_playback_states_play_queue_update_single_relationship_data_document import UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument
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
    api_instance = tidal.UserPlaybackStatesApi(api_client)
    id = 'me' # str | User playback session id. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_playback_states_play_queue_relationship_update_operation_payload = tidal.UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload() # UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update playQueue relationship (\"to-one\").
        api_response = api_instance.user_playback_states_id_relationships_play_queue_patch(id, idempotency_key=idempotency_key, user_playback_states_play_queue_relationship_update_operation_payload=user_playback_states_play_queue_relationship_update_operation_payload)
        print("The response of UserPlaybackStatesApi->user_playback_states_id_relationships_play_queue_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserPlaybackStatesApi->user_playback_states_id_relationships_play_queue_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User playback session id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_playback_states_play_queue_relationship_update_operation_payload** | [**UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload**](UserPlaybackStatesPlayQueueRelationshipUpdateOperationPayload.md)|  | [optional] 

### Return type

[**UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument**](UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument.md)

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

