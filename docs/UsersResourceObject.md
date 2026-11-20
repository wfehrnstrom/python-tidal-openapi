# UsersResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UsersAttributes**](UsersAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UsersRelationships**](UsersRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.users_resource_object import UsersResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UsersResourceObject from a JSON string
users_resource_object_instance = UsersResourceObject.from_json(json)
# print the JSON string representation of the object
print(UsersResourceObject.to_json())

# convert the object into a dict
users_resource_object_dict = users_resource_object_instance.to_dict()
# create an instance of UsersResourceObject from a dict
users_resource_object_from_dict = UsersResourceObject.from_dict(users_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


