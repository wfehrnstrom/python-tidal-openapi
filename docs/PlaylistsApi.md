# tidal.PlaylistsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playlists_get**](PlaylistsApi.md#playlists_get) | **GET** /playlists | Get multiple playlists.
[**playlists_id_delete**](PlaylistsApi.md#playlists_id_delete) | **DELETE** /playlists/{id} | Delete single playlist.
[**playlists_id_get**](PlaylistsApi.md#playlists_id_get) | **GET** /playlists/{id} | Get single playlist.
[**playlists_id_patch**](PlaylistsApi.md#playlists_id_patch) | **PATCH** /playlists/{id} | Update single playlist.
[**playlists_id_relationships_collaborator_profiles_delete**](PlaylistsApi.md#playlists_id_relationships_collaborator_profiles_delete) | **DELETE** /playlists/{id}/relationships/collaboratorProfiles | Delete from collaboratorProfiles relationship (\&quot;to-many\&quot;).
[**playlists_id_relationships_collaborator_profiles_get**](PlaylistsApi.md#playlists_id_relationships_collaborator_profiles_get) | **GET** /playlists/{id}/relationships/collaboratorProfiles | Get collaboratorProfiles relationship (\&quot;to-many\&quot;).
[**playlists_id_relationships_collaborators_get**](PlaylistsApi.md#playlists_id_relationships_collaborators_get) | **GET** /playlists/{id}/relationships/collaborators | Get collaborators relationship (\&quot;to-many\&quot;).
[**playlists_id_relationships_cover_art_get**](PlaylistsApi.md#playlists_id_relationships_cover_art_get) | **GET** /playlists/{id}/relationships/coverArt | Get coverArt relationship (\&quot;to-many\&quot;).
[**playlists_id_relationships_cover_art_patch**](PlaylistsApi.md#playlists_id_relationships_cover_art_patch) | **PATCH** /playlists/{id}/relationships/coverArt | Update coverArt relationship (\&quot;to-many\&quot;).
[**playlists_id_relationships_curators_get**](PlaylistsApi.md#playlists_id_relationships_curators_get) | **GET** /playlists/{id}/relationships/curators | Get curators relationship (\&quot;to-many\&quot;).
[**playlists_id_relationships_items_delete**](PlaylistsApi.md#playlists_id_relationships_items_delete) | **DELETE** /playlists/{id}/relationships/items | Delete from items relationship (\&quot;to-many\&quot;).
[**playlists_id_relationships_items_get**](PlaylistsApi.md#playlists_id_relationships_items_get) | **GET** /playlists/{id}/relationships/items | Get items relationship (\&quot;to-many\&quot;).
[**playlists_id_relationships_items_patch**](PlaylistsApi.md#playlists_id_relationships_items_patch) | **PATCH** /playlists/{id}/relationships/items | Update items relationship (\&quot;to-many\&quot;).
[**playlists_id_relationships_items_post**](PlaylistsApi.md#playlists_id_relationships_items_post) | **POST** /playlists/{id}/relationships/items | Add to items relationship (\&quot;to-many\&quot;).
[**playlists_id_relationships_owner_profiles_get**](PlaylistsApi.md#playlists_id_relationships_owner_profiles_get) | **GET** /playlists/{id}/relationships/ownerProfiles | Get ownerProfiles relationship (\&quot;to-many\&quot;).
[**playlists_id_relationships_owners_get**](PlaylistsApi.md#playlists_id_relationships_owners_get) | **GET** /playlists/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**playlists_id_relationships_suggested_cover_arts_get**](PlaylistsApi.md#playlists_id_relationships_suggested_cover_arts_get) | **GET** /playlists/{id}/relationships/suggestedCoverArts | Get suggestedCoverArts relationship (\&quot;to-many\&quot;).
[**playlists_post**](PlaylistsApi.md#playlists_post) | **POST** /playlists | Create single playlist.


# **playlists_get**
> PlaylistsMultiResourceDataDocument playlists_get(country_code=country_code, filter_collaborators_id=filter_collaborators_id, filter_id=filter_id, filter_owners_id=filter_owners_id, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media, sort=sort)

Get multiple playlists.

Retrieves multiple playlists by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.playlists_multi_resource_data_document import PlaylistsMultiResourceDataDocument
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
    api_instance = tidal.PlaylistsApi(api_client)
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    filter_collaborators_id = ['filter_collaborators_id_example'] # List[str] | User id. Also accepts `me`. (optional)
    filter_id = ['filter_id_example'] # List[str] | List of playlist IDs (e.g. `550e8400-e29b-41d4-a716-446655440000`) (optional)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`. (optional)
    include = ['curators.albums'] # List[str] | Include related resources. Available relationships: collaboratorProfiles, collaborators, coverArt, curators, items, ownerProfiles, owners, suggestedCoverArts (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'curators.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: curators.albums (optional)
    sort = ['sort_example'] # List[str] | Values prefixed with \"-\" are sorted descending; values without it are sorted ascending. (optional)

    try:
        # Get multiple playlists.
        api_response = api_instance.playlists_get(country_code=country_code, filter_collaborators_id=filter_collaborators_id, filter_id=filter_id, filter_owners_id=filter_owners_id, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media, sort=sort)
        print("The response of PlaylistsApi->playlists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **filter_collaborators_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | [optional] 
 **filter_id** | [**List[str]**](str.md)| List of playlist IDs (e.g. &#x60;550e8400-e29b-41d4-a716-446655440000&#x60;) | [optional] 
 **filter_owners_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: collaboratorProfiles, collaborators, coverArt, curators, items, ownerProfiles, owners, suggestedCoverArts | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: curators.albums | [optional] 
 **sort** | [**List[str]**](str.md)| Values prefixed with \&quot;-\&quot; are sorted descending; values without it are sorted ascending. | [optional] 

### Return type

[**PlaylistsMultiResourceDataDocument**](PlaylistsMultiResourceDataDocument.md)

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

# **playlists_id_delete**
> MutationResponseDocument playlists_id_delete(id, idempotency_key=idempotency_key)

Delete single playlist.

Deletes existing playlist.

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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)

    try:
        # Delete single playlist.
        api_response = api_instance.playlists_id_delete(id, idempotency_key=idempotency_key)
        print("The response of PlaylistsApi->playlists_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
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

# **playlists_id_get**
> PlaylistsSingleResourceDataDocument playlists_id_get(id, country_code=country_code, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get single playlist.

Retrieves single playlist by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.playlists_single_resource_data_document import PlaylistsSingleResourceDataDocument
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['curators.albums'] # List[str] | Include related resources. Available relationships: collaboratorProfiles, collaborators, coverArt, curators, items, ownerProfiles, owners, suggestedCoverArts (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'curators.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: curators.albums (optional)

    try:
        # Get single playlist.
        api_response = api_instance.playlists_id_get(id, country_code=country_code, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of PlaylistsApi->playlists_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: collaboratorProfiles, collaborators, coverArt, curators, items, ownerProfiles, owners, suggestedCoverArts | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: curators.albums | [optional] 

### Return type

[**PlaylistsSingleResourceDataDocument**](PlaylistsSingleResourceDataDocument.md)

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

# **playlists_id_patch**
> PlaylistsUpdateSingleResourceDataDocument playlists_id_patch(id, idempotency_key=idempotency_key, playlists_update_operation_payload=playlists_update_operation_payload)

Update single playlist.

Updates existing playlist.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlists_update_operation_payload import PlaylistsUpdateOperationPayload
from tidal.models.playlists_update_single_resource_data_document import PlaylistsUpdateSingleResourceDataDocument
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    playlists_update_operation_payload = tidal.PlaylistsUpdateOperationPayload() # PlaylistsUpdateOperationPayload |  (optional)

    try:
        # Update single playlist.
        api_response = api_instance.playlists_id_patch(id, idempotency_key=idempotency_key, playlists_update_operation_payload=playlists_update_operation_payload)
        print("The response of PlaylistsApi->playlists_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **playlists_update_operation_payload** | [**PlaylistsUpdateOperationPayload**](PlaylistsUpdateOperationPayload.md)|  | [optional] 

### Return type

[**PlaylistsUpdateSingleResourceDataDocument**](PlaylistsUpdateSingleResourceDataDocument.md)

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

# **playlists_id_relationships_collaborator_profiles_delete**
> MutationResponseDocument playlists_id_relationships_collaborator_profiles_delete(id, idempotency_key=idempotency_key, playlists_collaborator_profiles_relationship_remove_operation_payload=playlists_collaborator_profiles_relationship_remove_operation_payload)

Delete from collaboratorProfiles relationship (\"to-many\").

Deletes item(s) from collaboratorProfiles relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.playlists_collaborator_profiles_relationship_remove_operation_payload import PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    playlists_collaborator_profiles_relationship_remove_operation_payload = tidal.PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload() # PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload |  (optional)

    try:
        # Delete from collaboratorProfiles relationship (\"to-many\").
        api_response = api_instance.playlists_id_relationships_collaborator_profiles_delete(id, idempotency_key=idempotency_key, playlists_collaborator_profiles_relationship_remove_operation_payload=playlists_collaborator_profiles_relationship_remove_operation_payload)
        print("The response of PlaylistsApi->playlists_id_relationships_collaborator_profiles_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_relationships_collaborator_profiles_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **playlists_collaborator_profiles_relationship_remove_operation_payload** | [**PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload**](PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload.md)|  | [optional] 

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

# **playlists_id_relationships_collaborator_profiles_get**
> PlaylistsCollaboratorProfilesMultiRelationshipDataDocument playlists_id_relationships_collaborator_profiles_get(id, include=include, page_cursor=page_cursor)

Get collaboratorProfiles relationship (\"to-many\").

Deprecated. Use curators for attribution.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.playlists_collaborator_profiles_multi_relationship_data_document import PlaylistsCollaboratorProfilesMultiRelationshipDataDocument
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    include = ['collaboratorProfiles'] # List[str] | Include related resources. Available relationships: collaboratorProfiles (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get collaboratorProfiles relationship (\"to-many\").
        api_response = api_instance.playlists_id_relationships_collaborator_profiles_get(id, include=include, page_cursor=page_cursor)
        print("The response of PlaylistsApi->playlists_id_relationships_collaborator_profiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_relationships_collaborator_profiles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: collaboratorProfiles | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**PlaylistsCollaboratorProfilesMultiRelationshipDataDocument**](PlaylistsCollaboratorProfilesMultiRelationshipDataDocument.md)

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

# **playlists_id_relationships_collaborators_get**
> PlaylistsCollaboratorsMultiRelationshipDataDocument playlists_id_relationships_collaborators_get(id, include=include, page_cursor=page_cursor)

Get collaborators relationship (\"to-many\").

Retrieves collaborators relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.playlists_collaborators_multi_relationship_data_document import PlaylistsCollaboratorsMultiRelationshipDataDocument
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    include = ['collaborators'] # List[str] | Include related resources. Available relationships: collaborators (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get collaborators relationship (\"to-many\").
        api_response = api_instance.playlists_id_relationships_collaborators_get(id, include=include, page_cursor=page_cursor)
        print("The response of PlaylistsApi->playlists_id_relationships_collaborators_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_relationships_collaborators_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: collaborators | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**PlaylistsCollaboratorsMultiRelationshipDataDocument**](PlaylistsCollaboratorsMultiRelationshipDataDocument.md)

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

# **playlists_id_relationships_cover_art_get**
> PlaylistsCoverArtMultiRelationshipDataDocument playlists_id_relationships_cover_art_get(id, country_code=country_code, include=include, page_cursor=page_cursor)

Get coverArt relationship (\"to-many\").

Retrieves coverArt relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.playlists_cover_art_multi_relationship_data_document import PlaylistsCoverArtMultiRelationshipDataDocument
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['coverArt'] # List[str] | Include related resources. Available relationships: coverArt (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get coverArt relationship (\"to-many\").
        api_response = api_instance.playlists_id_relationships_cover_art_get(id, country_code=country_code, include=include, page_cursor=page_cursor)
        print("The response of PlaylistsApi->playlists_id_relationships_cover_art_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_relationships_cover_art_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: coverArt | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**PlaylistsCoverArtMultiRelationshipDataDocument**](PlaylistsCoverArtMultiRelationshipDataDocument.md)

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

# **playlists_id_relationships_cover_art_patch**
> MutationResponseDocument playlists_id_relationships_cover_art_patch(id, idempotency_key=idempotency_key, playlists_cover_art_relationship_update_operation_payload=playlists_cover_art_relationship_update_operation_payload)

Update coverArt relationship (\"to-many\").

Replaces the custom cover artwork selection with one attachable artwork. Empty data clears the custom selection. Previously attached uploaded artwork is soft-deleted unless system-managed. Returns an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.playlists_cover_art_relationship_update_operation_payload import PlaylistsCoverArtRelationshipUpdateOperationPayload
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    playlists_cover_art_relationship_update_operation_payload = tidal.PlaylistsCoverArtRelationshipUpdateOperationPayload() # PlaylistsCoverArtRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update coverArt relationship (\"to-many\").
        api_response = api_instance.playlists_id_relationships_cover_art_patch(id, idempotency_key=idempotency_key, playlists_cover_art_relationship_update_operation_payload=playlists_cover_art_relationship_update_operation_payload)
        print("The response of PlaylistsApi->playlists_id_relationships_cover_art_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_relationships_cover_art_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **playlists_cover_art_relationship_update_operation_payload** | [**PlaylistsCoverArtRelationshipUpdateOperationPayload**](PlaylistsCoverArtRelationshipUpdateOperationPayload.md)|  | [optional] 

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

# **playlists_id_relationships_curators_get**
> PlaylistsCuratorsMultiRelationshipDataDocument playlists_id_relationships_curators_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)

Get curators relationship (\"to-many\").

Artist profiles credited for the playlist

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.playlists_curators_multi_relationship_data_document import PlaylistsCuratorsMultiRelationshipDataDocument
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    include = ['curators.albums'] # List[str] | Include related resources. Available relationships: curators (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'curators.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: curators.albums (optional)

    try:
        # Get curators relationship (\"to-many\").
        api_response = api_instance.playlists_id_relationships_curators_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media)
        print("The response of PlaylistsApi->playlists_id_relationships_curators_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_relationships_curators_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: curators | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: curators.albums | [optional] 

### Return type

[**PlaylistsCuratorsMultiRelationshipDataDocument**](PlaylistsCuratorsMultiRelationshipDataDocument.md)

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

# **playlists_id_relationships_items_delete**
> MutationResponseDocument playlists_id_relationships_items_delete(id, idempotency_key=idempotency_key, playlists_items_relationship_remove_operation_payload=playlists_items_relationship_remove_operation_payload)

Delete from items relationship (\"to-many\").

Deletes item(s) from items relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.playlists_items_relationship_remove_operation_payload import PlaylistsItemsRelationshipRemoveOperationPayload
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    playlists_items_relationship_remove_operation_payload = tidal.PlaylistsItemsRelationshipRemoveOperationPayload() # PlaylistsItemsRelationshipRemoveOperationPayload |  (optional)

    try:
        # Delete from items relationship (\"to-many\").
        api_response = api_instance.playlists_id_relationships_items_delete(id, idempotency_key=idempotency_key, playlists_items_relationship_remove_operation_payload=playlists_items_relationship_remove_operation_payload)
        print("The response of PlaylistsApi->playlists_id_relationships_items_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_relationships_items_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **playlists_items_relationship_remove_operation_payload** | [**PlaylistsItemsRelationshipRemoveOperationPayload**](PlaylistsItemsRelationshipRemoveOperationPayload.md)|  | [optional] 

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

# **playlists_id_relationships_items_get**
> PlaylistsItemsMultiRelationshipDataDocument playlists_id_relationships_items_get(id, country_code=country_code, filter_self_matches_query=filter_self_matches_query, include=include, page_cursor=page_cursor, replace_media=replace_media, sort=sort)

Get items relationship (\"to-many\").

Retrieves items relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.playlists_items_multi_relationship_data_document import PlaylistsItemsMultiRelationshipDataDocument
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    filter_self_matches_query = 'filter_self_matches_query_example' # str | Filter playlist items by a free-text query (e.g. `halo`) (optional)
    include = ['items'] # List[str] | Include related resources. Available relationships: items (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'items' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items (optional)
    sort = ['sort_example'] # List[str] | Values prefixed with \"-\" are sorted descending; values without it are sorted ascending. (optional)

    try:
        # Get items relationship (\"to-many\").
        api_response = api_instance.playlists_id_relationships_items_get(id, country_code=country_code, filter_self_matches_query=filter_self_matches_query, include=include, page_cursor=page_cursor, replace_media=replace_media, sort=sort)
        print("The response of PlaylistsApi->playlists_id_relationships_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_relationships_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **filter_self_matches_query** | **str**| Filter playlist items by a free-text query (e.g. &#x60;halo&#x60;) | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: items | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: items | [optional] 
 **sort** | [**List[str]**](str.md)| Values prefixed with \&quot;-\&quot; are sorted descending; values without it are sorted ascending. | [optional] 

### Return type

[**PlaylistsItemsMultiRelationshipDataDocument**](PlaylistsItemsMultiRelationshipDataDocument.md)

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

# **playlists_id_relationships_items_patch**
> MutationResponseDocument playlists_id_relationships_items_patch(id, idempotency_key=idempotency_key, playlists_items_relationship_update_operation_payload=playlists_items_relationship_update_operation_payload)

Update items relationship (\"to-many\").

Incrementally moves the occurrences selected by data[].meta.itemId before meta.positionBefore, or to the end when meta is omitted. Preserves unselected memberships, their metadata and relative order; no items are added or removed. Empty data is rejected. Returns an acknowledgement.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.models.playlists_items_relationship_update_operation_payload import PlaylistsItemsRelationshipUpdateOperationPayload
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    playlists_items_relationship_update_operation_payload = tidal.PlaylistsItemsRelationshipUpdateOperationPayload() # PlaylistsItemsRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update items relationship (\"to-many\").
        api_response = api_instance.playlists_id_relationships_items_patch(id, idempotency_key=idempotency_key, playlists_items_relationship_update_operation_payload=playlists_items_relationship_update_operation_payload)
        print("The response of PlaylistsApi->playlists_id_relationships_items_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_relationships_items_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **playlists_items_relationship_update_operation_payload** | [**PlaylistsItemsRelationshipUpdateOperationPayload**](PlaylistsItemsRelationshipUpdateOperationPayload.md)|  | [optional] 

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

# **playlists_id_relationships_items_post**
> PlaylistsItemsAddMultiRelationshipDataDocument playlists_id_relationships_items_post(id, idempotency_key=idempotency_key, playlists_items_relationship_add_operation_payload=playlists_items_relationship_add_operation_payload)

Add to items relationship (\"to-many\").

Adds item(s) to items relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlists_items_add_multi_relationship_data_document import PlaylistsItemsAddMultiRelationshipDataDocument
from tidal.models.playlists_items_relationship_add_operation_payload import PlaylistsItemsRelationshipAddOperationPayload
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    playlists_items_relationship_add_operation_payload = tidal.PlaylistsItemsRelationshipAddOperationPayload() # PlaylistsItemsRelationshipAddOperationPayload |  (optional)

    try:
        # Add to items relationship (\"to-many\").
        api_response = api_instance.playlists_id_relationships_items_post(id, idempotency_key=idempotency_key, playlists_items_relationship_add_operation_payload=playlists_items_relationship_add_operation_payload)
        print("The response of PlaylistsApi->playlists_id_relationships_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_relationships_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **playlists_items_relationship_add_operation_payload** | [**PlaylistsItemsRelationshipAddOperationPayload**](PlaylistsItemsRelationshipAddOperationPayload.md)|  | [optional] 

### Return type

[**PlaylistsItemsAddMultiRelationshipDataDocument**](PlaylistsItemsAddMultiRelationshipDataDocument.md)

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
**409** | Playlist already contains one or more requested items; Playlist item limit reached; Request already in progress for this idempotency key |  -  |
**415** | Unsupported request media type or encoding |  -  |
**422** | Idempotency key reused for a different request |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlists_id_relationships_owner_profiles_get**
> PlaylistsOwnerProfilesMultiRelationshipDataDocument playlists_id_relationships_owner_profiles_get(id, include=include, page_cursor=page_cursor)

Get ownerProfiles relationship (\"to-many\").

Deprecated. Use curators for attribution.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.playlists_owner_profiles_multi_relationship_data_document import PlaylistsOwnerProfilesMultiRelationshipDataDocument
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    include = ['ownerProfiles'] # List[str] | Include related resources. Available relationships: ownerProfiles (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get ownerProfiles relationship (\"to-many\").
        api_response = api_instance.playlists_id_relationships_owner_profiles_get(id, include=include, page_cursor=page_cursor)
        print("The response of PlaylistsApi->playlists_id_relationships_owner_profiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_relationships_owner_profiles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: ownerProfiles | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**PlaylistsOwnerProfilesMultiRelationshipDataDocument**](PlaylistsOwnerProfilesMultiRelationshipDataDocument.md)

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

# **playlists_id_relationships_owners_get**
> PlaylistsOwnersMultiRelationshipDataDocument playlists_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.playlists_owners_multi_relationship_data_document import PlaylistsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.playlists_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of PlaylistsApi->playlists_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**PlaylistsOwnersMultiRelationshipDataDocument**](PlaylistsOwnersMultiRelationshipDataDocument.md)

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

# **playlists_id_relationships_suggested_cover_arts_get**
> PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument playlists_id_relationships_suggested_cover_arts_get(id, include=include, page_cursor=page_cursor)

Get suggestedCoverArts relationship (\"to-many\").

Retrieves suggestedCoverArts relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlists_suggested_cover_arts_multi_relationship_data_document import PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument
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
    api_instance = tidal.PlaylistsApi(api_client)
    id = '550e8400-e29b-41d4-a716-446655440000' # str | Playlist id
    include = ['suggestedCoverArts'] # List[str] | Include related resources. Available relationships: suggestedCoverArts (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get suggestedCoverArts relationship (\"to-many\").
        api_response = api_instance.playlists_id_relationships_suggested_cover_arts_get(id, include=include, page_cursor=page_cursor)
        print("The response of PlaylistsApi->playlists_id_relationships_suggested_cover_arts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_id_relationships_suggested_cover_arts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Playlist id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: suggestedCoverArts | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument**](PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument.md)

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

# **playlists_post**
> PlaylistsCreateSingleResourceDataDocument playlists_post(idempotency_key=idempotency_key, playlists_create_operation_payload=playlists_create_operation_payload)

Create single playlist.

Creates a new playlist.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.playlists_create_operation_payload import PlaylistsCreateOperationPayload
from tidal.models.playlists_create_single_resource_data_document import PlaylistsCreateSingleResourceDataDocument
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
    api_instance = tidal.PlaylistsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    playlists_create_operation_payload = tidal.PlaylistsCreateOperationPayload() # PlaylistsCreateOperationPayload |  (optional)

    try:
        # Create single playlist.
        api_response = api_instance.playlists_post(idempotency_key=idempotency_key, playlists_create_operation_payload=playlists_create_operation_payload)
        print("The response of PlaylistsApi->playlists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->playlists_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **playlists_create_operation_payload** | [**PlaylistsCreateOperationPayload**](PlaylistsCreateOperationPayload.md)|  | [optional] 

### Return type

[**PlaylistsCreateSingleResourceDataDocument**](PlaylistsCreateSingleResourceDataDocument.md)

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

