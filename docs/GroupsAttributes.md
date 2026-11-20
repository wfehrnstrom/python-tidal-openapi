# GroupsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Group name | 

## Example

```python
from tidal.models.groups_attributes import GroupsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsAttributes from a JSON string
groups_attributes_instance = GroupsAttributes.from_json(json)
# print the JSON string representation of the object
print(GroupsAttributes.to_json())

# convert the object into a dict
groups_attributes_dict = groups_attributes_instance.to_dict()
# create an instance of GroupsAttributes from a dict
groups_attributes_from_dict = GroupsAttributes.from_dict(groups_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


