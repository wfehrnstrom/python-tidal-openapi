# SquareItemVariationsUpdateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_revision** | **int** | Observed variation revision; does not guard the parent item or inventory quantity | 

## Example

```python
from tidal.models.square_item_variations_update_operation_payload_meta import SquareItemVariationsUpdateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationsUpdateOperationPayloadMeta from a JSON string
square_item_variations_update_operation_payload_meta_instance = SquareItemVariationsUpdateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationsUpdateOperationPayloadMeta.to_json())

# convert the object into a dict
square_item_variations_update_operation_payload_meta_dict = square_item_variations_update_operation_payload_meta_instance.to_dict()
# create an instance of SquareItemVariationsUpdateOperationPayloadMeta from a dict
square_item_variations_update_operation_payload_meta_from_dict = SquareItemVariationsUpdateOperationPayloadMeta.from_dict(square_item_variations_update_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


