# tidal.TrackFilesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**track_files_id_get**](TrackFilesApi.md#track_files_id_get) | **GET** /trackFiles/{id} | Get single trackFile.


# **track_files_id_get**
> TrackFilesSingleResourceDataDocument track_files_id_get(formats, id, usage)

Get single trackFile.

Retrieves single trackFile by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.track_files_single_resource_data_document import TrackFilesSingleResourceDataDocument
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tidal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tidal.TrackFilesApi(api_client)
    formats = ['formats_example'] # List[str] | 
    id = '123456' # str | Track file id
    usage = 'usage_example' # str | 

    try:
        # Get single trackFile.
        api_response = api_instance.track_files_id_get(formats, id, usage)
        print("The response of TrackFilesApi->track_files_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackFilesApi->track_files_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **formats** | [**List[str]**](str.md)|  | 
 **id** | **str**| Track file id | 
 **usage** | **str**|  | 

### Return type

[**TrackFilesSingleResourceDataDocument**](TrackFilesSingleResourceDataDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE), [Client_Credentials](../README.md#Client_Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request |  -  |
**403** | Required playback prerequisites are missing; Content is unavailable in your location; Content must be purchased before playback; Client cannot access this content; Account is playing on another app or device |  -  |
**404** | Content does not exist or is no longer available |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**415** | Unsupported request media type or encoding |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

