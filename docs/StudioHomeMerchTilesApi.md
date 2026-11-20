# tidal.StudioHomeMerchTilesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**studio_home_merch_tiles_id_get**](StudioHomeMerchTilesApi.md#studio_home_merch_tiles_id_get) | **GET** /studioHomeMerchTiles/{id} | Get single studioHomeMerchTile.
[**studio_home_merch_tiles_id_relationships_items_get**](StudioHomeMerchTilesApi.md#studio_home_merch_tiles_id_relationships_items_get) | **GET** /studioHomeMerchTiles/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).


# **studio_home_merch_tiles_id_get**
> StudioHomeMerchTilesSingleResourceDataDocument studio_home_merch_tiles_id_get(id, include=include, include_linkage=include_linkage)

Get single studioHomeMerchTile.

Retrieves single studioHomeMerchTile by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.studio_home_merch_tiles_single_resource_data_document import StudioHomeMerchTilesSingleResourceDataDocument
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
    api_instance = tidal.StudioHomeMerchTilesApi(api_client)
    id = 'me' # str | Studio Home merch tile id. Use `me` for the authenticated user's resource
    include = ['items'] # List[str] | Include related resources. Available relationships: items (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get single studioHomeMerchTile.
        api_response = api_instance.studio_home_merch_tiles_id_get(id, include=include, include_linkage=include_linkage)
        print("The response of StudioHomeMerchTilesApi->studio_home_merch_tiles_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioHomeMerchTilesApi->studio_home_merch_tiles_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Studio Home merch tile id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 

### Return type

[**StudioHomeMerchTilesSingleResourceDataDocument**](StudioHomeMerchTilesSingleResourceDataDocument.md)

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

# **studio_home_merch_tiles_id_relationships_items_get**
> StudioHomeMerchTilesItemsMultiRelationshipDataDocument studio_home_merch_tiles_id_relationships_items_get(id, include=include, page_cursor=page_cursor)

Get items relationship (\"to-many\").

The seller's catalog items, in title order; empty until the latest merch guidelines are accepted. A page can be short or empty and still have a next cursor.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.studio_home_merch_tiles_items_multi_relationship_data_document import StudioHomeMerchTilesItemsMultiRelationshipDataDocument
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
    api_instance = tidal.StudioHomeMerchTilesApi(api_client)
    id = 'me' # str | Studio Home merch tile id. Use `me` for the authenticated user's resource
    include = ['items'] # List[str] | Include related resources. Available relationships: items (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get items relationship (\"to-many\").
        api_response = api_instance.studio_home_merch_tiles_id_relationships_items_get(id, include=include, page_cursor=page_cursor)
        print("The response of StudioHomeMerchTilesApi->studio_home_merch_tiles_id_relationships_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioHomeMerchTilesApi->studio_home_merch_tiles_id_relationships_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Studio Home merch tile id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**StudioHomeMerchTilesItemsMultiRelationshipDataDocument**](StudioHomeMerchTilesItemsMultiRelationshipDataDocument.md)

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

