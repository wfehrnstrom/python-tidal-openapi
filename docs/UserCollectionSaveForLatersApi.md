# tidal.UserCollectionSaveForLatersApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_collection_save_for_laters_id_get**](UserCollectionSaveForLatersApi.md#user_collection_save_for_laters_id_get) | **GET** /userCollectionSaveForLaters/{id} | Get single userCollectionSaveForLater.
[**user_collection_save_for_laters_id_relationships_items_delete**](UserCollectionSaveForLatersApi.md#user_collection_save_for_laters_id_relationships_items_delete) | **DELETE** /userCollectionSaveForLaters/{id}/relationships/items | Delete from items relationship (\&quot;to-many\&quot;).
[**user_collection_save_for_laters_id_relationships_items_get**](UserCollectionSaveForLatersApi.md#user_collection_save_for_laters_id_relationships_items_get) | **GET** /userCollectionSaveForLaters/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
[**user_collection_save_for_laters_id_relationships_items_post**](UserCollectionSaveForLatersApi.md#user_collection_save_for_laters_id_relationships_items_post) | **POST** /userCollectionSaveForLaters/{id}/relationships/items | Add to items relationship (\&quot;to-many\&quot;).
[**user_collection_save_for_laters_id_relationships_owners_get**](UserCollectionSaveForLatersApi.md#user_collection_save_for_laters_id_relationships_owners_get) | **GET** /userCollectionSaveForLaters/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).


# **user_collection_save_for_laters_id_get**
> UserCollectionSaveForLatersSingleResourceDataDocument user_collection_save_for_laters_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single userCollectionSaveForLater.

Retrieves single userCollectionSaveForLater by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_collection_save_for_laters_single_resource_data_document import UserCollectionSaveForLatersSingleResourceDataDocument
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
    api_instance = tidal.UserCollectionSaveForLatersApi(api_client)
    id = 'me' # str | User collection save for later id. Use `me` for the authenticated user's resource
    include = ['items'] # List[str] | Include related resources. Available relationships: items, owners (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items (optional)

    try:
        # Get single userCollectionSaveForLater.
        api_response = api_instance.user_collection_save_for_laters_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of UserCollectionSaveForLatersApi->user_collection_save_for_laters_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionSaveForLatersApi->user_collection_save_for_laters_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User collection save for later id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items, owners | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items | [optional] 

### Return type

[**UserCollectionSaveForLatersSingleResourceDataDocument**](UserCollectionSaveForLatersSingleResourceDataDocument.md)

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

# **user_collection_save_for_laters_id_relationships_items_delete**
> MutationResponseDocument user_collection_save_for_laters_id_relationships_items_delete(id, idempotency_key=idempotency_key, user_collection_save_for_laters_items_relationship_remove_operation_payload=user_collection_save_for_laters_items_relationship_remove_operation_payload)

Delete from items relationship (\"to-many\").

Deletes item(s) from items relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.user_collection_save_for_laters_items_relationship_remove_operation_payload import UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayload
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
    api_instance = tidal.UserCollectionSaveForLatersApi(api_client)
    id = 'me' # str | User collection save for later id. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_collection_save_for_laters_items_relationship_remove_operation_payload = tidal.UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayload() # UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayload |  (optional)

    try:
        # Delete from items relationship (\"to-many\").
        api_response = api_instance.user_collection_save_for_laters_id_relationships_items_delete(id, idempotency_key=idempotency_key, user_collection_save_for_laters_items_relationship_remove_operation_payload=user_collection_save_for_laters_items_relationship_remove_operation_payload)
        print("The response of UserCollectionSaveForLatersApi->user_collection_save_for_laters_id_relationships_items_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionSaveForLatersApi->user_collection_save_for_laters_id_relationships_items_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User collection save for later id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_collection_save_for_laters_items_relationship_remove_operation_payload** | [**UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayload**](UserCollectionSaveForLatersItemsRelationshipRemoveOperationPayload.md)|  | [optional] 

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

# **user_collection_save_for_laters_id_relationships_items_get**
> UserCollectionSaveForLatersItemsMultiRelationshipDataDocument user_collection_save_for_laters_id_relationships_items_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get items relationship (\"to-many\").

Retrieves items relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_collection_save_for_laters_items_multi_relationship_data_document import UserCollectionSaveForLatersItemsMultiRelationshipDataDocument
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
    api_instance = tidal.UserCollectionSaveForLatersApi(api_client)
    id = 'me' # str | User collection save for later id. Use `me` for the authenticated user's resource
    include = ['items'] # List[str] | Include related resources. Available relationships: items (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items (optional)

    try:
        # Get items relationship (\"to-many\").
        api_response = api_instance.user_collection_save_for_laters_id_relationships_items_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of UserCollectionSaveForLatersApi->user_collection_save_for_laters_id_relationships_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionSaveForLatersApi->user_collection_save_for_laters_id_relationships_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User collection save for later id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items | [optional] 

### Return type

[**UserCollectionSaveForLatersItemsMultiRelationshipDataDocument**](UserCollectionSaveForLatersItemsMultiRelationshipDataDocument.md)

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

# **user_collection_save_for_laters_id_relationships_items_post**
> UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocument user_collection_save_for_laters_id_relationships_items_post(id, idempotency_key=idempotency_key, user_collection_save_for_laters_items_relationship_add_operation_payload=user_collection_save_for_laters_items_relationship_add_operation_payload)

Add to items relationship (\"to-many\").

Adds item(s) to items relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_collection_save_for_laters_items_add_multi_relationship_data_document import UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocument
from tidal.models.user_collection_save_for_laters_items_relationship_add_operation_payload import UserCollectionSaveForLatersItemsRelationshipAddOperationPayload
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
    api_instance = tidal.UserCollectionSaveForLatersApi(api_client)
    id = 'me' # str | User collection save for later id. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_collection_save_for_laters_items_relationship_add_operation_payload = tidal.UserCollectionSaveForLatersItemsRelationshipAddOperationPayload() # UserCollectionSaveForLatersItemsRelationshipAddOperationPayload |  (optional)

    try:
        # Add to items relationship (\"to-many\").
        api_response = api_instance.user_collection_save_for_laters_id_relationships_items_post(id, idempotency_key=idempotency_key, user_collection_save_for_laters_items_relationship_add_operation_payload=user_collection_save_for_laters_items_relationship_add_operation_payload)
        print("The response of UserCollectionSaveForLatersApi->user_collection_save_for_laters_id_relationships_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionSaveForLatersApi->user_collection_save_for_laters_id_relationships_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User collection save for later id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_collection_save_for_laters_items_relationship_add_operation_payload** | [**UserCollectionSaveForLatersItemsRelationshipAddOperationPayload**](UserCollectionSaveForLatersItemsRelationshipAddOperationPayload.md)|  | [optional] 

### Return type

[**UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocument**](UserCollectionSaveForLatersItemsAddMultiRelationshipDataDocument.md)

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
**409** | Collection item limit reached; Collection already contains one or more items; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_collection_save_for_laters_id_relationships_owners_get**
> UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument user_collection_save_for_laters_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_collection_save_for_laters_owners_multi_relationship_data_document import UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.UserCollectionSaveForLatersApi(api_client)
    id = 'me' # str | User collection save for later id. Use `me` for the authenticated user's resource
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.user_collection_save_for_laters_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of UserCollectionSaveForLatersApi->user_collection_save_for_laters_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCollectionSaveForLatersApi->user_collection_save_for_laters_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User collection save for later id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument**](UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument.md)

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

