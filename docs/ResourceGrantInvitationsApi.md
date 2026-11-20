# tidal.ResourceGrantInvitationsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_grant_invitations_get**](ResourceGrantInvitationsApi.md#resource_grant_invitations_get) | **GET** /resourceGrantInvitations | Get multiple resourceGrantInvitations.
[**resource_grant_invitations_id_delete**](ResourceGrantInvitationsApi.md#resource_grant_invitations_id_delete) | **DELETE** /resourceGrantInvitations/{id} | Delete single resourceGrantInvitation.
[**resource_grant_invitations_id_get**](ResourceGrantInvitationsApi.md#resource_grant_invitations_id_get) | **GET** /resourceGrantInvitations/{id} | Get single resourceGrantInvitation.
[**resource_grant_invitations_id_patch**](ResourceGrantInvitationsApi.md#resource_grant_invitations_id_patch) | **PATCH** /resourceGrantInvitations/{id} | Update single resourceGrantInvitation.
[**resource_grant_invitations_id_relationships_owners_get**](ResourceGrantInvitationsApi.md#resource_grant_invitations_id_relationships_owners_get) | **GET** /resourceGrantInvitations/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**resource_grant_invitations_id_relationships_preview_grant_get**](ResourceGrantInvitationsApi.md#resource_grant_invitations_id_relationships_preview_grant_get) | **GET** /resourceGrantInvitations/{id}/relationships/previewGrant | Get previewGrant relationship (\&quot;to-one\&quot;).
[**resource_grant_invitations_id_relationships_subject_get**](ResourceGrantInvitationsApi.md#resource_grant_invitations_id_relationships_subject_get) | **GET** /resourceGrantInvitations/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
[**resource_grant_invitations_post**](ResourceGrantInvitationsApi.md#resource_grant_invitations_post) | **POST** /resourceGrantInvitations | Create single resourceGrantInvitation.


# **resource_grant_invitations_get**
> ResourceGrantInvitationsMultiResourceDataDocument resource_grant_invitations_get(filter_code=filter_code, filter_self_applies_to=filter_self_applies_to, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media)

Get multiple resourceGrantInvitations.

Retrieves multiple resourceGrantInvitations by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.resource_grant_invitations_multi_resource_data_document import ResourceGrantInvitationsMultiResourceDataDocument
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
    api_instance = tidal.ResourceGrantInvitationsApi(api_client)
    filter_code = 'filter_code_example' # str | Invitation code (e.g. `42179b73-6f0c-405c-b926-2fdb45363c44`) (optional)
    filter_self_applies_to = 'filter_self_applies_to_example' # str | Album, track or folder owned by the caller. Selects undeleted, unexpired invitations on the resource or its ancestors; used-up ones are included. Each keeps its own subject. Cannot be combined with other filters. Missing or non-owned resources and subjects without a live access node return no records. Ordered by expiry then ID; at most 20 invitations per page. Also accepts `folders:me`. (optional)
    include = ['previewGrant.subject'] # List[str] | Include related resources. Available relationships: owners, previewGrant, subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'previewGrant.subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: previewGrant.subject (optional)

    try:
        # Get multiple resourceGrantInvitations.
        api_response = api_instance.resource_grant_invitations_get(filter_code=filter_code, filter_self_applies_to=filter_self_applies_to, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of ResourceGrantInvitationsApi->resource_grant_invitations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantInvitationsApi->resource_grant_invitations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_code** | **str**| Invitation code (e.g. &#x60;42179b73-6f0c-405c-b926-2fdb45363c44&#x60;) | [optional] 
 **filter_self_applies_to** | **str**| Album, track or folder owned by the caller. Selects undeleted, unexpired invitations on the resource or its ancestors; used-up ones are included. Each keeps its own subject. Cannot be combined with other filters. Missing or non-owned resources and subjects without a live access node return no records. Ordered by expiry then ID; at most 20 invitations per page. Also accepts &#x60;folders:me&#x60;. | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners, previewGrant, subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: previewGrant.subject | [optional] 

### Return type

[**ResourceGrantInvitationsMultiResourceDataDocument**](ResourceGrantInvitationsMultiResourceDataDocument.md)

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

# **resource_grant_invitations_id_delete**
> MutationResponseDocument resource_grant_invitations_id_delete(id, idempotency_key=idempotency_key, revoke_grants=revoke_grants)

Delete single resourceGrantInvitation.

Delete the invitation, ending redemption and its preview.

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
    api_instance = tidal.ResourceGrantInvitationsApi(api_client)
    id = 'e0163a07-8eee-4d30-ae44-75d44b1e47b0' # str | Invitation id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    revoke_grants = True # bool | Also revoke the grants redemptions issued; access from other sources stays. Defaults to false. (optional)

    try:
        # Delete single resourceGrantInvitation.
        api_response = api_instance.resource_grant_invitations_id_delete(id, idempotency_key=idempotency_key, revoke_grants=revoke_grants)
        print("The response of ResourceGrantInvitationsApi->resource_grant_invitations_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantInvitationsApi->resource_grant_invitations_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Invitation id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **revoke_grants** | **bool**| Also revoke the grants redemptions issued; access from other sources stays. Defaults to false. | [optional] 

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

# **resource_grant_invitations_id_get**
> ResourceGrantInvitationsSingleResourceDataDocument resource_grant_invitations_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single resourceGrantInvitation.

Retrieves single resourceGrantInvitation by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.resource_grant_invitations_single_resource_data_document import ResourceGrantInvitationsSingleResourceDataDocument
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
    api_instance = tidal.ResourceGrantInvitationsApi(api_client)
    id = 'e0163a07-8eee-4d30-ae44-75d44b1e47b0' # str | Invitation id
    include = ['previewGrant.subject'] # List[str] | Include related resources. Available relationships: owners, previewGrant, subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'previewGrant.subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: previewGrant.subject (optional)

    try:
        # Get single resourceGrantInvitation.
        api_response = api_instance.resource_grant_invitations_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of ResourceGrantInvitationsApi->resource_grant_invitations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantInvitationsApi->resource_grant_invitations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Invitation id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners, previewGrant, subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: previewGrant.subject | [optional] 

### Return type

[**ResourceGrantInvitationsSingleResourceDataDocument**](ResourceGrantInvitationsSingleResourceDataDocument.md)

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

# **resource_grant_invitations_id_patch**
> ResourceGrantInvitationsUpdateSingleResourceDataDocument resource_grant_invitations_id_patch(id, idempotency_key=idempotency_key, resource_grant_invitations_update_operation_payload=resource_grant_invitations_update_operation_payload)

Update single resourceGrantInvitation.

Set, change or remove the password, or turn the preview on or off. Users who redeemed keep their grants.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.resource_grant_invitations_update_operation_payload import ResourceGrantInvitationsUpdateOperationPayload
from tidal.models.resource_grant_invitations_update_single_resource_data_document import ResourceGrantInvitationsUpdateSingleResourceDataDocument
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
    api_instance = tidal.ResourceGrantInvitationsApi(api_client)
    id = 'e0163a07-8eee-4d30-ae44-75d44b1e47b0' # str | Invitation id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    resource_grant_invitations_update_operation_payload = tidal.ResourceGrantInvitationsUpdateOperationPayload() # ResourceGrantInvitationsUpdateOperationPayload |  (optional)

    try:
        # Update single resourceGrantInvitation.
        api_response = api_instance.resource_grant_invitations_id_patch(id, idempotency_key=idempotency_key, resource_grant_invitations_update_operation_payload=resource_grant_invitations_update_operation_payload)
        print("The response of ResourceGrantInvitationsApi->resource_grant_invitations_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantInvitationsApi->resource_grant_invitations_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Invitation id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **resource_grant_invitations_update_operation_payload** | [**ResourceGrantInvitationsUpdateOperationPayload**](ResourceGrantInvitationsUpdateOperationPayload.md)|  | [optional] 

### Return type

[**ResourceGrantInvitationsUpdateSingleResourceDataDocument**](ResourceGrantInvitationsUpdateSingleResourceDataDocument.md)

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

# **resource_grant_invitations_id_relationships_owners_get**
> ResourceGrantInvitationsOwnersMultiRelationshipDataDocument resource_grant_invitations_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.resource_grant_invitations_owners_multi_relationship_data_document import ResourceGrantInvitationsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.ResourceGrantInvitationsApi(api_client)
    id = 'e0163a07-8eee-4d30-ae44-75d44b1e47b0' # str | Invitation id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.resource_grant_invitations_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of ResourceGrantInvitationsApi->resource_grant_invitations_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantInvitationsApi->resource_grant_invitations_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Invitation id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**ResourceGrantInvitationsOwnersMultiRelationshipDataDocument**](ResourceGrantInvitationsOwnersMultiRelationshipDataDocument.md)

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

# **resource_grant_invitations_id_relationships_preview_grant_get**
> ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument resource_grant_invitations_id_relationships_preview_grant_get(id, include=include, replace_media=replace_media)

Get previewGrant relationship (\"to-one\").

Retrieves previewGrant relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.resource_grant_invitations_preview_grant_single_relationship_data_document import ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument
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
    api_instance = tidal.ResourceGrantInvitationsApi(api_client)
    id = 'e0163a07-8eee-4d30-ae44-75d44b1e47b0' # str | Invitation id
    include = ['previewGrant.subject'] # List[str] | Include related resources. Available relationships: previewGrant (optional)
    replace_media = 'previewGrant.subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: previewGrant.subject (optional)

    try:
        # Get previewGrant relationship (\"to-one\").
        api_response = api_instance.resource_grant_invitations_id_relationships_preview_grant_get(id, include=include, replace_media=replace_media)
        print("The response of ResourceGrantInvitationsApi->resource_grant_invitations_id_relationships_preview_grant_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantInvitationsApi->resource_grant_invitations_id_relationships_preview_grant_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Invitation id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: previewGrant | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: previewGrant.subject | [optional] 

### Return type

[**ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument**](ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument.md)

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

# **resource_grant_invitations_id_relationships_subject_get**
> ResourceGrantInvitationsSubjectSingleRelationshipDataDocument resource_grant_invitations_id_relationships_subject_get(id, include=include, replace_media=replace_media)

Get subject relationship (\"to-one\").

Retrieves subject relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.resource_grant_invitations_subject_single_relationship_data_document import ResourceGrantInvitationsSubjectSingleRelationshipDataDocument
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
    api_instance = tidal.ResourceGrantInvitationsApi(api_client)
    id = 'e0163a07-8eee-4d30-ae44-75d44b1e47b0' # str | Invitation id
    include = ['subject'] # List[str] | Include related resources. Available relationships: subject (optional)
    replace_media = 'subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject (optional)

    try:
        # Get subject relationship (\"to-one\").
        api_response = api_instance.resource_grant_invitations_id_relationships_subject_get(id, include=include, replace_media=replace_media)
        print("The response of ResourceGrantInvitationsApi->resource_grant_invitations_id_relationships_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantInvitationsApi->resource_grant_invitations_id_relationships_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Invitation id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject | [optional] 

### Return type

[**ResourceGrantInvitationsSubjectSingleRelationshipDataDocument**](ResourceGrantInvitationsSubjectSingleRelationshipDataDocument.md)

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

# **resource_grant_invitations_post**
> ResourceGrantInvitationsCreateSingleResourceDataDocument resource_grant_invitations_post(idempotency_key=idempotency_key, resource_grant_invitations_create_operation_payload=resource_grant_invitations_create_operation_payload)

Create single resourceGrantInvitation.

Creates a new resourceGrantInvitation.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.resource_grant_invitations_create_operation_payload import ResourceGrantInvitationsCreateOperationPayload
from tidal.models.resource_grant_invitations_create_single_resource_data_document import ResourceGrantInvitationsCreateSingleResourceDataDocument
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
    api_instance = tidal.ResourceGrantInvitationsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    resource_grant_invitations_create_operation_payload = tidal.ResourceGrantInvitationsCreateOperationPayload() # ResourceGrantInvitationsCreateOperationPayload |  (optional)

    try:
        # Create single resourceGrantInvitation.
        api_response = api_instance.resource_grant_invitations_post(idempotency_key=idempotency_key, resource_grant_invitations_create_operation_payload=resource_grant_invitations_create_operation_payload)
        print("The response of ResourceGrantInvitationsApi->resource_grant_invitations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceGrantInvitationsApi->resource_grant_invitations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **resource_grant_invitations_create_operation_payload** | [**ResourceGrantInvitationsCreateOperationPayload**](ResourceGrantInvitationsCreateOperationPayload.md)|  | [optional] 

### Return type

[**ResourceGrantInvitationsCreateSingleResourceDataDocument**](ResourceGrantInvitationsCreateSingleResourceDataDocument.md)

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

