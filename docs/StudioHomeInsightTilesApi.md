# tidal.StudioHomeInsightTilesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**studio_home_insight_tiles_id_get**](StudioHomeInsightTilesApi.md#studio_home_insight_tiles_id_get) | **GET** /studioHomeInsightTiles/{id} | Get single studioHomeInsightTile.


# **studio_home_insight_tiles_id_get**
> StudioHomeInsightTilesSingleResourceDataDocument studio_home_insight_tiles_id_get(id)

Get single studioHomeInsightTile.

Retrieves single studioHomeInsightTile by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.studio_home_insight_tiles_single_resource_data_document import StudioHomeInsightTilesSingleResourceDataDocument
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
    api_instance = tidal.StudioHomeInsightTilesApi(api_client)
    id = 'me' # str | Studio Home insight tile id. Use `me` for the authenticated user's resource

    try:
        # Get single studioHomeInsightTile.
        api_response = api_instance.studio_home_insight_tiles_id_get(id)
        print("The response of StudioHomeInsightTilesApi->studio_home_insight_tiles_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioHomeInsightTilesApi->studio_home_insight_tiles_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Studio Home insight tile id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 

### Return type

[**StudioHomeInsightTilesSingleResourceDataDocument**](StudioHomeInsightTilesSingleResourceDataDocument.md)

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

