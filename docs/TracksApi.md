# tidal.TracksApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tracks_get**](TracksApi.md#tracks_get) | **GET** /tracks | Get multiple tracks.
[**tracks_id_delete**](TracksApi.md#tracks_id_delete) | **DELETE** /tracks/{id} | Delete single track.
[**tracks_id_get**](TracksApi.md#tracks_id_get) | **GET** /tracks/{id} | Get single track.
[**tracks_id_patch**](TracksApi.md#tracks_id_patch) | **PATCH** /tracks/{id} | Update single track.
[**tracks_id_relationships_albums_get**](TracksApi.md#tracks_id_relationships_albums_get) | **GET** /tracks/{id}/relationships/albums | Get albums relationship (\&quot;to-many\&quot;).
[**tracks_id_relationships_albums_patch**](TracksApi.md#tracks_id_relationships_albums_patch) | **PATCH** /tracks/{id}/relationships/albums | Update albums relationship (\&quot;to-many\&quot;).
[**tracks_id_relationships_artists_get**](TracksApi.md#tracks_id_relationships_artists_get) | **GET** /tracks/{id}/relationships/artists | Get artists relationship (\&quot;to-many\&quot;).
[**tracks_id_relationships_artists_patch**](TracksApi.md#tracks_id_relationships_artists_patch) | **PATCH** /tracks/{id}/relationships/artists | Update artists relationship (\&quot;to-many\&quot;).
[**tracks_id_relationships_credits_get**](TracksApi.md#tracks_id_relationships_credits_get) | **GET** /tracks/{id}/relationships/credits | Get credits relationship (\&quot;to-many\&quot;).
[**tracks_id_relationships_download_get**](TracksApi.md#tracks_id_relationships_download_get) | **GET** /tracks/{id}/relationships/download | Get download relationship (\&quot;to-one\&quot;).
[**tracks_id_relationships_genres_get**](TracksApi.md#tracks_id_relationships_genres_get) | **GET** /tracks/{id}/relationships/genres | Get genres relationship (\&quot;to-many\&quot;).
[**tracks_id_relationships_lyrics_get**](TracksApi.md#tracks_id_relationships_lyrics_get) | **GET** /tracks/{id}/relationships/lyrics | Get lyrics relationship (\&quot;to-many\&quot;).
[**tracks_id_relationships_metadata_status_get**](TracksApi.md#tracks_id_relationships_metadata_status_get) | **GET** /tracks/{id}/relationships/metadataStatus | Get metadataStatus relationship (\&quot;to-one\&quot;).
[**tracks_id_relationships_owners_get**](TracksApi.md#tracks_id_relationships_owners_get) | **GET** /tracks/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**tracks_id_relationships_price_config_get**](TracksApi.md#tracks_id_relationships_price_config_get) | **GET** /tracks/{id}/relationships/priceConfig | Get priceConfig relationship (\&quot;to-one\&quot;).
[**tracks_id_relationships_providers_get**](TracksApi.md#tracks_id_relationships_providers_get) | **GET** /tracks/{id}/relationships/providers | Get providers relationship (\&quot;to-many\&quot;).
[**tracks_id_relationships_radio_get**](TracksApi.md#tracks_id_relationships_radio_get) | **GET** /tracks/{id}/relationships/radio | Get radio relationship (\&quot;to-many\&quot;).
[**tracks_id_relationships_replacement_get**](TracksApi.md#tracks_id_relationships_replacement_get) | **GET** /tracks/{id}/relationships/replacement | Get replacement relationship (\&quot;to-one\&quot;).
[**tracks_id_relationships_shares_get**](TracksApi.md#tracks_id_relationships_shares_get) | **GET** /tracks/{id}/relationships/shares | Get shares relationship (\&quot;to-many\&quot;).
[**tracks_id_relationships_similar_tracks_get**](TracksApi.md#tracks_id_relationships_similar_tracks_get) | **GET** /tracks/{id}/relationships/similarTracks | Get similarTracks relationship (\&quot;to-many\&quot;).
[**tracks_id_relationships_source_file_get**](TracksApi.md#tracks_id_relationships_source_file_get) | **GET** /tracks/{id}/relationships/sourceFile | Get sourceFile relationship (\&quot;to-one\&quot;).
[**tracks_id_relationships_suggested_tracks_get**](TracksApi.md#tracks_id_relationships_suggested_tracks_get) | **GET** /tracks/{id}/relationships/suggestedTracks | Get suggestedTracks relationship (\&quot;to-many\&quot;).
[**tracks_id_relationships_track_statistics_get**](TracksApi.md#tracks_id_relationships_track_statistics_get) | **GET** /tracks/{id}/relationships/trackStatistics | Get trackStatistics relationship (\&quot;to-one\&quot;).
[**tracks_id_relationships_usage_rules_get**](TracksApi.md#tracks_id_relationships_usage_rules_get) | **GET** /tracks/{id}/relationships/usageRules | Get usageRules relationship (\&quot;to-one\&quot;).
[**tracks_post**](TracksApi.md#tracks_post) | **POST** /tracks | Create single track.


# **tracks_get**
> TracksMultiResourceDataDocument tracks_get(country_code=country_code, filter_id=filter_id, filter_isrc=filter_isrc, filter_owners_id=filter_owners_id, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code, sort=sort)

Get multiple tracks.

Retrieves multiple tracks by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_multi_resource_data_document import TracksMultiResourceDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    filter_id = ['filter_id_example'] # List[str] | List of track IDs (e.g. `75413016`) (optional)
    filter_isrc = ['filter_isrc_example'] # List[str] | List of ISRCs. When a single ISRC is provided, pagination is supported and multiple tracks may be returned. When multiple ISRCs are provided, one track per ISRC is returned without pagination. (e.g. `QMJMT1701237`) (optional)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`. (optional)
    include = ['albums'] # List[str] | Include related resources. Available relationships: albums, artists, credits, download, genres, lyrics, metadataStatus, owners, priceConfig, providers, radio, replacement, shares, similarTracks, sourceFile, suggestedTracks, trackStatistics, usageRules (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)
    sort = ['sort_example'] # List[str] | Values prefixed with \"-\" are sorted descending; values without it are sorted ascending. (optional)

    try:
        # Get multiple tracks.
        api_response = api_instance.tracks_get(country_code=country_code, filter_id=filter_id, filter_isrc=filter_isrc, filter_owners_id=filter_owners_id, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code, sort=sort)
        print("The response of TracksApi->tracks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **filter_id** | [**List[str]**](str.md)| List of track IDs (e.g. &#x60;75413016&#x60;) | [optional] 
 **filter_isrc** | [**List[str]**](str.md)| List of ISRCs. When a single ISRC is provided, pagination is supported and multiple tracks may be returned. When multiple ISRCs are provided, one track per ISRC is returned without pagination. (e.g. &#x60;QMJMT1701237&#x60;) | [optional] 
 **filter_owners_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: albums, artists, credits, download, genres, lyrics, metadataStatus, owners, priceConfig, providers, radio, replacement, shares, similarTracks, sourceFile, suggestedTracks, trackStatistics, usageRules | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 
 **sort** | [**List[str]**](str.md)| Values prefixed with \&quot;-\&quot; are sorted descending; values without it are sorted ascending. | [optional] 

### Return type

[**TracksMultiResourceDataDocument**](TracksMultiResourceDataDocument.md)

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

# **tracks_id_delete**
> MutationResponseDocument tracks_id_delete(id, idempotency_key=idempotency_key, share_code=share_code)

Delete single track.

Deletes existing track.

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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Delete single track.
        api_response = api_instance.tracks_id_delete(id, idempotency_key=idempotency_key, share_code=share_code)
        print("The response of TracksApi->tracks_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
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

# **tracks_id_get**
> TracksSingleResourceDataDocument tracks_id_get(id, country_code=country_code, include=include, include_linkage=include_linkage, replace_media=replace_media, share_code=share_code)

Get single track.

Retrieves single track by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_single_resource_data_document import TracksSingleResourceDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['albums'] # List[str] | Include related resources. Available relationships: albums, artists, credits, download, genres, lyrics, metadataStatus, owners, priceConfig, providers, radio, replacement, shares, similarTracks, sourceFile, suggestedTracks, trackStatistics, usageRules (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get single track.
        api_response = api_instance.tracks_id_get(id, country_code=country_code, include=include, include_linkage=include_linkage, replace_media=replace_media, share_code=share_code)
        print("The response of TracksApi->tracks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: albums, artists, credits, download, genres, lyrics, metadataStatus, owners, priceConfig, providers, radio, replacement, shares, similarTracks, sourceFile, suggestedTracks, trackStatistics, usageRules | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksSingleResourceDataDocument**](TracksSingleResourceDataDocument.md)

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

# **tracks_id_patch**
> MutationResponseDocument tracks_id_patch(id, idempotency_key=idempotency_key, share_code=share_code, tracks_update_operation_payload=tracks_update_operation_payload)

Update single track.

Updates existing track. A COLLABORATOR on the track may update it; changing accessType or isrc needs OWNER.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.tracks_update_operation_payload import TracksUpdateOperationPayload
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)
    tracks_update_operation_payload = tidal.TracksUpdateOperationPayload() # TracksUpdateOperationPayload |  (optional)

    try:
        # Update single track.
        api_response = api_instance.tracks_id_patch(id, idempotency_key=idempotency_key, share_code=share_code, tracks_update_operation_payload=tracks_update_operation_payload)
        print("The response of TracksApi->tracks_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 
 **tracks_update_operation_payload** | [**TracksUpdateOperationPayload**](TracksUpdateOperationPayload.md)|  | [optional] 

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

# **tracks_id_relationships_albums_get**
> TracksAlbumsMultiRelationshipDataDocument tracks_id_relationships_albums_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)

Get albums relationship (\"to-many\").

Retrieves albums relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_albums_multi_relationship_data_document import TracksAlbumsMultiRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['albums'] # List[str] | Include related resources. Available relationships: albums (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get albums relationship (\"to-many\").
        api_response = api_instance.tracks_id_relationships_albums_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_albums_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_albums_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: albums | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: albums | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksAlbumsMultiRelationshipDataDocument**](TracksAlbumsMultiRelationshipDataDocument.md)

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

# **tracks_id_relationships_albums_patch**
> MutationResponseDocument tracks_id_relationships_albums_patch(id, idempotency_key=idempotency_key, share_code=share_code, tracks_albums_relationship_update_operation_payload=tracks_albums_relationship_update_operation_payload)

Update albums relationship (\"to-many\").

Moves the uploaded track to the supplied album, replacing its previous album association. Exactly one album is required; empty data cannot clear it. The caller needs COLLABORATOR on the track and the album. The album must be in the same user's folders as the track (409 otherwise). Returns an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.tracks_albums_relationship_update_operation_payload import TracksAlbumsRelationshipUpdateOperationPayload
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)
    tracks_albums_relationship_update_operation_payload = tidal.TracksAlbumsRelationshipUpdateOperationPayload() # TracksAlbumsRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update albums relationship (\"to-many\").
        api_response = api_instance.tracks_id_relationships_albums_patch(id, idempotency_key=idempotency_key, share_code=share_code, tracks_albums_relationship_update_operation_payload=tracks_albums_relationship_update_operation_payload)
        print("The response of TracksApi->tracks_id_relationships_albums_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_albums_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 
 **tracks_albums_relationship_update_operation_payload** | [**TracksAlbumsRelationshipUpdateOperationPayload**](TracksAlbumsRelationshipUpdateOperationPayload.md)|  | [optional] 

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

# **tracks_id_relationships_artists_get**
> TracksArtistsMultiRelationshipDataDocument tracks_id_relationships_artists_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)

Get artists relationship (\"to-many\").

Retrieves artists relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_artists_multi_relationship_data_document import TracksArtistsMultiRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['artists.albums'] # List[str] | Include related resources. Available relationships: artists (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'artists.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get artists relationship (\"to-many\").
        api_response = api_instance.tracks_id_relationships_artists_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_artists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_artists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artists | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksArtistsMultiRelationshipDataDocument**](TracksArtistsMultiRelationshipDataDocument.md)

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

# **tracks_id_relationships_artists_patch**
> MutationResponseDocument tracks_id_relationships_artists_patch(id, idempotency_key=idempotency_key, share_code=share_code, tracks_artists_relationship_update_operation_payload=tracks_artists_relationship_update_operation_payload)

Update artists relationship (\"to-many\").

Sets the track's artists, replacing the current list. Artists are listed in the order given. Provide 1 to 10 distinct artists. You can add your own artist profile and the profiles of users who have owner or collaborator access to the track or its album. Owners and collaborators can change its artists. Returns an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.tracks_artists_relationship_update_operation_payload import TracksArtistsRelationshipUpdateOperationPayload
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)
    tracks_artists_relationship_update_operation_payload = tidal.TracksArtistsRelationshipUpdateOperationPayload() # TracksArtistsRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update artists relationship (\"to-many\").
        api_response = api_instance.tracks_id_relationships_artists_patch(id, idempotency_key=idempotency_key, share_code=share_code, tracks_artists_relationship_update_operation_payload=tracks_artists_relationship_update_operation_payload)
        print("The response of TracksApi->tracks_id_relationships_artists_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_artists_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 
 **tracks_artists_relationship_update_operation_payload** | [**TracksArtistsRelationshipUpdateOperationPayload**](TracksArtistsRelationshipUpdateOperationPayload.md)|  | [optional] 

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

# **tracks_id_relationships_credits_get**
> TracksCreditsMultiRelationshipDataDocument tracks_id_relationships_credits_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)

Get credits relationship (\"to-many\").

Retrieves credits relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_credits_multi_relationship_data_document import TracksCreditsMultiRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    include = ['credits.artist.albums'] # List[str] | Include related resources. Available relationships: credits (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'credits.artist.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: credits.artist.albums (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get credits relationship (\"to-many\").
        api_response = api_instance.tracks_id_relationships_credits_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_credits_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_credits_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: credits | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: credits.artist.albums | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksCreditsMultiRelationshipDataDocument**](TracksCreditsMultiRelationshipDataDocument.md)

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

# **tracks_id_relationships_download_get**
> TracksDownloadSingleRelationshipDataDocument tracks_id_relationships_download_get(id, include=include, share_code=share_code)

Get download relationship (\"to-one\").

Retrieves download relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.tracks_download_single_relationship_data_document import TracksDownloadSingleRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    include = ['download'] # List[str] | Include related resources. Available relationships: download (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get download relationship (\"to-one\").
        api_response = api_instance.tracks_id_relationships_download_get(id, include=include, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: download | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksDownloadSingleRelationshipDataDocument**](TracksDownloadSingleRelationshipDataDocument.md)

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

# **tracks_id_relationships_genres_get**
> TracksGenresMultiRelationshipDataDocument tracks_id_relationships_genres_get(id, country_code=country_code, include=include, page_cursor=page_cursor, share_code=share_code)

Get genres relationship (\"to-many\").

Retrieves genres relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_genres_multi_relationship_data_document import TracksGenresMultiRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['genres'] # List[str] | Include related resources. Available relationships: genres (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get genres relationship (\"to-many\").
        api_response = api_instance.tracks_id_relationships_genres_get(id, country_code=country_code, include=include, page_cursor=page_cursor, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_genres_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_genres_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: genres | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksGenresMultiRelationshipDataDocument**](TracksGenresMultiRelationshipDataDocument.md)

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

# **tracks_id_relationships_lyrics_get**
> TracksLyricsMultiRelationshipDataDocument tracks_id_relationships_lyrics_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)

Get lyrics relationship (\"to-many\").

Retrieves lyrics relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_lyrics_multi_relationship_data_document import TracksLyricsMultiRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    include = ['lyrics.track'] # List[str] | Include related resources. Available relationships: lyrics (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'lyrics.track' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: lyrics.track (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get lyrics relationship (\"to-many\").
        api_response = api_instance.tracks_id_relationships_lyrics_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_lyrics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_lyrics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: lyrics | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: lyrics.track | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksLyricsMultiRelationshipDataDocument**](TracksLyricsMultiRelationshipDataDocument.md)

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

# **tracks_id_relationships_metadata_status_get**
> TracksMetadataStatusSingleRelationshipDataDocument tracks_id_relationships_metadata_status_get(id, include=include, share_code=share_code)

Get metadataStatus relationship (\"to-one\").

Retrieves metadataStatus relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.tracks_metadata_status_single_relationship_data_document import TracksMetadataStatusSingleRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    include = ['metadataStatus'] # List[str] | Include related resources. Available relationships: metadataStatus (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get metadataStatus relationship (\"to-one\").
        api_response = api_instance.tracks_id_relationships_metadata_status_get(id, include=include, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_metadata_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_metadata_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: metadataStatus | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksMetadataStatusSingleRelationshipDataDocument**](TracksMetadataStatusSingleRelationshipDataDocument.md)

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

# **tracks_id_relationships_owners_get**
> TracksOwnersMultiRelationshipDataDocument tracks_id_relationships_owners_get(id, include=include, page_cursor=page_cursor, share_code=share_code)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_owners_multi_relationship_data_document import TracksOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.tracks_id_relationships_owners_get(id, include=include, page_cursor=page_cursor, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksOwnersMultiRelationshipDataDocument**](TracksOwnersMultiRelationshipDataDocument.md)

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

# **tracks_id_relationships_price_config_get**
> TracksPriceConfigSingleRelationshipDataDocument tracks_id_relationships_price_config_get(id, country_code=country_code, include=include, share_code=share_code)

Get priceConfig relationship (\"to-one\").

Retrieves priceConfig relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_price_config_single_relationship_data_document import TracksPriceConfigSingleRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['priceConfig'] # List[str] | Include related resources. Available relationships: priceConfig (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get priceConfig relationship (\"to-one\").
        api_response = api_instance.tracks_id_relationships_price_config_get(id, country_code=country_code, include=include, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_price_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_price_config_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: priceConfig | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksPriceConfigSingleRelationshipDataDocument**](TracksPriceConfigSingleRelationshipDataDocument.md)

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

# **tracks_id_relationships_providers_get**
> TracksProvidersMultiRelationshipDataDocument tracks_id_relationships_providers_get(id, country_code=country_code, include=include, page_cursor=page_cursor, share_code=share_code)

Get providers relationship (\"to-many\").

Retrieves providers relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_providers_multi_relationship_data_document import TracksProvidersMultiRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['providers'] # List[str] | Include related resources. Available relationships: providers (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get providers relationship (\"to-many\").
        api_response = api_instance.tracks_id_relationships_providers_get(id, country_code=country_code, include=include, page_cursor=page_cursor, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_providers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: providers | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksProvidersMultiRelationshipDataDocument**](TracksProvidersMultiRelationshipDataDocument.md)

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

# **tracks_id_relationships_radio_get**
> TracksRadioMultiRelationshipDataDocument tracks_id_relationships_radio_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)

Get radio relationship (\"to-many\").

Retrieves radio relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_radio_multi_relationship_data_document import TracksRadioMultiRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    include = ['radio.items'] # List[str] | Include related resources. Available relationships: radio (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'radio.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: radio.items (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get radio relationship (\"to-many\").
        api_response = api_instance.tracks_id_relationships_radio_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_radio_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_radio_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: radio | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: radio.items | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksRadioMultiRelationshipDataDocument**](TracksRadioMultiRelationshipDataDocument.md)

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

# **tracks_id_relationships_replacement_get**
> TracksReplacementSingleRelationshipDataDocument tracks_id_relationships_replacement_get(id, country_code=country_code, include=include, replace_media=replace_media, share_code=share_code)

Get replacement relationship (\"to-one\").

Retrieves replacement relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_replacement_single_relationship_data_document import TracksReplacementSingleRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['replacement'] # List[str] | Include related resources. Available relationships: replacement (optional)
    replace_media = 'replacement' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: replacement (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get replacement relationship (\"to-one\").
        api_response = api_instance.tracks_id_relationships_replacement_get(id, country_code=country_code, include=include, replace_media=replace_media, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_replacement_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_replacement_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: replacement | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: replacement | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksReplacementSingleRelationshipDataDocument**](TracksReplacementSingleRelationshipDataDocument.md)

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

# **tracks_id_relationships_shares_get**
> TracksSharesMultiRelationshipDataDocument tracks_id_relationships_shares_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)

Get shares relationship (\"to-many\").

The track's share links, active and expired, newest first.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.tracks_shares_multi_relationship_data_document import TracksSharesMultiRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    include = ['shares.sharedResources'] # List[str] | Include related resources. Available relationships: shares (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'shares.sharedResources' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: shares.sharedResources (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get shares relationship (\"to-many\").
        api_response = api_instance.tracks_id_relationships_shares_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_shares_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_shares_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: shares | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: shares.sharedResources | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksSharesMultiRelationshipDataDocument**](TracksSharesMultiRelationshipDataDocument.md)

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

# **tracks_id_relationships_similar_tracks_get**
> TracksSimilarTracksMultiRelationshipDataDocument tracks_id_relationships_similar_tracks_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)

Get similarTracks relationship (\"to-many\").

Retrieves similarTracks relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_similar_tracks_multi_relationship_data_document import TracksSimilarTracksMultiRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['similarTracks'] # List[str] | Include related resources. Available relationships: similarTracks (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'similarTracks' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarTracks (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get similarTracks relationship (\"to-many\").
        api_response = api_instance.tracks_id_relationships_similar_tracks_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_similar_tracks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_similar_tracks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: similarTracks | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: similarTracks | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksSimilarTracksMultiRelationshipDataDocument**](TracksSimilarTracksMultiRelationshipDataDocument.md)

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

# **tracks_id_relationships_source_file_get**
> TracksSourceFileSingleRelationshipDataDocument tracks_id_relationships_source_file_get(id, include=include, share_code=share_code)

Get sourceFile relationship (\"to-one\").

Retrieves sourceFile relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_source_file_single_relationship_data_document import TracksSourceFileSingleRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    include = ['sourceFile'] # List[str] | Include related resources. Available relationships: sourceFile (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get sourceFile relationship (\"to-one\").
        api_response = api_instance.tracks_id_relationships_source_file_get(id, include=include, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_source_file_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_source_file_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: sourceFile | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksSourceFileSingleRelationshipDataDocument**](TracksSourceFileSingleRelationshipDataDocument.md)

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

# **tracks_id_relationships_suggested_tracks_get**
> TracksSuggestedTracksMultiRelationshipDataDocument tracks_id_relationships_suggested_tracks_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)

Get suggestedTracks relationship (\"to-many\").

Retrieves suggestedTracks relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_suggested_tracks_multi_relationship_data_document import TracksSuggestedTracksMultiRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['suggestedTracks'] # List[str] | Include related resources. Available relationships: suggestedTracks (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'suggestedTracks' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: suggestedTracks (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get suggestedTracks relationship (\"to-many\").
        api_response = api_instance.tracks_id_relationships_suggested_tracks_get(id, country_code=country_code, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_suggested_tracks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_suggested_tracks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: suggestedTracks | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: suggestedTracks | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksSuggestedTracksMultiRelationshipDataDocument**](TracksSuggestedTracksMultiRelationshipDataDocument.md)

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

# **tracks_id_relationships_track_statistics_get**
> TracksTrackStatisticsSingleRelationshipDataDocument tracks_id_relationships_track_statistics_get(id, include=include, share_code=share_code)

Get trackStatistics relationship (\"to-one\").

Retrieves trackStatistics relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.tracks_track_statistics_single_relationship_data_document import TracksTrackStatisticsSingleRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    include = ['trackStatistics'] # List[str] | Include related resources. Available relationships: trackStatistics (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get trackStatistics relationship (\"to-one\").
        api_response = api_instance.tracks_id_relationships_track_statistics_get(id, include=include, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_track_statistics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_track_statistics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: trackStatistics | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksTrackStatisticsSingleRelationshipDataDocument**](TracksTrackStatisticsSingleRelationshipDataDocument.md)

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

# **tracks_id_relationships_usage_rules_get**
> TracksUsageRulesSingleRelationshipDataDocument tracks_id_relationships_usage_rules_get(id, country_code=country_code, include=include, share_code=share_code)

Get usageRules relationship (\"to-one\").

Retrieves usageRules relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.tracks_usage_rules_single_relationship_data_document import TracksUsageRulesSingleRelationshipDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    id = '75413016' # str | Track id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['usageRules'] # List[str] | Include related resources. Available relationships: usageRules (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get usageRules relationship (\"to-one\").
        api_response = api_instance.tracks_id_relationships_usage_rules_get(id, country_code=country_code, include=include, share_code=share_code)
        print("The response of TracksApi->tracks_id_relationships_usage_rules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_id_relationships_usage_rules_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: usageRules | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TracksUsageRulesSingleRelationshipDataDocument**](TracksUsageRulesSingleRelationshipDataDocument.md)

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

# **tracks_post**
> TracksCreateSingleResourceDataDocument tracks_post(idempotency_key=idempotency_key, tracks_create_operation_payload=tracks_create_operation_payload)

Create single track.

Creates a new track.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.tracks_create_operation_payload import TracksCreateOperationPayload
from tidal.models.tracks_create_single_resource_data_document import TracksCreateSingleResourceDataDocument
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
    api_instance = tidal.TracksApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    tracks_create_operation_payload = tidal.TracksCreateOperationPayload() # TracksCreateOperationPayload |  (optional)

    try:
        # Create single track.
        api_response = api_instance.tracks_post(idempotency_key=idempotency_key, tracks_create_operation_payload=tracks_create_operation_payload)
        print("The response of TracksApi->tracks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracksApi->tracks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **tracks_create_operation_payload** | [**TracksCreateOperationPayload**](TracksCreateOperationPayload.md)|  | [optional] 

### Return type

[**TracksCreateSingleResourceDataDocument**](TracksCreateSingleResourceDataDocument.md)

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

