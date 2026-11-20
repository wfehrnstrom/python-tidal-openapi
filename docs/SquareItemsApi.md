# tidal.SquareItemsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operations_post**](SquareItemsApi.md#operations_post) | **POST** /operations | Commit atomic resource operations
[**square_items_get**](SquareItemsApi.md#square_items_get) | **GET** /squareItems | Get multiple squareItems.
[**square_items_id_delete**](SquareItemsApi.md#square_items_id_delete) | **DELETE** /squareItems/{id} | Delete single squareItem.
[**square_items_id_get**](SquareItemsApi.md#square_items_id_get) | **GET** /squareItems/{id} | Get single squareItem.
[**square_items_id_patch**](SquareItemsApi.md#square_items_id_patch) | **PATCH** /squareItems/{id} | Update single squareItem.
[**square_items_id_relationships_artworks_get**](SquareItemsApi.md#square_items_id_relationships_artworks_get) | **GET** /squareItems/{id}/relationships/artworks | Get artworks relationship (\&quot;to-many\&quot;).
[**square_items_id_relationships_artworks_patch**](SquareItemsApi.md#square_items_id_relationships_artworks_patch) | **PATCH** /squareItems/{id}/relationships/artworks | Update artworks relationship (\&quot;to-many\&quot;).
[**square_items_id_relationships_owners_get**](SquareItemsApi.md#square_items_id_relationships_owners_get) | **GET** /squareItems/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**square_items_id_relationships_variations_get**](SquareItemsApi.md#square_items_id_relationships_variations_get) | **GET** /squareItems/{id}/relationships/variations | Get variations relationship (\&quot;to-many\&quot;).
[**square_items_id_relationships_variations_patch**](SquareItemsApi.md#square_items_id_relationships_variations_patch) | **PATCH** /squareItems/{id}/relationships/variations | Update variations relationship (\&quot;to-many\&quot;).


# **operations_post**
> AtomicOperationsResponse operations_post(idempotency_key, atomic_operations_request)

Commit atomic resource operations

Commits a supported group of resource creations together. Only add operations without ref or href are supported. Local linkage must reference an earlier creation. Each resource's mutation policy applies. After a timeout or server error, retry unchanged with the original Idempotency-Key. Replay is bounded by downstream receipt and idempotency retention.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.atomic_operations_request import AtomicOperationsRequest
from tidal.models.atomic_operations_response import AtomicOperationsResponse
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
    api_instance = tidal.SquareItemsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Retry an unchanged request with the original key after a timeout or server error. Replay is bounded by downstream receipt and idempotency retention.
    atomic_operations_request = tidal.AtomicOperationsRequest() # AtomicOperationsRequest | 

    try:
        # Commit atomic resource operations
        api_response = api_instance.operations_post(idempotency_key, atomic_operations_request)
        print("The response of SquareItemsApi->operations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemsApi->operations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Retry an unchanged request with the original key after a timeout or server error. Replay is bounded by downstream receipt and idempotency retention. | 
 **atomic_operations_request** | [**AtomicOperationsRequest**](AtomicOperationsRequest.md)|  | 

### Return type

[**AtomicOperationsResponse**](AtomicOperationsResponse.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json;ext="https://jsonapi.org/ext/atomic"
 - **Accept**: application/vnd.api+json;ext="https://jsonapi.org/ext/atomic"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Committed results, in the order of the requested operations |  -  |
**400** | Invalid request |  -  |
**403** | Latest terms and conditions must be accepted |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | Request already in progress for this idempotency key; Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Another request is changing the Square catalog; The site isn&#39;t the seller&#39;s selected Square Online site; select it to manage its items |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_items_get**
> SquareItemsMultiResourceDataDocument square_items_get(filter_owners_id, filter_origin=filter_origin, filter_self_matches_query=filter_self_matches_query, include=include, include_linkage=include_linkage, page_cursor=page_cursor)

Get multiple squareItems.

Retrieves multiple squareItems by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_items_multi_resource_data_document import SquareItemsMultiResourceDataDocument
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
    api_instance = tidal.SquareItemsApi(api_client)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`.
    filter_origin = 'filter_origin_example' # str | Only items with this origin (e.g. `TIDAL`) (optional)
    filter_self_matches_query = 'filter_self_matches_query_example' # str | Word-prefix match on item titles, descriptions and abbreviations, and on variation names, SKUs and UPCs (e.g. `tee`) (optional)
    include = ['artworks'] # List[str] | Include related resources. Available relationships: artworks, owners, variations (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get multiple squareItems.
        api_response = api_instance.square_items_get(filter_owners_id, filter_origin=filter_origin, filter_self_matches_query=filter_self_matches_query, include=include, include_linkage=include_linkage, page_cursor=page_cursor)
        print("The response of SquareItemsApi->square_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemsApi->square_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_owners_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | 
 **filter_origin** | **str**| Only items with this origin (e.g. &#x60;TIDAL&#x60;) | [optional] 
 **filter_self_matches_query** | **str**| Word-prefix match on item titles, descriptions and abbreviations, and on variation names, SKUs and UPCs (e.g. &#x60;tee&#x60;) | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artworks, owners, variations | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**SquareItemsMultiResourceDataDocument**](SquareItemsMultiResourceDataDocument.md)

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
**409** | Square credential lacks the catalog scopes; run Square onboarding again to reconnect |  -  |
**415** | Unsupported request media type or encoding |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_items_id_delete**
> MutationResponseDocument square_items_id_delete(id, idempotency_key=idempotency_key)

Delete single squareItem.

Deletes existing squareItem.

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
    api_instance = tidal.SquareItemsApi(api_client)
    id = 'p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay' # str | Square item id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)

    try:
        # Delete single squareItem.
        api_response = api_instance.square_items_id_delete(id, idempotency_key=idempotency_key)
        print("The response of SquareItemsApi->square_items_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemsApi->square_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square item id | 
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
**403** | Latest terms and conditions must be accepted |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Another request is changing the Square catalog; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_items_id_get**
> SquareItemsSingleResourceDataDocument square_items_id_get(id, include=include, include_linkage=include_linkage)

Get single squareItem.

Retrieves single squareItem by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_items_single_resource_data_document import SquareItemsSingleResourceDataDocument
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
    api_instance = tidal.SquareItemsApi(api_client)
    id = 'p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay' # str | Square item id
    include = ['artworks'] # List[str] | Include related resources. Available relationships: artworks, owners, variations (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get single squareItem.
        api_response = api_instance.square_items_id_get(id, include=include, include_linkage=include_linkage)
        print("The response of SquareItemsApi->square_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemsApi->square_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square item id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artworks, owners, variations | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 

### Return type

[**SquareItemsSingleResourceDataDocument**](SquareItemsSingleResourceDataDocument.md)

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
**409** | Square credential lacks the catalog scopes; run Square onboarding again to reconnect |  -  |
**415** | Unsupported request media type or encoding |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_items_id_patch**
> SquareItemsUpdateSingleResourceDataDocument square_items_id_patch(id, idempotency_key, square_items_update_operation_payload=square_items_update_operation_payload)

Update single squareItem.

Updates existing squareItem.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_items_update_operation_payload import SquareItemsUpdateOperationPayload
from tidal.models.square_items_update_single_resource_data_document import SquareItemsUpdateSingleResourceDataDocument
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
    api_instance = tidal.SquareItemsApi(api_client)
    id = 'p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay' # str | Square item id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
    square_items_update_operation_payload = tidal.SquareItemsUpdateOperationPayload() # SquareItemsUpdateOperationPayload |  (optional)

    try:
        # Update single squareItem.
        api_response = api_instance.square_items_id_patch(id, idempotency_key, square_items_update_operation_payload=square_items_update_operation_payload)
        print("The response of SquareItemsApi->square_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemsApi->square_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square item id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | 
 **square_items_update_operation_payload** | [**SquareItemsUpdateOperationPayload**](SquareItemsUpdateOperationPayload.md)|  | [optional] 

### Return type

[**SquareItemsUpdateSingleResourceDataDocument**](SquareItemsUpdateSingleResourceDataDocument.md)

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
**409** | Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Another request is changing the Square catalog; Square catalog item changed; reload it before editing; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_items_id_relationships_artworks_get**
> SquareItemsArtworksMultiRelationshipDataDocument square_items_id_relationships_artworks_get(id, include=include, page_cursor=page_cursor)

Get artworks relationship (\"to-many\").

A photo Square has no URL for stays in the list and its artwork has no files.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_items_artworks_multi_relationship_data_document import SquareItemsArtworksMultiRelationshipDataDocument
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
    api_instance = tidal.SquareItemsApi(api_client)
    id = 'p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay' # str | Square item id
    include = ['artworks'] # List[str] | Include related resources. Available relationships: artworks (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get artworks relationship (\"to-many\").
        api_response = api_instance.square_items_id_relationships_artworks_get(id, include=include, page_cursor=page_cursor)
        print("The response of SquareItemsApi->square_items_id_relationships_artworks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemsApi->square_items_id_relationships_artworks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square item id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artworks | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**SquareItemsArtworksMultiRelationshipDataDocument**](SquareItemsArtworksMultiRelationshipDataDocument.md)

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
**409** | Square credential lacks the catalog scopes; run Square onboarding again to reconnect |  -  |
**415** | Unsupported request media type or encoding |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_items_id_relationships_artworks_patch**
> SquareItemsArtworksUpdateMultiRelationshipDataDocument square_items_id_relationships_artworks_patch(id, idempotency_key, square_items_artworks_relationship_update_operation_payload=square_items_artworks_relationship_update_operation_payload)

Update artworks relationship (\"to-many\").

Replaces the item's photos with the complete ordered list. Omitted photos are detached and stay in the seller's Square catalog; an empty list clears them. The first artwork is the primary photo. Duplicate artwork IDs are rejected. Uploaded TIDAL JPEG artworks, at most 15,000,000 bytes, are copied to Square and attached under new artwork IDs; their originals stay unchanged. Existing Square artworks must belong to this seller and are attached directly. Returns the complete resulting linkage in display order and the committed item revision. Copies may remain in Square if the replacement fails. Retry unchanged with the original Idempotency-Key after a timeout or 5xx. Recovery is bounded by Marketplace receipts and Square's idempotency retention, and can be blocked if the item is deleted or a source becomes unavailable or ineligible. Read the item again to reconcile its current state.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_items_artworks_relationship_update_operation_payload import SquareItemsArtworksRelationshipUpdateOperationPayload
from tidal.models.square_items_artworks_update_multi_relationship_data_document import SquareItemsArtworksUpdateMultiRelationshipDataDocument
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
    api_instance = tidal.SquareItemsApi(api_client)
    id = 'p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay' # str | Square item id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
    square_items_artworks_relationship_update_operation_payload = tidal.SquareItemsArtworksRelationshipUpdateOperationPayload() # SquareItemsArtworksRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update artworks relationship (\"to-many\").
        api_response = api_instance.square_items_id_relationships_artworks_patch(id, idempotency_key, square_items_artworks_relationship_update_operation_payload=square_items_artworks_relationship_update_operation_payload)
        print("The response of SquareItemsApi->square_items_id_relationships_artworks_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemsApi->square_items_id_relationships_artworks_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square item id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | 
 **square_items_artworks_relationship_update_operation_payload** | [**SquareItemsArtworksRelationshipUpdateOperationPayload**](SquareItemsArtworksRelationshipUpdateOperationPayload.md)|  | [optional] 

### Return type

[**SquareItemsArtworksUpdateMultiRelationshipDataDocument**](SquareItemsArtworksUpdateMultiRelationshipDataDocument.md)

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
**409** | Square item changed; reload it before editing its artworks; Another request is changing the Square catalog; Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Request already in progress for this idempotency key |  -  |
**413** | Square images must be at most 15 MB (15,000,000 bytes) |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_items_id_relationships_owners_get**
> SquareItemsOwnersMultiRelationshipDataDocument square_items_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_items_owners_multi_relationship_data_document import SquareItemsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.SquareItemsApi(api_client)
    id = 'p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay' # str | Square item id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.square_items_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of SquareItemsApi->square_items_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemsApi->square_items_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square item id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**SquareItemsOwnersMultiRelationshipDataDocument**](SquareItemsOwnersMultiRelationshipDataDocument.md)

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

# **square_items_id_relationships_variations_get**
> SquareItemsVariationsMultiRelationshipDataDocument square_items_id_relationships_variations_get(id, include=include, page_cursor=page_cursor)

Get variations relationship (\"to-many\").

Variations in Square's display order.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_items_variations_multi_relationship_data_document import SquareItemsVariationsMultiRelationshipDataDocument
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
    api_instance = tidal.SquareItemsApi(api_client)
    id = 'p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay' # str | Square item id
    include = ['variations'] # List[str] | Include related resources. Available relationships: variations (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get variations relationship (\"to-many\").
        api_response = api_instance.square_items_id_relationships_variations_get(id, include=include, page_cursor=page_cursor)
        print("The response of SquareItemsApi->square_items_id_relationships_variations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemsApi->square_items_id_relationships_variations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square item id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: variations | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**SquareItemsVariationsMultiRelationshipDataDocument**](SquareItemsVariationsMultiRelationshipDataDocument.md)

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
**409** | Square credential lacks the catalog scopes; run Square onboarding again to reconnect |  -  |
**415** | Unsupported request media type or encoding |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_items_id_relationships_variations_patch**
> SquareItemsVariationsUpdateMultiRelationshipDataDocument square_items_id_relationships_variations_patch(id, idempotency_key, square_items_variations_relationship_update_operation_payload=square_items_variations_relationship_update_operation_payload)

Update variations relationship (\"to-many\").

Incrementally moves the selected variations as an ordered block before positionBefore, or to the end when omitted. Memberships are preserved; unselected variations retain their metadata and relative order. Empty data is rejected. Returns the affected linkage only and the updated item revision. After a timeout or `5xx`, retry unchanged with the original Idempotency-Key. Replay protection is bounded by receipt availability and Square's idempotency retention.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_items_variations_relationship_update_operation_payload import SquareItemsVariationsRelationshipUpdateOperationPayload
from tidal.models.square_items_variations_update_multi_relationship_data_document import SquareItemsVariationsUpdateMultiRelationshipDataDocument
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
    api_instance = tidal.SquareItemsApi(api_client)
    id = 'p67ILh4Qr7GGjIlwk4gBeQ5IHZIu0pXANdpGDmZfnFay' # str | Square item id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
    square_items_variations_relationship_update_operation_payload = tidal.SquareItemsVariationsRelationshipUpdateOperationPayload() # SquareItemsVariationsRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update variations relationship (\"to-many\").
        api_response = api_instance.square_items_id_relationships_variations_patch(id, idempotency_key, square_items_variations_relationship_update_operation_payload=square_items_variations_relationship_update_operation_payload)
        print("The response of SquareItemsApi->square_items_id_relationships_variations_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemsApi->square_items_id_relationships_variations_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square item id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | 
 **square_items_variations_relationship_update_operation_payload** | [**SquareItemsVariationsRelationshipUpdateOperationPayload**](SquareItemsVariationsRelationshipUpdateOperationPayload.md)|  | [optional] 

### Return type

[**SquareItemsVariationsUpdateMultiRelationshipDataDocument**](SquareItemsVariationsUpdateMultiRelationshipDataDocument.md)

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
**409** | Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Square catalog item changed; reload it before editing; Another request is changing the Square catalog; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

