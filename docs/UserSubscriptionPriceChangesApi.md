# tidal.UserSubscriptionPriceChangesApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_subscription_price_changes_get**](UserSubscriptionPriceChangesApi.md#user_subscription_price_changes_get) | **GET** /userSubscriptionPriceChanges | Get multiple userSubscriptionPriceChanges.
[**user_subscription_price_changes_id_relationships_decision_get**](UserSubscriptionPriceChangesApi.md#user_subscription_price_changes_id_relationships_decision_get) | **GET** /userSubscriptionPriceChanges/{id}/relationships/decision | Get decision relationship (\&quot;to-one\&quot;).


# **user_subscription_price_changes_get**
> UserSubscriptionPriceChangesMultiResourceDataDocument user_subscription_price_changes_get(filter_owners_id, include=include, include_linkage=include_linkage)

Get multiple userSubscriptionPriceChanges.

Retrieves multiple userSubscriptionPriceChanges by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_subscription_price_changes_multi_resource_data_document import UserSubscriptionPriceChangesMultiResourceDataDocument
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
    api_instance = tidal.UserSubscriptionPriceChangesApi(api_client)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`.
    include = ['decision'] # List[str] | Include related resources. Available relationships: decision (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get multiple userSubscriptionPriceChanges.
        api_response = api_instance.user_subscription_price_changes_get(filter_owners_id, include=include, include_linkage=include_linkage)
        print("The response of UserSubscriptionPriceChangesApi->user_subscription_price_changes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSubscriptionPriceChangesApi->user_subscription_price_changes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_owners_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: decision | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 

### Return type

[**UserSubscriptionPriceChangesMultiResourceDataDocument**](UserSubscriptionPriceChangesMultiResourceDataDocument.md)

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

# **user_subscription_price_changes_id_relationships_decision_get**
> UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument user_subscription_price_changes_id_relationships_decision_get(id, include=include)

Get decision relationship (\"to-one\").

Retrieves decision relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.user_subscription_price_changes_decision_single_relationship_data_document import UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument
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
    api_instance = tidal.UserSubscriptionPriceChangesApi(api_client)
    id = '1AC1yHZWFAFVjnFOn8XoXA' # str | Price change id
    include = ['decision'] # List[str] | Include related resources. Available relationships: decision (optional)

    try:
        # Get decision relationship (\"to-one\").
        api_response = api_instance.user_subscription_price_changes_id_relationships_decision_get(id, include=include)
        print("The response of UserSubscriptionPriceChangesApi->user_subscription_price_changes_id_relationships_decision_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSubscriptionPriceChangesApi->user_subscription_price_changes_id_relationships_decision_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price change id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: decision | [optional] 

### Return type

[**UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument**](UserSubscriptionPriceChangesDecisionSingleRelationshipDataDocument.md)

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

