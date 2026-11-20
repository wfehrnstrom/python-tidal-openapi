# tidal.TrackStatisticsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**track_statistics_id_get**](TrackStatisticsApi.md#track_statistics_id_get) | **GET** /trackStatistics/{id} | Get single trackStatistic.
[**track_statistics_id_relationships_owners_get**](TrackStatisticsApi.md#track_statistics_id_relationships_owners_get) | **GET** /trackStatistics/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).


# **track_statistics_id_get**
> TrackStatisticsSingleResourceDataDocument track_statistics_id_get(id, country_code=country_code, include=include, include_linkage=include_linkage)

Get single trackStatistic.

Retrieves single trackStatistic by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.track_statistics_single_resource_data_document import TrackStatisticsSingleResourceDataDocument
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
    api_instance = tidal.TrackStatisticsApi(api_client)
    id = '123456' # str | Track statistic id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['include_example'] # List[str] | Include related resources. Available relationships: owners (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get single trackStatistic.
        api_response = api_instance.track_statistics_id_get(id, country_code=country_code, include=include, include_linkage=include_linkage)
        print("The response of TrackStatisticsApi->track_statistics_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackStatisticsApi->track_statistics_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track statistic id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 

### Return type

[**TrackStatisticsSingleResourceDataDocument**](TrackStatisticsSingleResourceDataDocument.md)

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

# **track_statistics_id_relationships_owners_get**
> TrackStatisticsOwnersMultiRelationshipDataDocument track_statistics_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.track_statistics_owners_multi_relationship_data_document import TrackStatisticsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.TrackStatisticsApi(api_client)
    id = '123456' # str | Track statistic id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.track_statistics_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of TrackStatisticsApi->track_statistics_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackStatisticsApi->track_statistics_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track statistic id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**TrackStatisticsOwnersMultiRelationshipDataDocument**](TrackStatisticsOwnersMultiRelationshipDataDocument.md)

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

