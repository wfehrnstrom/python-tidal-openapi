# tidal.ArtistSalesStatisticsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artist_sales_statistics_get**](ArtistSalesStatisticsApi.md#artist_sales_statistics_get) | **GET** /artistSalesStatistics | Get multiple artistSalesStatistics.
[**artist_sales_statistics_id_relationships_artist_get**](ArtistSalesStatisticsApi.md#artist_sales_statistics_id_relationships_artist_get) | **GET** /artistSalesStatistics/{id}/relationships/artist | Get artist relationship (\&quot;to-one\&quot;).
[**artist_sales_statistics_id_relationships_top_sellers_get**](ArtistSalesStatisticsApi.md#artist_sales_statistics_id_relationships_top_sellers_get) | **GET** /artistSalesStatistics/{id}/relationships/topSellers | Get topSellers relationship (\&quot;to-many\&quot;).


# **artist_sales_statistics_get**
> ArtistSalesStatisticsMultiResourceDataDocument artist_sales_statistics_get(filter_artist_id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get multiple artistSalesStatistics.

Retrieves multiple artistSalesStatistics by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artist_sales_statistics_multi_resource_data_document import ArtistSalesStatisticsMultiResourceDataDocument
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
    api_instance = tidal.ArtistSalesStatisticsApi(api_client)
    filter_artist_id = ['filter_artist_id_example'] # List[str] | Artist ID. Every published range of the artist is returned (e.g. `1566`)
    include = ['artist.albums'] # List[str] | Include related resources. Available relationships: artist, topSellers (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'artist.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artist.albums (optional)

    try:
        # Get multiple artistSalesStatistics.
        api_response = api_instance.artist_sales_statistics_get(filter_artist_id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of ArtistSalesStatisticsApi->artist_sales_statistics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistSalesStatisticsApi->artist_sales_statistics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_artist_id** | [**List[str]**](str.md)| Artist ID. Every published range of the artist is returned (e.g. &#x60;1566&#x60;) | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artist, topSellers | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artist.albums | [optional] 

### Return type

[**ArtistSalesStatisticsMultiResourceDataDocument**](ArtistSalesStatisticsMultiResourceDataDocument.md)

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

# **artist_sales_statistics_id_relationships_artist_get**
> ArtistSalesStatisticsArtistSingleRelationshipDataDocument artist_sales_statistics_id_relationships_artist_get(id, include=include, replace_media=replace_media)

Get artist relationship (\"to-one\").

Retrieves artist relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artist_sales_statistics_artist_single_relationship_data_document import ArtistSalesStatisticsArtistSingleRelationshipDataDocument
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
    api_instance = tidal.ArtistSalesStatisticsApi(api_client)
    id = 'LPtReLsCUO7kRhYq' # str | Artist sales statistics id
    include = ['artist.albums'] # List[str] | Include related resources. Available relationships: artist (optional)
    replace_media = 'artist.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artist.albums (optional)

    try:
        # Get artist relationship (\"to-one\").
        api_response = api_instance.artist_sales_statistics_id_relationships_artist_get(id, include=include, replace_media=replace_media)
        print("The response of ArtistSalesStatisticsApi->artist_sales_statistics_id_relationships_artist_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistSalesStatisticsApi->artist_sales_statistics_id_relationships_artist_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist sales statistics id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artist | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artist.albums | [optional] 

### Return type

[**ArtistSalesStatisticsArtistSingleRelationshipDataDocument**](ArtistSalesStatisticsArtistSingleRelationshipDataDocument.md)

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

# **artist_sales_statistics_id_relationships_top_sellers_get**
> ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument artist_sales_statistics_id_relationships_top_sellers_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get topSellers relationship (\"to-many\").

Retrieves topSellers relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artist_sales_statistics_top_sellers_multi_relationship_data_document import ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistSalesStatisticsApi(api_client)
    id = 'LPtReLsCUO7kRhYq' # str | Artist sales statistics id
    include = ['topSellers'] # List[str] | Include related resources. Available relationships: topSellers (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'topSellers' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: topSellers (optional)

    try:
        # Get topSellers relationship (\"to-many\").
        api_response = api_instance.artist_sales_statistics_id_relationships_top_sellers_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of ArtistSalesStatisticsApi->artist_sales_statistics_id_relationships_top_sellers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistSalesStatisticsApi->artist_sales_statistics_id_relationships_top_sellers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist sales statistics id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: topSellers | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: topSellers | [optional] 

### Return type

[**ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument**](ArtistSalesStatisticsTopSellersMultiRelationshipDataDocument.md)

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

