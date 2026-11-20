# tidal.StripeDashboardLinksApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stripe_dashboard_links_get**](StripeDashboardLinksApi.md#stripe_dashboard_links_get) | **GET** /stripeDashboardLinks | Get multiple stripeDashboardLinks.
[**stripe_dashboard_links_id_relationships_owners_get**](StripeDashboardLinksApi.md#stripe_dashboard_links_id_relationships_owners_get) | **GET** /stripeDashboardLinks/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).


# **stripe_dashboard_links_get**
> StripeDashboardLinksMultiResourceDataDocument stripe_dashboard_links_get(filter_owners_id, include=include, include_linkage=include_linkage)

Get multiple stripeDashboardLinks.

Retrieves multiple stripeDashboardLinks by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.stripe_dashboard_links_multi_resource_data_document import StripeDashboardLinksMultiResourceDataDocument
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
    api_instance = tidal.StripeDashboardLinksApi(api_client)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`.
    include = ['include_example'] # List[str] | Include related resources. Available relationships: owners (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get multiple stripeDashboardLinks.
        api_response = api_instance.stripe_dashboard_links_get(filter_owners_id, include=include, include_linkage=include_linkage)
        print("The response of StripeDashboardLinksApi->stripe_dashboard_links_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeDashboardLinksApi->stripe_dashboard_links_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_owners_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 

### Return type

[**StripeDashboardLinksMultiResourceDataDocument**](StripeDashboardLinksMultiResourceDataDocument.md)

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

# **stripe_dashboard_links_id_relationships_owners_get**
> StripeDashboardLinksOwnersMultiRelationshipDataDocument stripe_dashboard_links_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.stripe_dashboard_links_owners_multi_relationship_data_document import StripeDashboardLinksOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.StripeDashboardLinksApi(api_client)
    id = 'me' # str | Stripe dashboard link id. Use `me` for the authenticated user's resource
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.stripe_dashboard_links_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of StripeDashboardLinksApi->stripe_dashboard_links_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeDashboardLinksApi->stripe_dashboard_links_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Stripe dashboard link id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**StripeDashboardLinksOwnersMultiRelationshipDataDocument**](StripeDashboardLinksOwnersMultiRelationshipDataDocument.md)

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

