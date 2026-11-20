# tidal.SquareItemVariationsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operations_post**](SquareItemVariationsApi.md#operations_post) | **POST** /operations | Commit atomic resource operations
[**square_item_variations_id_delete**](SquareItemVariationsApi.md#square_item_variations_id_delete) | **DELETE** /squareItemVariations/{id} | Delete single squareItemVariation.
[**square_item_variations_id_get**](SquareItemVariationsApi.md#square_item_variations_id_get) | **GET** /squareItemVariations/{id} | Get single squareItemVariation.
[**square_item_variations_id_patch**](SquareItemVariationsApi.md#square_item_variations_id_patch) | **PATCH** /squareItemVariations/{id} | Update single squareItemVariation.
[**square_item_variations_id_relationships_artworks_get**](SquareItemVariationsApi.md#square_item_variations_id_relationships_artworks_get) | **GET** /squareItemVariations/{id}/relationships/artworks | Get artworks relationship (\&quot;to-many\&quot;).
[**square_item_variations_id_relationships_artworks_patch**](SquareItemVariationsApi.md#square_item_variations_id_relationships_artworks_patch) | **PATCH** /squareItemVariations/{id}/relationships/artworks | Update artworks relationship (\&quot;to-many\&quot;).
[**square_item_variations_id_relationships_owners_get**](SquareItemVariationsApi.md#square_item_variations_id_relationships_owners_get) | **GET** /squareItemVariations/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**square_item_variations_post**](SquareItemVariationsApi.md#square_item_variations_post) | **POST** /squareItemVariations | Create single squareItemVariation.


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
    api_instance = tidal.SquareItemVariationsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Retry an unchanged request with the original key after a timeout or server error. Replay is bounded by downstream receipt and idempotency retention.
    atomic_operations_request = tidal.AtomicOperationsRequest() # AtomicOperationsRequest | 

    try:
        # Commit atomic resource operations
        api_response = api_instance.operations_post(idempotency_key, atomic_operations_request)
        print("The response of SquareItemVariationsApi->operations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemVariationsApi->operations_post: %s\n" % e)
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

# **square_item_variations_id_delete**
> MutationResponseDocument square_item_variations_id_delete(id, idempotency_key)

Delete single squareItemVariation.

Deletes this variation by ID without a revision precondition, preserving its siblings. The last variation cannot be deleted; delete the item instead. Returns an acknowledgement; read the parent item for its current revision. After a timeout or `5xx`, retry unchanged with the original Idempotency-Key. Replay protection is bounded by receipt availability and Square's idempotency retention.

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
    api_instance = tidal.SquareItemVariationsApi(api_client)
    id = 'p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm' # str | Square variation id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.

    try:
        # Delete single squareItemVariation.
        api_response = api_instance.square_item_variations_id_delete(id, idempotency_key)
        print("The response of SquareItemVariationsApi->square_item_variations_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemVariationsApi->square_item_variations_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square variation id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | 

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
**409** | Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Square item changed; reload it before changing its variations; An item must retain at least one variation; Another request is changing the Square catalog; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_item_variations_id_get**
> SquareItemVariationsSingleResourceDataDocument square_item_variations_id_get(id, include=include, include_linkage=include_linkage)

Get single squareItemVariation.

Retrieves single squareItemVariation by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_item_variations_single_resource_data_document import SquareItemVariationsSingleResourceDataDocument
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
    api_instance = tidal.SquareItemVariationsApi(api_client)
    id = 'p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm' # str | Square variation id
    include = ['artworks'] # List[str] | Include related resources. Available relationships: artworks, owners (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get single squareItemVariation.
        api_response = api_instance.square_item_variations_id_get(id, include=include, include_linkage=include_linkage)
        print("The response of SquareItemVariationsApi->square_item_variations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemVariationsApi->square_item_variations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square variation id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artworks, owners | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 

### Return type

[**SquareItemVariationsSingleResourceDataDocument**](SquareItemVariationsSingleResourceDataDocument.md)

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

# **square_item_variations_id_patch**
> SquareItemVariationsUpdateSingleResourceDataDocument square_item_variations_id_patch(id, idempotency_key, square_item_variations_update_operation_payload=square_item_variations_update_operation_payload)

Update single squareItemVariation.

Updates the variation's global name or its price and stock tracking at the selected site's shipping location, with merchant-main fallback. Stock quantity is changed through physical-count submissions. Price changes require existing positive fixed pricing at that location; name and stock tracking preserve other pricing modes. After a timeout or `5xx`, retry unchanged with the original Idempotency-Key. Replay protection is bounded by receipt availability and Square's idempotency retention.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_item_variations_update_operation_payload import SquareItemVariationsUpdateOperationPayload
from tidal.models.square_item_variations_update_single_resource_data_document import SquareItemVariationsUpdateSingleResourceDataDocument
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
    api_instance = tidal.SquareItemVariationsApi(api_client)
    id = 'p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm' # str | Square variation id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
    square_item_variations_update_operation_payload = tidal.SquareItemVariationsUpdateOperationPayload() # SquareItemVariationsUpdateOperationPayload |  (optional)

    try:
        # Update single squareItemVariation.
        api_response = api_instance.square_item_variations_id_patch(id, idempotency_key, square_item_variations_update_operation_payload=square_item_variations_update_operation_payload)
        print("The response of SquareItemVariationsApi->square_item_variations_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemVariationsApi->square_item_variations_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square variation id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | 
 **square_item_variations_update_operation_payload** | [**SquareItemVariationsUpdateOperationPayload**](SquareItemVariationsUpdateOperationPayload.md)|  | [optional] 

### Return type

[**SquareItemVariationsUpdateSingleResourceDataDocument**](SquareItemVariationsUpdateSingleResourceDataDocument.md)

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
**409** | Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Square variation changed; reload it before editing; This variation&#39;s pricing cannot be edited here; edit it in Square Dashboard; Another request is changing the Square catalog; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_item_variations_id_relationships_artworks_get**
> SquareItemVariationsArtworksMultiRelationshipDataDocument square_item_variations_id_relationships_artworks_get(id, include=include, page_cursor=page_cursor)

Get artworks relationship (\"to-many\").

Artworks of the variation's Square catalog images in Square's display order. An image Square has no URL for stays in the list and its artwork has no files. Returns the variation revision the list was read at.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_item_variations_artworks_multi_relationship_data_document import SquareItemVariationsArtworksMultiRelationshipDataDocument
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
    api_instance = tidal.SquareItemVariationsApi(api_client)
    id = 'p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm' # str | Square variation id
    include = ['artworks'] # List[str] | Include related resources. Available relationships: artworks (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get artworks relationship (\"to-many\").
        api_response = api_instance.square_item_variations_id_relationships_artworks_get(id, include=include, page_cursor=page_cursor)
        print("The response of SquareItemVariationsApi->square_item_variations_id_relationships_artworks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemVariationsApi->square_item_variations_id_relationships_artworks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square variation id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artworks | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**SquareItemVariationsArtworksMultiRelationshipDataDocument**](SquareItemVariationsArtworksMultiRelationshipDataDocument.md)

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
**409** | Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Another request is changing the Square catalog |  -  |
**415** | Unsupported request media type or encoding |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_item_variations_id_relationships_artworks_patch**
> SquareItemVariationsArtworksUpdateMultiRelationshipDataDocument square_item_variations_id_relationships_artworks_patch(id, idempotency_key, square_item_variations_artworks_relationship_update_operation_payload=square_item_variations_artworks_relationship_update_operation_payload)

Update artworks relationship (\"to-many\").

Replaces the variation's photos with the complete ordered list. Omitted photos are detached and stay in the seller's Square catalog; an empty list clears them. The first artwork is the primary photo. Duplicate artwork IDs are rejected. Uploaded TIDAL JPEG artworks, at most 15,000,000 bytes, are copied to Square and attached under new artwork IDs; their originals stay unchanged. Existing Square artworks must belong to this seller and are attached directly; they need not be the item's photos. Returns the complete resulting linkage in display order and the committed variation revision. Copies may remain in Square if the replacement fails. Retry unchanged with the original Idempotency-Key after a timeout or 5xx. Recovery is bounded by Marketplace receipts and Square's idempotency retention, and can be blocked if the variation is deleted or a source becomes unavailable or ineligible. Read the variation again to reconcile its current state.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_item_variations_artworks_relationship_update_operation_payload import SquareItemVariationsArtworksRelationshipUpdateOperationPayload
from tidal.models.square_item_variations_artworks_update_multi_relationship_data_document import SquareItemVariationsArtworksUpdateMultiRelationshipDataDocument
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
    api_instance = tidal.SquareItemVariationsApi(api_client)
    id = 'p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm' # str | Square variation id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
    square_item_variations_artworks_relationship_update_operation_payload = tidal.SquareItemVariationsArtworksRelationshipUpdateOperationPayload() # SquareItemVariationsArtworksRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update artworks relationship (\"to-many\").
        api_response = api_instance.square_item_variations_id_relationships_artworks_patch(id, idempotency_key, square_item_variations_artworks_relationship_update_operation_payload=square_item_variations_artworks_relationship_update_operation_payload)
        print("The response of SquareItemVariationsApi->square_item_variations_id_relationships_artworks_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemVariationsApi->square_item_variations_id_relationships_artworks_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square variation id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | 
 **square_item_variations_artworks_relationship_update_operation_payload** | [**SquareItemVariationsArtworksRelationshipUpdateOperationPayload**](SquareItemVariationsArtworksRelationshipUpdateOperationPayload.md)|  | [optional] 

### Return type

[**SquareItemVariationsArtworksUpdateMultiRelationshipDataDocument**](SquareItemVariationsArtworksUpdateMultiRelationshipDataDocument.md)

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
**409** | Square variation changed; reload it before editing its artworks; Another request is changing the Square catalog; Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Request already in progress for this idempotency key |  -  |
**413** | Square images must be at most 15 MB (15,000,000 bytes) |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_item_variations_id_relationships_owners_get**
> SquareItemVariationsOwnersMultiRelationshipDataDocument square_item_variations_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_item_variations_owners_multi_relationship_data_document import SquareItemVariationsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.SquareItemVariationsApi(api_client)
    id = 'p67ILh4Qr7GGobTNrt3N7OK7wBV836KfxXfJMf7OGhHm' # str | Square variation id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.square_item_variations_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of SquareItemVariationsApi->square_item_variations_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemVariationsApi->square_item_variations_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square variation id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**SquareItemVariationsOwnersMultiRelationshipDataDocument**](SquareItemVariationsOwnersMultiRelationshipDataDocument.md)

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

# **square_item_variations_post**
> SquareItemVariationsCreateSingleResourceDataDocument square_item_variations_post(idempotency_key, square_item_variations_create_operation_payload=square_item_variations_create_operation_payload)

Create single squareItemVariation.

Adds a fixed-price variation at the end of the item's display order, preserving all existing variations and their pricing modes. After a timeout or `5xx`, retry unchanged with the original Idempotency-Key. Replay protection is bounded by receipt availability and Square's idempotency retention.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_item_variations_create_operation_payload import SquareItemVariationsCreateOperationPayload
from tidal.models.square_item_variations_create_single_resource_data_document import SquareItemVariationsCreateSingleResourceDataDocument
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
    api_instance = tidal.SquareItemVariationsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
    square_item_variations_create_operation_payload = tidal.SquareItemVariationsCreateOperationPayload() # SquareItemVariationsCreateOperationPayload |  (optional)

    try:
        # Create single squareItemVariation.
        api_response = api_instance.square_item_variations_post(idempotency_key, square_item_variations_create_operation_payload=square_item_variations_create_operation_payload)
        print("The response of SquareItemVariationsApi->square_item_variations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareItemVariationsApi->square_item_variations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | 
 **square_item_variations_create_operation_payload** | [**SquareItemVariationsCreateOperationPayload**](SquareItemVariationsCreateOperationPayload.md)|  | [optional] 

### Return type

[**SquareItemVariationsCreateSingleResourceDataDocument**](SquareItemVariationsCreateSingleResourceDataDocument.md)

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
**403** | Latest terms and conditions must be accepted |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | Square credential lacks the catalog scopes; run Square onboarding again to reconnect; Square item changed; reload it before changing its variations; Another request is changing the Square catalog; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

