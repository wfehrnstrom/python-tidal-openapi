# tidal.CommentSummariesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comment_summaries_get**](CommentSummariesApi.md#comment_summaries_get) | **GET** /commentSummaries | Get multiple commentSummaries.
[**comment_summaries_id_relationships_subject_get**](CommentSummariesApi.md#comment_summaries_id_relationships_subject_get) | **GET** /commentSummaries/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).


# **comment_summaries_get**
> CommentSummariesMultiResourceDataDocument comment_summaries_get(filter_subject, country_code=country_code, include=include, include_linkage=include_linkage, replace_media=replace_media, share_code=share_code)

Get multiple commentSummaries.

Returns one current summary per accessible subject, for up to 20 subjects. Duplicates are returned once. Inaccessible or missing subjects are omitted. Empty supported subjects still have a summary. IDs remain stable as counts change. Counts include root comments on source files and direct replies on comments.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.comment_summaries_multi_resource_data_document import CommentSummariesMultiResourceDataDocument
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
    api_instance = tidal.CommentSummariesApi(api_client)
    filter_subject = ['filter_subject_example'] # List[str] | Subjects whose counts to return.
    country_code = 'US' # str | ISO 3166-1 alpha-2 country code (optional)
    include = ['subject.author.albums'] # List[str] | Include related resources. Available relationships: subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'subject.author.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.author.albums (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get multiple commentSummaries.
        api_response = api_instance.comment_summaries_get(filter_subject, country_code=country_code, include=include, include_linkage=include_linkage, replace_media=replace_media, share_code=share_code)
        print("The response of CommentSummariesApi->comment_summaries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentSummariesApi->comment_summaries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_subject** | [**List[str]**](str.md)| Subjects whose counts to return. | 
 **country_code** | **str**| ISO 3166-1 alpha-2 country code | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject.author.albums | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**CommentSummariesMultiResourceDataDocument**](CommentSummariesMultiResourceDataDocument.md)

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

# **comment_summaries_id_relationships_subject_get**
> CommentSummariesSubjectSingleRelationshipDataDocument comment_summaries_id_relationships_subject_get(id, include=include, replace_media=replace_media, share_code=share_code)

Get subject relationship (\"to-one\").

Retrieves subject relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.comment_summaries_subject_single_relationship_data_document import CommentSummariesSubjectSingleRelationshipDataDocument
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
    api_instance = tidal.CommentSummariesApi(api_client)
    id = 'id_example' # str | Opaque identifier of one subject's current summary
    include = ['subject.author.albums'] # List[str] | Include related resources. Available relationships: subject (optional)
    replace_media = 'subject.author.albums' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject.author.albums (optional)
    share_code = 'xyz' # str | Share code used as a bearer credential for the resource. (optional)

    try:
        # Get subject relationship (\"to-one\").
        api_response = api_instance.comment_summaries_id_relationships_subject_get(id, include=include, replace_media=replace_media, share_code=share_code)
        print("The response of CommentSummariesApi->comment_summaries_id_relationships_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentSummariesApi->comment_summaries_id_relationships_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Opaque identifier of one subject&#39;s current summary | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject.author.albums | [optional] 
 **share_code** | **str**| Share code used as a bearer credential for the resource. | [optional] 

### Return type

[**CommentSummariesSubjectSingleRelationshipDataDocument**](CommentSummariesSubjectSingleRelationshipDataDocument.md)

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

