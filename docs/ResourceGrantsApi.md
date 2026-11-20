# tidal.ResourceGrantsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_grants_get**](ResourceGrantsApi.md#resource_grants_get) | **GET** /resourceGrants | Get multiple resourceGrants.
[**resource_grants_id_delete**](ResourceGrantsApi.md#resource_grants_id_delete) | **DELETE** /resourceGrants/{id} | Delete single resourceGrant.
[**resource_grants_id_get**](ResourceGrantsApi.md#resource_grants_id_get) | **GET** /resourceGrants/{id} | Get single resourceGrant.
[**resource_grants_id_patch**](ResourceGrantsApi.md#resource_grants_id_patch) | **PATCH** /resourceGrants/{id} | Update single resourceGrant.
[**resource_grants_id_relationships_grantee_get**](ResourceGrantsApi.md#resource_grants_id_relationships_grantee_get) | **GET** /resourceGrants/{id}/relationships/grantee | Get grantee relationship (\&quot;to-one\&quot;).
[**resource_grants_id_relationships_invitation_get**](ResourceGrantsApi.md#resource_grants_id_relationships_invitation_get) | **GET** /resourceGrants/{id}/relationships/invitation | Get invitation relationship (\&quot;to-one\&quot;).
[**resource_grants_id_relationships_subject_get**](ResourceGrantsApi.md#resource_grants_id_relationships_subject_get) | **GET** /resourceGrants/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
[**resource_grants_post**](ResourceGrantsApi.md#resource_grants_post) | **POST** /resourceGrants | Create single resourceGrant.


# **resource_grants_get**
> ResourceGrantsMultiResourceDataDocument resource_grants_get(filter_grantee=filter_grantee, filter_role=filter_role, filter_self_applies_to=filter_self_applies_to, filter_subject=filter_subject, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media)

Get multiple resourceGrants.

Retrieves multiple resourceGrants by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.resource_grants_multi_resource_data_document import ResourceGrantsMultiResourceDataDocument
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
    api_instance = tidal.ResourceGrantsApi(api_client)
    filter_grantee = 'filter_grantee_example' # str | Filter by grantee. Use `groups:everyone` for the Everyone group. Also accepts `users:me`. (optional)
    filter_role = 'filter_role_example' # str | One of: VIEWER, COLLABORATOR, OWNER (e.g. `VIEWER`) (optional)
    filter_self_applies_to = 'filter_self_applies_to_example' # str | Album, track or folder whose grants are listed, including those on its ancestor folders and albums. Each grant keeps the subject it is stored on. Also accepts `folders:me`. (optional)
    filter_subject = 'filter_subject_example' # str | Filter by subject. Required unless `filter[self][appliesTo]` is used. The subject's owner reads all its grants; other callers read only grants made directly to them. Also accepts `folders:me`. (optional)
    include = ['grantee.artist.albums'] # List[str] | Include related resources. Available relationships: grantee, invitation, subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'grantee.artist.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: grantee.artist.albums (optional)

    try:
        # Get multiple resourceGrants.
        api_response = api_instance.resource_grants_get(filter_grantee=filter_grantee, filter_role=filter_role, filter_self_applies_to=filter_self_applies_to, filter_subject=filter_subject, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of ResourceGrantsApi->resource_grants_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantsApi->resource_grants_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_grantee** | **str**| Filter by grantee. Use &#x60;groups:everyone&#x60; for the Everyone group. Also accepts &#x60;users:me&#x60;. | [optional] 
 **filter_role** | **str**| One of: VIEWER, COLLABORATOR, OWNER (e.g. &#x60;VIEWER&#x60;) | [optional] 
 **filter_self_applies_to** | **str**| Album, track or folder whose grants are listed, including those on its ancestor folders and albums. Each grant keeps the subject it is stored on. Also accepts &#x60;folders:me&#x60;. | [optional] 
 **filter_subject** | **str**| Filter by subject. Required unless &#x60;filter[self][appliesTo]&#x60; is used. The subject&#39;s owner reads all its grants; other callers read only grants made directly to them. Also accepts &#x60;folders:me&#x60;. | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: grantee, invitation, subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: grantee.artist.albums | [optional] 

### Return type

[**ResourceGrantsMultiResourceDataDocument**](ResourceGrantsMultiResourceDataDocument.md)

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

# **resource_grants_id_delete**
> MutationResponseDocument resource_grants_id_delete(id, idempotency_key=idempotency_key)

Delete single resourceGrant.

Deletes existing resourceGrant.

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
    api_instance = tidal.ResourceGrantsApi(api_client)
    id = 'id_example' # str | Opaque resource grant ID
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)

    try:
        # Delete single resourceGrant.
        api_response = api_instance.resource_grants_id_delete(id, idempotency_key=idempotency_key)
        print("The response of ResourceGrantsApi->resource_grants_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantsApi->resource_grants_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque resource grant ID | 
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

# **resource_grants_id_get**
> ResourceGrantsSingleResourceDataDocument resource_grants_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single resourceGrant.

Retrieves single resourceGrant by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.resource_grants_single_resource_data_document import ResourceGrantsSingleResourceDataDocument
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
    api_instance = tidal.ResourceGrantsApi(api_client)
    id = 'id_example' # str | Opaque resource grant ID
    include = ['grantee.artist.albums'] # List[str] | Include related resources. Available relationships: grantee, invitation, subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'grantee.artist.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: grantee.artist.albums (optional)

    try:
        # Get single resourceGrant.
        api_response = api_instance.resource_grants_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of ResourceGrantsApi->resource_grants_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantsApi->resource_grants_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque resource grant ID | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: grantee, invitation, subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: grantee.artist.albums | [optional] 

### Return type

[**ResourceGrantsSingleResourceDataDocument**](ResourceGrantsSingleResourceDataDocument.md)

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

# **resource_grants_id_patch**
> ResourceGrantsUpdateSingleResourceDataDocument resource_grants_id_patch(id, idempotency_key=idempotency_key, resource_grants_update_operation_payload=resource_grants_update_operation_payload)

Update single resourceGrant.

Updates existing resourceGrant.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.resource_grants_update_operation_payload import ResourceGrantsUpdateOperationPayload
from tidal.models.resource_grants_update_single_resource_data_document import ResourceGrantsUpdateSingleResourceDataDocument
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
    api_instance = tidal.ResourceGrantsApi(api_client)
    id = 'id_example' # str | Opaque resource grant ID
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    resource_grants_update_operation_payload = tidal.ResourceGrantsUpdateOperationPayload() # ResourceGrantsUpdateOperationPayload |  (optional)

    try:
        # Update single resourceGrant.
        api_response = api_instance.resource_grants_id_patch(id, idempotency_key=idempotency_key, resource_grants_update_operation_payload=resource_grants_update_operation_payload)
        print("The response of ResourceGrantsApi->resource_grants_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantsApi->resource_grants_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque resource grant ID | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **resource_grants_update_operation_payload** | [**ResourceGrantsUpdateOperationPayload**](ResourceGrantsUpdateOperationPayload.md)|  | [optional] 

### Return type

[**ResourceGrantsUpdateSingleResourceDataDocument**](ResourceGrantsUpdateSingleResourceDataDocument.md)

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

# **resource_grants_id_relationships_grantee_get**
> ResourceGrantsGranteeSingleRelationshipDataDocument resource_grants_id_relationships_grantee_get(id, include=include, replace_media=replace_media)

Get grantee relationship (\"to-one\").

Retrieves grantee relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.resource_grants_grantee_single_relationship_data_document import ResourceGrantsGranteeSingleRelationshipDataDocument
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
    api_instance = tidal.ResourceGrantsApi(api_client)
    id = 'id_example' # str | Opaque resource grant ID
    include = ['grantee.artist.albums'] # List[str] | Include related resources. Available relationships: grantee (optional)
    replace_media = 'grantee.artist.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: grantee.artist.albums (optional)

    try:
        # Get grantee relationship (\"to-one\").
        api_response = api_instance.resource_grants_id_relationships_grantee_get(id, include=include, replace_media=replace_media)
        print("The response of ResourceGrantsApi->resource_grants_id_relationships_grantee_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantsApi->resource_grants_id_relationships_grantee_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque resource grant ID | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: grantee | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: grantee.artist.albums | [optional] 

### Return type

[**ResourceGrantsGranteeSingleRelationshipDataDocument**](ResourceGrantsGranteeSingleRelationshipDataDocument.md)

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

# **resource_grants_id_relationships_invitation_get**
> ResourceGrantsInvitationSingleRelationshipDataDocument resource_grants_id_relationships_invitation_get(id, include=include, replace_media=replace_media)

Get invitation relationship (\"to-one\").

Retrieves invitation relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.resource_grants_invitation_single_relationship_data_document import ResourceGrantsInvitationSingleRelationshipDataDocument
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
    api_instance = tidal.ResourceGrantsApi(api_client)
    id = 'id_example' # str | Opaque resource grant ID
    include = ['invitation.subject'] # List[str] | Include related resources. Available relationships: invitation (optional)
    replace_media = 'invitation.subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: invitation.subject (optional)

    try:
        # Get invitation relationship (\"to-one\").
        api_response = api_instance.resource_grants_id_relationships_invitation_get(id, include=include, replace_media=replace_media)
        print("The response of ResourceGrantsApi->resource_grants_id_relationships_invitation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantsApi->resource_grants_id_relationships_invitation_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque resource grant ID | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: invitation | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: invitation.subject | [optional] 

### Return type

[**ResourceGrantsInvitationSingleRelationshipDataDocument**](ResourceGrantsInvitationSingleRelationshipDataDocument.md)

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

# **resource_grants_id_relationships_subject_get**
> ResourceGrantsSubjectSingleRelationshipDataDocument resource_grants_id_relationships_subject_get(id, include=include, replace_media=replace_media)

Get subject relationship (\"to-one\").

Retrieves subject relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.resource_grants_subject_single_relationship_data_document import ResourceGrantsSubjectSingleRelationshipDataDocument
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
    api_instance = tidal.ResourceGrantsApi(api_client)
    id = 'id_example' # str | Opaque resource grant ID
    include = ['subject'] # List[str] | Include related resources. Available relationships: subject (optional)
    replace_media = 'subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject (optional)

    try:
        # Get subject relationship (\"to-one\").
        api_response = api_instance.resource_grants_id_relationships_subject_get(id, include=include, replace_media=replace_media)
        print("The response of ResourceGrantsApi->resource_grants_id_relationships_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantsApi->resource_grants_id_relationships_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque resource grant ID | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject | [optional] 

### Return type

[**ResourceGrantsSubjectSingleRelationshipDataDocument**](ResourceGrantsSubjectSingleRelationshipDataDocument.md)

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

# **resource_grants_post**
> ResourceGrantsCreateSingleResourceDataDocument resource_grants_post(idempotency_key=idempotency_key, resource_grants_create_operation_payload=resource_grants_create_operation_payload)

Create single resourceGrant.

Create a direct grant from `role`, `subject` and `grantee`. Alternatively, redeem an invitation with only the `invitation` relationship: the caller receives the invitation's role on its subject, and the response is the caller's grant. Redeeming again returns the same grant. Every redemption, repeated ones included, needs a password-protected invitation's password and counts as a use of a limited invitation; password attempts are rate limited. The invitation's creator cannot redeem it.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.resource_grants_create_operation_payload import ResourceGrantsCreateOperationPayload
from tidal.models.resource_grants_create_single_resource_data_document import ResourceGrantsCreateSingleResourceDataDocument
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
    api_instance = tidal.ResourceGrantsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    resource_grants_create_operation_payload = tidal.ResourceGrantsCreateOperationPayload() # ResourceGrantsCreateOperationPayload |  (optional)

    try:
        # Create single resourceGrant.
        api_response = api_instance.resource_grants_post(idempotency_key=idempotency_key, resource_grants_create_operation_payload=resource_grants_create_operation_payload)
        print("The response of ResourceGrantsApi->resource_grants_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantsApi->resource_grants_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **resource_grants_create_operation_payload** | [**ResourceGrantsCreateOperationPayload**](ResourceGrantsCreateOperationPayload.md)|  | [optional] 

### Return type

[**ResourceGrantsCreateSingleResourceDataDocument**](ResourceGrantsCreateSingleResourceDataDocument.md)

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
**403** | This invitation can no longer be accepted; The invitation is password protected; send its password; The invitation password is incorrect |  -  |
**404** | Resource not found |  -  |
**405** | HTTP method not allowed |  -  |
**406** | No acceptable response media type |  -  |
**409** | Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Too many invitation password attempts; try again later |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

