# PriceConfigurationsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PriceConfigurationsCreateOperationPayloadData**](PriceConfigurationsCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.price_configurations_create_operation_payload import PriceConfigurationsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PriceConfigurationsCreateOperationPayload from a JSON string
price_configurations_create_operation_payload_instance = PriceConfigurationsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PriceConfigurationsCreateOperationPayload.to_json())

# convert the object into a dict
price_configurations_create_operation_payload_dict = price_configurations_create_operation_payload_instance.to_dict()
# create an instance of PriceConfigurationsCreateOperationPayload from a dict
price_configurations_create_operation_payload_from_dict = PriceConfigurationsCreateOperationPayload.from_dict(price_configurations_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


