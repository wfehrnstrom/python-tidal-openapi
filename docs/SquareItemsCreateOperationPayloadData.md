# SquareItemsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SquareItemsCreateOperationPayloadDataAttributes**](SquareItemsCreateOperationPayloadDataAttributes.md) |  | 
**lid** | **str** | Local identity available to later operations in this request | [optional] 
**relationships** | [**SquareItemsCreateOperationPayloadDataRelationships**](SquareItemsCreateOperationPayloadDataRelationships.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.square_items_create_operation_payload_data import SquareItemsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemsCreateOperationPayloadData from a JSON string
square_items_create_operation_payload_data_instance = SquareItemsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(SquareItemsCreateOperationPayloadData.to_json())

# convert the object into a dict
square_items_create_operation_payload_data_dict = square_items_create_operation_payload_data_instance.to_dict()
# create an instance of SquareItemsCreateOperationPayloadData from a dict
square_items_create_operation_payload_data_from_dict = SquareItemsCreateOperationPayloadData.from_dict(square_items_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


