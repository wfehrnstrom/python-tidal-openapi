# tidal.FolderItemsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_items_get**](FolderItemsApi.md#folder_items_get) | **GET** /folderItems | Get multiple folderItems.
[**folder_items_id_delete**](FolderItemsApi.md#folder_items_id_delete) | **DELETE** /folderItems/{id} | Delete single folderItem.
[**folder_items_id_get**](FolderItemsApi.md#folder_items_id_get) | **GET** /folderItems/{id} | Get single folderItem.
[**folder_items_id_relationships_breadcrumb_get**](FolderItemsApi.md#folder_items_id_relationships_breadcrumb_get) | **GET** /folderItems/{id}/relationships/breadcrumb | Get breadcrumb relationship (\&quot;to-many\&quot;).
[**folder_items_id_relationships_owners_get**](FolderItemsApi.md#folder_items_id_relationships_owners_get) | **GET** /folderItems/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**folder_items_id_relationships_parent_get**](FolderItemsApi.md#folder_items_id_relationships_parent_get) | **GET** /folderItems/{id}/relationships/parent | Get parent relationship (\&quot;to-one\&quot;).
[**folder_items_id_relationships_parent_patch**](FolderItemsApi.md#folder_items_id_relationships_parent_patch) | **PATCH** /folderItems/{id}/relationships/parent | Update parent relationship (\&quot;to-one\&quot;).
[**folder_items_id_relationships_sharing_summary_get**](FolderItemsApi.md#folder_items_id_relationships_sharing_summary_get) | **GET** /folderItems/{id}/relationships/sharingSummary | Get sharingSummary relationship (\&quot;to-one\&quot;).
[**folder_items_id_relationships_subject_get**](FolderItemsApi.md#folder_items_id_relationships_subject_get) | **GET** /folderItems/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).
[**folder_items_post**](FolderItemsApi.md#folder_items_post) | **POST** /folderItems | Create single folderItem.


# **folder_items_get**
> FolderItemsMultiResourceDataDocument folder_items_get(filter_parent_id=filter_parent_id, filter_parent_is_root=filter_parent_is_root, filter_parent_owners_id=filter_parent_owners_id, filter_self_matches_query=filter_self_matches_query, filter_subject_albums_published=filter_subject_albums_published, filter_subject_owners_id=filter_subject_owners_id, filter_subject_owners_id_ne=filter_subject_owners_id_ne, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)

Get multiple folderItems.

Lists items in a folder, newest placement first. Select a folder with parent.id, or select your root with parent.isRoot=true and parent.owners.id=me. These forms cannot be combined; no other parent-filter combinations are supported. To search every folder in your tree instead, use query, subject.albums:published or both with parent.owners.id=me alone.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.folder_items_multi_resource_data_document import FolderItemsMultiResourceDataDocument
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
    api_instance = tidal.FolderItemsApi(api_client)
    filter_parent_id = 'filter_parent_id_example' # str | Folder id (e.g. `e3226624-355b-48f8-aa93-db42532caa66`). Also accepts `me`. (optional)
    filter_parent_is_root = 'filter_parent_is_root_example' # str | Filter by parent.isRoot (optional)
    filter_parent_owners_id = 'filter_parent_owners_id_example' # str | Owner of the folder an item is in; must be the authenticated user. With parent.isRoot=true it selects your root, and with query or subject.albums:published your whole tree. Also accepts `me`. (optional)
    filter_self_matches_query = 'filter_self_matches_query_example' # str | Searches every folder in your tree, selected with parent.owners.id=me, and lists the matching items in one flat list. An item matches when each word given starts a word in its folder's name, its album's title or the title of one of the album's tracks, ignoring case. An item shared with you matches by its subject, and only while you can open it. (e.g. `demo`) (optional)
    filter_subject_albums_published = 'filter_subject_albums_published_example' # str | Searches every folder in your tree, selected with parent.owners.id=me, for albums that are (true) or are not (false) published, and lists them in one flat list. Other items never match. Combines with filter[self][matchesQuery]. (e.g. `true`) (optional)
    filter_subject_owners_id = 'filter_subject_owners_id_example' # str | In your folders, `=me` selects owned placements and `[ne]=me` selects shared placements. In someone else's folder, `=me` returns no items and `[ne]=me` returns all items. Accepts only `me` or your own user ID. (optional)
    filter_subject_owners_id_ne = 'filter_subject_owners_id_ne_example' # str | In your folders, `=me` selects owned placements and `[ne]=me` selects shared placements. In someone else's folder, `=me` returns no items and `[ne]=me` returns all items. Accepts only `me` or your own user ID. (optional)
    include = ['breadcrumb.children.subject'] # List[str] | Include related resources. Available relationships: breadcrumb, owners, parent, sharingSummary, subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'breadcrumb.children.subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: breadcrumb.children.subject (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get multiple folderItems.
        api_response = api_instance.folder_items_get(filter_parent_id=filter_parent_id, filter_parent_is_root=filter_parent_is_root, filter_parent_owners_id=filter_parent_owners_id, filter_self_matches_query=filter_self_matches_query, filter_subject_albums_published=filter_subject_albums_published, filter_subject_owners_id=filter_subject_owners_id, filter_subject_owners_id_ne=filter_subject_owners_id_ne, include=include, include_linkage=include_linkage, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)
        print("The response of FolderItemsApi->folder_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderItemsApi->folder_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_parent_id** | **str**| Folder id (e.g. &#x60;e3226624-355b-48f8-aa93-db42532caa66&#x60;). Also accepts &#x60;me&#x60;. | [optional] 
 **filter_parent_is_root** | **str**| Filter by parent.isRoot | [optional] 
 **filter_parent_owners_id** | **str**| Owner of the folder an item is in; must be the authenticated user. With parent.isRoot&#x3D;true it selects your root, and with query or subject.albums:published your whole tree. Also accepts &#x60;me&#x60;. | [optional] 
 **filter_self_matches_query** | **str**| Searches every folder in your tree, selected with parent.owners.id&#x3D;me, and lists the matching items in one flat list. An item matches when each word given starts a word in its folder&#39;s name, its album&#39;s title or the title of one of the album&#39;s tracks, ignoring case. An item shared with you matches by its subject, and only while you can open it. (e.g. &#x60;demo&#x60;) | [optional] 
 **filter_subject_albums_published** | **str**| Searches every folder in your tree, selected with parent.owners.id&#x3D;me, for albums that are (true) or are not (false) published, and lists them in one flat list. Other items never match. Combines with filter[self][matchesQuery]. (e.g. &#x60;true&#x60;) | [optional] 
 **filter_subject_owners_id** | **str**| In your folders, &#x60;&#x3D;me&#x60; selects owned placements and &#x60;[ne]&#x3D;me&#x60; selects shared placements. In someone else&#39;s folder, &#x60;&#x3D;me&#x60; returns no items and &#x60;[ne]&#x3D;me&#x60; returns all items. Accepts only &#x60;me&#x60; or your own user ID. | [optional] 
 **filter_subject_owners_id_ne** | **str**| In your folders, &#x60;&#x3D;me&#x60; selects owned placements and &#x60;[ne]&#x3D;me&#x60; selects shared placements. In someone else&#39;s folder, &#x60;&#x3D;me&#x60; returns no items and &#x60;[ne]&#x3D;me&#x60; returns all items. Accepts only &#x60;me&#x60; or your own user ID. | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: breadcrumb, owners, parent, sharingSummary, subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: breadcrumb.children.subject | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**FolderItemsMultiResourceDataDocument**](FolderItemsMultiResourceDataDocument.md)

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

# **folder_items_id_delete**
> MutationResponseDocument folder_items_id_delete(id, idempotency_key=idempotency_key, share_code=share_code)

Delete single folderItem.

Deletes existing folderItem.

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
    api_instance = tidal.FolderItemsApi(api_client)
    id = 'e3226624-355b-48f8-aa93-db42532caa66' # str | Folder item id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Delete single folderItem.
        api_response = api_instance.folder_items_id_delete(id, idempotency_key=idempotency_key, share_code=share_code)
        print("The response of FolderItemsApi->folder_items_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderItemsApi->folder_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder item id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

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

# **folder_items_id_get**
> FolderItemsSingleResourceDataDocument folder_items_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media, share_code=share_code)

Get single folderItem.

Retrieves single folderItem by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.folder_items_single_resource_data_document import FolderItemsSingleResourceDataDocument
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
    api_instance = tidal.FolderItemsApi(api_client)
    id = 'e3226624-355b-48f8-aa93-db42532caa66' # str | Folder item id
    include = ['breadcrumb.children.subject'] # List[str] | Include related resources. Available relationships: breadcrumb, owners, parent, sharingSummary, subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'breadcrumb.children.subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: breadcrumb.children.subject (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get single folderItem.
        api_response = api_instance.folder_items_id_get(id, include=include, include_linkage=include_linkage, replace_media=replace_media, share_code=share_code)
        print("The response of FolderItemsApi->folder_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderItemsApi->folder_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder item id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: breadcrumb, owners, parent, sharingSummary, subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: breadcrumb.children.subject | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**FolderItemsSingleResourceDataDocument**](FolderItemsSingleResourceDataDocument.md)

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

# **folder_items_id_relationships_breadcrumb_get**
> FolderItemsBreadcrumbMultiRelationshipDataDocument folder_items_id_relationships_breadcrumb_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)

Get breadcrumb relationship (\"to-many\").

The folders from the root to this item's parent; only for the tree's owner, empty otherwise.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.folder_items_breadcrumb_multi_relationship_data_document import FolderItemsBreadcrumbMultiRelationshipDataDocument
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
    api_instance = tidal.FolderItemsApi(api_client)
    id = 'e3226624-355b-48f8-aa93-db42532caa66' # str | Folder item id
    include = ['breadcrumb.children.subject'] # List[str] | Include related resources. Available relationships: breadcrumb (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    replace_media = 'breadcrumb.children.subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: breadcrumb.children.subject (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get breadcrumb relationship (\"to-many\").
        api_response = api_instance.folder_items_id_relationships_breadcrumb_get(id, include=include, page_cursor=page_cursor, replace_media=replace_media, share_code=share_code)
        print("The response of FolderItemsApi->folder_items_id_relationships_breadcrumb_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderItemsApi->folder_items_id_relationships_breadcrumb_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder item id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: breadcrumb | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: breadcrumb.children.subject | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**FolderItemsBreadcrumbMultiRelationshipDataDocument**](FolderItemsBreadcrumbMultiRelationshipDataDocument.md)

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

# **folder_items_id_relationships_owners_get**
> FolderItemsOwnersMultiRelationshipDataDocument folder_items_id_relationships_owners_get(id, include=include, page_cursor=page_cursor, share_code=share_code)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.folder_items_owners_multi_relationship_data_document import FolderItemsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.FolderItemsApi(api_client)
    id = 'e3226624-355b-48f8-aa93-db42532caa66' # str | Folder item id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.folder_items_id_relationships_owners_get(id, include=include, page_cursor=page_cursor, share_code=share_code)
        print("The response of FolderItemsApi->folder_items_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderItemsApi->folder_items_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder item id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**FolderItemsOwnersMultiRelationshipDataDocument**](FolderItemsOwnersMultiRelationshipDataDocument.md)

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

# **folder_items_id_relationships_parent_get**
> FolderItemsParentSingleRelationshipDataDocument folder_items_id_relationships_parent_get(id, include=include, replace_media=replace_media, share_code=share_code)

Get parent relationship (\"to-one\").

Retrieves parent relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.folder_items_parent_single_relationship_data_document import FolderItemsParentSingleRelationshipDataDocument
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
    api_instance = tidal.FolderItemsApi(api_client)
    id = 'e3226624-355b-48f8-aa93-db42532caa66' # str | Folder item id
    include = ['parent.children.subject'] # List[str] | Include related resources. Available relationships: parent (optional)
    replace_media = 'parent.children.subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: parent.children.subject (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get parent relationship (\"to-one\").
        api_response = api_instance.folder_items_id_relationships_parent_get(id, include=include, replace_media=replace_media, share_code=share_code)
        print("The response of FolderItemsApi->folder_items_id_relationships_parent_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderItemsApi->folder_items_id_relationships_parent_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder item id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: parent | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: parent.children.subject | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**FolderItemsParentSingleRelationshipDataDocument**](FolderItemsParentSingleRelationshipDataDocument.md)

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

# **folder_items_id_relationships_parent_patch**
> FolderItemsParentUpdateSingleRelationshipDataDocument folder_items_id_relationships_parent_patch(id, idempotency_key=idempotency_key, share_code=share_code, folder_items_parent_relationship_update_operation_payload=folder_items_parent_relationship_update_operation_payload)

Update parent relationship (\"to-one\").

Moves the item to the supplied parent folder, replacing its previous parent. To move to the top level, supply the root folder explicitly; null data is rejected. The caller needs at least COLLABORATOR on the new parent. Within the item's tree they need OWNER on the item or COLLABORATOR on the folder holding it; only its creator moves it into another user's tree. Returns the new parent linkage.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.folder_items_parent_relationship_update_operation_payload import FolderItemsParentRelationshipUpdateOperationPayload
from tidal.models.folder_items_parent_update_single_relationship_data_document import FolderItemsParentUpdateSingleRelationshipDataDocument
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
    api_instance = tidal.FolderItemsApi(api_client)
    id = 'e3226624-355b-48f8-aa93-db42532caa66' # str | Folder item id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)
    folder_items_parent_relationship_update_operation_payload = tidal.FolderItemsParentRelationshipUpdateOperationPayload() # FolderItemsParentRelationshipUpdateOperationPayload |  (optional)

    try:
        # Update parent relationship (\"to-one\").
        api_response = api_instance.folder_items_id_relationships_parent_patch(id, idempotency_key=idempotency_key, share_code=share_code, folder_items_parent_relationship_update_operation_payload=folder_items_parent_relationship_update_operation_payload)
        print("The response of FolderItemsApi->folder_items_id_relationships_parent_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderItemsApi->folder_items_id_relationships_parent_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder item id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 
 **folder_items_parent_relationship_update_operation_payload** | [**FolderItemsParentRelationshipUpdateOperationPayload**](FolderItemsParentRelationshipUpdateOperationPayload.md)|  | [optional] 

### Return type

[**FolderItemsParentUpdateSingleRelationshipDataDocument**](FolderItemsParentUpdateSingleRelationshipDataDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | A folder cannot be placed inside itself or one of its descendants |  -  |
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

# **folder_items_id_relationships_sharing_summary_get**
> FolderItemsSharingSummarySingleRelationshipDataDocument folder_items_id_relationships_sharing_summary_get(id, include=include, replace_media=replace_media, share_code=share_code)

Get sharingSummary relationship (\"to-one\").

Retrieves sharingSummary relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.folder_items_sharing_summary_single_relationship_data_document import FolderItemsSharingSummarySingleRelationshipDataDocument
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
    api_instance = tidal.FolderItemsApi(api_client)
    id = 'e3226624-355b-48f8-aa93-db42532caa66' # str | Folder item id
    include = ['sharingSummary.subject'] # List[str] | Include related resources. Available relationships: sharingSummary (optional)
    replace_media = 'sharingSummary.subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: sharingSummary.subject (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get sharingSummary relationship (\"to-one\").
        api_response = api_instance.folder_items_id_relationships_sharing_summary_get(id, include=include, replace_media=replace_media, share_code=share_code)
        print("The response of FolderItemsApi->folder_items_id_relationships_sharing_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderItemsApi->folder_items_id_relationships_sharing_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder item id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: sharingSummary | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: sharingSummary.subject | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**FolderItemsSharingSummarySingleRelationshipDataDocument**](FolderItemsSharingSummarySingleRelationshipDataDocument.md)

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

# **folder_items_id_relationships_subject_get**
> FolderItemsSubjectSingleRelationshipDataDocument folder_items_id_relationships_subject_get(id, include=include, replace_media=replace_media, share_code=share_code)

Get subject relationship (\"to-one\").

Retrieves subject relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.folder_items_subject_single_relationship_data_document import FolderItemsSubjectSingleRelationshipDataDocument
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
    api_instance = tidal.FolderItemsApi(api_client)
    id = 'e3226624-355b-48f8-aa93-db42532caa66' # str | Folder item id
    include = ['subject'] # List[str] | Include related resources. Available relationships: subject (optional)
    replace_media = 'subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get subject relationship (\"to-one\").
        api_response = api_instance.folder_items_id_relationships_subject_get(id, include=include, replace_media=replace_media, share_code=share_code)
        print("The response of FolderItemsApi->folder_items_id_relationships_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderItemsApi->folder_items_id_relationships_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Folder item id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**FolderItemsSubjectSingleRelationshipDataDocument**](FolderItemsSubjectSingleRelationshipDataDocument.md)

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

# **folder_items_post**
> FolderItemsCreateSingleResourceDataDocument folder_items_post(idempotency_key=idempotency_key, folder_items_create_operation_payload=folder_items_create_operation_payload)

Create single folderItem.

Creates a new folderItem.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.folder_items_create_operation_payload import FolderItemsCreateOperationPayload
from tidal.models.folder_items_create_single_resource_data_document import FolderItemsCreateSingleResourceDataDocument
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
    api_instance = tidal.FolderItemsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    folder_items_create_operation_payload = tidal.FolderItemsCreateOperationPayload() # FolderItemsCreateOperationPayload |  (optional)

    try:
        # Create single folderItem.
        api_response = api_instance.folder_items_post(idempotency_key=idempotency_key, folder_items_create_operation_payload=folder_items_create_operation_payload)
        print("The response of FolderItemsApi->folder_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderItemsApi->folder_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **folder_items_create_operation_payload** | [**FolderItemsCreateOperationPayload**](FolderItemsCreateOperationPayload.md)|  | [optional] 

### Return type

[**FolderItemsCreateSingleResourceDataDocument**](FolderItemsCreateSingleResourceDataDocument.md)

### Authorization

[Authorization_Code_PKCE](../README.md#Authorization_Code_PKCE)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | A folder cannot be placed inside itself or one of its descendants |  -  |
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

