# tidal.TermsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terms_get**](TermsApi.md#terms_get) | **GET** /terms | Get multiple terms.
[**terms_id_get**](TermsApi.md#terms_id_get) | **GET** /terms/{id} | Get single term.


# **terms_get**
> TermsMultiResourceDataDocument terms_get(filter_terms_type, filter_country_code=filter_country_code, filter_is_latest_version=filter_is_latest_version)

Get multiple terms.

Retrieves multiple terms by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.terms_multi_resource_data_document import TermsMultiResourceDataDocument
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
    api_instance = tidal.TermsApi(api_client)
    filter_terms_type = ['filter_terms_type_example'] # List[str] | One of: DEVELOPER, UPLOAD_MARKETPLACE, MERCH_GUIDELINES, TIDAL_CONNECT_DEVELOPER (e.g. `DEVELOPER`)
    filter_country_code = ['filter_country_code_example'] # List[str] | Selects the country-specific terms variant when it has an effective version; otherwise falls back to the worldwide (WW) variant. Combine with `filter[isLatestVersion]=true` to return the currently acceptable terms. (e.g. `US`) (optional)
    filter_is_latest_version = ['filter_is_latest_version_example'] # List[str] | Filter by isLatestVersion (optional)

    try:
        # Get multiple terms.
        api_response = api_instance.terms_get(filter_terms_type, filter_country_code=filter_country_code, filter_is_latest_version=filter_is_latest_version)
        print("The response of TermsApi->terms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->terms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_terms_type** | [**List[str]**](str.md)| One of: DEVELOPER, UPLOAD_MARKETPLACE, MERCH_GUIDELINES, TIDAL_CONNECT_DEVELOPER (e.g. &#x60;DEVELOPER&#x60;) | 
 **filter_country_code** | [**List[str]**](str.md)| Selects the country-specific terms variant when it has an effective version; otherwise falls back to the worldwide (WW) variant. Combine with &#x60;filter[isLatestVersion]&#x3D;true&#x60; to return the currently acceptable terms. (e.g. &#x60;US&#x60;) | [optional] 
 **filter_is_latest_version** | [**List[str]**](str.md)| Filter by isLatestVersion | [optional] 

### Return type

[**TermsMultiResourceDataDocument**](TermsMultiResourceDataDocument.md)

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

# **terms_id_get**
> TermsSingleResourceDataDocument terms_id_get(id)

Get single term.

Retrieves single term by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.terms_single_resource_data_document import TermsSingleResourceDataDocument
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
    api_instance = tidal.TermsApi(api_client)
    id = 'a468bee88def' # str | Terms id

    try:
        # Get single term.
        api_response = api_instance.terms_id_get(id)
        print("The response of TermsApi->terms_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->terms_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Terms id | 

### Return type

[**TermsSingleResourceDataDocument**](TermsSingleResourceDataDocument.md)

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

