# tidal.TrackSourceFilesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**track_source_files_id_get**](TrackSourceFilesApi.md#track_source_files_id_get) | **GET** /trackSourceFiles/{id} | Get single trackSourceFile.
[**track_source_files_id_relationships_comment_summary_get**](TrackSourceFilesApi.md#track_source_files_id_relationships_comment_summary_get) | **GET** /trackSourceFiles/{id}/relationships/commentSummary | Get commentSummary relationship (\&quot;to-one\&quot;).
[**track_source_files_id_relationships_owners_get**](TrackSourceFilesApi.md#track_source_files_id_relationships_owners_get) | **GET** /trackSourceFiles/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**track_source_files_id_relationships_reaction_summary_get**](TrackSourceFilesApi.md#track_source_files_id_relationships_reaction_summary_get) | **GET** /trackSourceFiles/{id}/relationships/reactionSummary | Get reactionSummary relationship (\&quot;to-one\&quot;).
[**track_source_files_post**](TrackSourceFilesApi.md#track_source_files_post) | **POST** /trackSourceFiles | Create single trackSourceFile.


# **track_source_files_id_get**
> TrackSourceFilesSingleResourceDataDocument track_source_files_id_get(id, include=include, include_linkage=include_linkage, share_code=share_code)

Get single trackSourceFile.

Retrieves single trackSourceFile by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.track_source_files_single_resource_data_document import TrackSourceFilesSingleResourceDataDocument
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
    api_instance = tidal.TrackSourceFilesApi(api_client)
    id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11' # str | Track source file id
    include = ['commentSummary'] # List[str] | Include related resources. Available relationships: commentSummary, owners, reactionSummary (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get single trackSourceFile.
        api_response = api_instance.track_source_files_id_get(id, include=include, include_linkage=include_linkage, share_code=share_code)
        print("The response of TrackSourceFilesApi->track_source_files_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackSourceFilesApi->track_source_files_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track source file id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: commentSummary, owners, reactionSummary | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TrackSourceFilesSingleResourceDataDocument**](TrackSourceFilesSingleResourceDataDocument.md)

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

# **track_source_files_id_relationships_comment_summary_get**
> TrackSourceFilesCommentSummarySingleRelationshipDataDocument track_source_files_id_relationships_comment_summary_get(id, include=include, share_code=share_code)

Get commentSummary relationship (\"to-one\").

Retrieves commentSummary relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.track_source_files_comment_summary_single_relationship_data_document import TrackSourceFilesCommentSummarySingleRelationshipDataDocument
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
    api_instance = tidal.TrackSourceFilesApi(api_client)
    id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11' # str | Track source file id
    include = ['commentSummary'] # List[str] | Include related resources. Available relationships: commentSummary (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get commentSummary relationship (\"to-one\").
        api_response = api_instance.track_source_files_id_relationships_comment_summary_get(id, include=include, share_code=share_code)
        print("The response of TrackSourceFilesApi->track_source_files_id_relationships_comment_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackSourceFilesApi->track_source_files_id_relationships_comment_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track source file id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: commentSummary | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TrackSourceFilesCommentSummarySingleRelationshipDataDocument**](TrackSourceFilesCommentSummarySingleRelationshipDataDocument.md)

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

# **track_source_files_id_relationships_owners_get**
> TrackSourceFilesOwnersMultiRelationshipDataDocument track_source_files_id_relationships_owners_get(id, include=include, page_cursor=page_cursor, share_code=share_code)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.track_source_files_owners_multi_relationship_data_document import TrackSourceFilesOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.TrackSourceFilesApi(api_client)
    id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11' # str | Track source file id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.track_source_files_id_relationships_owners_get(id, include=include, page_cursor=page_cursor, share_code=share_code)
        print("The response of TrackSourceFilesApi->track_source_files_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackSourceFilesApi->track_source_files_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track source file id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TrackSourceFilesOwnersMultiRelationshipDataDocument**](TrackSourceFilesOwnersMultiRelationshipDataDocument.md)

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

# **track_source_files_id_relationships_reaction_summary_get**
> TrackSourceFilesReactionSummarySingleRelationshipDataDocument track_source_files_id_relationships_reaction_summary_get(id, include=include, share_code=share_code)

Get reactionSummary relationship (\"to-one\").

Retrieves reactionSummary relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.track_source_files_reaction_summary_single_relationship_data_document import TrackSourceFilesReactionSummarySingleRelationshipDataDocument
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
    api_instance = tidal.TrackSourceFilesApi(api_client)
    id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11' # str | Track source file id
    include = ['reactionSummary'] # List[str] | Include related resources. Available relationships: reactionSummary (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get reactionSummary relationship (\"to-one\").
        api_response = api_instance.track_source_files_id_relationships_reaction_summary_get(id, include=include, share_code=share_code)
        print("The response of TrackSourceFilesApi->track_source_files_id_relationships_reaction_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackSourceFilesApi->track_source_files_id_relationships_reaction_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Track source file id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: reactionSummary | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**TrackSourceFilesReactionSummarySingleRelationshipDataDocument**](TrackSourceFilesReactionSummarySingleRelationshipDataDocument.md)

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

# **track_source_files_post**
> TrackSourceFilesCreateSingleResourceDataDocument track_source_files_post(idempotency_key=idempotency_key, track_source_files_create_operation_payload=track_source_files_create_operation_payload)

Create single trackSourceFile.

Create a track source file. <p/>
The response contains a upload link that must be used to upload the actual content.<p/>
The headers in the upload link response must be sent doing the actual upload.


### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.track_source_files_create_operation_payload import TrackSourceFilesCreateOperationPayload
from tidal.models.track_source_files_create_single_resource_data_document import TrackSourceFilesCreateSingleResourceDataDocument
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
    api_instance = tidal.TrackSourceFilesApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    track_source_files_create_operation_payload = tidal.TrackSourceFilesCreateOperationPayload() # TrackSourceFilesCreateOperationPayload |  (optional)

    try:
        # Create single trackSourceFile.
        api_response = api_instance.track_source_files_post(idempotency_key=idempotency_key, track_source_files_create_operation_payload=track_source_files_create_operation_payload)
        print("The response of TrackSourceFilesApi->track_source_files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackSourceFilesApi->track_source_files_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **track_source_files_create_operation_payload** | [**TrackSourceFilesCreateOperationPayload**](TrackSourceFilesCreateOperationPayload.md)|  | [optional] 

### Return type

[**TrackSourceFilesCreateSingleResourceDataDocument**](TrackSourceFilesCreateSingleResourceDataDocument.md)

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

