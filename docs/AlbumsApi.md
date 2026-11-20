# tidal.AlbumsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**albums_get**](AlbumsApi.md#albums_get) | **GET** /albums | Get multiple albums.
[**albums_id_delete**](AlbumsApi.md#albums_id_delete) | **DELETE** /albums/{id} | Delete single album.
[**albums_id_get**](AlbumsApi.md#albums_id_get) | **GET** /albums/{id} | Get single album.
[**albums_id_patch**](AlbumsApi.md#albums_id_patch) | **PATCH** /albums/{id} | Update single album.
[**albums_id_relationships_album_statistics_get**](AlbumsApi.md#albums_id_relationships_album_statistics_get) | **GET** /albums/{id}/relationships/albumStatistics | Get albumStatistics relationship (\&quot;to-one\&quot;).
[**albums_id_relationships_artists_get**](AlbumsApi.md#albums_id_relationships_artists_get) | **GET** /albums/{id}/relationships/artists | Get artists relationship (\&quot;to-many\&quot;).
[**albums_id_relationships_artists_patch**](AlbumsApi.md#albums_id_relationships_artists_patch) | **PATCH** /albums/{id}/relationships/artists | Update artists relationship (\&quot;to-many\&quot;).
[**albums_id_relationships_cover_art_get**](AlbumsApi.md#albums_id_relationships_cover_art_get) | **GET** /albums/{id}/relationships/coverArt | Get coverArt relationship (\&quot;to-many\&quot;).
[**albums_id_relationships_cover_art_patch**](AlbumsApi.md#albums_id_relationships_cover_art_patch) | **PATCH** /albums/{id}/relationships/coverArt | Update coverArt relationship (\&quot;to-many\&quot;).
[**albums_id_relationships_genres_get**](AlbumsApi.md#albums_id_relationships_genres_get) | **GET** /albums/{id}/relationships/genres | Get genres relationship (\&quot;to-many\&quot;).
[**albums_id_relationships_items_get**](AlbumsApi.md#albums_id_relationships_items_get) | **GET** /albums/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
[**albums_id_relationships_items_patch**](AlbumsApi.md#albums_id_relationships_items_patch) | **PATCH** /albums/{id}/relationships/items | Update items relationship (\&quot;to-many\&quot;).
[**albums_id_relationships_owners_get**](AlbumsApi.md#albums_id_relationships_owners_get) | **GET** /albums/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**albums_id_relationships_price_config_get**](AlbumsApi.md#albums_id_relationships_price_config_get) | **GET** /albums/{id}/relationships/priceConfig | Get priceConfig relationship (\&quot;to-one\&quot;).
[**albums_id_relationships_providers_get**](AlbumsApi.md#albums_id_relationships_providers_get) | **GET** /albums/{id}/relationships/providers | Get providers relationship (\&quot;to-many\&quot;).
[**albums_id_relationships_replacement_get**](AlbumsApi.md#albums_id_relationships_replacement_get) | **GET** /albums/{id}/relationships/replacement | Get replacement relationship (\&quot;to-one\&quot;).
[**albums_id_relationships_shares_get**](AlbumsApi.md#albums_id_relationships_shares_get) | **GET** /albums/{id}/relationships/shares | Get shares relationship (\&quot;to-many\&quot;).
[**albums_id_relationships_similar_albums_get**](AlbumsApi.md#albums_id_relationships_similar_albums_get) | **GET** /albums/{id}/relationships/similarAlbums | Get similarAlbums relationship (\&quot;to-many\&quot;).
[**albums_id_relationships_suggested_cover_arts_get**](AlbumsApi.md#albums_id_relationships_suggested_cover_arts_get) | **GET** /albums/{id}/relationships/suggestedCoverArts | Get suggestedCoverArts relationship (\&quot;to-many\&quot;).
[**albums_id_relationships_usage_rules_get**](AlbumsApi.md#albums_id_relationships_usage_rules_get) | **GET** /albums/{id}/relationships/usageRules | Get usageRules relationship (\&quot;to-one\&quot;).
[**albums_post**](AlbumsApi.md#albums_post) | **POST** /albums | Create single album.


# **albums_get**
> AlbumsMultiResourceDataDocument albums_get(country_code=country_code, filter_barcode_id=filter_barcode_id, filter_id=filter_id, filter_owners_id=filter_owners_id, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code, sort=sort)

Get multiple albums.

Retrieves multiple albums by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.albums_multi_resource_data_document import AlbumsMultiResourceDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    filter_barcode_id = ['filter_barcode_id_example'] # List[str] | List of barcode IDs (EAN-13 or UPC-A). NOTE: Supplying more than one barcode ID will currently only return one album per barcode ID. (e.g. `196589525444`) (optional)
    filter_id = ['filter_id_example'] # List[str] | List of album IDs (e.g. `251380836`) (optional)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`. (optional)
    include = ['artists.albums'] # List[str] | Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'artists.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)
    sort = ['sort_example'] # List[str] | Values prefixed with \"-\" are sorted descending; values without it are sorted ascending. (optional)

    try:
        # Get multiple albums.
        api_response = api_instance.albums_get(country_code=country_code, filter_barcode_id=filter_barcode_id, filter_id=filter_id, filter_owners_id=filter_owners_id, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code, sort=sort)
        print("The response of AlbumsApi->albums_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **filter_barcode_id** | [**List[str]**](str.md)| List of barcode IDs (EAN-13 or UPC-A). NOTE: Supplying more than one barcode ID will currently only return one album per barcode ID. (e.g. &#x60;196589525444&#x60;) | [optional] 
 **filter_id** | [**List[str]**](str.md)| List of album IDs (e.g. &#x60;251380836&#x60;) | [optional] 
 **filter_owners_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 
 **sort** | [**List[str]**](str.md)| Values prefixed with \&quot;-\&quot; are sorted descending; values without it are sorted ascending. | [optional] 

### Return type

[**AlbumsMultiResourceDataDocument**](AlbumsMultiResourceDataDocument.md)

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

# **albums_id_delete**
> MutationResponseDocument albums_id_delete(id, idempotency_key=idempotency_key, share_code=share_code)

Delete single album.

Deletes existing album.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Delete single album.
        api_response = api_instance.albums_id_delete(id, idempotency_key=idempotency_key, share_code=share_code)
        print("The response of AlbumsApi->albums_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**MutationResponseDocument**](MutationResponseDocument.md)

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
**409** | Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **albums_id_get**
> AlbumsSingleResourceDataDocument albums_id_get(id, country_code=country_code, include=include, include_linkage=include_linkage, replace_media=replace_media, share_code=share_code)

Get single album.

Retrieves single album by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.albums_single_resource_data_document import AlbumsSingleResourceDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['artists.albums'] # List[str] | Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'artists.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get single album.
        api_response = api_instance.albums_id_get(id, country_code=country_code, include=include, include_linkage=include_linkage, replace_media=replace_media, share_code=share_code)
        print("The response of AlbumsApi->albums_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**AlbumsSingleResourceDataDocument**](AlbumsSingleResourceDataDocument.md)

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

# **albums_id_patch**
> MutationResponseDocument albums_id_patch(id, idempotency_key=idempotency_key, share_code=share_code, albums_update_operation_payload=albums_update_operation_payload)

Update single album.

Updates existing album. A COLLABORATOR on the album may update it; changing accessType, published or barcodeId needs OWNER.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.albums_update_operation_payload import AlbumsUpdateOperationPayload
from tidal.models.mutation_response_document import MutationResponseDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)
    albums_update_operation_payload = tidal.AlbumsUpdateOperationPayload() # AlbumsUpdateOperationPayload |  (optional)

    try:
        # Update single album.
        api_response = api_instance.albums_id_patch(id, idempotency_key=idempotency_key, share_code=share_code, albums_update_operation_payload=albums_update_operation_payload)
        print("The response of AlbumsApi->albums_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 
 **albums_update_operation_payload** | [**AlbumsUpdateOperationPayload**](AlbumsUpdateOperationPayload.md)|  | [optional] 

### Return type

[**MutationResponseDocument**](MutationResponseDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **albums_id_relationships_album_statistics_get**
> AlbumsAlbumStatisticsSingleRelationshipDataDocument albums_id_relationships_album_statistics_get(id, include=include, share_code=share_code)

Get albumStatistics relationship (\"to-one\").

Retrieves albumStatistics relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.albums_album_statistics_single_relationship_data_document import AlbumsAlbumStatisticsSingleRelationshipDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    include = ['albumStatistics'] # List[str] | Include related resources. Available relationships: albumStatistics (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get albumStatistics relationship (\"to-one\").
        api_response = api_instance.albums_id_relationships_album_statistics_get(id, include=include, share_code=share_code)
        print("The response of AlbumsApi->albums_id_relationships_album_statistics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_album_statistics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: albumStatistics | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**AlbumsAlbumStatisticsSingleRelationshipDataDocument**](AlbumsAlbumStatisticsSingleRelationshipDataDocument.md)

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

# **albums_id_relationships_artists_get**
> AlbumsArtistsMultiRelationshipDataDocument albums_id_relationships_artists_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)

Get artists relationship (\"to-many\").

Retrieves artists relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.albums_artists_multi_relationship_data_document import AlbumsArtistsMultiRelationshipDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['artists.albums'] # List[str] | Include related resources. Available relationships: artists (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'artists.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get artists relationship (\"to-many\").
        api_response = api_instance.albums_id_relationships_artists_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)
        print("The response of AlbumsApi->albums_id_relationships_artists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_artists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artists | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**AlbumsArtistsMultiRelationshipDataDocument**](AlbumsArtistsMultiRelationshipDataDocument.md)

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

# **albums_id_relationships_artists_patch**
> MutationResponseDocument albums_id_relationships_artists_patch(id, idempotency_key=idempotency_key, share_code=share_code, albums_artists_relationship_update_operation_payload=albums_artists_relationship_update_operation_payload)

Update artists relationship (\"to-many\").

Sets the album's artists, replacing the current list. Artists are listed in the order given. Provide 1 to 10 distinct artists. You can add your own artist profile and the profiles of users who have owner or collaborator access to the album. Owners and collaborators can change its artists. Returns an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.albums_artists_relationship_update_operation_payload import AlbumsArtistsRelationshipUpdateOperationPayload
from tidal.models.mutation_response_document import MutationResponseDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)
    albums_artists_relationship_update_operation_payload = tidal.AlbumsArtistsRelationshipUpdateOperationPayload() # AlbumsArtistsRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update artists relationship (\"to-many\").
        api_response = api_instance.albums_id_relationships_artists_patch(id, idempotency_key=idempotency_key, share_code=share_code, albums_artists_relationship_update_operation_payload=albums_artists_relationship_update_operation_payload)
        print("The response of AlbumsApi->albums_id_relationships_artists_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_artists_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 
 **albums_artists_relationship_update_operation_payload** | [**AlbumsArtistsRelationshipUpdateOperationPayload**](AlbumsArtistsRelationshipUpdateOperationPayload.md)|  | [optional] 

### Return type

[**MutationResponseDocument**](MutationResponseDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **albums_id_relationships_cover_art_get**
> AlbumsCoverArtMultiRelationshipDataDocument albums_id_relationships_cover_art_get(id, country_code=country_code, include=include, page_cursor=page_cursor, share_code=share_code)

Get coverArt relationship (\"to-many\").

Retrieves coverArt relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.albums_cover_art_multi_relationship_data_document import AlbumsCoverArtMultiRelationshipDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['coverArt'] # List[str] | Include related resources. Available relationships: coverArt (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get coverArt relationship (\"to-many\").
        api_response = api_instance.albums_id_relationships_cover_art_get(id, country_code=country_code, include=include, page_cursor=page_cursor, share_code=share_code)
        print("The response of AlbumsApi->albums_id_relationships_cover_art_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_cover_art_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: coverArt | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**AlbumsCoverArtMultiRelationshipDataDocument**](AlbumsCoverArtMultiRelationshipDataDocument.md)

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

# **albums_id_relationships_cover_art_patch**
> MutationResponseDocument albums_id_relationships_cover_art_patch(id, idempotency_key=idempotency_key, share_code=share_code, albums_cover_art_relationship_update_operation_payload=albums_cover_art_relationship_update_operation_payload)

Update coverArt relationship (\"to-many\").

Replaces the uploaded cover artwork selection with one attachable artwork. Empty data clears the selection. Previously attached uploaded artwork is soft-deleted unless system-managed. Returns an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.albums_cover_art_relationship_update_operation_payload import AlbumsCoverArtRelationshipUpdateOperationPayload
from tidal.models.mutation_response_document import MutationResponseDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)
    albums_cover_art_relationship_update_operation_payload = tidal.AlbumsCoverArtRelationshipUpdateOperationPayload() # AlbumsCoverArtRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update coverArt relationship (\"to-many\").
        api_response = api_instance.albums_id_relationships_cover_art_patch(id, idempotency_key=idempotency_key, share_code=share_code, albums_cover_art_relationship_update_operation_payload=albums_cover_art_relationship_update_operation_payload)
        print("The response of AlbumsApi->albums_id_relationships_cover_art_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_cover_art_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 
 **albums_cover_art_relationship_update_operation_payload** | [**AlbumsCoverArtRelationshipUpdateOperationPayload**](AlbumsCoverArtRelationshipUpdateOperationPayload.md)|  | [optional] 

### Return type

[**MutationResponseDocument**](MutationResponseDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **albums_id_relationships_genres_get**
> AlbumsGenresMultiRelationshipDataDocument albums_id_relationships_genres_get(id, country_code=country_code, include=include, page_cursor=page_cursor, share_code=share_code)

Get genres relationship (\"to-many\").

Retrieves genres relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.albums_genres_multi_relationship_data_document import AlbumsGenresMultiRelationshipDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['genres'] # List[str] | Include related resources. Available relationships: genres (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get genres relationship (\"to-many\").
        api_response = api_instance.albums_id_relationships_genres_get(id, country_code=country_code, include=include, page_cursor=page_cursor, share_code=share_code)
        print("The response of AlbumsApi->albums_id_relationships_genres_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_genres_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: genres | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**AlbumsGenresMultiRelationshipDataDocument**](AlbumsGenresMultiRelationshipDataDocument.md)

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

# **albums_id_relationships_items_get**
> AlbumsItemsMultiRelationshipDataDocument albums_id_relationships_items_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)

Get items relationship (\"to-many\").

Retrieves items relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.albums_items_multi_relationship_data_document import AlbumsItemsMultiRelationshipDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['items'] # List[str] | Include related resources. Available relationships: items (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get items relationship (\"to-many\").
        api_response = api_instance.albums_id_relationships_items_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)
        print("The response of AlbumsApi->albums_id_relationships_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**AlbumsItemsMultiRelationshipDataDocument**](AlbumsItemsMultiRelationshipDataDocument.md)

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

# **albums_id_relationships_items_patch**
> MutationResponseDocument albums_id_relationships_items_patch(id, idempotency_key=idempotency_key, share_code=share_code, albums_items_relationship_update_operation_payload=albums_items_relationship_update_operation_payload)

Update items relationship (\"to-many\").

Incrementally updates one existing track's 1-based track number to meta.positionIndex. Does not replace the album's items or add or remove tracks. Empty data is rejected. A COLLABORATOR on the album may reorder. Returns an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.albums_items_relationship_update_operation_payload import AlbumsItemsRelationshipUpdateOperationPayload
from tidal.models.mutation_response_document import MutationResponseDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)
    albums_items_relationship_update_operation_payload = tidal.AlbumsItemsRelationshipUpdateOperationPayload() # AlbumsItemsRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update items relationship (\"to-many\").
        api_response = api_instance.albums_id_relationships_items_patch(id, idempotency_key=idempotency_key, share_code=share_code, albums_items_relationship_update_operation_payload=albums_items_relationship_update_operation_payload)
        print("The response of AlbumsApi->albums_id_relationships_items_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_items_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 
 **albums_items_relationship_update_operation_payload** | [**AlbumsItemsRelationshipUpdateOperationPayload**](AlbumsItemsRelationshipUpdateOperationPayload.md)|  | [optional] 

### Return type

[**MutationResponseDocument**](MutationResponseDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **albums_id_relationships_owners_get**
> AlbumsOwnersMultiRelationshipDataDocument albums_id_relationships_owners_get(id, include=include, page_cursor=page_cursor, share_code=share_code)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.albums_owners_multi_relationship_data_document import AlbumsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.albums_id_relationships_owners_get(id, include=include, page_cursor=page_cursor, share_code=share_code)
        print("The response of AlbumsApi->albums_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**AlbumsOwnersMultiRelationshipDataDocument**](AlbumsOwnersMultiRelationshipDataDocument.md)

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

# **albums_id_relationships_price_config_get**
> AlbumsPriceConfigSingleRelationshipDataDocument albums_id_relationships_price_config_get(id, country_code=country_code, include=include, share_code=share_code)

Get priceConfig relationship (\"to-one\").

Retrieves priceConfig relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.albums_price_config_single_relationship_data_document import AlbumsPriceConfigSingleRelationshipDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['priceConfig'] # List[str] | Include related resources. Available relationships: priceConfig (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get priceConfig relationship (\"to-one\").
        api_response = api_instance.albums_id_relationships_price_config_get(id, country_code=country_code, include=include, share_code=share_code)
        print("The response of AlbumsApi->albums_id_relationships_price_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_price_config_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: priceConfig | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**AlbumsPriceConfigSingleRelationshipDataDocument**](AlbumsPriceConfigSingleRelationshipDataDocument.md)

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

# **albums_id_relationships_providers_get**
> AlbumsProvidersMultiRelationshipDataDocument albums_id_relationships_providers_get(id, country_code=country_code, include=include, page_cursor=page_cursor, share_code=share_code)

Get providers relationship (\"to-many\").

Retrieves providers relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.albums_providers_multi_relationship_data_document import AlbumsProvidersMultiRelationshipDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['providers'] # List[str] | Include related resources. Available relationships: providers (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get providers relationship (\"to-many\").
        api_response = api_instance.albums_id_relationships_providers_get(id, country_code=country_code, include=include, page_cursor=page_cursor, share_code=share_code)
        print("The response of AlbumsApi->albums_id_relationships_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_providers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: providers | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**AlbumsProvidersMultiRelationshipDataDocument**](AlbumsProvidersMultiRelationshipDataDocument.md)

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

# **albums_id_relationships_replacement_get**
> AlbumsReplacementSingleRelationshipDataDocument albums_id_relationships_replacement_get(id, country_code=country_code, include=include, replace_media=replace_media, share_code=share_code)

Get replacement relationship (\"to-one\").

Retrieves replacement relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.albums_replacement_single_relationship_data_document import AlbumsReplacementSingleRelationshipDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['replacement'] # List[str] | Include related resources. Available relationships: replacement (optional)
    replace_media = 'replacement' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: replacement (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get replacement relationship (\"to-one\").
        api_response = api_instance.albums_id_relationships_replacement_get(id, country_code=country_code, include=include, replace_media=replace_media, share_code=share_code)
        print("The response of AlbumsApi->albums_id_relationships_replacement_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_replacement_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: replacement | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: replacement | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**AlbumsReplacementSingleRelationshipDataDocument**](AlbumsReplacementSingleRelationshipDataDocument.md)

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

# **albums_id_relationships_shares_get**
> AlbumsSharesMultiRelationshipDataDocument albums_id_relationships_shares_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)

Get shares relationship (\"to-many\").

The album's share links, active and expired, newest first.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.albums_shares_multi_relationship_data_document import AlbumsSharesMultiRelationshipDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    include = ['shares.sharedResources'] # List[str] | Include related resources. Available relationships: shares (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'shares.sharedResources' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: shares.sharedResources (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get shares relationship (\"to-many\").
        api_response = api_instance.albums_id_relationships_shares_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)
        print("The response of AlbumsApi->albums_id_relationships_shares_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_shares_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: shares | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: shares.sharedResources | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**AlbumsSharesMultiRelationshipDataDocument**](AlbumsSharesMultiRelationshipDataDocument.md)

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

# **albums_id_relationships_similar_albums_get**
> AlbumsSimilarAlbumsMultiRelationshipDataDocument albums_id_relationships_similar_albums_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)

Get similarAlbums relationship (\"to-many\").

Retrieves similarAlbums relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.albums_similar_albums_multi_relationship_data_document import AlbumsSimilarAlbumsMultiRelationshipDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['similarAlbums'] # List[str] | Include related resources. Available relationships: similarAlbums (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'similarAlbums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarAlbums (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get similarAlbums relationship (\"to-many\").
        api_response = api_instance.albums_id_relationships_similar_albums_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)
        print("The response of AlbumsApi->albums_id_relationships_similar_albums_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_similar_albums_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: similarAlbums | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: similarAlbums | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**AlbumsSimilarAlbumsMultiRelationshipDataDocument**](AlbumsSimilarAlbumsMultiRelationshipDataDocument.md)

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

# **albums_id_relationships_suggested_cover_arts_get**
> AlbumsSuggestedCoverArtsMultiRelationshipDataDocument albums_id_relationships_suggested_cover_arts_get(id, include=include, page_cursor=page_cursor, share_code=share_code)

Get suggestedCoverArts relationship (\"to-many\").

Retrieves suggestedCoverArts relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.albums_suggested_cover_arts_multi_relationship_data_document import AlbumsSuggestedCoverArtsMultiRelationshipDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    include = ['suggestedCoverArts'] # List[str] | Include related resources. Available relationships: suggestedCoverArts (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get suggestedCoverArts relationship (\"to-many\").
        api_response = api_instance.albums_id_relationships_suggested_cover_arts_get(id, include=include, page_cursor=page_cursor, share_code=share_code)
        print("The response of AlbumsApi->albums_id_relationships_suggested_cover_arts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_suggested_cover_arts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: suggestedCoverArts | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**AlbumsSuggestedCoverArtsMultiRelationshipDataDocument**](AlbumsSuggestedCoverArtsMultiRelationshipDataDocument.md)

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

# **albums_id_relationships_usage_rules_get**
> AlbumsUsageRulesSingleRelationshipDataDocument albums_id_relationships_usage_rules_get(id, country_code=country_code, include=include, share_code=share_code)

Get usageRules relationship (\"to-one\").

Retrieves usageRules relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.albums_usage_rules_single_relationship_data_document import AlbumsUsageRulesSingleRelationshipDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    id = '251380836' # str | Album id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['usageRules'] # List[str] | Include related resources. Available relationships: usageRules (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get usageRules relationship (\"to-one\").
        api_response = api_instance.albums_id_relationships_usage_rules_get(id, country_code=country_code, include=include, share_code=share_code)
        print("The response of AlbumsApi->albums_id_relationships_usage_rules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_id_relationships_usage_rules_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Album id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: usageRules | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**AlbumsUsageRulesSingleRelationshipDataDocument**](AlbumsUsageRulesSingleRelationshipDataDocument.md)

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

# **albums_post**
> AlbumsCreateSingleResourceDataDocument albums_post(idempotency_key=idempotency_key, albums_create_operation_payload=albums_create_operation_payload)

Create single album.

Creates an uploaded album. Album creation is not atomic with its artist assignment, so the caller must be OWNER of every listed artist; COLLABORATOR, or a role on an album, is not enough until the album exists.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.albums_create_operation_payload import AlbumsCreateOperationPayload
from tidal.models.albums_create_single_resource_data_document import AlbumsCreateSingleResourceDataDocument
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
    api_instance = tidal.AlbumsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    albums_create_operation_payload = tidal.AlbumsCreateOperationPayload() # AlbumsCreateOperationPayload |  (optional)

    try:
        # Create single album.
        api_response = api_instance.albums_post(idempotency_key=idempotency_key, albums_create_operation_payload=albums_create_operation_payload)
        print("The response of AlbumsApi->albums_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlbumsApi->albums_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **albums_create_operation_payload** | [**AlbumsCreateOperationPayload**](AlbumsCreateOperationPayload.md)|  | [optional] 

### Return type

[**AlbumsCreateSingleResourceDataDocument**](AlbumsCreateSingleResourceDataDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | Invalid request |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

