# CommentsUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**CommentsUpdateOperationPayloadDataAttributes**](CommentsUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.comments_update_operation_payload_data import CommentsUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsUpdateOperationPayloadData from a JSON string
comments_update_operation_payload_data_instance = CommentsUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(CommentsUpdateOperationPayloadData.to_json())

# convert the object into a dict
comments_update_operation_payload_data_dict = comments_update_operation_payload_data_instance.to_dict()
# create an instance of CommentsUpdateOperationPayloadData from a dict
comments_update_operation_payload_data_from_dict = CommentsUpdateOperationPayloadData.from_dict(comments_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


