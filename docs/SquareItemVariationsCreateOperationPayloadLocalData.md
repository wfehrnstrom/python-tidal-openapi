# SquareItemVariationsCreateOperationPayloadLocalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SquareItemVariationsCreateOperationPayloadDataAttributes**](SquareItemVariationsCreateOperationPayloadDataAttributes.md) |  | 
**lid** | **str** | Local identity available to later operations in this request | [optional] 
**relationships** | [**SquareItemVariationsCreateOperationPayloadLocalDataRelationships**](SquareItemVariationsCreateOperationPayloadLocalDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.square_item_variations_create_operation_payload_local_data import SquareItemVariationsCreateOperationPayloadLocalData

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationsCreateOperationPayloadLocalData from a JSON string
square_item_variations_create_operation_payload_local_data_instance = SquareItemVariationsCreateOperationPayloadLocalData.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationsCreateOperationPayloadLocalData.to_json())

# convert the object into a dict
square_item_variations_create_operation_payload_local_data_dict = square_item_variations_create_operation_payload_local_data_instance.to_dict()
# create an instance of SquareItemVariationsCreateOperationPayloadLocalData from a dict
square_item_variations_create_operation_payload_local_data_from_dict = SquareItemVariationsCreateOperationPayloadLocalData.from_dict(square_item_variations_create_operation_payload_local_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


