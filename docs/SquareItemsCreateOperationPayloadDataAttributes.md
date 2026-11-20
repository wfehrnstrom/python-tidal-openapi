# SquareItemsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Item description | [optional] 
**title** | **str** | Item title | 

## Example

```python
from tidal.models.square_items_create_operation_payload_data_attributes import SquareItemsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemsCreateOperationPayloadDataAttributes from a JSON string
square_items_create_operation_payload_data_attributes_instance = SquareItemsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(SquareItemsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
square_items_create_operation_payload_data_attributes_dict = square_items_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of SquareItemsCreateOperationPayloadDataAttributes from a dict
square_items_create_operation_payload_data_attributes_from_dict = SquareItemsCreateOperationPayloadDataAttributes.from_dict(square_items_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


