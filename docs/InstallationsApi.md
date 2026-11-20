# tidal.InstallationsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**installations_get**](InstallationsApi.md#installations_get) | **GET** /installations | Get multiple installations.
[**installations_id_get**](InstallationsApi.md#installations_id_get) | **GET** /installations/{id} | Get single installation.
[**installations_id_relationships_offline_inventory_delete**](InstallationsApi.md#installations_id_relationships_offline_inventory_delete) | **DELETE** /installations/{id}/relationships/offlineInventory | Delete from offlineInventory relationship (\&quot;to-many\&quot;).
[**installations_id_relationships_offline_inventory_get**](InstallationsApi.md#installations_id_relationships_offline_inventory_get) | **GET** /installations/{id}/relationships/offlineInventory | Get offlineInventory relationship (\&quot;to-many\&quot;).
[**installations_id_relationships_offline_inventory_post**](InstallationsApi.md#installations_id_relationships_offline_inventory_post) | **POST** /installations/{id}/relationships/offlineInventory | Add to offlineInventory relationship (\&quot;to-many\&quot;).
[**installations_id_relationships_owners_get**](InstallationsApi.md#installations_id_relationships_owners_get) | **GET** /installations/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**installations_post**](InstallationsApi.md#installations_post) | **POST** /installations | Create single installation.


# **installations_get**
> InstallationsMultiResourceDataDocument installations_get(filter_client_provided_installation_id=filter_client_provided_installation_id, filter_owners_id=filter_owners_id, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media)

Get multiple installations.

Retrieves multiple installations by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.installations_multi_resource_data_document import InstallationsMultiResourceDataDocument
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
    api_instance = tidal.InstallationsApi(api_client)
    filter_client_provided_installation_id = ['filter_client_provided_installation_id_example'] # List[str] | Client-provided installation identifier to filter by (e.g. `a468bee88def`) (optional)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User ID to filter by. Also accepts `me`. (optional)
    include = ['offlineInventory'] # List[str] | Include related resources. Available relationships: offlineInventory, owners (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'offlineInventory' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: offlineInventory (optional)

    try:
        # Get multiple installations.
        api_response = api_instance.installations_get(filter_client_provided_installation_id=filter_client_provided_installation_id, filter_owners_id=filter_owners_id, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of InstallationsApi->installations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallationsApi->installations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_client_provided_installation_id** | [**List[str]**](str.md)| Client-provided installation identifier to filter by (e.g. &#x60;a468bee88def&#x60;) | [optional] 
 **filter_owners_id** | [**List[str]**](str.md)| User ID to filter by. Also accepts &#x60;me&#x60;. | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: offlineInventory, owners | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: offlineInventory | [optional] 

### Return type

[**InstallationsMultiResourceDataDocument**](InstallationsMultiResourceDataDocument.md)

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

# **installations_id_get**
> InstallationsSingleResourceDataDocument installations_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single installation.

Retrieves single installation by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.installations_single_resource_data_document import InstallationsSingleResourceDataDocument
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
    api_instance = tidal.InstallationsApi(api_client)
    id = 'a468bee88def' # str | Installation id
    include = ['offlineInventory'] # List[str] | Include related resources. Available relationships: offlineInventory, owners (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'offlineInventory' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: offlineInventory (optional)

    try:
        # Get single installation.
        api_response = api_instance.installations_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of InstallationsApi->installations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallationsApi->installations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Installation id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: offlineInventory, owners | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: offlineInventory | [optional] 

### Return type

[**InstallationsSingleResourceDataDocument**](InstallationsSingleResourceDataDocument.md)

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

# **installations_id_relationships_offline_inventory_delete**
> MutationResponseDocument installations_id_relationships_offline_inventory_delete(id, idempotency_key=idempotency_key, installations_offline_inventory_relationship_remove_operation_payload=installations_offline_inventory_relationship_remove_operation_payload)

Delete from offlineInventory relationship (\"to-many\").

Deletes item(s) from offlineInventory relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.installations_offline_inventory_relationship_remove_operation_payload import InstallationsOfflineInventoryRelationshipRemoveOperationPayload
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
    api_instance = tidal.InstallationsApi(api_client)
    id = 'a468bee88def' # str | Installation id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    installations_offline_inventory_relationship_remove_operation_payload = tidal.InstallationsOfflineInventoryRelationshipRemoveOperationPayload() # InstallationsOfflineInventoryRelationshipRemoveOperationPayload |  (optional)

    try:
        # Delete from offlineInventory relationship (\"to-many\").
        api_response = api_instance.installations_id_relationships_offline_inventory_delete(id, idempotency_key=idempotency_key, installations_offline_inventory_relationship_remove_operation_payload=installations_offline_inventory_relationship_remove_operation_payload)
        print("The response of InstallationsApi->installations_id_relationships_offline_inventory_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallationsApi->installations_id_relationships_offline_inventory_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Installation id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **installations_offline_inventory_relationship_remove_operation_payload** | [**InstallationsOfflineInventoryRelationshipRemoveOperationPayload**](InstallationsOfflineInventoryRelationshipRemoveOperationPayload.md)|  | [optional] 

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

# **installations_id_relationships_offline_inventory_get**
> InstallationsOfflineInventoryMultiRelationshipDataDocument installations_id_relationships_offline_inventory_get(filter_type, id, filter_client_storage_state=filter_client_storage_state, filter_id=filter_id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get offlineInventory relationship (\"to-many\").

Retrieves offlineInventory relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.installations_offline_inventory_multi_relationship_data_document import InstallationsOfflineInventoryMultiRelationshipDataDocument
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
    api_instance = tidal.InstallationsApi(api_client)
    filter_type = ['filter_type_example'] # List[str] | One of: tracks, videos, albums, playlists, userCollectionTracks (e.g. `tracks`)
    id = 'a468bee88def' # str | Installation id
    filter_client_storage_state = ['filter_client_storage_state_example'] # List[str] | One of: PENDING, STORED, FAILED (e.g. `PENDING`) (optional)
    filter_id = ['filter_id_example'] # List[str] | Offline item id (e.g. `1234`) (optional)
    include = ['offlineInventory'] # List[str] | Include related resources. Available relationships: offlineInventory (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'offlineInventory' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: offlineInventory (optional)

    try:
        # Get offlineInventory relationship (\"to-many\").
        api_response = api_instance.installations_id_relationships_offline_inventory_get(filter_type, id, filter_client_storage_state=filter_client_storage_state, filter_id=filter_id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of InstallationsApi->installations_id_relationships_offline_inventory_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallationsApi->installations_id_relationships_offline_inventory_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_type** | [**List[str]**](str.md)| One of: tracks, videos, albums, playlists, userCollectionTracks (e.g. &#x60;tracks&#x60;) | 
 **id** | **str**| Installation id | 
 **filter_client_storage_state** | [**List[str]**](str.md)| One of: PENDING, STORED, FAILED (e.g. &#x60;PENDING&#x60;) | [optional] 
 **filter_id** | [**List[str]**](str.md)| Offline item id (e.g. &#x60;1234&#x60;) | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: offlineInventory | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: offlineInventory | [optional] 

### Return type

[**InstallationsOfflineInventoryMultiRelationshipDataDocument**](InstallationsOfflineInventoryMultiRelationshipDataDocument.md)

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

# **installations_id_relationships_offline_inventory_post**
> MutationResponseDocument installations_id_relationships_offline_inventory_post(id, idempotency_key=idempotency_key, installations_offline_inventory_relationship_add_operation_payload=installations_offline_inventory_relationship_add_operation_payload)

Add to offlineInventory relationship (\"to-many\").

Adds item(s) to offlineInventory relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.installations_offline_inventory_relationship_add_operation_payload import InstallationsOfflineInventoryRelationshipAddOperationPayload
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
    api_instance = tidal.InstallationsApi(api_client)
    id = 'a468bee88def' # str | Installation id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    installations_offline_inventory_relationship_add_operation_payload = tidal.InstallationsOfflineInventoryRelationshipAddOperationPayload() # InstallationsOfflineInventoryRelationshipAddOperationPayload |  (optional)

    try:
        # Add to offlineInventory relationship (\"to-many\").
        api_response = api_instance.installations_id_relationships_offline_inventory_post(id, idempotency_key=idempotency_key, installations_offline_inventory_relationship_add_operation_payload=installations_offline_inventory_relationship_add_operation_payload)
        print("The response of InstallationsApi->installations_id_relationships_offline_inventory_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallationsApi->installations_id_relationships_offline_inventory_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Installation id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **installations_offline_inventory_relationship_add_operation_payload** | [**InstallationsOfflineInventoryRelationshipAddOperationPayload**](InstallationsOfflineInventoryRelationshipAddOperationPayload.md)|  | [optional] 

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

# **installations_id_relationships_owners_get**
> InstallationsOwnersMultiRelationshipDataDocument installations_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.installations_owners_multi_relationship_data_document import InstallationsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.InstallationsApi(api_client)
    id = 'a468bee88def' # str | Installation id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.installations_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of InstallationsApi->installations_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallationsApi->installations_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Installation id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**InstallationsOwnersMultiRelationshipDataDocument**](InstallationsOwnersMultiRelationshipDataDocument.md)

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

# **installations_post**
> InstallationsCreateSingleResourceDataDocument installations_post(idempotency_key=idempotency_key, installations_create_operation_payload=installations_create_operation_payload)

Create single installation.

Creates a new installation.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.installations_create_operation_payload import InstallationsCreateOperationPayload
from tidal.models.installations_create_single_resource_data_document import InstallationsCreateSingleResourceDataDocument
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
    api_instance = tidal.InstallationsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    installations_create_operation_payload = tidal.InstallationsCreateOperationPayload() # InstallationsCreateOperationPayload |  (optional)

    try:
        # Create single installation.
        api_response = api_instance.installations_post(idempotency_key=idempotency_key, installations_create_operation_payload=installations_create_operation_payload)
        print("The response of InstallationsApi->installations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstallationsApi->installations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **installations_create_operation_payload** | [**InstallationsCreateOperationPayload**](InstallationsCreateOperationPayload.md)|  | [optional] 

### Return type

[**InstallationsCreateSingleResourceDataDocument**](InstallationsCreateSingleResourceDataDocument.md)

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

