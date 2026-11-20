# CommentsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Datetime when the comment was created (ISO 8601) | 
**end_offset** | **str** | End offset from the beginning of the source file (ISO 8601 duration) | [optional] 
**last_modified_at** | **datetime** | Datetime when the comment was last modified (ISO 8601) | 
**message** | **str** | The comment message content | 
**moderation_status** | **str** | Moderation status of the comment | 
**start_offset** | **str** | Start offset from the beginning of the source file (ISO 8601 duration) | [optional] 

## Example

```python
from tidal.models.comments_attributes import CommentsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsAttributes from a JSON string
comments_attributes_instance = CommentsAttributes.from_json(json)
# print the JSON string representation of the object
print(CommentsAttributes.to_json())

# convert the object into a dict
comments_attributes_dict = comments_attributes_instance.to_dict()
# create an instance of CommentsAttributes from a dict
comments_attributes_from_dict = CommentsAttributes.from_dict(comments_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


