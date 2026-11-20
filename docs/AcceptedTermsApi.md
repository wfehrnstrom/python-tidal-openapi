# tidal.AcceptedTermsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accepted_terms_get**](AcceptedTermsApi.md#accepted_terms_get) | **GET** /acceptedTerms | Get multiple acceptedTerms.
[**accepted_terms_id_relationships_owners_get**](AcceptedTermsApi.md#accepted_terms_id_relationships_owners_get) | **GET** /acceptedTerms/{id}/relationships/owners | Get owners relationship (\&quot;to-many\&quot;).
[**accepted_terms_id_relationships_terms_get**](AcceptedTermsApi.md#accepted_terms_id_relationships_terms_get) | **GET** /acceptedTerms/{id}/relationships/terms | Get terms relationship (\&quot;to-one\&quot;).
[**accepted_terms_post**](AcceptedTermsApi.md#accepted_terms_post) | **POST** /acceptedTerms | Create single acceptedTerm.


# **accepted_terms_get**
> AcceptedTermsMultiResourceDataDocument accepted_terms_get(filter_owners_id, filter_terms_terms_type, filter_terms_is_latest_version=filter_terms_is_latest_version, include=include, include_linkage=include_linkage)

Get multiple acceptedTerms.

Retrieves multiple acceptedTerms by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.accepted_terms_multi_resource_data_document import AcceptedTermsMultiResourceDataDocument
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
    api_instance = tidal.AcceptedTermsApi(api_client)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`.
    filter_terms_terms_type = ['filter_terms_terms_type_example'] # List[str] | One of: DEVELOPER, UPLOAD_MARKETPLACE, MERCH_GUIDELINES, TIDAL_CONNECT_DEVELOPER (e.g. `DEVELOPER`)
    filter_terms_is_latest_version = ['filter_terms_is_latest_version_example'] # List[str] | Filter by terms.isLatestVersion (optional)
    include = ['terms'] # List[str] | Include related resources. Available relationships: owners, terms (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get multiple acceptedTerms.
        api_response = api_instance.accepted_terms_get(filter_owners_id, filter_terms_terms_type, filter_terms_is_latest_version=filter_terms_is_latest_version, include=include, include_linkage=include_linkage)
        print("The response of AcceptedTermsApi->accepted_terms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcceptedTermsApi->accepted_terms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_owners_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | 
 **filter_terms_terms_type** | [**List[str]**](str.md)| One of: DEVELOPER, UPLOAD_MARKETPLACE, MERCH_GUIDELINES, TIDAL_CONNECT_DEVELOPER (e.g. &#x60;DEVELOPER&#x60;) | 
 **filter_terms_is_latest_version** | [**List[str]**](str.md)| Filter by terms.isLatestVersion | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners, terms | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 

### Return type

[**AcceptedTermsMultiResourceDataDocument**](AcceptedTermsMultiResourceDataDocument.md)

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

# **accepted_terms_id_relationships_owners_get**
> AcceptedTermsOwnersMultiRelationshipDataDocument accepted_terms_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)

Get owners relationship (\"to-many\").

Retrieves owners relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.accepted_terms_owners_multi_relationship_data_document import AcceptedTermsOwnersMultiRelationshipDataDocument
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
    api_instance = tidal.AcceptedTermsApi(api_client)
    id = 'a468bee88def' # str | Accepted terms id
    include = ['owners'] # List[str] | Include related resources. Available relationships: owners (optional)
    page_cursor = 'page_cursor_example' # str | Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified (optional)

    try:
        # Get owners relationship (\"to-many\").
        api_response = api_instance.accepted_terms_id_relationships_owners_get(id, include=include, page_cursor=page_cursor)
        print("The response of AcceptedTermsApi->accepted_terms_id_relationships_owners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcceptedTermsApi->accepted_terms_id_relationships_owners_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Accepted terms id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: owners | [optional] 
 **page_cursor** | **str**| Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified | [optional] 

### Return type

[**AcceptedTermsOwnersMultiRelationshipDataDocument**](AcceptedTermsOwnersMultiRelationshipDataDocument.md)

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

# **accepted_terms_id_relationships_terms_get**
> AcceptedTermsTermsSingleRelationshipDataDocument accepted_terms_id_relationships_terms_get(id, include=include)

Get terms relationship (\"to-one\").

Retrieves terms relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.accepted_terms_terms_single_relationship_data_document import AcceptedTermsTermsSingleRelationshipDataDocument
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
    api_instance = tidal.AcceptedTermsApi(api_client)
    id = 'a468bee88def' # str | Accepted terms id
    include = ['terms'] # List[str] | Include related resources. Available relationships: terms (optional)

    try:
        # Get terms relationship (\"to-one\").
        api_response = api_instance.accepted_terms_id_relationships_terms_get(id, include=include)
        print("The response of AcceptedTermsApi->accepted_terms_id_relationships_terms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcceptedTermsApi->accepted_terms_id_relationships_terms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Accepted terms id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: terms | [optional] 

### Return type

[**AcceptedTermsTermsSingleRelationshipDataDocument**](AcceptedTermsTermsSingleRelationshipDataDocument.md)

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

# **accepted_terms_post**
> AcceptedTermsCreateSingleResourceDataDocument accepted_terms_post(idempotency_key=idempotency_key, accepted_terms_create_operation_payload=accepted_terms_create_operation_payload)

Create single acceptedTerm.

Creates a new acceptedTerm.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.accepted_terms_create_operation_payload import AcceptedTermsCreateOperationPayload
from tidal.models.accepted_terms_create_single_resource_data_document import AcceptedTermsCreateSingleResourceDataDocument
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
    api_instance = tidal.AcceptedTermsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    accepted_terms_create_operation_payload = tidal.AcceptedTermsCreateOperationPayload() # AcceptedTermsCreateOperationPayload |  (optional)

    try:
        # Create single acceptedTerm.
        api_response = api_instance.accepted_terms_post(idempotency_key=idempotency_key, accepted_terms_create_operation_payload=accepted_terms_create_operation_payload)
        print("The response of AcceptedTermsApi->accepted_terms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcceptedTermsApi->accepted_terms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **accepted_terms_create_operation_payload** | [**AcceptedTermsCreateOperationPayload**](AcceptedTermsCreateOperationPayload.md)|  | [optional] 

### Return type

[**AcceptedTermsCreateSingleResourceDataDocument**](AcceptedTermsCreateSingleResourceDataDocument.md)

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

