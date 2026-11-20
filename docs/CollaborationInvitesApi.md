# tidal.CollaborationInvitesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collaboration_invites_get**](CollaborationInvitesApi.md#collaboration_invites_get) | **GET** /collaborationInvites | Get multiple collaborationInvites.
[**collaboration_invites_id_delete**](CollaborationInvitesApi.md#collaboration_invites_id_delete) | **DELETE** /collaborationInvites/{id} | Delete single collaborationInvite.
[**collaboration_invites_id_get**](CollaborationInvitesApi.md#collaboration_invites_id_get) | **GET** /collaborationInvites/{id} | Get single collaborationInvite.
[**collaboration_invites_id_relationships_owners_get**](CollaborationInvitesApi.md#collaboration_invites_id_relationships_owners_get) | **GET** /collaborationInvites/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**collaboration_invites_id_relationships_subject_get**](CollaborationInvitesApi.md#collaboration_invites_id_relationships_subject_get) | **GET** /collaborationInvites/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
[**collaboration_invites_post**](CollaborationInvitesApi.md#collaboration_invites_post) | **POST** /collaborationInvites | Create single collaborationInvite.


# **collaboration_invites_get**
> CollaborationInvitesMultiResourceDataDocument collaboration_invites_get(filter_code, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get multiple collaborationInvites.

Retrieves multiple collaborationInvites by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.collaboration_invites_multi_resource_data_document import CollaborationInvitesMultiResourceDataDocument
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
    api_instance = tidal.CollaborationInvitesApi(api_client)
    filter_code = ['filter_code_example'] # List[str] | Invite code
    include = ['subject.items'] # List[str] | Include related resources. Available relationships: owners, subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'subject.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.items (optional)

    try:
        # Get multiple collaborationInvites.
        api_response = api_instance.collaboration_invites_get(filter_code, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of CollaborationInvitesApi->collaboration_invites_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationInvitesApi->collaboration_invites_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_code** | [**List[str]**](str.md)| Invite code | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners, subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject.items | [optional] 

### Return type

[**CollaborationInvitesMultiResourceDataDocument**](CollaborationInvitesMultiResourceDataDocument.md)

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

# **collaboration_invites_id_delete**
> MutationResponseDocument collaboration_invites_id_delete(id, idempotency_key=idempotency_key)

Delete single collaborationInvite.

Deletes existing collaborationInvite.

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
    api_instance = tidal.CollaborationInvitesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Collaboration invite id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)

    try:
        # Delete single collaborationInvite.
        api_response = api_instance.collaboration_invites_id_delete(id, idempotency_key=idempotency_key)
        print("The response of CollaborationInvitesApi->collaboration_invites_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationInvitesApi->collaboration_invites_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collaboration invite id | 
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

# **collaboration_invites_id_get**
> CollaborationInvitesSingleResourceDataDocument collaboration_invites_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single collaborationInvite.

Retrieves single collaborationInvite by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.collaboration_invites_single_resource_data_document import CollaborationInvitesSingleResourceDataDocument
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
    api_instance = tidal.CollaborationInvitesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Collaboration invite id
    include = ['subject.items'] # List[str] | Include related resources. Available relationships: owners, subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'subject.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.items (optional)

    try:
        # Get single collaborationInvite.
        api_response = api_instance.collaboration_invites_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of CollaborationInvitesApi->collaboration_invites_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationInvitesApi->collaboration_invites_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collaboration invite id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners, subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject.items | [optional] 

### Return type

[**CollaborationInvitesSingleResourceDataDocument**](CollaborationInvitesSingleResourceDataDocument.md)

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

# **collaboration_invites_id_relationships_owners_get**
> CollaborationInvitesOwnersMultiRelationshipDataDocument collaboration_invites_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.collaboration_invites_owners_multi_relationship_data_document import CollaborationInvitesOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.CollaborationInvitesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Collaboration invite id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.collaboration_invites_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of CollaborationInvitesApi->collaboration_invites_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationInvitesApi->collaboration_invites_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collaboration invite id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**CollaborationInvitesOwnersMultiRelationshipDataDocument**](CollaborationInvitesOwnersMultiRelationshipDataDocument.md)

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

# **collaboration_invites_id_relationships_subject_get**
> CollaborationInvitesSubjectSingleRelationshipDataDocument collaboration_invites_id_relationships_subject_get(id, include=include, replace_media=replace_media)

Get subject relationship (\"to-one\").

Retrieves subject relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.collaboration_invites_subject_single_relationship_data_document import CollaborationInvitesSubjectSingleRelationshipDataDocument
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
    api_instance = tidal.CollaborationInvitesApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Collaboration invite id
    include = ['subject.items'] # List[str] | Include related resources. Available relationships: subject (optional)
    replace_media = 'subject.items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.items (optional)

    try:
        # Get subject relationship (\"to-one\").
        api_response = api_instance.collaboration_invites_id_relationships_subject_get(id, include=include, replace_media=replace_media)
        print("The response of CollaborationInvitesApi->collaboration_invites_id_relationships_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationInvitesApi->collaboration_invites_id_relationships_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collaboration invite id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject.items | [optional] 

### Return type

[**CollaborationInvitesSubjectSingleRelationshipDataDocument**](CollaborationInvitesSubjectSingleRelationshipDataDocument.md)

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

# **collaboration_invites_post**
> CollaborationInvitesCreateSingleResourceDataDocument collaboration_invites_post(idempotency_key=idempotency_key, collaboration_invites_create_operation_payload=collaboration_invites_create_operation_payload)

Create single collaborationInvite.

Creates a new collaborationInvite.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.collaboration_invites_create_operation_payload import CollaborationInvitesCreateOperationPayload
from tidal.models.collaboration_invites_create_single_resource_data_document import CollaborationInvitesCreateSingleResourceDataDocument
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
    api_instance = tidal.CollaborationInvitesApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    collaboration_invites_create_operation_payload = tidal.CollaborationInvitesCreateOperationPayload() # CollaborationInvitesCreateOperationPayload |  (optional)

    try:
        # Create single collaborationInvite.
        api_response = api_instance.collaboration_invites_post(idempotency_key=idempotency_key, collaboration_invites_create_operation_payload=collaboration_invites_create_operation_payload)
        print("The response of CollaborationInvitesApi->collaboration_invites_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationInvitesApi->collaboration_invites_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **collaboration_invites_create_operation_payload** | [**CollaborationInvitesCreateOperationPayload**](CollaborationInvitesCreateOperationPayload.md)|  | [optional] 

### Return type

[**CollaborationInvitesCreateSingleResourceDataDocument**](CollaborationInvitesCreateSingleResourceDataDocument.md)

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

