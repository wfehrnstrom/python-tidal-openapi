# GroupsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**GroupsAttributes**](GroupsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.groups_resource_object import GroupsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsResourceObject from a JSON string
groups_resource_object_instance = GroupsResourceObject.from_json(json)
# print the JSON string representation of the object
print(GroupsResourceObject.to_json())

# convert the object into a dict
groups_resource_object_dict = groups_resource_object_instance.to_dict()
# create an instance of GroupsResourceObject from a dict
groups_resource_object_from_dict = GroupsResourceObject.from_dict(groups_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


