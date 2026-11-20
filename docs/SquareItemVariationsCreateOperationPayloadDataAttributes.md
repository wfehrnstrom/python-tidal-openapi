# SquareItemVariationsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**price** | **str** | Amount in the currency&#39;s major units | 
**stock_tracked** | **bool** |  | 

## Example

```python
from tidal.models.square_item_variations_create_operation_payload_data_attributes import SquareItemVariationsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationsCreateOperationPayloadDataAttributes from a JSON string
square_item_variations_create_operation_payload_data_attributes_instance = SquareItemVariationsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
square_item_variations_create_operation_payload_data_attributes_dict = square_item_variations_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of SquareItemVariationsCreateOperationPayloadDataAttributes from a dict
square_item_variations_create_operation_payload_data_attributes_from_dict = SquareItemVariationsCreateOperationPayloadDataAttributes.from_dict(square_item_variations_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


