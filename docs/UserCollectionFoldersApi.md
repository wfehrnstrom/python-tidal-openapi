# tidal.UserCollectionFoldersApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_collection_folders_get**](UserCollectionFoldersApi.md#user_collection_folders_get) | **GET** /userCollectionFolders | Get multiple userCollectionFolders.
[**user_collection_folders_id_delete**](UserCollectionFoldersApi.md#user_collection_folders_id_delete) | **DELETE** /userCollectionFolders/{id} | Delete single userCollectionFolder.
[**user_collection_folders_id_get**](UserCollectionFoldersApi.md#user_collection_folders_id_get) | **GET** /userCollectionFolders/{id} | Get single userCollectionFolder.
[**user_collection_folders_id_patch**](UserCollectionFoldersApi.md#user_collection_folders_id_patch) | **PATCH** /userCollectionFolders/{id} | Update single userCollectionFolder.
[**user_collection_folders_id_relationships_items_delete**](UserCollectionFoldersApi.md#user_collection_folders_id_relationships_items_delete) | **DELETE** /userCollectionFolders/{id}/relationships/items | Delete from items relationship (\&quot;to-many\&quot;).
[**user_collection_folders_id_relationships_items_get**](UserCollectionFoldersApi.md#user_collection_folders_id_relationships_items_get) | **GET** /userCollectionFolders/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
[**user_collection_folders_id_relationships_items_post**](UserCollectionFoldersApi.md#user_collection_folders_id_relationships_items_post) | **POST** /userCollectionFolders/{id}/relationships/items | Add to items relationship (\&quot;to-many\&quot;).
[**user_collection_folders_id_relationships_owners_get**](UserCollectionFoldersApi.md#user_collection_folders_id_relationships_owners_get) | **GET** /userCollectionFolders/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**user_collection_folders_id_relationships_user_collection_get**](UserCollectionFoldersApi.md#user_collection_folders_id_relationships_user_collection_get) | **GET** /userCollectionFolders/{id}/relationships/userCollection | Get userCollection relationship (\&quot;to-one\&quot;).
[**user_collection_folders_post**](UserCollectionFoldersApi.md#user_collection_folders_post) | **POST** /userCollectionFolders | Create single userCollectionFolder.


# **user_collection_folders_get**
> UserCollectionFoldersMultiResourceDataDocument user_collection_folders_get(filter_id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get multiple userCollectionFolders.

Retrieves multiple userCollectionFolders by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_collection_folders_multi_resource_data_document import UserCollectionFoldersMultiResourceDataDocument
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
    api_instance = tidal.UserCollectionFoldersApi(api_client)
    filter_id = ['filter_id_example'] # List[str] | Folder Id (e.g. `CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX`)
    include = ['items.items'] # List[str] | Include related resources. Available relationships: items, owners, userCollection (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'items.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items (optional)

    try:
        # Get multiple userCollectionFolders.
        api_response = api_instance.user_collection_folders_get(filter_id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of UserCollectionFoldersApi->user_collection_folders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionFoldersApi->user_collection_folders_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | [**List[str]**](str.md)| Folder Id (e.g. &#x60;CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX&#x60;) | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items, owners, userCollection | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items.items | [optional] 

### Return type

[**UserCollectionFoldersMultiResourceDataDocument**](UserCollectionFoldersMultiResourceDataDocument.md)

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

# **user_collection_folders_id_delete**
> MutationResponseDocument user_collection_folders_id_delete(id, idempotency_key=idempotency_key)

Delete single userCollectionFolder.

Deletes existing userCollectionFolder.

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
    api_instance = tidal.UserCollectionFoldersApi(api_client)
    id = 'CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX' # str | Folder Id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)

    try:
        # Delete single userCollectionFolder.
        api_response = api_instance.user_collection_folders_id_delete(id, idempotency_key=idempotency_key)
        print("The response of UserCollectionFoldersApi->user_collection_folders_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionFoldersApi->user_collection_folders_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder Id | 
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
**400** | Folder must be empty and owned by you |  -  |
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

# **user_collection_folders_id_get**
> UserCollectionFoldersSingleResourceDataDocument user_collection_folders_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single userCollectionFolder.

Retrieves single userCollectionFolder by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_collection_folders_single_resource_data_document import UserCollectionFoldersSingleResourceDataDocument
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
    api_instance = tidal.UserCollectionFoldersApi(api_client)
    id = 'CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX' # str | Folder Id
    include = ['items.items'] # List[str] | Include related resources. Available relationships: items, owners, userCollection (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'items.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items (optional)

    try:
        # Get single userCollectionFolder.
        api_response = api_instance.user_collection_folders_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of UserCollectionFoldersApi->user_collection_folders_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionFoldersApi->user_collection_folders_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items, owners, userCollection | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items.items | [optional] 

### Return type

[**UserCollectionFoldersSingleResourceDataDocument**](UserCollectionFoldersSingleResourceDataDocument.md)

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

# **user_collection_folders_id_patch**
> MutationResponseDocument user_collection_folders_id_patch(id, idempotency_key=idempotency_key, user_collection_folders_update_operation_payload=user_collection_folders_update_operation_payload)

Update single userCollectionFolder.

Updates existing userCollectionFolder.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.user_collection_folders_update_operation_payload import UserCollectionFoldersUpdateOperationPayload
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
    api_instance = tidal.UserCollectionFoldersApi(api_client)
    id = 'CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX' # str | Folder Id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_collection_folders_update_operation_payload = tidal.UserCollectionFoldersUpdateOperationPayload() # UserCollectionFoldersUpdateOperationPayload |  (optional)

    try:
        # Update single userCollectionFolder.
        api_response = api_instance.user_collection_folders_id_patch(id, idempotency_key=idempotency_key, user_collection_folders_update_operation_payload=user_collection_folders_update_operation_payload)
        print("The response of UserCollectionFoldersApi->user_collection_folders_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionFoldersApi->user_collection_folders_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder Id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_collection_folders_update_operation_payload** | [**UserCollectionFoldersUpdateOperationPayload**](UserCollectionFoldersUpdateOperationPayload.md)|  | [optional] 

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

# **user_collection_folders_id_relationships_items_delete**
> MutationResponseDocument user_collection_folders_id_relationships_items_delete(id, idempotency_key=idempotency_key, user_collection_folders_items_relationship_remove_operation_payload=user_collection_folders_items_relationship_remove_operation_payload)

Delete from items relationship (\"to-many\").

Deletes item(s) from items relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.user_collection_folders_items_relationship_remove_operation_payload import UserCollectionFoldersItemsRelationshipRemoveOperationPayload
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
    api_instance = tidal.UserCollectionFoldersApi(api_client)
    id = 'CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX' # str | Folder Id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_collection_folders_items_relationship_remove_operation_payload = tidal.UserCollectionFoldersItemsRelationshipRemoveOperationPayload() # UserCollectionFoldersItemsRelationshipRemoveOperationPayload |  (optional)

    try:
        # Delete from items relationship (\"to-many\").
        api_response = api_instance.user_collection_folders_id_relationships_items_delete(id, idempotency_key=idempotency_key, user_collection_folders_items_relationship_remove_operation_payload=user_collection_folders_items_relationship_remove_operation_payload)
        print("The response of UserCollectionFoldersApi->user_collection_folders_id_relationships_items_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionFoldersApi->user_collection_folders_id_relationships_items_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder Id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_collection_folders_items_relationship_remove_operation_payload** | [**UserCollectionFoldersItemsRelationshipRemoveOperationPayload**](UserCollectionFoldersItemsRelationshipRemoveOperationPayload.md)|  | [optional] 

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

# **user_collection_folders_id_relationships_items_get**
> UserCollectionFoldersItemsMultiRelationshipDataDocument user_collection_folders_id_relationships_items_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, sort=sort)

Get items relationship (\"to-many\").

Retrieves items relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_collection_folders_items_multi_relationship_data_document import UserCollectionFoldersItemsMultiRelationshipDataDocument
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
    api_instance = tidal.UserCollectionFoldersApi(api_client)
    id = 'CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX' # str | Folder Id
    include = ['items.items'] # List[str] | Include related resources. Available relationships: items (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'items.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items.items (optional)
    sort = ['sort_example'] # List[str] | Values prefixed with \"-\" are sorted descending; values without it are sorted ascending. (optional)

    try:
        # Get items relationship (\"to-many\").
        api_response = api_instance.user_collection_folders_id_relationships_items_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, sort=sort)
        print("The response of UserCollectionFoldersApi->user_collection_folders_id_relationships_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionFoldersApi->user_collection_folders_id_relationships_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items.items | [optional] 
 **sort** | [**List[str]**](str.md)| Values prefixed with \&quot;-\&quot; are sorted descending; values without it are sorted ascending. | [optional] 

### Return type

[**UserCollectionFoldersItemsMultiRelationshipDataDocument**](UserCollectionFoldersItemsMultiRelationshipDataDocument.md)

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

# **user_collection_folders_id_relationships_items_post**
> MutationResponseDocument user_collection_folders_id_relationships_items_post(id, idempotency_key=idempotency_key, user_collection_folders_items_relationship_add_operation_payload=user_collection_folders_items_relationship_add_operation_payload)

Add to items relationship (\"to-many\").

Adds item(s) to items relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.user_collection_folders_items_relationship_add_operation_payload import UserCollectionFoldersItemsRelationshipAddOperationPayload
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
    api_instance = tidal.UserCollectionFoldersApi(api_client)
    id = 'CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX' # str | Folder Id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_collection_folders_items_relationship_add_operation_payload = tidal.UserCollectionFoldersItemsRelationshipAddOperationPayload() # UserCollectionFoldersItemsRelationshipAddOperationPayload |  (optional)

    try:
        # Add to items relationship (\"to-many\").
        api_response = api_instance.user_collection_folders_id_relationships_items_post(id, idempotency_key=idempotency_key, user_collection_folders_items_relationship_add_operation_payload=user_collection_folders_items_relationship_add_operation_payload)
        print("The response of UserCollectionFoldersApi->user_collection_folders_id_relationships_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionFoldersApi->user_collection_folders_id_relationships_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder Id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_collection_folders_items_relationship_add_operation_payload** | [**UserCollectionFoldersItemsRelationshipAddOperationPayload**](UserCollectionFoldersItemsRelationshipAddOperationPayload.md)|  | [optional] 

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

# **user_collection_folders_id_relationships_owners_get**
> UserCollectionFoldersOwnersMultiRelationshipDataDocument user_collection_folders_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_collection_folders_owners_multi_relationship_data_document import UserCollectionFoldersOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.UserCollectionFoldersApi(api_client)
    id = 'CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX' # str | Folder Id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.user_collection_folders_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of UserCollectionFoldersApi->user_collection_folders_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionFoldersApi->user_collection_folders_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**UserCollectionFoldersOwnersMultiRelationshipDataDocument**](UserCollectionFoldersOwnersMultiRelationshipDataDocument.md)

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

# **user_collection_folders_id_relationships_user_collection_get**
> UserCollectionFoldersUserCollectionSingleRelationshipDataDocument user_collection_folders_id_relationships_user_collection_get(id, include=include, replace_media=replace_media)

Get userCollection relationship (\"to-one\").

Retrieves userCollection relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_collection_folders_user_collection_single_relationship_data_document import UserCollectionFoldersUserCollectionSingleRelationshipDataDocument
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
    api_instance = tidal.UserCollectionFoldersApi(api_client)
    id = 'CBMHXUOuJZgroV2kWpeVLL1I7xdgvF6ocDEGCXov8SZq3WVhrOcOq5pjnGawKX' # str | Folder Id
    include = ['userCollection.items.items'] # List[str] | Include related resources. Available relationships: userCollection (optional)
    replace_media = 'userCollection.items.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: userCollection.items.items (optional)

    try:
        # Get userCollection relationship (\"to-one\").
        api_response = api_instance.user_collection_folders_id_relationships_user_collection_get(id, include=include, replace_media=replace_media)
        print("The response of UserCollectionFoldersApi->user_collection_folders_id_relationships_user_collection_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionFoldersApi->user_collection_folders_id_relationships_user_collection_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: userCollection | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: userCollection.items.items | [optional] 

### Return type

[**UserCollectionFoldersUserCollectionSingleRelationshipDataDocument**](UserCollectionFoldersUserCollectionSingleRelationshipDataDocument.md)

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

# **user_collection_folders_post**
> UserCollectionFoldersCreateSingleResourceDataDocument user_collection_folders_post(idempotency_key=idempotency_key, user_collection_folders_create_operation_payload=user_collection_folders_create_operation_payload)

Create single userCollectionFolder.

Creates a new userCollectionFolder.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_collection_folders_create_operation_payload import UserCollectionFoldersCreateOperationPayload
from tidal.models.user_collection_folders_create_single_resource_data_document import UserCollectionFoldersCreateSingleResourceDataDocument
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
    api_instance = tidal.UserCollectionFoldersApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_collection_folders_create_operation_payload = tidal.UserCollectionFoldersCreateOperationPayload() # UserCollectionFoldersCreateOperationPayload |  (optional)

    try:
        # Create single userCollectionFolder.
        api_response = api_instance.user_collection_folders_post(idempotency_key=idempotency_key, user_collection_folders_create_operation_payload=user_collection_folders_create_operation_payload)
        print("The response of UserCollectionFoldersApi->user_collection_folders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionFoldersApi->user_collection_folders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_collection_folders_create_operation_payload** | [**UserCollectionFoldersCreateOperationPayload**](UserCollectionFoldersCreateOperationPayload.md)|  | [optional] 

### Return type

[**UserCollectionFoldersCreateSingleResourceDataDocument**](UserCollectionFoldersCreateSingleResourceDataDocument.md)

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

