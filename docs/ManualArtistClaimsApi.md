# tidal.ManualArtistClaimsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**manual_artist_claims_post**](ManualArtistClaimsApi.md#manual_artist_claims_post) | **POST** /manualArtistClaims | Create single manualArtistClaim.


# **manual_artist_claims_post**
> ManualArtistClaimsCreateSingleResourceDataDocument manual_artist_claims_post(idempotency_key=idempotency_key, manual_artist_claims_create_operation_payload=manual_artist_claims_create_operation_payload)

Create single manualArtistClaim.

Creates a new manualArtistClaim.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.manual_artist_claims_create_operation_payload import ManualArtistClaimsCreateOperationPayload
from tidal.models.manual_artist_claims_create_single_resource_data_document import ManualArtistClaimsCreateSingleResourceDataDocument
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
    api_instance = tidal.ManualArtistClaimsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    manual_artist_claims_create_operation_payload = tidal.ManualArtistClaimsCreateOperationPayload() # ManualArtistClaimsCreateOperationPayload |  (optional)

    try:
        # Create single manualArtistClaim.
        api_response = api_instance.manual_artist_claims_post(idempotency_key=idempotency_key, manual_artist_claims_create_operation_payload=manual_artist_claims_create_operation_payload)
        print("The response of ManualArtistClaimsApi->manual_artist_claims_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManualArtistClaimsApi->manual_artist_claims_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **manual_artist_claims_create_operation_payload** | [**ManualArtistClaimsCreateOperationPayload**](ManualArtistClaimsCreateOperationPayload.md)|  | [optional] 

### Return type

[**ManualArtistClaimsCreateSingleResourceDataDocument**](ManualArtistClaimsCreateSingleResourceDataDocument.md)

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

