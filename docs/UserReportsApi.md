# tidal.UserReportsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_reports_post**](UserReportsApi.md#user_reports_post) | **POST** /userReports | Create single userReport.


# **user_reports_post**
> UserReportsCreateSingleResourceDataDocument user_reports_post(idempotency_key=idempotency_key, user_reports_create_operation_payload=user_reports_create_operation_payload)

Create single userReport.

Creates a new userReport.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_reports_create_operation_payload import UserReportsCreateOperationPayload
from tidal.models.user_reports_create_single_resource_data_document import UserReportsCreateSingleResourceDataDocument
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
    api_instance = tidal.UserReportsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_reports_create_operation_payload = tidal.UserReportsCreateOperationPayload() # UserReportsCreateOperationPayload |  (optional)

    try:
        # Create single userReport.
        api_response = api_instance.user_reports_post(idempotency_key=idempotency_key, user_reports_create_operation_payload=user_reports_create_operation_payload)
        print("The response of UserReportsApi->user_reports_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserReportsApi->user_reports_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_reports_create_operation_payload** | [**UserReportsCreateOperationPayload**](UserReportsCreateOperationPayload.md)|  | [optional] 

### Return type

[**UserReportsCreateSingleResourceDataDocument**](UserReportsCreateSingleResourceDataDocument.md)

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
**403** | Active report limit reached |  -  |
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

