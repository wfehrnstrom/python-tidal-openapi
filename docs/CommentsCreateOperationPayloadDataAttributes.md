# CommentsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_offset** | **str** | End offset from the beginning of the source file (ISO 8601 duration). | [optional] 
**message** | **str** | The comment message content | 
**start_offset** | **str** | Start offset from the beginning of the source file (ISO 8601 duration). | [optional] 

## Example

```python
from tidal.models.comments_create_operation_payload_data_attributes import CommentsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsCreateOperationPayloadDataAttributes from a JSON string
comments_create_operation_payload_data_attributes_instance = CommentsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(CommentsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
comments_create_operation_payload_data_attributes_dict = comments_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of CommentsCreateOperationPayloadDataAttributes from a dict
comments_create_operation_payload_data_attributes_from_dict = CommentsCreateOperationPayloadDataAttributes.from_dict(comments_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


