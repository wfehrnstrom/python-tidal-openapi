# CommentSummariesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**CommentSummariesAttributes**](CommentSummariesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**CommentSummariesRelationships**](CommentSummariesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.comment_summaries_resource_object import CommentSummariesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of CommentSummariesResourceObject from a JSON string
comment_summaries_resource_object_instance = CommentSummariesResourceObject.from_json(json)
# print the JSON string representation of the object
print(CommentSummariesResourceObject.to_json())

# convert the object into a dict
comment_summaries_resource_object_dict = comment_summaries_resource_object_instance.to_dict()
# create an instance of CommentSummariesResourceObject from a dict
comment_summaries_resource_object_from_dict = CommentSummariesResourceObject.from_dict(comment_summaries_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


