# SquareItemVariationsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SquareItemVariationsCreateOperationPayloadDataAttributes**](SquareItemVariationsCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**SquareItemVariationsCreateOperationPayloadDataRelationships**](SquareItemVariationsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.square_item_variations_create_operation_payload_data import SquareItemVariationsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationsCreateOperationPayloadData from a JSON string
square_item_variations_create_operation_payload_data_instance = SquareItemVariationsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationsCreateOperationPayloadData.to_json())

# convert the object into a dict
square_item_variations_create_operation_payload_data_dict = square_item_variations_create_operation_payload_data_instance.to_dict()
# create an instance of SquareItemVariationsCreateOperationPayloadData from a dict
square_item_variations_create_operation_payload_data_from_dict = SquareItemVariationsCreateOperationPayloadData.from_dict(square_item_variations_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


