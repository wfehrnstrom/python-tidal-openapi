# tidal.ArtistClaimsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artist_claims_get**](ArtistClaimsApi.md#artist_claims_get) | **GET** /artistClaims | Get multiple artistClaims.
[**artist_claims_id_delete**](ArtistClaimsApi.md#artist_claims_id_delete) | **DELETE** /artistClaims/{id} | Delete single artistClaim.
[**artist_claims_id_get**](ArtistClaimsApi.md#artist_claims_id_get) | **GET** /artistClaims/{id} | Get single artistClaim.
[**artist_claims_id_patch**](ArtistClaimsApi.md#artist_claims_id_patch) | **PATCH** /artistClaims/{id} | Update single artistClaim.
[**artist_claims_id_relationships_accepted_artists_get**](ArtistClaimsApi.md#artist_claims_id_relationships_accepted_artists_get) | **GET** /artistClaims/{id}/relationships/acceptedArtists | Get acceptedArtists relationship (\&quot;to-many\&quot;).
[**artist_claims_id_relationships_accepted_artists_patch**](ArtistClaimsApi.md#artist_claims_id_relationships_accepted_artists_patch) | **PATCH** /artistClaims/{id}/relationships/acceptedArtists | Update acceptedArtists relationship (\&quot;to-many\&quot;).
[**artist_claims_id_relationships_owners_get**](ArtistClaimsApi.md#artist_claims_id_relationships_owners_get) | **GET** /artistClaims/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**artist_claims_id_relationships_recommended_artists_get**](ArtistClaimsApi.md#artist_claims_id_relationships_recommended_artists_get) | **GET** /artistClaims/{id}/relationships/recommendedArtists | Get recommendedArtists relationship (\&quot;to-many\&quot;).
[**artist_claims_post**](ArtistClaimsApi.md#artist_claims_post) | **POST** /artistClaims | Create single artistClaim.


# **artist_claims_get**
> ArtistClaimsMultiResourceDataDocument artist_claims_get(filter_owners_id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get multiple artistClaims.

Retrieves multiple artistClaims by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artist_claims_multi_resource_data_document import ArtistClaimsMultiResourceDataDocument
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
    api_instance = tidal.ArtistClaimsApi(api_client)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`.
    include = ['acceptedArtists.albums'] # List[str] | Include related resources. Available relationships: acceptedArtists, owners, recommendedArtists (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'acceptedArtists.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: acceptedArtists.albums (optional)

    try:
        # Get multiple artistClaims.
        api_response = api_instance.artist_claims_get(filter_owners_id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of ArtistClaimsApi->artist_claims_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistClaimsApi->artist_claims_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_owners_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: acceptedArtists, owners, recommendedArtists | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: acceptedArtists.albums | [optional] 

### Return type

[**ArtistClaimsMultiResourceDataDocument**](ArtistClaimsMultiResourceDataDocument.md)

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

# **artist_claims_id_delete**
> MutationResponseDocument artist_claims_id_delete(id, idempotency_key=idempotency_key)

Delete single artistClaim.

Deletes existing artistClaim.

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
    api_instance = tidal.ArtistClaimsApi(api_client)
    id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | Artist claim id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)

    try:
        # Delete single artistClaim.
        api_response = api_instance.artist_claims_id_delete(id, idempotency_key=idempotency_key)
        print("The response of ArtistClaimsApi->artist_claims_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistClaimsApi->artist_claims_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist claim id | 
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

# **artist_claims_id_get**
> ArtistClaimsSingleResourceDataDocument artist_claims_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single artistClaim.

Retrieves single artistClaim by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artist_claims_single_resource_data_document import ArtistClaimsSingleResourceDataDocument
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
    api_instance = tidal.ArtistClaimsApi(api_client)
    id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | Artist claim id
    include = ['acceptedArtists.albums'] # List[str] | Include related resources. Available relationships: acceptedArtists, owners, recommendedArtists (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'acceptedArtists.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: acceptedArtists.albums (optional)

    try:
        # Get single artistClaim.
        api_response = api_instance.artist_claims_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of ArtistClaimsApi->artist_claims_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistClaimsApi->artist_claims_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist claim id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: acceptedArtists, owners, recommendedArtists | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: acceptedArtists.albums | [optional] 

### Return type

[**ArtistClaimsSingleResourceDataDocument**](ArtistClaimsSingleResourceDataDocument.md)

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

# **artist_claims_id_patch**
> MutationResponseDocument artist_claims_id_patch(id, idempotency_key=idempotency_key, artist_claims_update_operation_payload=artist_claims_update_operation_payload)

Update single artistClaim.

Updates existing artistClaim.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artist_claims_update_operation_payload import ArtistClaimsUpdateOperationPayload
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
    api_instance = tidal.ArtistClaimsApi(api_client)
    id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | Artist claim id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    artist_claims_update_operation_payload = tidal.ArtistClaimsUpdateOperationPayload() # ArtistClaimsUpdateOperationPayload |  (optional)

    try:
        # Update single artistClaim.
        api_response = api_instance.artist_claims_id_patch(id, idempotency_key=idempotency_key, artist_claims_update_operation_payload=artist_claims_update_operation_payload)
        print("The response of ArtistClaimsApi->artist_claims_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistClaimsApi->artist_claims_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist claim id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **artist_claims_update_operation_payload** | [**ArtistClaimsUpdateOperationPayload**](ArtistClaimsUpdateOperationPayload.md)|  | [optional] 

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

# **artist_claims_id_relationships_accepted_artists_get**
> ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument artist_claims_id_relationships_accepted_artists_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get acceptedArtists relationship (\"to-many\").

Retrieves acceptedArtists relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artist_claims_accepted_artists_multi_relationship_data_document import ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistClaimsApi(api_client)
    id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | Artist claim id
    include = ['acceptedArtists.albums'] # List[str] | Include related resources. Available relationships: acceptedArtists (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'acceptedArtists.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: acceptedArtists.albums (optional)

    try:
        # Get acceptedArtists relationship (\"to-many\").
        api_response = api_instance.artist_claims_id_relationships_accepted_artists_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of ArtistClaimsApi->artist_claims_id_relationships_accepted_artists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistClaimsApi->artist_claims_id_relationships_accepted_artists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist claim id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: acceptedArtists | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: acceptedArtists.albums | [optional] 

### Return type

[**ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument**](ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument.md)

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

# **artist_claims_id_relationships_accepted_artists_patch**
> MutationResponseDocument artist_claims_id_relationships_accepted_artists_patch(id, idempotency_key=idempotency_key, artist_claims_accepted_artists_relationship_update_operation_payload=artist_claims_accepted_artists_relationship_update_operation_payload)

Update acceptedArtists relationship (\"to-many\").

Accepts one recommended artist and processes the claim, merging profile metadata or moving claimed albums according to the recommendation. Empty data cancels the claim; it does not delete any artist. Returns an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artist_claims_accepted_artists_relationship_update_operation_payload import ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload
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
    api_instance = tidal.ArtistClaimsApi(api_client)
    id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | Artist claim id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    artist_claims_accepted_artists_relationship_update_operation_payload = tidal.ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload() # ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update acceptedArtists relationship (\"to-many\").
        api_response = api_instance.artist_claims_id_relationships_accepted_artists_patch(id, idempotency_key=idempotency_key, artist_claims_accepted_artists_relationship_update_operation_payload=artist_claims_accepted_artists_relationship_update_operation_payload)
        print("The response of ArtistClaimsApi->artist_claims_id_relationships_accepted_artists_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistClaimsApi->artist_claims_id_relationships_accepted_artists_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist claim id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **artist_claims_accepted_artists_relationship_update_operation_payload** | [**ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload**](ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload.md)|  | [optional] 

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

# **artist_claims_id_relationships_owners_get**
> ArtistClaimsOwnersMultiRelationshipDataDocument artist_claims_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artist_claims_owners_multi_relationship_data_document import ArtistClaimsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistClaimsApi(api_client)
    id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | Artist claim id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.artist_claims_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of ArtistClaimsApi->artist_claims_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistClaimsApi->artist_claims_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist claim id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**ArtistClaimsOwnersMultiRelationshipDataDocument**](ArtistClaimsOwnersMultiRelationshipDataDocument.md)

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

# **artist_claims_id_relationships_recommended_artists_get**
> ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument artist_claims_id_relationships_recommended_artists_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get recommendedArtists relationship (\"to-many\").

Retrieves recommendedArtists relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artist_claims_recommended_artists_multi_relationship_data_document import ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument
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
    api_instance = tidal.ArtistClaimsApi(api_client)
    id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | Artist claim id
    include = ['recommendedArtists.albums'] # List[str] | Include related resources. Available relationships: recommendedArtists (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'recommendedArtists.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: recommendedArtists.albums (optional)

    try:
        # Get recommendedArtists relationship (\"to-many\").
        api_response = api_instance.artist_claims_id_relationships_recommended_artists_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of ArtistClaimsApi->artist_claims_id_relationships_recommended_artists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistClaimsApi->artist_claims_id_relationships_recommended_artists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Artist claim id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: recommendedArtists | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: recommendedArtists.albums | [optional] 

### Return type

[**ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument**](ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument.md)

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

# **artist_claims_post**
> ArtistClaimsCreateSingleResourceDataDocument artist_claims_post(idempotency_key=idempotency_key, artist_claims_create_operation_payload=artist_claims_create_operation_payload)

Create single artistClaim.

Creates a new artistClaim.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.artist_claims_create_operation_payload import ArtistClaimsCreateOperationPayload
from tidal.models.artist_claims_create_single_resource_data_document import ArtistClaimsCreateSingleResourceDataDocument
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
    api_instance = tidal.ArtistClaimsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    artist_claims_create_operation_payload = tidal.ArtistClaimsCreateOperationPayload() # ArtistClaimsCreateOperationPayload |  (optional)

    try:
        # Create single artistClaim.
        api_response = api_instance.artist_claims_post(idempotency_key=idempotency_key, artist_claims_create_operation_payload=artist_claims_create_operation_payload)
        print("The response of ArtistClaimsApi->artist_claims_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistClaimsApi->artist_claims_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **artist_claims_create_operation_payload** | [**ArtistClaimsCreateOperationPayload**](ArtistClaimsCreateOperationPayload.md)|  | [optional] 

### Return type

[**ArtistClaimsCreateSingleResourceDataDocument**](ArtistClaimsCreateSingleResourceDataDocument.md)

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

