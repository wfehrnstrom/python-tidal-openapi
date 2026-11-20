# tidal.TemporaryUserTokensApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temporary_user_tokens_id_get**](TemporaryUserTokensApi.md#temporary_user_tokens_id_get) | **GET** /temporaryUserTokens/{id} | Get single temporaryUserToken.
[**temporary_user_tokens_id_relationships_owners_get**](TemporaryUserTokensApi.md#temporary_user_tokens_id_relationships_owners_get) | **GET** /temporaryUserTokens/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**temporary_user_tokens_post**](TemporaryUserTokensApi.md#temporary_user_tokens_post) | **POST** /temporaryUserTokens | Create single temporaryUserToken.


# **temporary_user_tokens_id_get**
> TemporaryUserTokensSingleResourceDataDocument temporary_user_tokens_id_get(id, include=include, include_linkage=include_linkage)

Get single temporaryUserToken.

Retrieves single temporaryUserToken by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.temporary_user_tokens_single_resource_data_document import TemporaryUserTokensSingleResourceDataDocument
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
    api_instance = tidal.TemporaryUserTokensApi(api_client)
    id = 'abc123' # str | Temporary user token id
    include = ['include_example'] # List[str] | Include related resources. Available relationships: owners (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get single temporaryUserToken.
        api_response = api_instance.temporary_user_tokens_id_get(id, include=include, include_linkage=include_linkage)
        print("The response of TemporaryUserTokensApi->temporary_user_tokens_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporaryUserTokensApi->temporary_user_tokens_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Temporary user token id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 

### Return type

[**TemporaryUserTokensSingleResourceDataDocument**](TemporaryUserTokensSingleResourceDataDocument.md)

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

# **temporary_user_tokens_id_relationships_owners_get**
> TemporaryUserTokensOwnersMultiRelationshipDataDocument temporary_user_tokens_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.temporary_user_tokens_owners_multi_relationship_data_document import TemporaryUserTokensOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.TemporaryUserTokensApi(api_client)
    id = 'abc123' # str | Temporary user token id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.temporary_user_tokens_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of TemporaryUserTokensApi->temporary_user_tokens_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporaryUserTokensApi->temporary_user_tokens_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Temporary user token id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**TemporaryUserTokensOwnersMultiRelationshipDataDocument**](TemporaryUserTokensOwnersMultiRelationshipDataDocument.md)

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

# **temporary_user_tokens_post**
> TemporaryUserTokensCreateSingleResourceDataDocument temporary_user_tokens_post(idempotency_key=idempotency_key, temporary_user_tokens_create_operation_payload=temporary_user_tokens_create_operation_payload)

Create single temporaryUserToken.

Creates a new temporaryUserToken.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.temporary_user_tokens_create_operation_payload import TemporaryUserTokensCreateOperationPayload
from tidal.models.temporary_user_tokens_create_single_resource_data_document import TemporaryUserTokensCreateSingleResourceDataDocument
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
    api_instance = tidal.TemporaryUserTokensApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    temporary_user_tokens_create_operation_payload = tidal.TemporaryUserTokensCreateOperationPayload() # TemporaryUserTokensCreateOperationPayload |  (optional)

    try:
        # Create single temporaryUserToken.
        api_response = api_instance.temporary_user_tokens_post(idempotency_key=idempotency_key, temporary_user_tokens_create_operation_payload=temporary_user_tokens_create_operation_payload)
        print("The response of TemporaryUserTokensApi->temporary_user_tokens_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporaryUserTokensApi->temporary_user_tokens_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **temporary_user_tokens_create_operation_payload** | [**TemporaryUserTokensCreateOperationPayload**](TemporaryUserTokensCreateOperationPayload.md)|  | [optional] 

### Return type

[**TemporaryUserTokensCreateSingleResourceDataDocument**](TemporaryUserTokensCreateSingleResourceDataDocument.md)

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

