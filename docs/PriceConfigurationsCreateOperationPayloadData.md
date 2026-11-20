# PriceConfigurationsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PriceConfigurationsCreateOperationPayloadDataAttributes**](PriceConfigurationsCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**PriceConfigurationsCreateOperationPayloadDataRelationships**](PriceConfigurationsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.price_configurations_create_operation_payload_data import PriceConfigurationsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of PriceConfigurationsCreateOperationPayloadData from a JSON string
price_configurations_create_operation_payload_data_instance = PriceConfigurationsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(PriceConfigurationsCreateOperationPayloadData.to_json())

# convert the object into a dict
price_configurations_create_operation_payload_data_dict = price_configurations_create_operation_payload_data_instance.to_dict()
# create an instance of PriceConfigurationsCreateOperationPayloadData from a dict
price_configurations_create_operation_payload_data_from_dict = PriceConfigurationsCreateOperationPayloadData.from_dict(price_configurations_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


