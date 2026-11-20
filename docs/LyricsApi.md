# tidal.LyricsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lyrics_id_delete**](LyricsApi.md#lyrics_id_delete) | **DELETE** /lyrics/{id} | Delete single lyric.
[**lyrics_id_get**](LyricsApi.md#lyrics_id_get) | **GET** /lyrics/{id} | Get single lyric.
[**lyrics_id_patch**](LyricsApi.md#lyrics_id_patch) | **PATCH** /lyrics/{id} | Update single lyric.
[**lyrics_id_relationships_owners_get**](LyricsApi.md#lyrics_id_relationships_owners_get) | **GET** /lyrics/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**lyrics_id_relationships_track_get**](LyricsApi.md#lyrics_id_relationships_track_get) | **GET** /lyrics/{id}/relationships/track | Get track relationship (\&quot;to-one\&quot;).
[**lyrics_post**](LyricsApi.md#lyrics_post) | **POST** /lyrics | Create single lyric.


# **lyrics_id_delete**
> MutationResponseDocument lyrics_id_delete(id, idempotency_key=idempotency_key)

Delete single lyric.

Deletes existing lyric.

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
    api_instance = tidal.LyricsApi(api_client)
    id = 'nejMcAhh5N8S3EQ4LaqysVdI0cZZ' # str | Lyrics Id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)

    try:
        # Delete single lyric.
        api_response = api_instance.lyrics_id_delete(id, idempotency_key=idempotency_key)
        print("The response of LyricsApi->lyrics_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LyricsApi->lyrics_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Lyrics Id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 

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

# **lyrics_id_get**
> LyricsSingleResourceDataDocument lyrics_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single lyric.

Retrieves single lyric by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.lyrics_single_resource_data_document import LyricsSingleResourceDataDocument
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
    api_instance = tidal.LyricsApi(api_client)
    id = 'nejMcAhh5N8S3EQ4LaqysVdI0cZZ' # str | Lyrics Id
    include = ['track'] # List[str] | Include related resources. Available relationships: owners, track (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'track' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: track (optional)

    try:
        # Get single lyric.
        api_response = api_instance.lyrics_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of LyricsApi->lyrics_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LyricsApi->lyrics_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Lyrics Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners, track | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: track | [optional] 

### Return type

[**LyricsSingleResourceDataDocument**](LyricsSingleResourceDataDocument.md)

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

# **lyrics_id_patch**
> MutationResponseDocument lyrics_id_patch(id, idempotency_key=idempotency_key, lyrics_update_operation_payload=lyrics_update_operation_payload)

Update single lyric.

Updates existing lyric.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.lyrics_update_operation_payload import LyricsUpdateOperationPayload
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
    api_instance = tidal.LyricsApi(api_client)
    id = 'nejMcAhh5N8S3EQ4LaqysVdI0cZZ' # str | Lyrics Id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    lyrics_update_operation_payload = tidal.LyricsUpdateOperationPayload() # LyricsUpdateOperationPayload |  (optional)

    try:
        # Update single lyric.
        api_response = api_instance.lyrics_id_patch(id, idempotency_key=idempotency_key, lyrics_update_operation_payload=lyrics_update_operation_payload)
        print("The response of LyricsApi->lyrics_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LyricsApi->lyrics_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Lyrics Id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **lyrics_update_operation_payload** | [**LyricsUpdateOperationPayload**](LyricsUpdateOperationPayload.md)|  | [optional] 

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

# **lyrics_id_relationships_owners_get**
> LyricsOwnersMultiRelationshipDataDocument lyrics_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.lyrics_owners_multi_relationship_data_document import LyricsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.LyricsApi(api_client)
    id = 'nejMcAhh5N8S3EQ4LaqysVdI0cZZ' # str | Lyrics Id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.lyrics_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of LyricsApi->lyrics_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LyricsApi->lyrics_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Lyrics Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**LyricsOwnersMultiRelationshipDataDocument**](LyricsOwnersMultiRelationshipDataDocument.md)

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

# **lyrics_id_relationships_track_get**
> LyricsTrackSingleRelationshipDataDocument lyrics_id_relationships_track_get(id, country_code=country_code, include=include, replace_media=replace_media)

Get track relationship (\"to-one\").

Retrieves track relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.lyrics_track_single_relationship_data_document import LyricsTrackSingleRelationshipDataDocument
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
    api_instance = tidal.LyricsApi(api_client)
    id = 'nejMcAhh5N8S3EQ4LaqysVdI0cZZ' # str | Lyrics Id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['track'] # List[str] | Include related resources. Available relationships: track (optional)
    replace_media = 'track' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: track (optional)

    try:
        # Get track relationship (\"to-one\").
        api_response = api_instance.lyrics_id_relationships_track_get(id, country_code=country_code, include=include, replace_media=replace_media)
        print("The response of LyricsApi->lyrics_id_relationships_track_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LyricsApi->lyrics_id_relationships_track_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Lyrics Id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: track | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: track | [optional] 

### Return type

[**LyricsTrackSingleRelationshipDataDocument**](LyricsTrackSingleRelationshipDataDocument.md)

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

# **lyrics_post**
> LyricsCreateSingleResourceDataDocument lyrics_post(idempotency_key=idempotency_key, lyrics_create_operation_payload=lyrics_create_operation_payload)

Create single lyric.

Creates a new lyric.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.lyrics_create_operation_payload import LyricsCreateOperationPayload
from tidal.models.lyrics_create_single_resource_data_document import LyricsCreateSingleResourceDataDocument
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
    api_instance = tidal.LyricsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    lyrics_create_operation_payload = tidal.LyricsCreateOperationPayload() # LyricsCreateOperationPayload |  (optional)

    try:
        # Create single lyric.
        api_response = api_instance.lyrics_post(idempotency_key=idempotency_key, lyrics_create_operation_payload=lyrics_create_operation_payload)
        print("The response of LyricsApi->lyrics_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LyricsApi->lyrics_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **lyrics_create_operation_payload** | [**LyricsCreateOperationPayload**](LyricsCreateOperationPayload.md)|  | [optional] 

### Return type

[**LyricsCreateSingleResourceDataDocument**](LyricsCreateSingleResourceDataDocument.md)

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

