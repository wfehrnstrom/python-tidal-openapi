# CommentsUpdateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_offset** | **str** | End offset from the beginning of the source file (ISO 8601 duration). | [optional] 
**message** | **str** | The comment message content | [optional] 
**start_offset** | **str** | Start offset from the beginning of the source file (ISO 8601 duration). | [optional] 

## Example

```python
from tidal.models.comments_update_operation_payload_data_attributes import CommentsUpdateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsUpdateOperationPayloadDataAttributes from a JSON string
comments_update_operation_payload_data_attributes_instance = CommentsUpdateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(CommentsUpdateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
comments_update_operation_payload_data_attributes_dict = comments_update_operation_payload_data_attributes_instance.to_dict()
# create an instance of CommentsUpdateOperationPayloadDataAttributes from a dict
comments_update_operation_payload_data_attributes_from_dict = CommentsUpdateOperationPayloadDataAttributes.from_dict(comments_update_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


