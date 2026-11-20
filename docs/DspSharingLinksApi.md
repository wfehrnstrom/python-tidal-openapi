# tidal.DspSharingLinksApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dsp_sharing_links_get**](DspSharingLinksApi.md#dsp_sharing_links_get) | **GET** /dspSharingLinks | Get multiple dspSharingLinks.
[**dsp_sharing_links_id_relationships_subject_get**](DspSharingLinksApi.md#dsp_sharing_links_id_relationships_subject_get) | **GET** /dspSharingLinks/{id}/relationships/subject | Get subject relationship (\&quot;to-one\&quot;).


# **dsp_sharing_links_get**
> DspSharingLinksMultiResourceDataDocument dsp_sharing_links_get(filter_subject_id=filter_subject_id, filter_subject_type=filter_subject_type, filter_subject=filter_subject, include=include, include_linkage=include_linkage, replace_media=replace_media)

Get multiple dspSharingLinks.

Retrieves multiple dspSharingLinks by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.dsp_sharing_links_multi_resource_data_document import DspSharingLinksMultiResourceDataDocument
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
    api_instance = tidal.DspSharingLinksApi(api_client)
    filter_subject_id = ['filter_subject_id_example'] # List[str] | Deprecated: use filter[subject]. The id of the subject resource (optional)
    filter_subject_type = ['filter_subject_type_example'] # List[str] | Deprecated: use filter[subject]. The type of the subject resource (e.g. `tracks`) (optional)
    filter_subject = 'filter_subject_example' # str | The subject whose DSP sharing links to return. Use either subject or the deprecated subject.id and subject.type pair. (optional)
    include = ['subject'] # List[str] | Include related resources. Available relationships: subject (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)
    replace_media = 'subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject (optional)

    try:
        # Get multiple dspSharingLinks.
        api_response = api_instance.dsp_sharing_links_get(filter_subject_id=filter_subject_id, filter_subject_type=filter_subject_type, filter_subject=filter_subject, include=include, include_linkage=include_linkage, replace_media=replace_media)
        print("The response of DspSharingLinksApi->dsp_sharing_links_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DspSharingLinksApi->dsp_sharing_links_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_subject_id** | [**List[str]**](str.md)| Deprecated: use filter[subject]. The id of the subject resource | [optional] 
 **filter_subject_type** | [**List[str]**](str.md)| Deprecated: use filter[subject]. The type of the subject resource (e.g. &#x60;tracks&#x60;) | [optional] 
 **filter_subject** | **str**| The subject whose DSP sharing links to return. Use either subject or the deprecated subject.id and subject.type pair. | [optional] 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject | [optional] 

### Return type

[**DspSharingLinksMultiResourceDataDocument**](DspSharingLinksMultiResourceDataDocument.md)

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

# **dsp_sharing_links_id_relationships_subject_get**
> DspSharingLinksSubjectSingleRelationshipDataDocument dsp_sharing_links_id_relationships_subject_get(id, include=include, replace_media=replace_media)

Get subject relationship (\"to-one\").

Retrieves subject relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.dsp_sharing_links_subject_single_relationship_data_document import DspSharingLinksSubjectSingleRelationshipDataDocument
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
    api_instance = tidal.DspSharingLinksApi(api_client)
    id = 'QUxCVU1TOjEyMzQ1' # str | DspSharingLinks Id
    include = ['subject'] # List[str] | Include related resources. Available relationships: subject (optional)
    replace_media = 'subject' # str | Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: subject (optional)

    try:
        # Get subject relationship (\"to-one\").
        api_response = api_instance.dsp_sharing_links_id_relationships_subject_get(id, include=include, replace_media=replace_media)
        print("The response of DspSharingLinksApi->dsp_sharing_links_id_relationships_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DspSharingLinksApi->dsp_sharing_links_id_relationships_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DspSharingLinks Id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: subject | [optional] 
 **replace_media** | **str**| Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow &#x60;include&#x60; syntax. Example: subject | [optional] 

### Return type

[**DspSharingLinksSubjectSingleRelationshipDataDocument**](DspSharingLinksSubjectSingleRelationshipDataDocument.md)

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

