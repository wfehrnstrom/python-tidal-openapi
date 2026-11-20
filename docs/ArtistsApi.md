# tidal.ArtistsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artists_get**](ArtistsApi.md#artists_get) | **GET** /artists | Get multiple artists.
[**artists_id_get**](ArtistsApi.md#artists_id_get) | **GET** /artists/{id} | Get single artist.
[**artists_id_patch**](ArtistsApi.md#artists_id_patch) | **PATCH** /artists/{id} | Update single artist.
[**artists_id_relationships_albums_get**](ArtistsApi.md#artists_id_relationships_albums_get) | **GET** /artists/{id}/relationships/albums | Get albums relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_banner_art_get**](ArtistsApi.md#artists_id_relationships_banner_art_get) | **GET** /artists/{id}/relationships/bannerArt | Get bannerArt relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_banner_art_patch**](ArtistsApi.md#artists_id_relationships_banner_art_patch) | **PATCH** /artists/{id}/relationships/bannerArt | Update bannerArt relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_biography_get**](ArtistsApi.md#artists_id_relationships_biography_get) | **GET** /artists/{id}/relationships/biography | Get biography relationship (\&quot;to-one\&quot;).
[**artists_id_relationships_claim_status_get**](ArtistsApi.md#artists_id_relationships_claim_status_get) | **GET** /artists/{id}/relationships/claimStatus | Get claimStatus relationship (\&quot;to-one\&quot;).
[**artists_id_relationships_followers_get**](ArtistsApi.md#artists_id_relationships_followers_get) | **GET** /artists/{id}/relationships/followers | Get followers relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_following_delete**](ArtistsApi.md#artists_id_relationships_following_delete) | **DELETE** /artists/{id}/relationships/following | Delete from following relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_following_get**](ArtistsApi.md#artists_id_relationships_following_get) | **GET** /artists/{id}/relationships/following | Get following relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_following_post**](ArtistsApi.md#artists_id_relationships_following_post) | **POST** /artists/{id}/relationships/following | Add to following relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_logo_art_get**](ArtistsApi.md#artists_id_relationships_logo_art_get) | **GET** /artists/{id}/relationships/logoArt | Get logoArt relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_logo_art_patch**](ArtistsApi.md#artists_id_relationships_logo_art_patch) | **PATCH** /artists/{id}/relationships/logoArt | Update logoArt relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_owners_get**](ArtistsApi.md#artists_id_relationships_owners_get) | **GET** /artists/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_profile_art_get**](ArtistsApi.md#artists_id_relationships_profile_art_get) | **GET** /artists/{id}/relationships/profileArt | Get profileArt relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_profile_art_patch**](ArtistsApi.md#artists_id_relationships_profile_art_patch) | **PATCH** /artists/{id}/relationships/profileArt | Update profileArt relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_radio_get**](ArtistsApi.md#artists_id_relationships_radio_get) | **GET** /artists/{id}/relationships/radio | Get radio relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_roles_get**](ArtistsApi.md#artists_id_relationships_roles_get) | **GET** /artists/{id}/relationships/roles | Get roles relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_similar_artists_get**](ArtistsApi.md#artists_id_relationships_similar_artists_get) | **GET** /artists/{id}/relationships/similarArtists | Get similarArtists relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_track_providers_get**](ArtistsApi.md#artists_id_relationships_track_providers_get) | **GET** /artists/{id}/relationships/trackProviders | Get trackProviders relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_tracks_get**](ArtistsApi.md#artists_id_relationships_tracks_get) | **GET** /artists/{id}/relationships/tracks | Get tracks relationship (\&quot;to-many\&quot;).
[**artists_id_relationships_videos_get**](ArtistsApi.md#artists_id_relationships_videos_get) | **GET** /artists/{id}/relationships/videos | Get videos relationship (\&quot;to-many\&quot;).
[**artists_post**](ArtistsApi.md#artists_post) | **POST** /artists | Create single artist.


# **artists_get**
> ArtistsMultiResourceDataDocument artists_get(country_code=country_code, filter_handle=filter_handle, filter_id=filter_id, filter_owners_id=filter_owners_id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get multiple artists.

Retrieves multiple artists by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artists_multi_resource_data_document import ArtistsMultiResourceDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    filter_handle = ['filter_handle_example'] # List[str] | Artist handle (e.g. `jayz`) (optional)
    filter_id = ['filter_id_example'] # List[str] | List of artist IDs (e.g. `1566`) (optional)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`. (optional)
    include = ['albums'] # List[str] | Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums (optional)

    try:
        # Get multiple artists.
        api_response = api_instance.artists_get(country_code=country_code, filter_handle=filter_handle, filter_id=filter_id, filter_owners_id=filter_owners_id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of ArtistsApi->artists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **filter_handle** | [**List[str]**](str.md)| Artist handle (e.g. &#x60;jayz&#x60;) | [optional] 
 **filter_id** | [**List[str]**](str.md)| List of artist IDs (e.g. &#x60;1566&#x60;) | [optional] 
 **filter_owners_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums | [optional] 

### Return type

[**ArtistsMultiResourceDataDocument**](ArtistsMultiResourceDataDocument.md)

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

# **artists_id_get**
> ArtistsSingleResourceDataDocument artists_id_get(id, country_code=country_code, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single artist.

Retrieves single artist by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artists_single_resource_data_document import ArtistsSingleResourceDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['albums'] # List[str] | Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums (optional)

    try:
        # Get single artist.
        api_response = api_instance.artists_id_get(id, country_code=country_code, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of ArtistsApi->artists_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums | [optional] 

### Return type

[**ArtistsSingleResourceDataDocument**](ArtistsSingleResourceDataDocument.md)

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

# **artists_id_patch**
> MutationResponseDocument artists_id_patch(id, idempotency_key=idempotency_key, artists_update_operation_payload=artists_update_operation_payload)

Update single artist.

When both profile colours are available, they must have at least 3:1 contrast.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artists_update_operation_payload import ArtistsUpdateOperationPayload
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    artists_update_operation_payload = tidal.ArtistsUpdateOperationPayload() # ArtistsUpdateOperationPayload |  (optional)

    try:
        # Update single artist.
        api_response = api_instance.artists_id_patch(id, idempotency_key=idempotency_key, artists_update_operation_payload=artists_update_operation_payload)
        print("The response of ArtistsApi->artists_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **artists_update_operation_payload** | [**ArtistsUpdateOperationPayload**](ArtistsUpdateOperationPayload.md)|  | [optional] 

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

# **artists_id_relationships_albums_get**
> ArtistsAlbumsMultiRelationshipDataDocument artists_id_relationships_albums_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get albums relationship (\"to-many\").

Retrieves albums relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artists_albums_multi_relationship_data_document import ArtistsAlbumsMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['albums'] # List[str] | Include related resources. Available relationships: albums (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums (optional)

    try:
        # Get albums relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_albums_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of ArtistsApi->artists_id_relationships_albums_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_albums_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: albums | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums | [optional] 

### Return type

[**ArtistsAlbumsMultiRelationshipDataDocument**](ArtistsAlbumsMultiRelationshipDataDocument.md)

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

# **artists_id_relationships_banner_art_get**
> ArtistsBannerArtMultiRelationshipDataDocument artists_id_relationships_banner_art_get(id, country_code=country_code, include=include, page_cursor=page_cursor)

Get bannerArt relationship (\"to-many\").

Reads the selected header banner artwork.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artists_banner_art_multi_relationship_data_document import ArtistsBannerArtMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['bannerArt'] # List[str] | Include related resources. Available relationships: bannerArt (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get bannerArt relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_banner_art_get(id, country_code=country_code, include=include, page_cursor=page_cursor)
        print("The response of ArtistsApi->artists_id_relationships_banner_art_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_banner_art_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: bannerArt | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**ArtistsBannerArtMultiRelationshipDataDocument**](ArtistsBannerArtMultiRelationshipDataDocument.md)

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

# **artists_id_relationships_banner_art_patch**
> MutationResponseDocument artists_id_relationships_banner_art_patch(id, idempotency_key=idempotency_key, artists_banner_art_relationship_update_operation_payload=artists_banner_art_relationship_update_operation_payload)

Update bannerArt relationship (\"to-many\").

Selects one owned, attachable IMAGE artwork by ID, replacing the selection. Empty data clears the selection; null data and more than one entry are rejected. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artists_banner_art_relationship_update_operation_payload import ArtistsBannerArtRelationshipUpdateOperationPayload
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    artists_banner_art_relationship_update_operation_payload = tidal.ArtistsBannerArtRelationshipUpdateOperationPayload() # ArtistsBannerArtRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update bannerArt relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_banner_art_patch(id, idempotency_key=idempotency_key, artists_banner_art_relationship_update_operation_payload=artists_banner_art_relationship_update_operation_payload)
        print("The response of ArtistsApi->artists_id_relationships_banner_art_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_banner_art_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **artists_banner_art_relationship_update_operation_payload** | [**ArtistsBannerArtRelationshipUpdateOperationPayload**](ArtistsBannerArtRelationshipUpdateOperationPayload.md)|  | [optional] 

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

# **artists_id_relationships_biography_get**
> ArtistsBiographySingleRelationshipDataDocument artists_id_relationships_biography_get(id, country_code=country_code, include=include)

Get biography relationship (\"to-one\").

Retrieves biography relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artists_biography_single_relationship_data_document import ArtistsBiographySingleRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['biography'] # List[str] | Include related resources. Available relationships: biography (optional)

    try:
        # Get biography relationship (\"to-one\").
        api_response = api_instance.artists_id_relationships_biography_get(id, country_code=country_code, include=include)
        print("The response of ArtistsApi->artists_id_relationships_biography_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_biography_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: biography | [optional] 

### Return type

[**ArtistsBiographySingleRelationshipDataDocument**](ArtistsBiographySingleRelationshipDataDocument.md)

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

# **artists_id_relationships_claim_status_get**
> ArtistsClaimStatusSingleRelationshipDataDocument artists_id_relationships_claim_status_get(id, include=include)

Get claimStatus relationship (\"to-one\").

Retrieves claimStatus relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artists_claim_status_single_relationship_data_document import ArtistsClaimStatusSingleRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    include = ['claimStatus'] # List[str] | Include related resources. Available relationships: claimStatus (optional)

    try:
        # Get claimStatus relationship (\"to-one\").
        api_response = api_instance.artists_id_relationships_claim_status_get(id, include=include)
        print("The response of ArtistsApi->artists_id_relationships_claim_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_claim_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: claimStatus | [optional] 

### Return type

[**ArtistsClaimStatusSingleRelationshipDataDocument**](ArtistsClaimStatusSingleRelationshipDataDocument.md)

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

# **artists_id_relationships_followers_get**
> ArtistsFollowersMultiRelationshipDataDocument artists_id_relationships_followers_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, viewer_context=viewer_context)

Get followers relationship (\"to-many\").

Retrieves followers relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artists_followers_multi_relationship_data_document import ArtistsFollowersMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    include = ['followers.albums'] # List[str] | Include related resources. Available relationships: followers (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'followers.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: followers.albums (optional)
    viewer_context = 'viewer_context_example' # str |  (optional)

    try:
        # Get followers relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_followers_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, viewer_context=viewer_context)
        print("The response of ArtistsApi->artists_id_relationships_followers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_followers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: followers | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: followers.albums | [optional] 
 **viewer_context** | **str**|  | [optional] 

### Return type

[**ArtistsFollowersMultiRelationshipDataDocument**](ArtistsFollowersMultiRelationshipDataDocument.md)

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

# **artists_id_relationships_following_delete**
> MutationResponseDocument artists_id_relationships_following_delete(id, idempotency_key=idempotency_key, artists_following_relationship_remove_operation_payload=artists_following_relationship_remove_operation_payload)

Delete from following relationship (\"to-many\").

Deletes item(s) from following relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artists_following_relationship_remove_operation_payload import ArtistsFollowingRelationshipRemoveOperationPayload
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    artists_following_relationship_remove_operation_payload = tidal.ArtistsFollowingRelationshipRemoveOperationPayload() # ArtistsFollowingRelationshipRemoveOperationPayload |  (optional)

    try:
        # Delete from following relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_following_delete(id, idempotency_key=idempotency_key, artists_following_relationship_remove_operation_payload=artists_following_relationship_remove_operation_payload)
        print("The response of ArtistsApi->artists_id_relationships_following_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_following_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **artists_following_relationship_remove_operation_payload** | [**ArtistsFollowingRelationshipRemoveOperationPayload**](ArtistsFollowingRelationshipRemoveOperationPayload.md)|  | [optional] 

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

# **artists_id_relationships_following_get**
> ArtistsFollowingMultiRelationshipDataDocument artists_id_relationships_following_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, viewer_context=viewer_context)

Get following relationship (\"to-many\").

Retrieves following relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artists_following_multi_relationship_data_document import ArtistsFollowingMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    include = ['following.albums'] # List[str] | Include related resources. Available relationships: following (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'following.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: following.albums (optional)
    viewer_context = 'viewer_context_example' # str |  (optional)

    try:
        # Get following relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_following_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, viewer_context=viewer_context)
        print("The response of ArtistsApi->artists_id_relationships_following_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_following_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: following | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: following.albums | [optional] 
 **viewer_context** | **str**|  | [optional] 

### Return type

[**ArtistsFollowingMultiRelationshipDataDocument**](ArtistsFollowingMultiRelationshipDataDocument.md)

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

# **artists_id_relationships_following_post**
> MutationResponseDocument artists_id_relationships_following_post(id, idempotency_key=idempotency_key, artists_following_relationship_add_operation_payload=artists_following_relationship_add_operation_payload)

Add to following relationship (\"to-many\").

Adds item(s) to following relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artists_following_relationship_add_operation_payload import ArtistsFollowingRelationshipAddOperationPayload
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    artists_following_relationship_add_operation_payload = tidal.ArtistsFollowingRelationshipAddOperationPayload() # ArtistsFollowingRelationshipAddOperationPayload |  (optional)

    try:
        # Add to following relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_following_post(id, idempotency_key=idempotency_key, artists_following_relationship_add_operation_payload=artists_following_relationship_add_operation_payload)
        print("The response of ArtistsApi->artists_id_relationships_following_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_following_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **artists_following_relationship_add_operation_payload** | [**ArtistsFollowingRelationshipAddOperationPayload**](ArtistsFollowingRelationshipAddOperationPayload.md)|  | [optional] 

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

# **artists_id_relationships_logo_art_get**
> ArtistsLogoArtMultiRelationshipDataDocument artists_id_relationships_logo_art_get(id, country_code=country_code, include=include, page_cursor=page_cursor)

Get logoArt relationship (\"to-many\").

Reads the selected logo artwork.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artists_logo_art_multi_relationship_data_document import ArtistsLogoArtMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['logoArt'] # List[str] | Include related resources. Available relationships: logoArt (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get logoArt relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_logo_art_get(id, country_code=country_code, include=include, page_cursor=page_cursor)
        print("The response of ArtistsApi->artists_id_relationships_logo_art_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_logo_art_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: logoArt | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**ArtistsLogoArtMultiRelationshipDataDocument**](ArtistsLogoArtMultiRelationshipDataDocument.md)

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

# **artists_id_relationships_logo_art_patch**
> MutationResponseDocument artists_id_relationships_logo_art_patch(id, idempotency_key=idempotency_key, artists_logo_art_relationship_update_operation_payload=artists_logo_art_relationship_update_operation_payload)

Update logoArt relationship (\"to-many\").

Selects one owned, attachable IMAGE artwork by ID, replacing the selection. Empty data clears the selection; null data and more than one entry are rejected. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artists_logo_art_relationship_update_operation_payload import ArtistsLogoArtRelationshipUpdateOperationPayload
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    artists_logo_art_relationship_update_operation_payload = tidal.ArtistsLogoArtRelationshipUpdateOperationPayload() # ArtistsLogoArtRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update logoArt relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_logo_art_patch(id, idempotency_key=idempotency_key, artists_logo_art_relationship_update_operation_payload=artists_logo_art_relationship_update_operation_payload)
        print("The response of ArtistsApi->artists_id_relationships_logo_art_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_logo_art_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **artists_logo_art_relationship_update_operation_payload** | [**ArtistsLogoArtRelationshipUpdateOperationPayload**](ArtistsLogoArtRelationshipUpdateOperationPayload.md)|  | [optional] 

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

# **artists_id_relationships_owners_get**
> ArtistsOwnersMultiRelationshipDataDocument artists_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artists_owners_multi_relationship_data_document import ArtistsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of ArtistsApi->artists_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**ArtistsOwnersMultiRelationshipDataDocument**](ArtistsOwnersMultiRelationshipDataDocument.md)

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

# **artists_id_relationships_profile_art_get**
> ArtistsProfileArtMultiRelationshipDataDocument artists_id_relationships_profile_art_get(id, country_code=country_code, include=include, page_cursor=page_cursor)

Get profileArt relationship (\"to-many\").

Reads the artist's avatar artwork.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artists_profile_art_multi_relationship_data_document import ArtistsProfileArtMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['profileArt'] # List[str] | Include related resources. Available relationships: profileArt (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get profileArt relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_profile_art_get(id, country_code=country_code, include=include, page_cursor=page_cursor)
        print("The response of ArtistsApi->artists_id_relationships_profile_art_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_profile_art_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: profileArt | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**ArtistsProfileArtMultiRelationshipDataDocument**](ArtistsProfileArtMultiRelationshipDataDocument.md)

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

# **artists_id_relationships_profile_art_patch**
> MutationResponseDocument artists_id_relationships_profile_art_patch(id, idempotency_key=idempotency_key, artists_profile_art_relationship_update_operation_payload=artists_profile_art_relationship_update_operation_payload)

Update profileArt relationship (\"to-many\").

Replaces the artist's uploaded avatar selection with one owned, attachable artwork. Empty data clears the uploaded selection; legacy pictures or album fallback artwork may still appear in profileArt. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artists_profile_art_relationship_update_operation_payload import ArtistsProfileArtRelationshipUpdateOperationPayload
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    artists_profile_art_relationship_update_operation_payload = tidal.ArtistsProfileArtRelationshipUpdateOperationPayload() # ArtistsProfileArtRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update profileArt relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_profile_art_patch(id, idempotency_key=idempotency_key, artists_profile_art_relationship_update_operation_payload=artists_profile_art_relationship_update_operation_payload)
        print("The response of ArtistsApi->artists_id_relationships_profile_art_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_profile_art_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **artists_profile_art_relationship_update_operation_payload** | [**ArtistsProfileArtRelationshipUpdateOperationPayload**](ArtistsProfileArtRelationshipUpdateOperationPayload.md)|  | [optional] 

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

# **artists_id_relationships_radio_get**
> ArtistsRadioMultiRelationshipDataDocument artists_id_relationships_radio_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get radio relationship (\"to-many\").

Retrieves radio relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artists_radio_multi_relationship_data_document import ArtistsRadioMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['radio.items'] # List[str] | Include related resources. Available relationships: radio (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'radio.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: radio.items (optional)

    try:
        # Get radio relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_radio_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of ArtistsApi->artists_id_relationships_radio_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_radio_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: radio | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: radio.items | [optional] 

### Return type

[**ArtistsRadioMultiRelationshipDataDocument**](ArtistsRadioMultiRelationshipDataDocument.md)

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

# **artists_id_relationships_roles_get**
> ArtistsRolesMultiRelationshipDataDocument artists_id_relationships_roles_get(id, include=include, page_cursor=page_cursor)

Get roles relationship (\"to-many\").

Retrieves roles relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artists_roles_multi_relationship_data_document import ArtistsRolesMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    include = ['roles'] # List[str] | Include related resources. Available relationships: roles (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get roles relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_roles_get(id, include=include, page_cursor=page_cursor)
        print("The response of ArtistsApi->artists_id_relationships_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_roles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: roles | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**ArtistsRolesMultiRelationshipDataDocument**](ArtistsRolesMultiRelationshipDataDocument.md)

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

# **artists_id_relationships_similar_artists_get**
> ArtistsSimilarArtistsMultiRelationshipDataDocument artists_id_relationships_similar_artists_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get similarArtists relationship (\"to-many\").

Retrieves similarArtists relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artists_similar_artists_multi_relationship_data_document import ArtistsSimilarArtistsMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['similarArtists.albums'] # List[str] | Include related resources. Available relationships: similarArtists (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'similarArtists.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarArtists.albums (optional)

    try:
        # Get similarArtists relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_similar_artists_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of ArtistsApi->artists_id_relationships_similar_artists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_similar_artists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: similarArtists | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: similarArtists.albums | [optional] 

### Return type

[**ArtistsSimilarArtistsMultiRelationshipDataDocument**](ArtistsSimilarArtistsMultiRelationshipDataDocument.md)

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

# **artists_id_relationships_track_providers_get**
> ArtistsTrackProvidersMultiRelationshipDataDocument artists_id_relationships_track_providers_get(id, include=include, page_cursor=page_cursor)

Get trackProviders relationship (\"to-many\").

Retrieves trackProviders relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artists_track_providers_multi_relationship_data_document import ArtistsTrackProvidersMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    include = ['trackProviders'] # List[str] | Include related resources. Available relationships: trackProviders (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get trackProviders relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_track_providers_get(id, include=include, page_cursor=page_cursor)
        print("The response of ArtistsApi->artists_id_relationships_track_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_track_providers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: trackProviders | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**ArtistsTrackProvidersMultiRelationshipDataDocument**](ArtistsTrackProvidersMultiRelationshipDataDocument.md)

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

# **artists_id_relationships_tracks_get**
> ArtistsTracksMultiRelationshipDataDocument artists_id_relationships_tracks_get(collapse_by, id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get tracks relationship (\"to-many\").

Retrieves tracks relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artists_tracks_multi_relationship_data_document import ArtistsTracksMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    collapse_by = 'FINGERPRINT' # str | Collapse by options for getting artist tracks. Available options: FINGERPRINT, ID. FINGERPRINT option might collapse similar tracks based entry fingerprints while collapsing by ID always returns all available items.
    id = '1566' # str | Artist id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['tracks'] # List[str] | Include related resources. Available relationships: tracks (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'tracks' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks (optional)

    try:
        # Get tracks relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_tracks_get(collapse_by, id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of ArtistsApi->artists_id_relationships_tracks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_tracks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collapse_by** | **str**| Collapse by options for getting artist tracks. Available options: FINGERPRINT, ID. FINGERPRINT option might collapse similar tracks based entry fingerprints while collapsing by ID always returns all available items. | 
 **id** | **str**| Artist id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: tracks | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: tracks | [optional] 

### Return type

[**ArtistsTracksMultiRelationshipDataDocument**](ArtistsTracksMultiRelationshipDataDocument.md)

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

# **artists_id_relationships_videos_get**
> ArtistsVideosMultiRelationshipDataDocument artists_id_relationships_videos_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get videos relationship (\"to-many\").

Retrieves videos relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.artists_videos_multi_relationship_data_document import ArtistsVideosMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistsApi(api_client)
    id = '1566' # str | Artist id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['videos'] # List[str] | Include related resources. Available relationships: videos (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'videos' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos (optional)

    try:
        # Get videos relationship (\"to-many\").
        api_response = api_instance.artists_id_relationships_videos_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of ArtistsApi->artists_id_relationships_videos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_id_relationships_videos_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: videos | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: videos | [optional] 

### Return type

[**ArtistsVideosMultiRelationshipDataDocument**](ArtistsVideosMultiRelationshipDataDocument.md)

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

# **artists_post**
> MutationResponseDocument artists_post(idempotency_key=idempotency_key, artists_create_operation_payload=artists_create_operation_payload)

Create single artist.

Creates a new artist.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artists_create_operation_payload import ArtistsCreateOperationPayload
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
    api_instance = tidal.ArtistsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    artists_create_operation_payload = tidal.ArtistsCreateOperationPayload() # ArtistsCreateOperationPayload |  (optional)

    try:
        # Create single artist.
        api_response = api_instance.artists_post(idempotency_key=idempotency_key, artists_create_operation_payload=artists_create_operation_payload)
        print("The response of ArtistsApi->artists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->artists_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **artists_create_operation_payload** | [**ArtistsCreateOperationPayload**](ArtistsCreateOperationPayload.md)|  | [optional] 

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
**200** | Successful dry run |  -  |
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

