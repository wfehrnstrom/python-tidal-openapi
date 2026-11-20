# tidal.SquareSitesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**square_sites_id_relationships_items_delete**](SquareSitesApi.md#square_sites_id_relationships_items_delete) | **DELETE** /squareSites/{id}/relationships/items | Delete from items relationship (\&quot;to-many\&quot;).
[**square_sites_id_relationships_items_get**](SquareSitesApi.md#square_sites_id_relationships_items_get) | **GET** /squareSites/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
[**square_sites_id_relationships_items_post**](SquareSitesApi.md#square_sites_id_relationships_items_post) | **POST** /squareSites/{id}/relationships/items | Add to items relationship (\&quot;to-many\&quot;).


# **square_sites_id_relationships_items_delete**
> MutationResponseDocument square_sites_id_relationships_items_delete(id, idempotency_key=idempotency_key, square_sites_items_relationship_remove_operation_payload=square_sites_items_relationship_remove_operation_payload)

Delete from items relationship (\"to-many\").

Removes the items from the site; they stay in the catalog. Items not published and repeated items are left alone. An item missing from the catalog fails the request before anything changes.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.square_sites_items_relationship_remove_operation_payload import SquareSitesItemsRelationshipRemoveOperationPayload
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
    api_instance = tidal.SquareSitesApi(api_client)
    id = 'IhETt7taHSVV2MUu9kqjMDengjnhVZa' # str | Square Online site id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    square_sites_items_relationship_remove_operation_payload = tidal.SquareSitesItemsRelationshipRemoveOperationPayload() # SquareSitesItemsRelationshipRemoveOperationPayload |  (optional)

    try:
        # Delete from items relationship (\"to-many\").
        api_response = api_instance.square_sites_id_relationships_items_delete(id, idempotency_key=idempotency_key, square_sites_items_relationship_remove_operation_payload=square_sites_items_relationship_remove_operation_payload)
        print("The response of SquareSitesApi->square_sites_id_relationships_items_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareSitesApi->square_sites_id_relationships_items_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square Online site id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **square_sites_items_relationship_remove_operation_payload** | [**SquareSitesItemsRelationshipRemoveOperationPayload**](SquareSitesItemsRelationshipRemoveOperationPayload.md)|  | [optional] 

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
**403** | Latest terms and conditions must be accepted |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Another request is changing the Square catalog; The site isn&#39;t the seller&#39;s selected Square Online site; select it to manage its items; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_sites_id_relationships_items_get**
> SquareSitesItemsMultiRelationshipDataDocument square_sites_id_relationships_items_get(id, include=include, page_cursor=page_cursor)

Get items relationship (\"to-many\").

Items published in the site, in title order. Missing catalog scopes return MISSING_ITEMS_SCOPE. A page can be short or empty and still have a next cursor.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_sites_items_multi_relationship_data_document import SquareSitesItemsMultiRelationshipDataDocument
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
    api_instance = tidal.SquareSitesApi(api_client)
    id = 'IhETt7taHSVV2MUu9kqjMDengjnhVZa' # str | Square Online site id
    include = ['items'] # List[str] | Include related resources. Available relationships: items (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get items relationship (\"to-many\").
        api_response = api_instance.square_sites_id_relationships_items_get(id, include=include, page_cursor=page_cursor)
        print("The response of SquareSitesApi->square_sites_id_relationships_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareSitesApi->square_sites_id_relationships_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square Online site id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**SquareSitesItemsMultiRelationshipDataDocument**](SquareSitesItemsMultiRelationshipDataDocument.md)

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
**403** | Latest terms and conditions must be accepted |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | Square credential lacks the catalog scopes; run Square onboarding again to reconnect; The site isn&#39;t the seller&#39;s selected Square Online site; select it to manage its items |  -  |
**415** | Unsupported request media type or encoding |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_sites_id_relationships_items_post**
> MutationResponseDocument square_sites_id_relationships_items_post(id, idempotency_key=idempotency_key, square_sites_items_relationship_add_operation_payload=square_sites_items_relationship_add_operation_payload)

Add to items relationship (\"to-many\").

Publishes the items in the site. Items already published and repeated items are left alone. An item missing from the catalog fails the request before anything changes.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.square_sites_items_relationship_add_operation_payload import SquareSitesItemsRelationshipAddOperationPayload
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
    api_instance = tidal.SquareSitesApi(api_client)
    id = 'IhETt7taHSVV2MUu9kqjMDengjnhVZa' # str | Square Online site id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    square_sites_items_relationship_add_operation_payload = tidal.SquareSitesItemsRelationshipAddOperationPayload() # SquareSitesItemsRelationshipAddOperationPayload |  (optional)

    try:
        # Add to items relationship (\"to-many\").
        api_response = api_instance.square_sites_id_relationships_items_post(id, idempotency_key=idempotency_key, square_sites_items_relationship_add_operation_payload=square_sites_items_relationship_add_operation_payload)
        print("The response of SquareSitesApi->square_sites_id_relationships_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareSitesApi->square_sites_id_relationships_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square Online site id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **square_sites_items_relationship_add_operation_payload** | [**SquareSitesItemsRelationshipAddOperationPayload**](SquareSitesItemsRelationshipAddOperationPayload.md)|  | [optional] 

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
**403** | Latest terms and conditions must be accepted |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Another request is changing the Square catalog; The site isn&#39;t the seller&#39;s selected Square Online site; select it to manage its items; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

