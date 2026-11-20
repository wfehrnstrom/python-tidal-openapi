# tidal.SubscriptionPriceChangeDecisionsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_price_change_decisions_get**](SubscriptionPriceChangeDecisionsApi.md#subscription_price_change_decisions_get) | **GET** /subscriptionPriceChangeDecisions | Get multiple subscriptionPriceChangeDecisions.
[**subscription_price_change_decisions_id_patch**](SubscriptionPriceChangeDecisionsApi.md#subscription_price_change_decisions_id_patch) | **PATCH** /subscriptionPriceChangeDecisions/{id} | Update single subscriptionPriceChangeDecision.
[**subscription_price_change_decisions_id_relationships_price_change_get**](SubscriptionPriceChangeDecisionsApi.md#subscription_price_change_decisions_id_relationships_price_change_get) | **GET** /subscriptionPriceChangeDecisions/{id}/relationships/priceChange | Get priceChange relationship (\&quot;to-one\&quot;).
[**subscription_price_change_decisions_post**](SubscriptionPriceChangeDecisionsApi.md#subscription_price_change_decisions_post) | **POST** /subscriptionPriceChangeDecisions | Create single subscriptionPriceChangeDecision.


# **subscription_price_change_decisions_get**
> SubscriptionPriceChangeDecisionsMultiResourceDataDocument subscription_price_change_decisions_get(filter_owners_id, include=include, include_linkage=include_linkage)

Get multiple subscriptionPriceChangeDecisions.

Retrieves multiple subscriptionPriceChangeDecisions by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.subscription_price_change_decisions_multi_resource_data_document import SubscriptionPriceChangeDecisionsMultiResourceDataDocument
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
    api_instance = tidal.SubscriptionPriceChangeDecisionsApi(api_client)
    filter_owners_id = ['filter_owners_id_example'] # List[str] | User id. Also accepts `me`.
    include = ['priceChange'] # List[str] | Include related resources. Available relationships: priceChange (optional)
    include_linkage = ['include_linkage_example'] # List[str] | Comma-separated direct relationships to return as linkage only, without related content. (optional)

    try:
        # Get multiple subscriptionPriceChangeDecisions.
        api_response = api_instance.subscription_price_change_decisions_get(filter_owners_id, include=include, include_linkage=include_linkage)
        print("The response of SubscriptionPriceChangeDecisionsApi->subscription_price_change_decisions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPriceChangeDecisionsApi->subscription_price_change_decisions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_owners_id** | [**List[str]**](str.md)| User id. Also accepts &#x60;me&#x60;. | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: priceChange | [optional] 
 **include_linkage** | [**List[str]**](str.md)| Comma-separated direct relationships to return as linkage only, without related content. | [optional] 

### Return type

[**SubscriptionPriceChangeDecisionsMultiResourceDataDocument**](SubscriptionPriceChangeDecisionsMultiResourceDataDocument.md)

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

# **subscription_price_change_decisions_id_patch**
> SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument subscription_price_change_decisions_id_patch(id, idempotency_key=idempotency_key, subscription_price_change_decisions_update_operation_payload=subscription_price_change_decisions_update_operation_payload)

Update single subscriptionPriceChangeDecision.

Updates existing subscriptionPriceChangeDecision.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.subscription_price_change_decisions_update_operation_payload import SubscriptionPriceChangeDecisionsUpdateOperationPayload
from tidal.models.subscription_price_change_decisions_update_single_resource_data_document import SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument
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
    api_instance = tidal.SubscriptionPriceChangeDecisionsApi(api_client)
    id = '1AC1yHZWFAFVjnFOn8XoXA' # str | Price change decision id
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    subscription_price_change_decisions_update_operation_payload = tidal.SubscriptionPriceChangeDecisionsUpdateOperationPayload() # SubscriptionPriceChangeDecisionsUpdateOperationPayload |  (optional)

    try:
        # Update single subscriptionPriceChangeDecision.
        api_response = api_instance.subscription_price_change_decisions_id_patch(id, idempotency_key=idempotency_key, subscription_price_change_decisions_update_operation_payload=subscription_price_change_decisions_update_operation_payload)
        print("The response of SubscriptionPriceChangeDecisionsApi->subscription_price_change_decisions_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPriceChangeDecisionsApi->subscription_price_change_decisions_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price change decision id | 
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **subscription_price_change_decisions_update_operation_payload** | [**SubscriptionPriceChangeDecisionsUpdateOperationPayload**](SubscriptionPriceChangeDecisionsUpdateOperationPayload.md)|  | [optional] 

### Return type

[**SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument**](SubscriptionPriceChangeDecisionsUpdateSingleResourceDataDocument.md)

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

# **subscription_price_change_decisions_id_relationships_price_change_get**
> SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument subscription_price_change_decisions_id_relationships_price_change_get(id, include=include)

Get priceChange relationship (\"to-one\").

Retrieves priceChange relationship.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.subscription_price_change_decisions_price_change_single_relationship_data_document import SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument
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
    api_instance = tidal.SubscriptionPriceChangeDecisionsApi(api_client)
    id = '1AC1yHZWFAFVjnFOn8XoXA' # str | Price change decision id
    include = ['priceChange'] # List[str] | Include related resources. Available relationships: priceChange (optional)

    try:
        # Get priceChange relationship (\"to-one\").
        api_response = api_instance.subscription_price_change_decisions_id_relationships_price_change_get(id, include=include)
        print("The response of SubscriptionPriceChangeDecisionsApi->subscription_price_change_decisions_id_relationships_price_change_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPriceChangeDecisionsApi->subscription_price_change_decisions_id_relationships_price_change_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price change decision id | 
 **include** | [**List[str]**](str.md)| Include related resources. Available relationships: priceChange | [optional] 

### Return type

[**SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument**](SubscriptionPriceChangeDecisionsPriceChangeSingleRelationshipDataDocument.md)

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

# **subscription_price_change_decisions_post**
> SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument subscription_price_change_decisions_post(idempotency_key=idempotency_key, subscription_price_change_decisions_create_operation_payload=subscription_price_change_decisions_create_operation_payload)

Create single subscriptionPriceChangeDecision.

Creates a new subscriptionPriceChangeDecision.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.subscription_price_change_decisions_create_operation_payload import SubscriptionPriceChangeDecisionsCreateOperationPayload
from tidal.models.subscription_price_change_decisions_create_single_resource_data_document import SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument
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
    api_instance = tidal.SubscriptionPriceChangeDecisionsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    subscription_price_change_decisions_create_operation_payload = tidal.SubscriptionPriceChangeDecisionsCreateOperationPayload() # SubscriptionPriceChangeDecisionsCreateOperationPayload |  (optional)

    try:
        # Create single subscriptionPriceChangeDecision.
        api_response = api_instance.subscription_price_change_decisions_post(idempotency_key=idempotency_key, subscription_price_change_decisions_create_operation_payload=subscription_price_change_decisions_create_operation_payload)
        print("The response of SubscriptionPriceChangeDecisionsApi->subscription_price_change_decisions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPriceChangeDecisionsApi->subscription_price_change_decisions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **subscription_price_change_decisions_create_operation_payload** | [**SubscriptionPriceChangeDecisionsCreateOperationPayload**](SubscriptionPriceChangeDecisionsCreateOperationPayload.md)|  | [optional] 

### Return type

[**SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument**](SubscriptionPriceChangeDecisionsCreateSingleResourceDataDocument.md)

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

