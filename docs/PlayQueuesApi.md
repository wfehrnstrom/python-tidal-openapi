# tidal.PlayQueuesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**play_queues_get**](PlayQueuesApi.md#play_queues_get) | **GET** /playQueues | Get multiple playQueues.
[**play_queues_id_delete**](PlayQueuesApi.md#play_queues_id_delete) | **DELETE** /playQueues/{id} | Delete single playQueue.
[**play_queues_id_get**](PlayQueuesApi.md#play_queues_id_get) | **GET** /playQueues/{id} | Get single playQueue.
[**play_queues_id_patch**](PlayQueuesApi.md#play_queues_id_patch) | **PATCH** /playQueues/{id} | Update single playQueue.
[**play_queues_id_relationships_change_event_stream_get**](PlayQueuesApi.md#play_queues_id_relationships_change_event_stream_get) | **GET** /playQueues/{id}/relationships/changeEventStream | Get changeEventStream relationship (\&quot;to-one\&quot;).
[**play_queues_id_relationships_current_get**](PlayQueuesApi.md#play_queues_id_relationships_current_get) | **GET** /playQueues/{id}/relationships/current | Get current relationship (\&quot;to-one\&quot;).
[**play_queues_id_relationships_current_patch**](PlayQueuesApi.md#play_queues_id_relationships_current_patch) | **PATCH** /playQueues/{id}/relationships/current | Update current relationship (\&quot;to-one\&quot;).
[**play_queues_id_relationships_future_delete**](PlayQueuesApi.md#play_queues_id_relationships_future_delete) | **DELETE** /playQueues/{id}/relationships/future | Delete from future relationship (\&quot;to-many\&quot;).
[**play_queues_id_relationships_future_get**](PlayQueuesApi.md#play_queues_id_relationships_future_get) | **GET** /playQueues/{id}/relationships/future | Get future relationship (\&quot;to-many\&quot;).
[**play_queues_id_relationships_future_patch**](PlayQueuesApi.md#play_queues_id_relationships_future_patch) | **PATCH** /playQueues/{id}/relationships/future | Update future relationship (\&quot;to-many\&quot;).
[**play_queues_id_relationships_future_post**](PlayQueuesApi.md#play_queues_id_relationships_future_post) | **POST** /playQueues/{id}/relationships/future | Add to future relationship (\&quot;to-many\&quot;).
[**play_queues_id_relationships_owners_get**](PlayQueuesApi.md#play_queues_id_relationships_owners_get) | **GET** /playQueues/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**play_queues_id_relationships_past_get**](PlayQueuesApi.md#play_queues_id_relationships_past_get) | **GET** /playQueues/{id}/relationships/past | Get past relationship (\&quot;to-many\&quot;).
[**play_queues_post**](PlayQueuesApi.md#play_queues_post) | **POST** /playQueues | Create single playQueue.


# **play_queues_get**
> PlayQueuesMultiResourceDataDocument play_queues_get(filter_owners_id, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media)

Get multiple playQueues.

Retrieves multiple playQueues by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.play_queues_multi_resource_data_document import PlayQueuesMultiResourceDataDocument
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
    api_instance = tidal.PlayQueuesApi(api_client)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`.
    include = ['current'] # List[str] | Include related resources. Available relationships: changeEventStream, current, future, owners, past (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'current' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: current (optional)

    try:
        # Get multiple playQueues.
        api_response = api_instance.play_queues_get(filter_owners_id, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of PlayQueuesApi->play_queues_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayQueuesApi->play_queues_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_owners_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: changeEventStream, current, future, owners, past | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: current | [optional] 

### Return type

[**PlayQueuesMultiResourceDataDocument**](PlayQueuesMultiResourceDataDocument.md)

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

# **play_queues_id_delete**
> MutationResponseDocument play_queues_id_delete(id, idempotency_key=idempotency_key)

Delete single playQueue.

Deletes existing playQueue.

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
    api_instance = tidal.PlayQueuesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Play queue id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)

    try:
        # Delete single playQueue.
        api_response = api_instance.play_queues_id_delete(id, idempotency_key=idempotency_key)
        print("The response of PlayQueuesApi->play_queues_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayQueuesApi->play_queues_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Play queue id | 
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

# **play_queues_id_get**
> PlayQueuesSingleResourceDataDocument play_queues_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single playQueue.

Retrieves single playQueue by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.play_queues_single_resource_data_document import PlayQueuesSingleResourceDataDocument
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
    api_instance = tidal.PlayQueuesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Play queue id
    include = ['current'] # List[str] | Include related resources. Available relationships: changeEventStream, current, future, owners, past (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'current' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: current (optional)

    try:
        # Get single playQueue.
        api_response = api_instance.play_queues_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of PlayQueuesApi->play_queues_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayQueuesApi->play_queues_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Play queue id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: changeEventStream, current, future, owners, past | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: current | [optional] 

### Return type

[**PlayQueuesSingleResourceDataDocument**](PlayQueuesSingleResourceDataDocument.md)

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

# **play_queues_id_patch**
> PlayQueuesUpdateSingleResourceDataDocument play_queues_id_patch(id, idempotency_key=idempotency_key, play_queues_update_operation_payload=play_queues_update_operation_payload)

Update single playQueue.

Atomically applies attributes, future items, then current selection.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.play_queues_update_operation_payload import PlayQueuesUpdateOperationPayload
from tidal.models.play_queues_update_single_resource_data_document import PlayQueuesUpdateSingleResourceDataDocument
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
    api_instance = tidal.PlayQueuesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Play queue id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    play_queues_update_operation_payload = tidal.PlayQueuesUpdateOperationPayload() # PlayQueuesUpdateOperationPayload |  (optional)

    try:
        # Update single playQueue.
        api_response = api_instance.play_queues_id_patch(id, idempotency_key=idempotency_key, play_queues_update_operation_payload=play_queues_update_operation_payload)
        print("The response of PlayQueuesApi->play_queues_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayQueuesApi->play_queues_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Play queue id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **play_queues_update_operation_payload** | [**PlayQueuesUpdateOperationPayload**](PlayQueuesUpdateOperationPayload.md)|  | [optional] 

### Return type

[**PlayQueuesUpdateSingleResourceDataDocument**](PlayQueuesUpdateSingleResourceDataDocument.md)

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

# **play_queues_id_relationships_change_event_stream_get**
> PlayQueuesChangeEventStreamSingleRelationshipDataDocument play_queues_id_relationships_change_event_stream_get(id, include=include)

Get changeEventStream relationship (\"to-one\").

Retrieves changeEventStream relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.play_queues_change_event_stream_single_relationship_data_document import PlayQueuesChangeEventStreamSingleRelationshipDataDocument
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
    api_instance = tidal.PlayQueuesApi(api_client)
    id = 'id_example' # str | 
    include = ['changeEventStream'] # List[str] | Include related resources. Available relationships: changeEventStream (optional)

    try:
        # Get changeEventStream relationship (\"to-one\").
        api_response = api_instance.play_queues_id_relationships_change_event_stream_get(id, include=include)
        print("The response of PlayQueuesApi->play_queues_id_relationships_change_event_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayQueuesApi->play_queues_id_relationships_change_event_stream_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: changeEventStream | [optional] 

### Return type

[**PlayQueuesChangeEventStreamSingleRelationshipDataDocument**](PlayQueuesChangeEventStreamSingleRelationshipDataDocument.md)

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

# **play_queues_id_relationships_current_get**
> PlayQueuesCurrentSingleRelationshipDataDocument play_queues_id_relationships_current_get(id, include=include, replace_media=replace_media)

Get current relationship (\"to-one\").

Retrieves current relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.play_queues_current_single_relationship_data_document import PlayQueuesCurrentSingleRelationshipDataDocument
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
    api_instance = tidal.PlayQueuesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Play queue id
    include = ['current'] # List[str] | Include related resources. Available relationships: current (optional)
    replace_media = 'current' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: current (optional)

    try:
        # Get current relationship (\"to-one\").
        api_response = api_instance.play_queues_id_relationships_current_get(id, include=include, replace_media=replace_media)
        print("The response of PlayQueuesApi->play_queues_id_relationships_current_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayQueuesApi->play_queues_id_relationships_current_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Play queue id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: current | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: current | [optional] 

### Return type

[**PlayQueuesCurrentSingleRelationshipDataDocument**](PlayQueuesCurrentSingleRelationshipDataDocument.md)

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

# **play_queues_id_relationships_current_patch**
> PlayQueuesCurrentUpdateSingleRelationshipDataDocument play_queues_id_relationships_current_patch(id, idempotency_key=idempotency_key, play_queues_current_relationship_update_operation_payload=play_queues_current_relationship_update_operation_payload)

Update current relationship (\"to-one\").

Sets the current item to the existing queue occurrence identified by data.meta.itemId, changing which entries are past and future. Null data is rejected. Optional position and updatedByInstallationId must be supplied together. Returns the current item linkage and queue revision.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.play_queues_current_relationship_update_operation_payload import PlayQueuesCurrentRelationshipUpdateOperationPayload
from tidal.models.play_queues_current_update_single_relationship_data_document import PlayQueuesCurrentUpdateSingleRelationshipDataDocument
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
    api_instance = tidal.PlayQueuesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Play queue id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    play_queues_current_relationship_update_operation_payload = tidal.PlayQueuesCurrentRelationshipUpdateOperationPayload() # PlayQueuesCurrentRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update current relationship (\"to-one\").
        api_response = api_instance.play_queues_id_relationships_current_patch(id, idempotency_key=idempotency_key, play_queues_current_relationship_update_operation_payload=play_queues_current_relationship_update_operation_payload)
        print("The response of PlayQueuesApi->play_queues_id_relationships_current_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayQueuesApi->play_queues_id_relationships_current_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Play queue id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **play_queues_current_relationship_update_operation_payload** | [**PlayQueuesCurrentRelationshipUpdateOperationPayload**](PlayQueuesCurrentRelationshipUpdateOperationPayload.md)|  | [optional] 

### Return type

[**PlayQueuesCurrentUpdateSingleRelationshipDataDocument**](PlayQueuesCurrentUpdateSingleRelationshipDataDocument.md)

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

# **play_queues_id_relationships_future_delete**
> MutationResponseDocument play_queues_id_relationships_future_delete(id, idempotency_key=idempotency_key, play_queues_future_relationship_remove_operation_payload=play_queues_future_relationship_remove_operation_payload)

Delete from future relationship (\"to-many\").

Removes the future occurrences selected by data[].meta.itemId without deleting their tracks or videos. Other queue entries are preserved. Returns an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.play_queues_future_relationship_remove_operation_payload import PlayQueuesFutureRelationshipRemoveOperationPayload
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
    api_instance = tidal.PlayQueuesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Play queue id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    play_queues_future_relationship_remove_operation_payload = tidal.PlayQueuesFutureRelationshipRemoveOperationPayload() # PlayQueuesFutureRelationshipRemoveOperationPayload |  (optional)

    try:
        # Delete from future relationship (\"to-many\").
        api_response = api_instance.play_queues_id_relationships_future_delete(id, idempotency_key=idempotency_key, play_queues_future_relationship_remove_operation_payload=play_queues_future_relationship_remove_operation_payload)
        print("The response of PlayQueuesApi->play_queues_id_relationships_future_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayQueuesApi->play_queues_id_relationships_future_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Play queue id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **play_queues_future_relationship_remove_operation_payload** | [**PlayQueuesFutureRelationshipRemoveOperationPayload**](PlayQueuesFutureRelationshipRemoveOperationPayload.md)|  | [optional] 

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

# **play_queues_id_relationships_future_get**
> PlayQueuesFutureMultiRelationshipDataDocument play_queues_id_relationships_future_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get future relationship (\"to-many\").

Retrieves future relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.play_queues_future_multi_relationship_data_document import PlayQueuesFutureMultiRelationshipDataDocument
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
    api_instance = tidal.PlayQueuesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Play queue id
    include = ['future'] # List[str] | Include related resources. Available relationships: future (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'future' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: future (optional)

    try:
        # Get future relationship (\"to-many\").
        api_response = api_instance.play_queues_id_relationships_future_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of PlayQueuesApi->play_queues_id_relationships_future_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayQueuesApi->play_queues_id_relationships_future_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Play queue id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: future | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: future | [optional] 

### Return type

[**PlayQueuesFutureMultiRelationshipDataDocument**](PlayQueuesFutureMultiRelationshipDataDocument.md)

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

# **play_queues_id_relationships_future_patch**
> PlayQueuesFutureUpdateMultiRelationshipDataDocument play_queues_id_relationships_future_patch(id, idempotency_key=idempotency_key, play_queues_future_relationship_update_operation_payload=play_queues_future_relationship_update_operation_payload)

Update future relationship (\"to-many\").

Incrementally moves existing future occurrences selected by data[].meta.itemId, in their current queue order, before meta.positionBefore. Preserves memberships and unselected entries' metadata and relative order. Empty data is rejected. Returns empty data and meta.revision as an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.play_queues_future_relationship_update_operation_payload import PlayQueuesFutureRelationshipUpdateOperationPayload
from tidal.models.play_queues_future_update_multi_relationship_data_document import PlayQueuesFutureUpdateMultiRelationshipDataDocument
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
    api_instance = tidal.PlayQueuesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Play queue id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    play_queues_future_relationship_update_operation_payload = tidal.PlayQueuesFutureRelationshipUpdateOperationPayload() # PlayQueuesFutureRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update future relationship (\"to-many\").
        api_response = api_instance.play_queues_id_relationships_future_patch(id, idempotency_key=idempotency_key, play_queues_future_relationship_update_operation_payload=play_queues_future_relationship_update_operation_payload)
        print("The response of PlayQueuesApi->play_queues_id_relationships_future_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayQueuesApi->play_queues_id_relationships_future_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Play queue id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **play_queues_future_relationship_update_operation_payload** | [**PlayQueuesFutureRelationshipUpdateOperationPayload**](PlayQueuesFutureRelationshipUpdateOperationPayload.md)|  | [optional] 

### Return type

[**PlayQueuesFutureUpdateMultiRelationshipDataDocument**](PlayQueuesFutureUpdateMultiRelationshipDataDocument.md)

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

# **play_queues_id_relationships_future_post**
> PlayQueuesFutureAddMultiRelationshipDataDocument play_queues_id_relationships_future_post(id, idempotency_key=idempotency_key, play_queues_future_relationship_add_operation_payload=play_queues_future_relationship_add_operation_payload)

Add to future relationship (\"to-many\").

Omitting top-level meta or setting it to null defaults to REPLACE_ALL, replacing future entries. Use ADD_TO_FRONT, ADD_TO_BACK or ADD_BEFORE in meta.mode to add without replacing existing entries. ADD_BEFORE requires meta.positionBefore. REPLACE_ALL_AND_CURRENT replaces future entries; ADD_TO_FRONT_REPLACE_CURRENT prepends entries. Both select the first newly inserted entry in the active queue order as current, which may differ from request order when shuffled. With empty data and no source, replacement modes clear future entries; the current entry is unchanged when no entries are inserted. With meta.source, startIndex selects an entry in the first page's data before unsupported types are skipped. Tracks and videos are added in page order, retaining duplicates; other types are skipped without expansion. Reaching 1000 added items or 100 pages queues the collected prefix. Invalid sources or indexes, a suffix with no playable items, repeated pages, and read failures encountered before a cap leave the queue unchanged. Returns empty data and meta.revision as an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.play_queues_future_add_multi_relationship_data_document import PlayQueuesFutureAddMultiRelationshipDataDocument
from tidal.models.play_queues_future_relationship_add_operation_payload import PlayQueuesFutureRelationshipAddOperationPayload
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
    api_instance = tidal.PlayQueuesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Play queue id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    play_queues_future_relationship_add_operation_payload = tidal.PlayQueuesFutureRelationshipAddOperationPayload() # PlayQueuesFutureRelationshipAddOperationPayload |  (optional)

    try:
        # Add to future relationship (\"to-many\").
        api_response = api_instance.play_queues_id_relationships_future_post(id, idempotency_key=idempotency_key, play_queues_future_relationship_add_operation_payload=play_queues_future_relationship_add_operation_payload)
        print("The response of PlayQueuesApi->play_queues_id_relationships_future_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayQueuesApi->play_queues_id_relationships_future_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Play queue id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **play_queues_future_relationship_add_operation_payload** | [**PlayQueuesFutureRelationshipAddOperationPayload**](PlayQueuesFutureRelationshipAddOperationPayload.md)|  | [optional] 

### Return type

[**PlayQueuesFutureAddMultiRelationshipDataDocument**](PlayQueuesFutureAddMultiRelationshipDataDocument.md)

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

# **play_queues_id_relationships_owners_get**
> PlayQueuesOwnersMultiRelationshipDataDocument play_queues_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.play_queues_owners_multi_relationship_data_document import PlayQueuesOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.PlayQueuesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Play queue id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.play_queues_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of PlayQueuesApi->play_queues_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayQueuesApi->play_queues_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Play queue id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**PlayQueuesOwnersMultiRelationshipDataDocument**](PlayQueuesOwnersMultiRelationshipDataDocument.md)

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

# **play_queues_id_relationships_past_get**
> PlayQueuesPastMultiRelationshipDataDocument play_queues_id_relationships_past_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get past relationship (\"to-many\").

Retrieves past relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.play_queues_past_multi_relationship_data_document import PlayQueuesPastMultiRelationshipDataDocument
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
    api_instance = tidal.PlayQueuesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Play queue id
    include = ['past'] # List[str] | Include related resources. Available relationships: past (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'past' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: past (optional)

    try:
        # Get past relationship (\"to-many\").
        api_response = api_instance.play_queues_id_relationships_past_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of PlayQueuesApi->play_queues_id_relationships_past_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayQueuesApi->play_queues_id_relationships_past_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Play queue id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: past | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: past | [optional] 

### Return type

[**PlayQueuesPastMultiRelationshipDataDocument**](PlayQueuesPastMultiRelationshipDataDocument.md)

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

# **play_queues_post**
> PlayQueuesCreateSingleResourceDataDocument play_queues_post(idempotency_key=idempotency_key, play_queues_create_operation_payload=play_queues_create_operation_payload)

Create single playQueue.

Creates a new playQueue.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.play_queues_create_operation_payload import PlayQueuesCreateOperationPayload
from tidal.models.play_queues_create_single_resource_data_document import PlayQueuesCreateSingleResourceDataDocument
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
    api_instance = tidal.PlayQueuesApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    play_queues_create_operation_payload = tidal.PlayQueuesCreateOperationPayload() # PlayQueuesCreateOperationPayload |  (optional)

    try:
        # Create single playQueue.
        api_response = api_instance.play_queues_post(idempotency_key=idempotency_key, play_queues_create_operation_payload=play_queues_create_operation_payload)
        print("The response of PlayQueuesApi->play_queues_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayQueuesApi->play_queues_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **play_queues_create_operation_payload** | [**PlayQueuesCreateOperationPayload**](PlayQueuesCreateOperationPayload.md)|  | [optional] 

### Return type

[**PlayQueuesCreateSingleResourceDataDocument**](PlayQueuesCreateSingleResourceDataDocument.md)

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
**409** | Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

