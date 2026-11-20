# tidal.ArtistClaimStatusesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artist_claim_statuses_get**](ArtistClaimStatusesApi.md#artist_claim_statuses_get) | **GET** /artistClaimStatuses | Get multiple artistClaimStatuses.


# **artist_claim_statuses_get**
> ArtistClaimStatusesMultiResourceDataDocument artist_claim_statuses_get(filter_id)

Get multiple artistClaimStatuses.

Retrieves multiple artistClaimStatuses by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artist_claim_statuses_multi_resource_data_document import ArtistClaimStatusesMultiResourceDataDocument
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
    api_instance = tidal.ArtistClaimStatusesApi(api_client)
    filter_id = ['filter_id_example'] # List[str] | List of artist claim status IDs (e.g. `QVJUSVNUUzoxNTY2`)

    try:
        # Get multiple artistClaimStatuses.
        api_response = api_instance.artist_claim_statuses_get(filter_id)
        print("The response of ArtistClaimStatusesApi->artist_claim_statuses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistClaimStatusesApi->artist_claim_statuses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | [**List[str]**](str.md)| List of artist claim status IDs (e.g. &#x60;QVJUSVNUUzoxNTY2&#x60;) | 

### Return type

[**ArtistClaimStatusesMultiResourceDataDocument**](ArtistClaimStatusesMultiResourceDataDocument.md)

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

