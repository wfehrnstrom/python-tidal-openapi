# tidal.SavedSharesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**saved_shares_post**](SavedSharesApi.md#saved_shares_post) | **POST** /savedShares | Create single savedShare.


# **saved_shares_post**
> SavedSharesCreateSingleResourceDataDocument saved_shares_post(idempotency_key=idempotency_key, saved_shares_create_operation_payload=saved_shares_create_operation_payload)

Create single savedShare.

Redeem an active share with VOUCHER access mode for its offered role. A share without VOUCHER mode returns 403. Every save, repeated ones included, needs a password-protected share's password and counts as a use of a limited share; password attempts are rate limited.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.saved_shares_create_operation_payload import SavedSharesCreateOperationPayload
from tidal.models.saved_shares_create_single_resource_data_document import SavedSharesCreateSingleResourceDataDocument
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
    api_instance = tidal.SavedSharesApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    saved_shares_create_operation_payload = tidal.SavedSharesCreateOperationPayload() # SavedSharesCreateOperationPayload |  (optional)

    try:
        # Create single savedShare.
        api_response = api_instance.saved_shares_post(idempotency_key=idempotency_key, saved_shares_create_operation_payload=saved_shares_create_operation_payload)
        print("The response of SavedSharesApi->saved_shares_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedSharesApi->saved_shares_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **saved_shares_create_operation_payload** | [**SavedSharesCreateOperationPayload**](SavedSharesCreateOperationPayload.md)|  | [optional] 

### Return type

[**SavedSharesCreateSingleResourceDataDocument**](SavedSharesCreateSingleResourceDataDocument.md)

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
**403** | This share does not permit redemption; This share can no longer be accepted; The share is password protected; send its password; The share password is incorrect |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Too many share password attempts; try again later |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

