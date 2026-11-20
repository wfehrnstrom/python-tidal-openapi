# tidal.UserFeedsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_feeds_id_get**](UserFeedsApi.md#user_feeds_id_get) | **GET** /userFeeds/{id} | Get single userFeed.
[**user_feeds_id_patch**](UserFeedsApi.md#user_feeds_id_patch) | **PATCH** /userFeeds/{id} | Update single userFeed.


# **user_feeds_id_get**
> UserFeedsSingleResourceDataDocument user_feeds_id_get(id)

Get single userFeed.

Retrieves single userFeed by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_feeds_single_resource_data_document import UserFeedsSingleResourceDataDocument
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
    api_instance = tidal.UserFeedsApi(api_client)
    id = 'me' # str | Opaque identifier of a user's feed state. Use `me` for the authenticated user's resource

    try:
        # Get single userFeed.
        api_response = api_instance.user_feeds_id_get(id)
        print("The response of UserFeedsApi->user_feeds_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFeedsApi->user_feeds_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque identifier of a user&#39;s feed state. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 

### Return type

[**UserFeedsSingleResourceDataDocument**](UserFeedsSingleResourceDataDocument.md)

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

# **user_feeds_id_patch**
> UserFeedsUpdateSingleResourceDataDocument user_feeds_id_patch(id, idempotency_key=idempotency_key, user_feeds_update_operation_payload=user_feeds_update_operation_payload)

Update single userFeed.

Advances the supplied seen positions and returns the updated feed state.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_feeds_update_operation_payload import UserFeedsUpdateOperationPayload
from tidal.models.user_feeds_update_single_resource_data_document import UserFeedsUpdateSingleResourceDataDocument
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
    api_instance = tidal.UserFeedsApi(api_client)
    id = 'me' # str | Opaque identifier of a user's feed state. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_feeds_update_operation_payload = tidal.UserFeedsUpdateOperationPayload() # UserFeedsUpdateOperationPayload |  (optional)

    try:
        # Update single userFeed.
        api_response = api_instance.user_feeds_id_patch(id, idempotency_key=idempotency_key, user_feeds_update_operation_payload=user_feeds_update_operation_payload)
        print("The response of UserFeedsApi->user_feeds_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFeedsApi->user_feeds_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque identifier of a user&#39;s feed state. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_feeds_update_operation_payload** | [**UserFeedsUpdateOperationPayload**](UserFeedsUpdateOperationPayload.md)|  | [optional] 

### Return type

[**UserFeedsUpdateSingleResourceDataDocument**](UserFeedsUpdateSingleResourceDataDocument.md)

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

