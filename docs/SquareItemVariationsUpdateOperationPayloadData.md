# SquareItemVariationsUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SquareItemVariationsUpdateOperationPayloadDataAttributes**](SquareItemVariationsUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.square_item_variations_update_operation_payload_data import SquareItemVariationsUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationsUpdateOperationPayloadData from a JSON string
square_item_variations_update_operation_payload_data_instance = SquareItemVariationsUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationsUpdateOperationPayloadData.to_json())

# convert the object into a dict
square_item_variations_update_operation_payload_data_dict = square_item_variations_update_operation_payload_data_instance.to_dict()
# create an instance of SquareItemVariationsUpdateOperationPayloadData from a dict
square_item_variations_update_operation_payload_data_from_dict = SquareItemVariationsUpdateOperationPayloadData.from_dict(square_item_variations_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


