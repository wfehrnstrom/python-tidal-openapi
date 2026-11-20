# tidal.OfflineTasksApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offline_tasks_get**](OfflineTasksApi.md#offline_tasks_get) | **GET** /offlineTasks | Get multiple offlineTasks.
[**offline_tasks_id_get**](OfflineTasksApi.md#offline_tasks_id_get) | **GET** /offlineTasks/{id} | Get single offlineTask.
[**offline_tasks_id_patch**](OfflineTasksApi.md#offline_tasks_id_patch) | **PATCH** /offlineTasks/{id} | Update single offlineTask.
[**offline_tasks_id_relationships_collection_get**](OfflineTasksApi.md#offline_tasks_id_relationships_collection_get) | **GET** /offlineTasks/{id}/relationships/collection | Get collection relationship (\&quot;to-one\&quot;).
[**offline_tasks_id_relationships_item_get**](OfflineTasksApi.md#offline_tasks_id_relationships_item_get) | **GET** /offlineTasks/{id}/relationships/item | Get item relationship (\&quot;to-one\&quot;).
[**offline_tasks_id_relationships_owners_get**](OfflineTasksApi.md#offline_tasks_id_relationships_owners_get) | **GET** /offlineTasks/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).


# **offline_tasks_get**
> OfflineTasksMultiResourceDataDocument offline_tasks_get(filter_installation_id, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media)

Get multiple offlineTasks.

Retrieves multiple offlineTasks by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.offline_tasks_multi_resource_data_document import OfflineTasksMultiResourceDataDocument
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
    api_instance = tidal.OfflineTasksApi(api_client)
    filter_installation_id = ['filter_installation_id_example'] # List[str] | List of offline task IDs (e.g. `a468bee88def`)
    include = ['collection'] # List[str] | Include related resources. Available relationships: collection, item, owners (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'collection' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: collection (optional)

    try:
        # Get multiple offlineTasks.
        api_response = api_instance.offline_tasks_get(filter_installation_id, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of OfflineTasksApi->offline_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfflineTasksApi->offline_tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_installation_id** | [**List[str]**](str.md)| List of offline task IDs (e.g. &#x60;a468bee88def&#x60;) | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: collection, item, owners | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: collection | [optional] 

### Return type

[**OfflineTasksMultiResourceDataDocument**](OfflineTasksMultiResourceDataDocument.md)

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

# **offline_tasks_id_get**
> OfflineTasksSingleResourceDataDocument offline_tasks_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single offlineTask.

Retrieves single offlineTask by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.offline_tasks_single_resource_data_document import OfflineTasksSingleResourceDataDocument
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
    api_instance = tidal.OfflineTasksApi(api_client)
    id = 'a468bee8-8def-4a1b-8c1e-123456789abc' # str | Offline task id
    include = ['collection'] # List[str] | Include related resources. Available relationships: collection, item, owners (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'collection' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: collection (optional)

    try:
        # Get single offlineTask.
        api_response = api_instance.offline_tasks_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of OfflineTasksApi->offline_tasks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfflineTasksApi->offline_tasks_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Offline task id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: collection, item, owners | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: collection | [optional] 

### Return type

[**OfflineTasksSingleResourceDataDocument**](OfflineTasksSingleResourceDataDocument.md)

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

# **offline_tasks_id_patch**
> MutationResponseDocument offline_tasks_id_patch(id, idempotency_key=idempotency_key, offline_tasks_update_operation_payload=offline_tasks_update_operation_payload)

Update single offlineTask.

Updates existing offlineTask.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.offline_tasks_update_operation_payload import OfflineTasksUpdateOperationPayload
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
    api_instance = tidal.OfflineTasksApi(api_client)
    id = 'a468bee8-8def-4a1b-8c1e-123456789abc' # str | Offline task id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    offline_tasks_update_operation_payload = tidal.OfflineTasksUpdateOperationPayload() # OfflineTasksUpdateOperationPayload |  (optional)

    try:
        # Update single offlineTask.
        api_response = api_instance.offline_tasks_id_patch(id, idempotency_key=idempotency_key, offline_tasks_update_operation_payload=offline_tasks_update_operation_payload)
        print("The response of OfflineTasksApi->offline_tasks_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfflineTasksApi->offline_tasks_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Offline task id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **offline_tasks_update_operation_payload** | [**OfflineTasksUpdateOperationPayload**](OfflineTasksUpdateOperationPayload.md)|  | [optional] 

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

# **offline_tasks_id_relationships_collection_get**
> OfflineTasksCollectionSingleRelationshipDataDocument offline_tasks_id_relationships_collection_get(id, include=include, replace_media=replace_media)

Get collection relationship (\"to-one\").

Retrieves collection relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.offline_tasks_collection_single_relationship_data_document import OfflineTasksCollectionSingleRelationshipDataDocument
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
    api_instance = tidal.OfflineTasksApi(api_client)
    id = 'a468bee8-8def-4a1b-8c1e-123456789abc' # str | Offline task id
    include = ['collection'] # List[str] | Include related resources. Available relationships: collection (optional)
    replace_media = 'collection' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: collection (optional)

    try:
        # Get collection relationship (\"to-one\").
        api_response = api_instance.offline_tasks_id_relationships_collection_get(id, include=include, replace_media=replace_media)
        print("The response of OfflineTasksApi->offline_tasks_id_relationships_collection_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfflineTasksApi->offline_tasks_id_relationships_collection_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Offline task id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: collection | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: collection | [optional] 

### Return type

[**OfflineTasksCollectionSingleRelationshipDataDocument**](OfflineTasksCollectionSingleRelationshipDataDocument.md)

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

# **offline_tasks_id_relationships_item_get**
> OfflineTasksItemSingleRelationshipDataDocument offline_tasks_id_relationships_item_get(id, include=include, replace_media=replace_media)

Get item relationship (\"to-one\").

Retrieves item relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.offline_tasks_item_single_relationship_data_document import OfflineTasksItemSingleRelationshipDataDocument
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
    api_instance = tidal.OfflineTasksApi(api_client)
    id = 'a468bee8-8def-4a1b-8c1e-123456789abc' # str | Offline task id
    include = ['item'] # List[str] | Include related resources. Available relationships: item (optional)
    replace_media = 'item' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: item (optional)

    try:
        # Get item relationship (\"to-one\").
        api_response = api_instance.offline_tasks_id_relationships_item_get(id, include=include, replace_media=replace_media)
        print("The response of OfflineTasksApi->offline_tasks_id_relationships_item_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfflineTasksApi->offline_tasks_id_relationships_item_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Offline task id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: item | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: item | [optional] 

### Return type

[**OfflineTasksItemSingleRelationshipDataDocument**](OfflineTasksItemSingleRelationshipDataDocument.md)

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

# **offline_tasks_id_relationships_owners_get**
> OfflineTasksOwnersMultiRelationshipDataDocument offline_tasks_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.offline_tasks_owners_multi_relationship_data_document import OfflineTasksOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.OfflineTasksApi(api_client)
    id = 'a468bee8-8def-4a1b-8c1e-123456789abc' # str | Offline task id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.offline_tasks_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of OfflineTasksApi->offline_tasks_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfflineTasksApi->offline_tasks_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Offline task id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**OfflineTasksOwnersMultiRelationshipDataDocument**](OfflineTasksOwnersMultiRelationshipDataDocument.md)

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

