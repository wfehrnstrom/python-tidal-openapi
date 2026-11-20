# tidal.ContentClaimsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_claims_get**](ContentClaimsApi.md#content_claims_get) | **GET** /contentClaims | Get multiple contentClaims.
[**content_claims_id_get**](ContentClaimsApi.md#content_claims_id_get) | **GET** /contentClaims/{id} | Get single contentClaim.
[**content_claims_id_relationships_claimed_resource_get**](ContentClaimsApi.md#content_claims_id_relationships_claimed_resource_get) | **GET** /contentClaims/{id}/relationships/claimedResource | Get claimedResource relationship (\&quot;to-one\&quot;).
[**content_claims_id_relationships_claiming_artist_get**](ContentClaimsApi.md#content_claims_id_relationships_claiming_artist_get) | **GET** /contentClaims/{id}/relationships/claimingArtist | Get claimingArtist relationship (\&quot;to-one\&quot;).
[**content_claims_id_relationships_owners_get**](ContentClaimsApi.md#content_claims_id_relationships_owners_get) | **GET** /contentClaims/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**content_claims_post**](ContentClaimsApi.md#content_claims_post) | **POST** /contentClaims | Create single contentClaim.


# **content_claims_get**
> ContentClaimsMultiResourceDataDocument content_claims_get(filter_owners_id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get multiple contentClaims.

Retrieves multiple contentClaims by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.content_claims_multi_resource_data_document import ContentClaimsMultiResourceDataDocument
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
    api_instance = tidal.ContentClaimsApi(api_client)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`.
    include = ['claimedResource'] # List[str] | Include related resources. Available relationships: claimedResource, claimingArtist, owners (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'claimedResource' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: claimedResource (optional)

    try:
        # Get multiple contentClaims.
        api_response = api_instance.content_claims_get(filter_owners_id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of ContentClaimsApi->content_claims_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentClaimsApi->content_claims_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_owners_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: claimedResource, claimingArtist, owners | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: claimedResource | [optional] 

### Return type

[**ContentClaimsMultiResourceDataDocument**](ContentClaimsMultiResourceDataDocument.md)

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

# **content_claims_id_get**
> ContentClaimsSingleResourceDataDocument content_claims_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single contentClaim.

Retrieves single contentClaim by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.content_claims_single_resource_data_document import ContentClaimsSingleResourceDataDocument
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
    api_instance = tidal.ContentClaimsApi(api_client)
    id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | Content claim id
    include = ['claimedResource'] # List[str] | Include related resources. Available relationships: claimedResource, claimingArtist, owners (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'claimedResource' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: claimedResource (optional)

    try:
        # Get single contentClaim.
        api_response = api_instance.content_claims_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of ContentClaimsApi->content_claims_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentClaimsApi->content_claims_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Content claim id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: claimedResource, claimingArtist, owners | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: claimedResource | [optional] 

### Return type

[**ContentClaimsSingleResourceDataDocument**](ContentClaimsSingleResourceDataDocument.md)

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

# **content_claims_id_relationships_claimed_resource_get**
> ContentClaimsClaimedResourceSingleRelationshipDataDocument content_claims_id_relationships_claimed_resource_get(id, include=include, replace_media=replace_media)

Get claimedResource relationship (\"to-one\").

Retrieves claimedResource relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.content_claims_claimed_resource_single_relationship_data_document import ContentClaimsClaimedResourceSingleRelationshipDataDocument
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
    api_instance = tidal.ContentClaimsApi(api_client)
    id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | Content claim id
    include = ['claimedResource'] # List[str] | Include related resources. Available relationships: claimedResource (optional)
    replace_media = 'claimedResource' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: claimedResource (optional)

    try:
        # Get claimedResource relationship (\"to-one\").
        api_response = api_instance.content_claims_id_relationships_claimed_resource_get(id, include=include, replace_media=replace_media)
        print("The response of ContentClaimsApi->content_claims_id_relationships_claimed_resource_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentClaimsApi->content_claims_id_relationships_claimed_resource_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Content claim id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: claimedResource | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: claimedResource | [optional] 

### Return type

[**ContentClaimsClaimedResourceSingleRelationshipDataDocument**](ContentClaimsClaimedResourceSingleRelationshipDataDocument.md)

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

# **content_claims_id_relationships_claiming_artist_get**
> ContentClaimsClaimingArtistSingleRelationshipDataDocument content_claims_id_relationships_claiming_artist_get(id, include=include, replace_media=replace_media)

Get claimingArtist relationship (\"to-one\").

Retrieves claimingArtist relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.content_claims_claiming_artist_single_relationship_data_document import ContentClaimsClaimingArtistSingleRelationshipDataDocument
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
    api_instance = tidal.ContentClaimsApi(api_client)
    id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | Content claim id
    include = ['claimingArtist.albums'] # List[str] | Include related resources. Available relationships: claimingArtist (optional)
    replace_media = 'claimingArtist.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: claimingArtist.albums (optional)

    try:
        # Get claimingArtist relationship (\"to-one\").
        api_response = api_instance.content_claims_id_relationships_claiming_artist_get(id, include=include, replace_media=replace_media)
        print("The response of ContentClaimsApi->content_claims_id_relationships_claiming_artist_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentClaimsApi->content_claims_id_relationships_claiming_artist_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Content claim id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: claimingArtist | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: claimingArtist.albums | [optional] 

### Return type

[**ContentClaimsClaimingArtistSingleRelationshipDataDocument**](ContentClaimsClaimingArtistSingleRelationshipDataDocument.md)

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

# **content_claims_id_relationships_owners_get**
> ContentClaimsOwnersMultiRelationshipDataDocument content_claims_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.content_claims_owners_multi_relationship_data_document import ContentClaimsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.ContentClaimsApi(api_client)
    id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | Content claim id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.content_claims_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of ContentClaimsApi->content_claims_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentClaimsApi->content_claims_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Content claim id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**ContentClaimsOwnersMultiRelationshipDataDocument**](ContentClaimsOwnersMultiRelationshipDataDocument.md)

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

# **content_claims_post**
> ContentClaimsCreateSingleResourceDataDocument content_claims_post(idempotency_key=idempotency_key, content_claims_create_operation_payload=content_claims_create_operation_payload)

Create single contentClaim.

Creates a new contentClaim.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.content_claims_create_operation_payload import ContentClaimsCreateOperationPayload
from tidal.models.content_claims_create_single_resource_data_document import ContentClaimsCreateSingleResourceDataDocument
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
    api_instance = tidal.ContentClaimsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    content_claims_create_operation_payload = tidal.ContentClaimsCreateOperationPayload() # ContentClaimsCreateOperationPayload |  (optional)

    try:
        # Create single contentClaim.
        api_response = api_instance.content_claims_post(idempotency_key=idempotency_key, content_claims_create_operation_payload=content_claims_create_operation_payload)
        print("The response of ContentClaimsApi->content_claims_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentClaimsApi->content_claims_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **content_claims_create_operation_payload** | [**ContentClaimsCreateOperationPayload**](ContentClaimsCreateOperationPayload.md)|  | [optional] 

### Return type

[**ContentClaimsCreateSingleResourceDataDocument**](ContentClaimsCreateSingleResourceDataDocument.md)

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

