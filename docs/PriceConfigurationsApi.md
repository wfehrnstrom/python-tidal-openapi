# tidal.PriceConfigurationsApi

All URIs are relative to *https://openapi.tidal.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**price_configurations_get**](PriceConfigurationsApi.md#price_configurations_get) | **GET** /priceConfigurations | Get multiple priceConfigurations.
[**price_configurations_id_get**](PriceConfigurationsApi.md#price_configurations_id_get) | **GET** /priceConfigurations/{id} | Get single priceConfiguration.
[**price_configurations_post**](PriceConfigurationsApi.md#price_configurations_post) | **POST** /priceConfigurations | Create single priceConfiguration.


# **price_configurations_get**
> PriceConfigurationsMultiResourceDataDocument price_configurations_get(filter_id)

Get multiple priceConfigurations.

Retrieves multiple priceConfigurations by available filters, or without if applicable.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.price_configurations_multi_resource_data_document import PriceConfigurationsMultiResourceDataDocument
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
    api_instance = tidal.PriceConfigurationsApi(api_client)
    filter_id = ['filter_id_example'] # List[str] | List of price configurations IDs (e.g. `cHJpY2UtY29uZmlnLTEyMzpVUw`)

    try:
        # Get multiple priceConfigurations.
        api_response = api_instance.price_configurations_get(filter_id)
        print("The response of PriceConfigurationsApi->price_configurations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceConfigurationsApi->price_configurations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | [**List[str]**](str.md)| List of price configurations IDs (e.g. &#x60;cHJpY2UtY29uZmlnLTEyMzpVUw&#x60;) | 

### Return type

[**PriceConfigurationsMultiResourceDataDocument**](PriceConfigurationsMultiResourceDataDocument.md)

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

# **price_configurations_id_get**
> PriceConfigurationsSingleResourceDataDocument price_configurations_id_get(id)

Get single priceConfiguration.

Retrieves single priceConfiguration by id.

### Example

* OAuth Authentication (Authorization_Code_PKCE):
* OAuth Authentication (Client_Credentials):

```python
import tidal
from tidal.models.price_configurations_single_resource_data_document import PriceConfigurationsSingleResourceDataDocument
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
    api_instance = tidal.PriceConfigurationsApi(api_client)
    id = 'cHJpY2UtY29uZmlnLTEyMzpVUw' # str | Price configuration id

    try:
        # Get single priceConfiguration.
        api_response = api_instance.price_configurations_id_get(id)
        print("The response of PriceConfigurationsApi->price_configurations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceConfigurationsApi->price_configurations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price configuration id | 

### Return type

[**PriceConfigurationsSingleResourceDataDocument**](PriceConfigurationsSingleResourceDataDocument.md)

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

# **price_configurations_post**
> PriceConfigurationsCreateSingleResourceDataDocument price_configurations_post(idempotency_key=idempotency_key, price_configurations_create_operation_payload=price_configurations_create_operation_payload)

Create single priceConfiguration.

Creates a new priceConfiguration.

### Example

* OAuth Authentication (Authorization_Code_PKCE):

```python
import tidal
from tidal.models.price_configurations_create_operation_payload import PriceConfigurationsCreateOperationPayload
from tidal.models.price_configurations_create_single_resource_data_document import PriceConfigurationsCreateSingleResourceDataDocument
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
    api_instance = tidal.PriceConfigurationsApi(api_client)
    idempotency_key = '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d' # str | Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. (optional)
    price_configurations_create_operation_payload = tidal.PriceConfigurationsCreateOperationPayload() # PriceConfigurationsCreateOperationPayload |  (optional)

    try:
        # Create single priceConfiguration.
        api_response = api_instance.price_configurations_post(idempotency_key=idempotency_key, price_configurations_create_operation_payload=price_configurations_create_operation_payload)
        print("The response of PriceConfigurationsApi->price_configurations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceConfigurationsApi->price_configurations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned. | [optional] 
 **price_configurations_create_operation_payload** | [**PriceConfigurationsCreateOperationPayload**](PriceConfigurationsCreateOperationPayload.md)|  | [optional] 

### Return type

[**PriceConfigurationsCreateSingleResourceDataDocument**](PriceConfigurationsCreateSingleResourceDataDocument.md)

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

