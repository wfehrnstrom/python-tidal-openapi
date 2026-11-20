# SquareItemsUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SquareItemsUpdateOperationPayloadDataAttributes**](SquareItemsUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.square_items_update_operation_payload_data import SquareItemsUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemsUpdateOperationPayloadData from a JSON string
square_items_update_operation_payload_data_instance = SquareItemsUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(SquareItemsUpdateOperationPayloadData.to_json())

# convert the object into a dict
square_items_update_operation_payload_data_dict = square_items_update_operation_payload_data_instance.to_dict()
# create an instance of SquareItemsUpdateOperationPayloadData from a dict
square_items_update_operation_payload_data_from_dict = SquareItemsUpdateOperationPayloadData.from_dict(square_items_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


