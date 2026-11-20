# tidal.ArtistRolesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artist_roles_id_get**](ArtistRolesApi.md#artist_roles_id_get) | **GET** /artistRoles/{id} | Get single artistRole.


# **artist_roles_id_get**
> ArtistRolesSingleResourceDataDocument artist_roles_id_get(id)

Get single artistRole.

Retrieves single artistRole by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artist_roles_single_resource_data_document import ArtistRolesSingleResourceDataDocument
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
    api_instance = tidal.ArtistRolesApi(api_client)
    id = '1' # str | Artist role id

    try:
        # Get single artistRole.
        api_response = api_instance.artist_roles_id_get(id)
        print("The response of ArtistRolesApi->artist_roles_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistRolesApi->artist_roles_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist role id | 

### Return type

[**ArtistRolesSingleResourceDataDocument**](ArtistRolesSingleResourceDataDocument.md)

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
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**415** | Unsupported request media type or encoding |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

