# CommentsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**CommentsAttributes**](CommentsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**CommentsRelationships**](CommentsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.comments_resource_object import CommentsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsResourceObject from a JSON string
comments_resource_object_instance = CommentsResourceObject.from_json(json)
# print the JSON string representation of the object
print(CommentsResourceObject.to_json())

# convert the object into a dict
comments_resource_object_dict = comments_resource_object_instance.to_dict()
# create an instance of CommentsResourceObject from a dict
comments_resource_object_from_dict = CommentsResourceObject.from_dict(comments_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


