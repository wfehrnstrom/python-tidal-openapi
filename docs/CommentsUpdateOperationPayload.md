# CommentsUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CommentsUpdateOperationPayloadData**](CommentsUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.comments_update_operation_payload import CommentsUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsUpdateOperationPayload from a JSON string
comments_update_operation_payload_instance = CommentsUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(CommentsUpdateOperationPayload.to_json())

# convert the object into a dict
comments_update_operation_payload_dict = comments_update_operation_payload_instance.to_dict()
# create an instance of CommentsUpdateOperationPayload from a dict
comments_update_operation_payload_from_dict = CommentsUpdateOperationPayload.from_dict(comments_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


