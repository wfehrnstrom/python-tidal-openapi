# tidal.ScopesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scopes_get**](ScopesApi.md#scopes_get) | **GET** /scopes | Get multiple scopes.


# **scopes_get**
> ScopesMultiResourceDataDocument scopes_get(filter_required_access_tier=filter_required_access_tier, filter_required_access_tier_satisfied_by=filter_required_access_tier_satisfied_by)

Get multiple scopes.

Retrieves multiple scopes by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.scopes_multi_resource_data_document import ScopesMultiResourceDataDocument
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
    api_instance = tidal.ScopesApi(api_client)
    filter_required_access_tier = ['filter_required_access_tier_example'] # List[str] | Filters scopes by their required client access tier. (e.g. `THIRD_PARTY`) (optional)
    filter_required_access_tier_satisfied_by = 'filter_required_access_tier_satisfied_by_example' # str | Selects scopes whose required access tier is satisfied by the client tier. (e.g. `PARTNER`) (optional)

    try:
        # Get multiple scopes.
        api_response = api_instance.scopes_get(filter_required_access_tier=filter_required_access_tier, filter_required_access_tier_satisfied_by=filter_required_access_tier_satisfied_by)
        print("The response of ScopesApi->scopes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScopesApi->scopes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_required_access_tier** | [**List[str]**](str.md)| Filters scopes by their required client access tier. (e.g. &#x60;THIRD_PARTY&#x60;) | [optional] 
 **filter_required_access_tier_satisfied_by** | **str**| Selects scopes whose required access tier is satisfied by the client tier. (e.g. &#x60;PARTNER&#x60;) | [optional] 

### Return type

[**ScopesMultiResourceDataDocument**](ScopesMultiResourceDataDocument.md)

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

