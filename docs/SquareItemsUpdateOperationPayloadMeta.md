# SquareItemsUpdateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_revision** | **int** | Catalog revision read by the editor; stale revisions return 409 | 

## Example

```python
from tidal.models.square_items_update_operation_payload_meta import SquareItemsUpdateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemsUpdateOperationPayloadMeta from a JSON string
square_items_update_operation_payload_meta_instance = SquareItemsUpdateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(SquareItemsUpdateOperationPayloadMeta.to_json())

# convert the object into a dict
square_items_update_operation_payload_meta_dict = square_items_update_operation_payload_meta_instance.to_dict()
# create an instance of SquareItemsUpdateOperationPayloadMeta from a dict
square_items_update_operation_payload_meta_from_dict = SquareItemsUpdateOperationPayloadMeta.from_dict(square_items_update_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


