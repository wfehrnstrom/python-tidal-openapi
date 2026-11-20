# tidal.ClientCertificatesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_certificates_id_get**](ClientCertificatesApi.md#client_certificates_id_get) | **GET** /clientCertificates/{id} | Get single clientCertificate.
[**client_certificates_id_relationships_owners_get**](ClientCertificatesApi.md#client_certificates_id_relationships_owners_get) | **GET** /clientCertificates/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**client_certificates_post**](ClientCertificatesApi.md#client_certificates_post) | **POST** /clientCertificates | Create single clientCertificate.


# **client_certificates_id_get**
> ClientCertificatesSingleResourceDataDocument client_certificates_id_get(id, include=include, include_linkage=include_linkage)

Get single clientCertificate.

Retrieves single clientCertificate by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.client_certificates_single_resource_data_document import ClientCertificatesSingleResourceDataDocument
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
    api_instance = tidal.ClientCertificatesApi(api_client)
    id = '0cb39ea1-1d2d-4f56-b5cf-195b34b2a727' # str | TIDAL Connect client certificate identifier
    include = ['include_example'] # List[str] | Include related resources. Available relationships: owners (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get single clientCertificate.
        api_response = api_instance.client_certificates_id_get(id, include=include, include_linkage=include_linkage)
        print("The response of ClientCertificatesApi->client_certificates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientCertificatesApi->client_certificates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TIDAL Connect client certificate identifier | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 

### Return type

[**ClientCertificatesSingleResourceDataDocument**](ClientCertificatesSingleResourceDataDocument.md)

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

# **client_certificates_id_relationships_owners_get**
> ClientCertificatesOwnersMultiRelationshipDataDocument client_certificates_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.client_certificates_owners_multi_relationship_data_document import ClientCertificatesOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.ClientCertificatesApi(api_client)
    id = '0cb39ea1-1d2d-4f56-b5cf-195b34b2a727' # str | TIDAL Connect client certificate identifier
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.client_certificates_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of ClientCertificatesApi->client_certificates_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientCertificatesApi->client_certificates_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TIDAL Connect client certificate identifier | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**ClientCertificatesOwnersMultiRelationshipDataDocument**](ClientCertificatesOwnersMultiRelationshipDataDocument.md)

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

# **client_certificates_post**
> ClientCertificatesCreateSingleResourceDataDocument client_certificates_post(idempotency_key=idempotency_key, client_certificates_create_operation_payload=client_certificates_create_operation_payload)

Create single clientCertificate.

Creates a new clientCertificate.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.client_certificates_create_operation_payload import ClientCertificatesCreateOperationPayload
from tidal.models.client_certificates_create_single_resource_data_document import ClientCertificatesCreateSingleResourceDataDocument
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
    api_instance = tidal.ClientCertificatesApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    client_certificates_create_operation_payload = tidal.ClientCertificatesCreateOperationPayload() # ClientCertificatesCreateOperationPayload |  (optional)

    try:
        # Create single clientCertificate.
        api_response = api_instance.client_certificates_post(idempotency_key=idempotency_key, client_certificates_create_operation_payload=client_certificates_create_operation_payload)
        print("The response of ClientCertificatesApi->client_certificates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientCertificatesApi->client_certificates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **client_certificates_create_operation_payload** | [**ClientCertificatesCreateOperationPayload**](ClientCertificatesCreateOperationPayload.md)|  | [optional] 

### Return type

[**ClientCertificatesCreateSingleResourceDataDocument**](ClientCertificatesCreateSingleResourceDataDocument.md)

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

