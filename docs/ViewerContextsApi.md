# tidal.ViewerContextsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**viewer_contexts_get**](ViewerContextsApi.md#viewer_contexts_get) | **GET** /viewerContexts | Get multiple viewerContexts.
[**viewer_contexts_id_get**](ViewerContextsApi.md#viewer_contexts_id_get) | **GET** /viewerContexts/{id} | Get single viewerContext.
[**viewer_contexts_id_relationships_comments_get**](ViewerContextsApi.md#viewer_contexts_id_relationships_comments_get) | **GET** /viewerContexts/{id}/relationships/comments | Get comments relationship (\&quot;to-many\&quot;).
[**viewer_contexts_id_relationships_reactions_get**](ViewerContextsApi.md#viewer_contexts_id_relationships_reactions_get) | **GET** /viewerContexts/{id}/relationships/reactions | Get reactions relationship (\&quot;to-many\&quot;).
[**viewer_contexts_id_relationships_subject_get**](ViewerContextsApi.md#viewer_contexts_id_relationships_subject_get) | **GET** /viewerContexts/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
[**viewer_contexts_id_relationships_viewer_get**](ViewerContextsApi.md#viewer_contexts_id_relationships_viewer_get) | **GET** /viewerContexts/{id}/relationships/viewer | Get viewer relationship (\&quot;to-one\&quot;).


# **viewer_contexts_get**
> ViewerContextsMultiResourceDataDocument viewer_contexts_get(filter_subject, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get multiple viewerContexts.

Returns viewer contexts for up to 20 original subjects. Duplicate subjects are returned once.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.viewer_contexts_multi_resource_data_document import ViewerContextsMultiResourceDataDocument
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
    api_instance = tidal.ViewerContextsApi(api_client)
    filter_subject = ['filter_subject_example'] # List[str] | Original subjects to look up. Also accepts `folders:me`.
    include = ['comments.author.albums'] # List[str] | Include related resources. Available relationships: comments, reactions, subject, viewer (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'comments.author.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: comments.author.albums (optional)

    try:
        # Get multiple viewerContexts.
        api_response = api_instance.viewer_contexts_get(filter_subject, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of ViewerContextsApi->viewer_contexts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewerContextsApi->viewer_contexts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_subject** | [**List[str]**](str.md)| Original subjects to look up. Also accepts &#x60;folders:me&#x60;. | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: comments, reactions, subject, viewer | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: comments.author.albums | [optional] 

### Return type

[**ViewerContextsMultiResourceDataDocument**](ViewerContextsMultiResourceDataDocument.md)

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

# **viewer_contexts_id_get**
> ViewerContextsSingleResourceDataDocument viewer_contexts_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single viewerContext.

Retrieves single viewerContext by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.viewer_contexts_single_resource_data_document import ViewerContextsSingleResourceDataDocument
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
    api_instance = tidal.ViewerContextsApi(api_client)
    id = 'id_example' # str | Opaque identifier of one authenticated viewer and original subject pair
    include = ['comments.author.albums'] # List[str] | Include related resources. Available relationships: comments, reactions, subject, viewer (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'comments.author.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: comments.author.albums (optional)

    try:
        # Get single viewerContext.
        api_response = api_instance.viewer_contexts_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of ViewerContextsApi->viewer_contexts_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewerContextsApi->viewer_contexts_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque identifier of one authenticated viewer and original subject pair | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: comments, reactions, subject, viewer | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: comments.author.albums | [optional] 

### Return type

[**ViewerContextsSingleResourceDataDocument**](ViewerContextsSingleResourceDataDocument.md)

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

# **viewer_contexts_id_relationships_comments_get**
> ViewerContextsCommentsMultiRelationshipDataDocument viewer_contexts_id_relationships_comments_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get comments relationship (\"to-many\").

Returns the viewer's comments on the subject.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.viewer_contexts_comments_multi_relationship_data_document import ViewerContextsCommentsMultiRelationshipDataDocument
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
    api_instance = tidal.ViewerContextsApi(api_client)
    id = 'id_example' # str | Opaque identifier of one authenticated viewer and original subject pair
    include = ['comments.author.albums'] # List[str] | Include related resources. Available relationships: comments (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'comments.author.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: comments.author.albums (optional)

    try:
        # Get comments relationship (\"to-many\").
        api_response = api_instance.viewer_contexts_id_relationships_comments_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of ViewerContextsApi->viewer_contexts_id_relationships_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewerContextsApi->viewer_contexts_id_relationships_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque identifier of one authenticated viewer and original subject pair | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: comments | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: comments.author.albums | [optional] 

### Return type

[**ViewerContextsCommentsMultiRelationshipDataDocument**](ViewerContextsCommentsMultiRelationshipDataDocument.md)

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

# **viewer_contexts_id_relationships_reactions_get**
> ViewerContextsReactionsMultiRelationshipDataDocument viewer_contexts_id_relationships_reactions_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get reactions relationship (\"to-many\").

Returns the viewer's reactions on the subject.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.viewer_contexts_reactions_multi_relationship_data_document import ViewerContextsReactionsMultiRelationshipDataDocument
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
    api_instance = tidal.ViewerContextsApi(api_client)
    id = 'id_example' # str | Opaque identifier of one authenticated viewer and original subject pair
    include = ['reactions.author.albums'] # List[str] | Include related resources. Available relationships: reactions (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'reactions.author.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: reactions.author.albums (optional)

    try:
        # Get reactions relationship (\"to-many\").
        api_response = api_instance.viewer_contexts_id_relationships_reactions_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of ViewerContextsApi->viewer_contexts_id_relationships_reactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewerContextsApi->viewer_contexts_id_relationships_reactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque identifier of one authenticated viewer and original subject pair | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: reactions | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: reactions.author.albums | [optional] 

### Return type

[**ViewerContextsReactionsMultiRelationshipDataDocument**](ViewerContextsReactionsMultiRelationshipDataDocument.md)

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

# **viewer_contexts_id_relationships_subject_get**
> ViewerContextsSubjectSingleRelationshipDataDocument viewer_contexts_id_relationships_subject_get(id, include=include, replace_media=replace_media)

Get subject relationship (\"to-one\").

Returns the subject of this viewer context.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.viewer_contexts_subject_single_relationship_data_document import ViewerContextsSubjectSingleRelationshipDataDocument
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
    api_instance = tidal.ViewerContextsApi(api_client)
    id = 'id_example' # str | Opaque identifier of one authenticated viewer and original subject pair
    include = ['subject'] # List[str] | Include related resources. Available relationships: subject (optional)
    replace_media = 'subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject (optional)

    try:
        # Get subject relationship (\"to-one\").
        api_response = api_instance.viewer_contexts_id_relationships_subject_get(id, include=include, replace_media=replace_media)
        print("The response of ViewerContextsApi->viewer_contexts_id_relationships_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewerContextsApi->viewer_contexts_id_relationships_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque identifier of one authenticated viewer and original subject pair | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject | [optional] 

### Return type

[**ViewerContextsSubjectSingleRelationshipDataDocument**](ViewerContextsSubjectSingleRelationshipDataDocument.md)

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

# **viewer_contexts_id_relationships_viewer_get**
> ViewerContextsViewerSingleRelationshipDataDocument viewer_contexts_id_relationships_viewer_get(id, include=include, replace_media=replace_media)

Get viewer relationship (\"to-one\").

Returns the authenticated viewer of this context.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.viewer_contexts_viewer_single_relationship_data_document import ViewerContextsViewerSingleRelationshipDataDocument
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
    api_instance = tidal.ViewerContextsApi(api_client)
    id = 'id_example' # str | Opaque identifier of one authenticated viewer and original subject pair
    include = ['viewer.artist.albums'] # List[str] | Include related resources. Available relationships: viewer (optional)
    replace_media = 'viewer.artist.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: viewer.artist.albums (optional)

    try:
        # Get viewer relationship (\"to-one\").
        api_response = api_instance.viewer_contexts_id_relationships_viewer_get(id, include=include, replace_media=replace_media)
        print("The response of ViewerContextsApi->viewer_contexts_id_relationships_viewer_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewerContextsApi->viewer_contexts_id_relationships_viewer_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque identifier of one authenticated viewer and original subject pair | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: viewer | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: viewer.artist.albums | [optional] 

### Return type

[**ViewerContextsViewerSingleRelationshipDataDocument**](ViewerContextsViewerSingleRelationshipDataDocument.md)

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

