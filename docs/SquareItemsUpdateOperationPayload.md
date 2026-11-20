# SquareItemsUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SquareItemsUpdateOperationPayloadData**](SquareItemsUpdateOperationPayloadData.md) |  | 
**meta** | [**SquareItemsUpdateOperationPayloadMeta**](SquareItemsUpdateOperationPayloadMeta.md) |  | 

## Example

```python
from tidal.models.square_items_update_operation_payload import SquareItemsUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemsUpdateOperationPayload from a JSON string
square_items_update_operation_payload_instance = SquareItemsUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(SquareItemsUpdateOperationPayload.to_json())

# convert the object into a dict
square_items_update_operation_payload_dict = square_items_update_operation_payload_instance.to_dict()
# create an instance of SquareItemsUpdateOperationPayload from a dict
square_items_update_operation_payload_from_dict = SquareItemsUpdateOperationPayload.from_dict(square_items_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


