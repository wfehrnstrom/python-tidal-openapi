# CommentsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**CommentsCreateOperationPayloadDataAttributes**](CommentsCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**CommentsCreateOperationPayloadDataRelationships**](CommentsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.comments_create_operation_payload_data import CommentsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsCreateOperationPayloadData from a JSON string
comments_create_operation_payload_data_instance = CommentsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(CommentsCreateOperationPayloadData.to_json())

# convert the object into a dict
comments_create_operation_payload_data_dict = comments_create_operation_payload_data_instance.to_dict()
# create an instance of CommentsCreateOperationPayloadData from a dict
comments_create_operation_payload_data_from_dict = CommentsCreateOperationPayloadData.from_dict(comments_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


