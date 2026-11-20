# tidal.UserRecommendationBlocksApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_recommendation_blocks_id_get**](UserRecommendationBlocksApi.md#user_recommendation_blocks_id_get) | **GET** /userRecommendationBlocks/{id} | Get single userRecommendationBlock.
[**user_recommendation_blocks_id_relationships_artists_delete**](UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_artists_delete) | **DELETE** /userRecommendationBlocks/{id}/relationships/artists | Delete from artists relationship (\&quot;to-many\&quot;).
[**user_recommendation_blocks_id_relationships_artists_get**](UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_artists_get) | **GET** /userRecommendationBlocks/{id}/relationships/artists | Get artists relationship (\&quot;to-many\&quot;).
[**user_recommendation_blocks_id_relationships_artists_post**](UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_artists_post) | **POST** /userRecommendationBlocks/{id}/relationships/artists | Add to artists relationship (\&quot;to-many\&quot;).
[**user_recommendation_blocks_id_relationships_owners_get**](UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_owners_get) | **GET** /userRecommendationBlocks/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**user_recommendation_blocks_id_relationships_tracks_delete**](UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_tracks_delete) | **DELETE** /userRecommendationBlocks/{id}/relationships/tracks | Delete from tracks relationship (\&quot;to-many\&quot;).
[**user_recommendation_blocks_id_relationships_tracks_get**](UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_tracks_get) | **GET** /userRecommendationBlocks/{id}/relationships/tracks | Get tracks relationship (\&quot;to-many\&quot;).
[**user_recommendation_blocks_id_relationships_tracks_post**](UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_tracks_post) | **POST** /userRecommendationBlocks/{id}/relationships/tracks | Add to tracks relationship (\&quot;to-many\&quot;).
[**user_recommendation_blocks_id_relationships_videos_delete**](UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_videos_delete) | **DELETE** /userRecommendationBlocks/{id}/relationships/videos | Delete from videos relationship (\&quot;to-many\&quot;).
[**user_recommendation_blocks_id_relationships_videos_get**](UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_videos_get) | **GET** /userRecommendationBlocks/{id}/relationships/videos | Get videos relationship (\&quot;to-many\&quot;).
[**user_recommendation_blocks_id_relationships_videos_post**](UserRecommendationBlocksApi.md#user_recommendation_blocks_id_relationships_videos_post) | **POST** /userRecommendationBlocks/{id}/relationships/videos | Add to videos relationship (\&quot;to-many\&quot;).


# **user_recommendation_blocks_id_get**
> UserRecommendationBlocksSingleResourceDataDocument user_recommendation_blocks_id_get(id, include=include, include_linkage=include_linkage, locale=locale, replace_media=replace_media)

Get single userRecommendationBlock.

Retrieves single userRecommendationBlock by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_recommendation_blocks_single_resource_data_document import UserRecommendationBlocksSingleResourceDataDocument
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
    api_instance = tidal.UserRecommendationBlocksApi(api_client)
    id = 'me' # str | User recommendation blocks id. Use `me` for the authenticated user's resource
    include = ['artists.albums'] # List[str] | Include related resources. Available relationships: artists, owners, tracks, videos (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    locale = 'en-US' # str | BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. (optional) (default to 'en-US')
    replace_media = 'artists.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums (optional)

    try:
        # Get single userRecommendationBlock.
        api_response = api_instance.user_recommendation_blocks_id_get(id, include=include, include_linkage=include_linkage, locale=locale, replace_media=replace_media)
        print("The response of UserRecommendationBlocksApi->user_recommendation_blocks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRecommendationBlocksApi->user_recommendation_blocks_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artists, owners, tracks, videos | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **locale** | **str**| BCP 47 locale (e.g., en-US, nb-NO, pt-BR). Defaults to en-US if not provided or unsupported. | [optional] [default to &#39;en-US&#39;]
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums | [optional] 

### Return type

[**UserRecommendationBlocksSingleResourceDataDocument**](UserRecommendationBlocksSingleResourceDataDocument.md)

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

# **user_recommendation_blocks_id_relationships_artists_delete**
> MutationResponseDocument user_recommendation_blocks_id_relationships_artists_delete(id, idempotency_key=idempotency_key, user_recommendation_blocks_artists_relationship_remove_operation_payload=user_recommendation_blocks_artists_relationship_remove_operation_payload)

Delete from artists relationship (\"to-many\").

Deletes item(s) from artists relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.user_recommendation_blocks_artists_relationship_remove_operation_payload import UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload
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
    api_instance = tidal.UserRecommendationBlocksApi(api_client)
    id = 'me' # str | User recommendation blocks id. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_recommendation_blocks_artists_relationship_remove_operation_payload = tidal.UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload() # UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload |  (optional)

    try:
        # Delete from artists relationship (\"to-many\").
        api_response = api_instance.user_recommendation_blocks_id_relationships_artists_delete(id, idempotency_key=idempotency_key, user_recommendation_blocks_artists_relationship_remove_operation_payload=user_recommendation_blocks_artists_relationship_remove_operation_payload)
        print("The response of UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_artists_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_artists_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_recommendation_blocks_artists_relationship_remove_operation_payload** | [**UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload**](UserRecommendationBlocksArtistsRelationshipRemoveOperationPayload.md)|  | [optional] 

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

# **user_recommendation_blocks_id_relationships_artists_get**
> UserRecommendationBlocksArtistsMultiRelationshipDataDocument user_recommendation_blocks_id_relationships_artists_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get artists relationship (\"to-many\").

Retrieves artists relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_recommendation_blocks_artists_multi_relationship_data_document import UserRecommendationBlocksArtistsMultiRelationshipDataDocument
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
    api_instance = tidal.UserRecommendationBlocksApi(api_client)
    id = 'me' # str | User recommendation blocks id. Use `me` for the authenticated user's resource
    include = ['artists.albums'] # List[str] | Include related resources. Available relationships: artists (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'artists.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums (optional)

    try:
        # Get artists relationship (\"to-many\").
        api_response = api_instance.user_recommendation_blocks_id_relationships_artists_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_artists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_artists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: artists | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: artists.albums | [optional] 

### Return type

[**UserRecommendationBlocksArtistsMultiRelationshipDataDocument**](UserRecommendationBlocksArtistsMultiRelationshipDataDocument.md)

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

# **user_recommendation_blocks_id_relationships_artists_post**
> UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument user_recommendation_blocks_id_relationships_artists_post(id, idempotency_key=idempotency_key, user_recommendation_blocks_artists_relationship_add_operation_payload=user_recommendation_blocks_artists_relationship_add_operation_payload)

Add to artists relationship (\"to-many\").

Adds item(s) to artists relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_recommendation_blocks_artists_add_multi_relationship_data_document import UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_artists_relationship_add_operation_payload import UserRecommendationBlocksArtistsRelationshipAddOperationPayload
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
    api_instance = tidal.UserRecommendationBlocksApi(api_client)
    id = 'me' # str | User recommendation blocks id. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_recommendation_blocks_artists_relationship_add_operation_payload = tidal.UserRecommendationBlocksArtistsRelationshipAddOperationPayload() # UserRecommendationBlocksArtistsRelationshipAddOperationPayload |  (optional)

    try:
        # Add to artists relationship (\"to-many\").
        api_response = api_instance.user_recommendation_blocks_id_relationships_artists_post(id, idempotency_key=idempotency_key, user_recommendation_blocks_artists_relationship_add_operation_payload=user_recommendation_blocks_artists_relationship_add_operation_payload)
        print("The response of UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_artists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_artists_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_recommendation_blocks_artists_relationship_add_operation_payload** | [**UserRecommendationBlocksArtistsRelationshipAddOperationPayload**](UserRecommendationBlocksArtistsRelationshipAddOperationPayload.md)|  | [optional] 

### Return type

[**UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument**](UserRecommendationBlocksArtistsAddMultiRelationshipDataDocument.md)

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
**409** | Recommendation block limit reached; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_recommendation_blocks_id_relationships_owners_get**
> UserRecommendationBlocksOwnersMultiRelationshipDataDocument user_recommendation_blocks_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_recommendation_blocks_owners_multi_relationship_data_document import UserRecommendationBlocksOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.UserRecommendationBlocksApi(api_client)
    id = 'me' # str | User recommendation blocks id. Use `me` for the authenticated user's resource
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.user_recommendation_blocks_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**UserRecommendationBlocksOwnersMultiRelationshipDataDocument**](UserRecommendationBlocksOwnersMultiRelationshipDataDocument.md)

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

# **user_recommendation_blocks_id_relationships_tracks_delete**
> MutationResponseDocument user_recommendation_blocks_id_relationships_tracks_delete(id, idempotency_key=idempotency_key, user_recommendation_blocks_tracks_relationship_remove_operation_payload=user_recommendation_blocks_tracks_relationship_remove_operation_payload)

Delete from tracks relationship (\"to-many\").

Deletes item(s) from tracks relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.user_recommendation_blocks_tracks_relationship_remove_operation_payload import UserRecommendationBlocksTracksRelationshipRemoveOperationPayload
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
    api_instance = tidal.UserRecommendationBlocksApi(api_client)
    id = 'me' # str | User recommendation blocks id. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_recommendation_blocks_tracks_relationship_remove_operation_payload = tidal.UserRecommendationBlocksTracksRelationshipRemoveOperationPayload() # UserRecommendationBlocksTracksRelationshipRemoveOperationPayload |  (optional)

    try:
        # Delete from tracks relationship (\"to-many\").
        api_response = api_instance.user_recommendation_blocks_id_relationships_tracks_delete(id, idempotency_key=idempotency_key, user_recommendation_blocks_tracks_relationship_remove_operation_payload=user_recommendation_blocks_tracks_relationship_remove_operation_payload)
        print("The response of UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_tracks_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_tracks_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_recommendation_blocks_tracks_relationship_remove_operation_payload** | [**UserRecommendationBlocksTracksRelationshipRemoveOperationPayload**](UserRecommendationBlocksTracksRelationshipRemoveOperationPayload.md)|  | [optional] 

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

# **user_recommendation_blocks_id_relationships_tracks_get**
> UserRecommendationBlocksTracksMultiRelationshipDataDocument user_recommendation_blocks_id_relationships_tracks_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get tracks relationship (\"to-many\").

Retrieves tracks relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_recommendation_blocks_tracks_multi_relationship_data_document import UserRecommendationBlocksTracksMultiRelationshipDataDocument
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
    api_instance = tidal.UserRecommendationBlocksApi(api_client)
    id = 'me' # str | User recommendation blocks id. Use `me` for the authenticated user's resource
    include = ['tracks'] # List[str] | Include related resources. Available relationships: tracks (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'tracks' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks (optional)

    try:
        # Get tracks relationship (\"to-many\").
        api_response = api_instance.user_recommendation_blocks_id_relationships_tracks_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_tracks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_tracks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: tracks | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: tracks | [optional] 

### Return type

[**UserRecommendationBlocksTracksMultiRelationshipDataDocument**](UserRecommendationBlocksTracksMultiRelationshipDataDocument.md)

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

# **user_recommendation_blocks_id_relationships_tracks_post**
> UserRecommendationBlocksTracksAddMultiRelationshipDataDocument user_recommendation_blocks_id_relationships_tracks_post(id, idempotency_key=idempotency_key, user_recommendation_blocks_tracks_relationship_add_operation_payload=user_recommendation_blocks_tracks_relationship_add_operation_payload)

Add to tracks relationship (\"to-many\").

Adds item(s) to tracks relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_recommendation_blocks_tracks_add_multi_relationship_data_document import UserRecommendationBlocksTracksAddMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_tracks_relationship_add_operation_payload import UserRecommendationBlocksTracksRelationshipAddOperationPayload
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
    api_instance = tidal.UserRecommendationBlocksApi(api_client)
    id = 'me' # str | User recommendation blocks id. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_recommendation_blocks_tracks_relationship_add_operation_payload = tidal.UserRecommendationBlocksTracksRelationshipAddOperationPayload() # UserRecommendationBlocksTracksRelationshipAddOperationPayload |  (optional)

    try:
        # Add to tracks relationship (\"to-many\").
        api_response = api_instance.user_recommendation_blocks_id_relationships_tracks_post(id, idempotency_key=idempotency_key, user_recommendation_blocks_tracks_relationship_add_operation_payload=user_recommendation_blocks_tracks_relationship_add_operation_payload)
        print("The response of UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_tracks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_tracks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_recommendation_blocks_tracks_relationship_add_operation_payload** | [**UserRecommendationBlocksTracksRelationshipAddOperationPayload**](UserRecommendationBlocksTracksRelationshipAddOperationPayload.md)|  | [optional] 

### Return type

[**UserRecommendationBlocksTracksAddMultiRelationshipDataDocument**](UserRecommendationBlocksTracksAddMultiRelationshipDataDocument.md)

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
**409** | Recommendation block limit reached; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_recommendation_blocks_id_relationships_videos_delete**
> MutationResponseDocument user_recommendation_blocks_id_relationships_videos_delete(id, idempotency_key=idempotency_key, user_recommendation_blocks_videos_relationship_remove_operation_payload=user_recommendation_blocks_videos_relationship_remove_operation_payload)

Delete from videos relationship (\"to-many\").

Deletes item(s) from videos relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.user_recommendation_blocks_videos_relationship_remove_operation_payload import UserRecommendationBlocksVideosRelationshipRemoveOperationPayload
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
    api_instance = tidal.UserRecommendationBlocksApi(api_client)
    id = 'me' # str | User recommendation blocks id. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_recommendation_blocks_videos_relationship_remove_operation_payload = tidal.UserRecommendationBlocksVideosRelationshipRemoveOperationPayload() # UserRecommendationBlocksVideosRelationshipRemoveOperationPayload |  (optional)

    try:
        # Delete from videos relationship (\"to-many\").
        api_response = api_instance.user_recommendation_blocks_id_relationships_videos_delete(id, idempotency_key=idempotency_key, user_recommendation_blocks_videos_relationship_remove_operation_payload=user_recommendation_blocks_videos_relationship_remove_operation_payload)
        print("The response of UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_videos_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_videos_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_recommendation_blocks_videos_relationship_remove_operation_payload** | [**UserRecommendationBlocksVideosRelationshipRemoveOperationPayload**](UserRecommendationBlocksVideosRelationshipRemoveOperationPayload.md)|  | [optional] 

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

# **user_recommendation_blocks_id_relationships_videos_get**
> UserRecommendationBlocksVideosMultiRelationshipDataDocument user_recommendation_blocks_id_relationships_videos_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get videos relationship (\"to-many\").

Retrieves videos relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_recommendation_blocks_videos_multi_relationship_data_document import UserRecommendationBlocksVideosMultiRelationshipDataDocument
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
    api_instance = tidal.UserRecommendationBlocksApi(api_client)
    id = 'me' # str | User recommendation blocks id. Use `me` for the authenticated user's resource
    include = ['videos'] # List[str] | Include related resources. Available relationships: videos (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'videos' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos (optional)

    try:
        # Get videos relationship (\"to-many\").
        api_response = api_instance.user_recommendation_blocks_id_relationships_videos_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_videos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_videos_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: videos | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: videos | [optional] 

### Return type

[**UserRecommendationBlocksVideosMultiRelationshipDataDocument**](UserRecommendationBlocksVideosMultiRelationshipDataDocument.md)

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

# **user_recommendation_blocks_id_relationships_videos_post**
> UserRecommendationBlocksVideosAddMultiRelationshipDataDocument user_recommendation_blocks_id_relationships_videos_post(id, idempotency_key=idempotency_key, user_recommendation_blocks_videos_relationship_add_operation_payload=user_recommendation_blocks_videos_relationship_add_operation_payload)

Add to videos relationship (\"to-many\").

Adds item(s) to videos relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_recommendation_blocks_videos_add_multi_relationship_data_document import UserRecommendationBlocksVideosAddMultiRelationshipDataDocument
from tidal.models.user_recommendation_blocks_videos_relationship_add_operation_payload import UserRecommendationBlocksVideosRelationshipAddOperationPayload
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
    api_instance = tidal.UserRecommendationBlocksApi(api_client)
    id = 'me' # str | User recommendation blocks id. Use `me` for the authenticated user's resource
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    user_recommendation_blocks_videos_relationship_add_operation_payload = tidal.UserRecommendationBlocksVideosRelationshipAddOperationPayload() # UserRecommendationBlocksVideosRelationshipAddOperationPayload |  (optional)

    try:
        # Add to videos relationship (\"to-many\").
        api_response = api_instance.user_recommendation_blocks_id_relationships_videos_post(id, idempotency_key=idempotency_key, user_recommendation_blocks_videos_relationship_add_operation_payload=user_recommendation_blocks_videos_relationship_add_operation_payload)
        print("The response of UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_videos_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRecommendationBlocksApi->user_recommendation_blocks_id_relationships_videos_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User recommendation blocks id. Use &#x60;me&#x60; for the authenticated user&#39;s resource | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **user_recommendation_blocks_videos_relationship_add_operation_payload** | [**UserRecommendationBlocksVideosRelationshipAddOperationPayload**](UserRecommendationBlocksVideosRelationshipAddOperationPayload.md)|  | [optional] 

### Return type

[**UserRecommendationBlocksVideosAddMultiRelationshipDataDocument**](UserRecommendationBlocksVideosAddMultiRelationshipDataDocument.md)

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
**409** | Recommendation block limit reached; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

