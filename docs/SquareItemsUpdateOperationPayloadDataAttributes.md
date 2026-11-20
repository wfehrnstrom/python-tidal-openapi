# SquareItemsUpdateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Item description; an empty string removes it | [optional] 
**title** | **str** | Item title | [optional] 

## Example

```python
from tidal.models.square_items_update_operation_payload_data_attributes import SquareItemsUpdateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemsUpdateOperationPayloadDataAttributes from a JSON string
square_items_update_operation_payload_data_attributes_instance = SquareItemsUpdateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(SquareItemsUpdateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
square_items_update_operation_payload_data_attributes_dict = square_items_update_operation_payload_data_attributes_instance.to_dict()
# create an instance of SquareItemsUpdateOperationPayloadDataAttributes from a dict
square_items_update_operation_payload_data_attributes_from_dict = SquareItemsUpdateOperationPayloadDataAttributes.from_dict(square_items_update_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


