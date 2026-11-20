# tidal.SquareConnectionsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**square_connections_id_get**](SquareConnectionsApi.md#square_connections_id_get) | **GET** /squareConnections/{id} | Get single squareConnection.
[**square_connections_id_relationships_selected_site_get**](SquareConnectionsApi.md#square_connections_id_relationships_selected_site_get) | **GET** /squareConnections/{id}/relationships/selectedSite | Get selectedSite relationship (\&quot;to-one\&quot;).
[**square_connections_id_relationships_selected_site_patch**](SquareConnectionsApi.md#square_connections_id_relationships_selected_site_patch) | **PATCH** /squareConnections/{id}/relationships/selectedSite | Update selectedSite relationship (\&quot;to-one\&quot;).
[**square_connections_id_relationships_sites_get**](SquareConnectionsApi.md#square_connections_id_relationships_sites_get) | **GET** /squareConnections/{id}/relationships/sites | Get sites relationship (\&quot;to-many\&quot;).
[**square_connections_post**](SquareConnectionsApi.md#square_connections_post) | **POST** /squareConnections | Create single squareConnection.


# **square_connections_id_get**
> SquareConnectionsSingleResourceDataDocument square_connections_id_get(id, include=include, include_linkage=include_linkage)

Get single squareConnection.

Retrieves single squareConnection by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_connections_single_resource_data_document import SquareConnectionsSingleResourceDataDocument
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
    api_instance = tidal.SquareConnectionsApi(api_client)
    id = 'me' # str | Square connection id. Use `me` for the authenticated user's resource
    include = ['selectedSite'] # List[str] | Include related resources. Available relationships: selectedSite, sites (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get single squareConnection.
        api_response = api_instance.square_connections_id_get(id, include=include, include_linkage=include_linkage)
        print("The response of SquareConnectionsApi->square_connections_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareConnectionsApi->square_connections_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square connection id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: selectedSite, sites | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 

### Return type

[**SquareConnectionsSingleResourceDataDocument**](SquareConnectionsSingleResourceDataDocument.md)

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
**415** | Unsupported request media type or encoding |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_connections_id_relationships_selected_site_get**
> SquareConnectionsSelectedSiteSingleRelationshipDataDocument square_connections_id_relationships_selected_site_get(id, include=include)

Get selectedSite relationship (\"to-one\").

Retrieves selectedSite relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_connections_selected_site_single_relationship_data_document import SquareConnectionsSelectedSiteSingleRelationshipDataDocument
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
    api_instance = tidal.SquareConnectionsApi(api_client)
    id = 'me' # str | Square connection id. Use `me` for the authenticated user's resource
    include = ['selectedSite'] # List[str] | Include related resources. Available relationships: selectedSite (optional)

    try:
        # Get selectedSite relationship (\"to-one\").
        api_response = api_instance.square_connections_id_relationships_selected_site_get(id, include=include)
        print("The response of SquareConnectionsApi->square_connections_id_relationships_selected_site_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareConnectionsApi->square_connections_id_relationships_selected_site_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square connection id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: selectedSite | [optional] 

### Return type

[**SquareConnectionsSelectedSiteSingleRelationshipDataDocument**](SquareConnectionsSelectedSiteSingleRelationshipDataDocument.md)

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
**415** | Unsupported request media type or encoding |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_connections_id_relationships_selected_site_patch**
> SquareConnectionsSelectedSiteUpdateSingleRelationshipDataDocument square_connections_id_relationships_selected_site_patch(id, idempotency_key=idempotency_key, square_connections_selected_site_relationship_update_operation_payload=square_connections_selected_site_relationship_update_operation_payload)

Update selectedSite relationship (\"to-one\").

Replaces the selected Square site. Explicit null data clears the selection without deleting the site. Returns the selected site linkage, or null data when cleared.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_connections_selected_site_relationship_update_operation_payload import SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload
from tidal.models.square_connections_selected_site_update_single_relationship_data_document import SquareConnectionsSelectedSiteUpdateSingleRelationshipDataDocument
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
    api_instance = tidal.SquareConnectionsApi(api_client)
    id = 'me' # str | Square connection id. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    square_connections_selected_site_relationship_update_operation_payload = tidal.SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload() # SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update selectedSite relationship (\"to-one\").
        api_response = api_instance.square_connections_id_relationships_selected_site_patch(id, idempotency_key=idempotency_key, square_connections_selected_site_relationship_update_operation_payload=square_connections_selected_site_relationship_update_operation_payload)
        print("The response of SquareConnectionsApi->square_connections_id_relationships_selected_site_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareConnectionsApi->square_connections_id_relationships_selected_site_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square connection id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **square_connections_selected_site_relationship_update_operation_payload** | [**SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload**](SquareConnectionsSelectedSiteRelationshipUpdateOperationPayload.md)|  | [optional] 

### Return type

[**SquareConnectionsSelectedSiteUpdateSingleRelationshipDataDocument**](SquareConnectionsSelectedSiteUpdateSingleRelationshipDataDocument.md)

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
**409** | Square credential lacks required site scopes; run Square onboarding again; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_connections_id_relationships_sites_get**
> SquareConnectionsSitesMultiRelationshipDataDocument square_connections_id_relationships_sites_get(id, include=include, page_cursor=page_cursor)

Get sites relationship (\"to-many\").

Retrieves sites relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_connections_sites_multi_relationship_data_document import SquareConnectionsSitesMultiRelationshipDataDocument
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
    api_instance = tidal.SquareConnectionsApi(api_client)
    id = 'me' # str | Square connection id. Use `me` for the authenticated user's resource
    include = ['sites'] # List[str] | Include related resources. Available relationships: sites (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get sites relationship (\"to-many\").
        api_response = api_instance.square_connections_id_relationships_sites_get(id, include=include, page_cursor=page_cursor)
        print("The response of SquareConnectionsApi->square_connections_id_relationships_sites_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareConnectionsApi->square_connections_id_relationships_sites_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Square connection id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: sites | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**SquareConnectionsSitesMultiRelationshipDataDocument**](SquareConnectionsSitesMultiRelationshipDataDocument.md)

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
**415** | Unsupported request media type or encoding |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **square_connections_post**
> SquareConnectionsCreateSingleResourceDataDocument square_connections_post(idempotency_key=idempotency_key, square_connections_create_operation_payload=square_connections_create_operation_payload)

Create single squareConnection.

Creates a new squareConnection.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.square_connections_create_operation_payload import SquareConnectionsCreateOperationPayload
from tidal.models.square_connections_create_single_resource_data_document import SquareConnectionsCreateSingleResourceDataDocument
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
    api_instance = tidal.SquareConnectionsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    square_connections_create_operation_payload = tidal.SquareConnectionsCreateOperationPayload() # SquareConnectionsCreateOperationPayload |  (optional)

    try:
        # Create single squareConnection.
        api_response = api_instance.square_connections_post(idempotency_key=idempotency_key, square_connections_create_operation_payload=square_connections_create_operation_payload)
        print("The response of SquareConnectionsApi->square_connections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SquareConnectionsApi->square_connections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **square_connections_create_operation_payload** | [**SquareConnectionsCreateOperationPayload**](SquareConnectionsCreateOperationPayload.md)|  | [optional] 

### Return type

[**SquareConnectionsCreateSingleResourceDataDocument**](SquareConnectionsCreateSingleResourceDataDocument.md)

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

