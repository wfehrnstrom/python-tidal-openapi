# tidal.SharingSummariesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharing_summaries_get**](SharingSummariesApi.md#sharing_summaries_get) | **GET** /sharingSummaries | Get multiple sharingSummaries.
[**sharing_summaries_id_relationships_subject_get**](SharingSummariesApi.md#sharing_summaries_id_relationships_subject_get) | **GET** /sharingSummaries/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).


# **sharing_summaries_get**
> SharingSummariesMultiResourceDataDocument sharing_summaries_get(filter_subject, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get multiple sharingSummaries.

Returns one current summary per distinct owned subject, for up to 20 subjects. Live subjects with no sharing return false flags. Missing or inaccessible subjects are omitted. IDs remain stable as sharing changes.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.sharing_summaries_multi_resource_data_document import SharingSummariesMultiResourceDataDocument
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
    api_instance = tidal.SharingSummariesApi(api_client)
    filter_subject = ['filter_subject_example'] # List[str] | Filter by subject. Also accepts `folders:me`.
    include = ['subject'] # List[str] | Include related resources. Available relationships: subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject (optional)

    try:
        # Get multiple sharingSummaries.
        api_response = api_instance.sharing_summaries_get(filter_subject, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of SharingSummariesApi->sharing_summaries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingSummariesApi->sharing_summaries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_subject** | [**List[str]**](str.md)| Filter by subject. Also accepts &#x60;folders:me&#x60;. | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject | [optional] 

### Return type

[**SharingSummariesMultiResourceDataDocument**](SharingSummariesMultiResourceDataDocument.md)

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

# **sharing_summaries_id_relationships_subject_get**
> SharingSummariesSubjectSingleRelationshipDataDocument sharing_summaries_id_relationships_subject_get(id, include=include, replace_media=replace_media)

Get subject relationship (\"to-one\").

Retrieves subject relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.sharing_summaries_subject_single_relationship_data_document import SharingSummariesSubjectSingleRelationshipDataDocument
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
    api_instance = tidal.SharingSummariesApi(api_client)
    id = 'id_example' # str | Opaque sharing summary ID
    include = ['subject'] # List[str] | Include related resources. Available relationships: subject (optional)
    replace_media = 'subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject (optional)

    try:
        # Get subject relationship (\"to-one\").
        api_response = api_instance.sharing_summaries_id_relationships_subject_get(id, include=include, replace_media=replace_media)
        print("The response of SharingSummariesApi->sharing_summaries_id_relationships_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharingSummariesApi->sharing_summaries_id_relationships_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque sharing summary ID | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject | [optional] 

### Return type

[**SharingSummariesSubjectSingleRelationshipDataDocument**](SharingSummariesSubjectSingleRelationshipDataDocument.md)

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

