# tidal.CommentsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comments_get**](CommentsApi.md#comments_get) | **GET** /comments | Get multiple comments.
[**comments_id_delete**](CommentsApi.md#comments_id_delete) | **DELETE** /comments/{id} | Delete single comment.
[**comments_id_get**](CommentsApi.md#comments_id_get) | **GET** /comments/{id} | Get single comment.
[**comments_id_patch**](CommentsApi.md#comments_id_patch) | **PATCH** /comments/{id} | Update single comment.
[**comments_id_relationships_author_get**](CommentsApi.md#comments_id_relationships_author_get) | **GET** /comments/{id}/relationships/author | Get author relationship (\&quot;to-one\&quot;).
[**comments_id_relationships_comment_summary_get**](CommentsApi.md#comments_id_relationships_comment_summary_get) | **GET** /comments/{id}/relationships/commentSummary | Get commentSummary relationship (\&quot;to-one\&quot;).
[**comments_id_relationships_owners_get**](CommentsApi.md#comments_id_relationships_owners_get) | **GET** /comments/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**comments_id_relationships_reaction_summary_get**](CommentsApi.md#comments_id_relationships_reaction_summary_get) | **GET** /comments/{id}/relationships/reactionSummary | Get reactionSummary relationship (\&quot;to-one\&quot;).
[**comments_id_relationships_root_subject_get**](CommentsApi.md#comments_id_relationships_root_subject_get) | **GET** /comments/{id}/relationships/rootSubject | Get rootSubject relationship (\&quot;to-one\&quot;).
[**comments_id_relationships_subject_get**](CommentsApi.md#comments_id_relationships_subject_get) | **GET** /comments/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
[**comments_post**](CommentsApi.md#comments_post) | **POST** /comments | Create single comment.


# **comments_get**
> CommentsMultiResourceDataDocument comments_get(filter_subject, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media, sort=sort)

Get multiple comments.

Returns root comments on a resource, or replies to a comment. Both support createdAt in either direction, newest first by default.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.comments_multi_resource_data_document import CommentsMultiResourceDataDocument
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
    api_instance = tidal.CommentsApi(api_client)
    filter_subject = 'filter_subject_example' # str | The immediate subject whose comments to return.
    include = ['author.albums'] # List[str] | Include related resources. Available relationships: author, commentSummary, owners, reactionSummary, rootSubject, subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'author.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums (optional)
    sort = ['sort_example'] # List[str] | Values prefixed with \"-\" are sorted descending; values without it are sorted ascending. (optional)

    try:
        # Get multiple comments.
        api_response = api_instance.comments_get(filter_subject, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media, sort=sort)
        print("The response of CommentsApi->comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_subject** | **str**| The immediate subject whose comments to return. | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: author, commentSummary, owners, reactionSummary, rootSubject, subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: author.albums | [optional] 
 **sort** | [**List[str]**](str.md)| Values prefixed with \&quot;-\&quot; are sorted descending; values without it are sorted ascending. | [optional] 

### Return type

[**CommentsMultiResourceDataDocument**](CommentsMultiResourceDataDocument.md)

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

# **comments_id_delete**
> MutationResponseDocument comments_id_delete(id, idempotency_key=idempotency_key)

Delete single comment.

Deletes existing comment.

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
    api_instance = tidal.CommentsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Comment Id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)

    try:
        # Delete single comment.
        api_response = api_instance.comments_id_delete(id, idempotency_key=idempotency_key)
        print("The response of CommentsApi->comments_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Comment Id | 
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

# **comments_id_get**
> CommentsSingleResourceDataDocument comments_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single comment.

Retrieves single comment by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.comments_single_resource_data_document import CommentsSingleResourceDataDocument
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
    api_instance = tidal.CommentsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Comment Id
    include = ['author.albums'] # List[str] | Include related resources. Available relationships: author, commentSummary, owners, reactionSummary, rootSubject, subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'author.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums (optional)

    try:
        # Get single comment.
        api_response = api_instance.comments_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of CommentsApi->comments_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Comment Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: author, commentSummary, owners, reactionSummary, rootSubject, subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: author.albums | [optional] 

### Return type

[**CommentsSingleResourceDataDocument**](CommentsSingleResourceDataDocument.md)

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

# **comments_id_patch**
> MutationResponseDocument comments_id_patch(id, idempotency_key=idempotency_key, comments_update_operation_payload=comments_update_operation_payload)

Update single comment.

Updates existing comment.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.comments_update_operation_payload import CommentsUpdateOperationPayload
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
    api_instance = tidal.CommentsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Comment Id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    comments_update_operation_payload = tidal.CommentsUpdateOperationPayload() # CommentsUpdateOperationPayload |  (optional)

    try:
        # Update single comment.
        api_response = api_instance.comments_id_patch(id, idempotency_key=idempotency_key, comments_update_operation_payload=comments_update_operation_payload)
        print("The response of CommentsApi->comments_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Comment Id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **comments_update_operation_payload** | [**CommentsUpdateOperationPayload**](CommentsUpdateOperationPayload.md)|  | [optional] 

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

# **comments_id_relationships_author_get**
> CommentsAuthorSingleRelationshipDataDocument comments_id_relationships_author_get(id, include=include, replace_media=replace_media)

Get author relationship (\"to-one\").

The artist who wrote the comment.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.comments_author_single_relationship_data_document import CommentsAuthorSingleRelationshipDataDocument
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
    api_instance = tidal.CommentsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Comment Id
    include = ['author.albums'] # List[str] | Include related resources. Available relationships: author (optional)
    replace_media = 'author.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: author.albums (optional)

    try:
        # Get author relationship (\"to-one\").
        api_response = api_instance.comments_id_relationships_author_get(id, include=include, replace_media=replace_media)
        print("The response of CommentsApi->comments_id_relationships_author_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_id_relationships_author_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Comment Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: author | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: author.albums | [optional] 

### Return type

[**CommentsAuthorSingleRelationshipDataDocument**](CommentsAuthorSingleRelationshipDataDocument.md)

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

# **comments_id_relationships_comment_summary_get**
> CommentsCommentSummarySingleRelationshipDataDocument comments_id_relationships_comment_summary_get(id, include=include)

Get commentSummary relationship (\"to-one\").

Retrieves commentSummary relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.comments_comment_summary_single_relationship_data_document import CommentsCommentSummarySingleRelationshipDataDocument
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
    api_instance = tidal.CommentsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Comment Id
    include = ['commentSummary'] # List[str] | Include related resources. Available relationships: commentSummary (optional)

    try:
        # Get commentSummary relationship (\"to-one\").
        api_response = api_instance.comments_id_relationships_comment_summary_get(id, include=include)
        print("The response of CommentsApi->comments_id_relationships_comment_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_id_relationships_comment_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Comment Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: commentSummary | [optional] 

### Return type

[**CommentsCommentSummarySingleRelationshipDataDocument**](CommentsCommentSummarySingleRelationshipDataDocument.md)

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

# **comments_id_relationships_owners_get**
> CommentsOwnersMultiRelationshipDataDocument comments_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.comments_owners_multi_relationship_data_document import CommentsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.CommentsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Comment Id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.comments_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of CommentsApi->comments_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Comment Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**CommentsOwnersMultiRelationshipDataDocument**](CommentsOwnersMultiRelationshipDataDocument.md)

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

# **comments_id_relationships_reaction_summary_get**
> CommentsReactionSummarySingleRelationshipDataDocument comments_id_relationships_reaction_summary_get(id, include=include)

Get reactionSummary relationship (\"to-one\").

Retrieves reactionSummary relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.comments_reaction_summary_single_relationship_data_document import CommentsReactionSummarySingleRelationshipDataDocument
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
    api_instance = tidal.CommentsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Comment Id
    include = ['reactionSummary'] # List[str] | Include related resources. Available relationships: reactionSummary (optional)

    try:
        # Get reactionSummary relationship (\"to-one\").
        api_response = api_instance.comments_id_relationships_reaction_summary_get(id, include=include)
        print("The response of CommentsApi->comments_id_relationships_reaction_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_id_relationships_reaction_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Comment Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: reactionSummary | [optional] 

### Return type

[**CommentsReactionSummarySingleRelationshipDataDocument**](CommentsReactionSummarySingleRelationshipDataDocument.md)

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

# **comments_id_relationships_root_subject_get**
> CommentsRootSubjectSingleRelationshipDataDocument comments_id_relationships_root_subject_get(id, include=include)

Get rootSubject relationship (\"to-one\").

Retrieves rootSubject relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.comments_root_subject_single_relationship_data_document import CommentsRootSubjectSingleRelationshipDataDocument
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
    api_instance = tidal.CommentsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Comment Id
    include = ['rootSubject'] # List[str] | Include related resources. Available relationships: rootSubject (optional)

    try:
        # Get rootSubject relationship (\"to-one\").
        api_response = api_instance.comments_id_relationships_root_subject_get(id, include=include)
        print("The response of CommentsApi->comments_id_relationships_root_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_id_relationships_root_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Comment Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: rootSubject | [optional] 

### Return type

[**CommentsRootSubjectSingleRelationshipDataDocument**](CommentsRootSubjectSingleRelationshipDataDocument.md)

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

# **comments_id_relationships_subject_get**
> CommentsSubjectSingleRelationshipDataDocument comments_id_relationships_subject_get(id, include=include, replace_media=replace_media)

Get subject relationship (\"to-one\").

Retrieves subject relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.comments_subject_single_relationship_data_document import CommentsSubjectSingleRelationshipDataDocument
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
    api_instance = tidal.CommentsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Comment Id
    include = ['subject.author.albums'] # List[str] | Include related resources. Available relationships: subject (optional)
    replace_media = 'subject.author.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.author.albums (optional)

    try:
        # Get subject relationship (\"to-one\").
        api_response = api_instance.comments_id_relationships_subject_get(id, include=include, replace_media=replace_media)
        print("The response of CommentsApi->comments_id_relationships_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_id_relationships_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Comment Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject.author.albums | [optional] 

### Return type

[**CommentsSubjectSingleRelationshipDataDocument**](CommentsSubjectSingleRelationshipDataDocument.md)

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

# **comments_post**
> CommentsCreateSingleResourceDataDocument comments_post(idempotency_key=idempotency_key, comments_create_operation_payload=comments_create_operation_payload)

Create single comment.

Creates a root comment on a resource or a reply whose subject is a root comment. Replies to replies are rejected.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.comments_create_operation_payload import CommentsCreateOperationPayload
from tidal.models.comments_create_single_resource_data_document import CommentsCreateSingleResourceDataDocument
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
    api_instance = tidal.CommentsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    comments_create_operation_payload = tidal.CommentsCreateOperationPayload() # CommentsCreateOperationPayload |  (optional)

    try:
        # Create single comment.
        api_response = api_instance.comments_post(idempotency_key=idempotency_key, comments_create_operation_payload=comments_create_operation_payload)
        print("The response of CommentsApi->comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **comments_create_operation_payload** | [**CommentsCreateOperationPayload**](CommentsCreateOperationPayload.md)|  | [optional] 

### Return type

[**CommentsCreateSingleResourceDataDocument**](CommentsCreateSingleResourceDataDocument.md)

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

