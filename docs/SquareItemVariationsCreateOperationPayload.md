# SquareItemVariationsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SquareItemVariationsCreateOperationPayloadData**](SquareItemVariationsCreateOperationPayloadData.md) |  | 
**meta** | [**SquareItemVariationsExpectedItemRevision**](SquareItemVariationsExpectedItemRevision.md) |  | 

## Example

```python
from tidal.models.square_item_variations_create_operation_payload import SquareItemVariationsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationsCreateOperationPayload from a JSON string
square_item_variations_create_operation_payload_instance = SquareItemVariationsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationsCreateOperationPayload.to_json())

# convert the object into a dict
square_item_variations_create_operation_payload_dict = square_item_variations_create_operation_payload_instance.to_dict()
# create an instance of SquareItemVariationsCreateOperationPayload from a dict
square_item_variations_create_operation_payload_from_dict = SquareItemVariationsCreateOperationPayload.from_dict(square_item_variations_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


