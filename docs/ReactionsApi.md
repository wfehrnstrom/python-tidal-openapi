# tidal.ReactionsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reactions_get**](ReactionsApi.md#reactions_get) | **GET** /reactions | Get multiple reactions.
[**reactions_id_delete**](ReactionsApi.md#reactions_id_delete) | **DELETE** /reactions/{id} | Delete single reaction.
[**reactions_id_relationships_author_get**](ReactionsApi.md#reactions_id_relationships_author_get) | **GET** /reactions/{id}/relationships/author | Get author relationship (\&quot;to-one\&quot;).
[**reactions_id_relationships_owners_get**](ReactionsApi.md#reactions_id_relationships_owners_get) | **GET** /reactions/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**reactions_id_relationships_subject_get**](ReactionsApi.md#reactions_id_relationships_subject_get) | **GET** /reactions/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
[**reactions_post**](ReactionsApi.md#reactions_post) | **POST** /reactions | Create single reaction.


# **reactions_get**
> ReactionsMultiResourceDataDocument reactions_get(filter_subject, filter_emoji=filter_emoji, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media)

Get multiple reactions.

Lists reactions on a source file or comment, newest first.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.reactions_multi_resource_data_document import ReactionsMultiResourceDataDocument
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
    api_instance = tidal.ReactionsApi(api_client)
    filter_subject = 'filter_subject_example' # str | The subject whose reactions to return.
    filter_emoji = ['filter_emoji_example'] # List[str] | Filter by emoji (e.g. `👍`) (optional)
    include = ['author.albums'] # List[str] | Include related resources. Available relationships: author, owners, subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'author.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums (optional)

    try:
        # Get multiple reactions.
        api_response = api_instance.reactions_get(filter_subject, filter_emoji=filter_emoji, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of ReactionsApi->reactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_subject** | **str**| The subject whose reactions to return. | 
 **filter_emoji** | [**List[str]**](str.md)| Filter by emoji (e.g. &#x60;👍&#x60;) | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: author, owners, subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: author.albums | [optional] 

### Return type

[**ReactionsMultiResourceDataDocument**](ReactionsMultiResourceDataDocument.md)

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

# **reactions_id_delete**
> MutationResponseDocument reactions_id_delete(id, idempotency_key=idempotency_key)

Delete single reaction.

Deletes existing reaction.

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
    api_instance = tidal.ReactionsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Reaction Id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)

    try:
        # Delete single reaction.
        api_response = api_instance.reactions_id_delete(id, idempotency_key=idempotency_key)
        print("The response of ReactionsApi->reactions_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Reaction Id | 
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

# **reactions_id_relationships_author_get**
> ReactionsAuthorSingleRelationshipDataDocument reactions_id_relationships_author_get(id, include=include, replace_media=replace_media)

Get author relationship (\"to-one\").

The artist who left the reaction.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.reactions_author_single_relationship_data_document import ReactionsAuthorSingleRelationshipDataDocument
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
    api_instance = tidal.ReactionsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Reaction Id
    include = ['author.albums'] # List[str] | Include related resources. Available relationships: author (optional)
    replace_media = 'author.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums (optional)

    try:
        # Get author relationship (\"to-one\").
        api_response = api_instance.reactions_id_relationships_author_get(id, include=include, replace_media=replace_media)
        print("The response of ReactionsApi->reactions_id_relationships_author_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_id_relationships_author_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Reaction Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: author | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: author.albums | [optional] 

### Return type

[**ReactionsAuthorSingleRelationshipDataDocument**](ReactionsAuthorSingleRelationshipDataDocument.md)

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

# **reactions_id_relationships_owners_get**
> ReactionsOwnersMultiRelationshipDataDocument reactions_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.reactions_owners_multi_relationship_data_document import ReactionsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.ReactionsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Reaction Id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.reactions_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of ReactionsApi->reactions_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Reaction Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**ReactionsOwnersMultiRelationshipDataDocument**](ReactionsOwnersMultiRelationshipDataDocument.md)

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

# **reactions_id_relationships_subject_get**
> ReactionsSubjectSingleRelationshipDataDocument reactions_id_relationships_subject_get(id, include=include, replace_media=replace_media)

Get subject relationship (\"to-one\").

Retrieves subject relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.reactions_subject_single_relationship_data_document import ReactionsSubjectSingleRelationshipDataDocument
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
    api_instance = tidal.ReactionsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Reaction Id
    include = ['subject.author.albums'] # List[str] | Include related resources. Available relationships: subject (optional)
    replace_media = 'subject.author.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.author.albums (optional)

    try:
        # Get subject relationship (\"to-one\").
        api_response = api_instance.reactions_id_relationships_subject_get(id, include=include, replace_media=replace_media)
        print("The response of ReactionsApi->reactions_id_relationships_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_id_relationships_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Reaction Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject.author.albums | [optional] 

### Return type

[**ReactionsSubjectSingleRelationshipDataDocument**](ReactionsSubjectSingleRelationshipDataDocument.md)

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

# **reactions_post**
> ReactionsCreateSingleResourceDataDocument reactions_post(idempotency_key=idempotency_key, reactions_create_operation_payload=reactions_create_operation_payload)

Create single reaction.

Adds the caller's emoji reaction on a subject and exact time offsets. Omit both offsets for the whole subject, provide startOffset for a point, or both for a section. Offsets are supported only on source files and must be nonnegative, with endOffset at or after startOffset. Each user can add different emojis at the same position or section. Repeating the same emoji returns the existing reaction with its UUID and creation time unchanged.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.reactions_create_operation_payload import ReactionsCreateOperationPayload
from tidal.models.reactions_create_single_resource_data_document import ReactionsCreateSingleResourceDataDocument
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
    api_instance = tidal.ReactionsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    reactions_create_operation_payload = tidal.ReactionsCreateOperationPayload() # ReactionsCreateOperationPayload |  (optional)

    try:
        # Create single reaction.
        api_response = api_instance.reactions_post(idempotency_key=idempotency_key, reactions_create_operation_payload=reactions_create_operation_payload)
        print("The response of ReactionsApi->reactions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **reactions_create_operation_payload** | [**ReactionsCreateOperationPayload**](ReactionsCreateOperationPayload.md)|  | [optional] 

### Return type

[**ReactionsCreateSingleResourceDataDocument**](ReactionsCreateSingleResourceDataDocument.md)

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

