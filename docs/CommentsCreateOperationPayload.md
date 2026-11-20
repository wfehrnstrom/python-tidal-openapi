# CommentsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CommentsCreateOperationPayloadData**](CommentsCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.comments_create_operation_payload import CommentsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsCreateOperationPayload from a JSON string
comments_create_operation_payload_instance = CommentsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(CommentsCreateOperationPayload.to_json())

# convert the object into a dict
comments_create_operation_payload_dict = comments_create_operation_payload_instance.to_dict()
# create an instance of CommentsCreateOperationPayload from a dict
comments_create_operation_payload_from_dict = CommentsCreateOperationPayload.from_dict(comments_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


