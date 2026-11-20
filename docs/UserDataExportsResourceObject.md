# UserDataExportsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserDataExportsAttributes**](UserDataExportsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserDataExportsRelationships**](UserDataExportsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_data_exports_resource_object import UserDataExportsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportsResourceObject from a JSON string
user_data_exports_resource_object_instance = UserDataExportsResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserDataExportsResourceObject.to_json())

# convert the object into a dict
user_data_exports_resource_object_dict = user_data_exports_resource_object_instance.to_dict()
# create an instance of UserDataExportsResourceObject from a dict
user_data_exports_resource_object_from_dict = UserDataExportsResourceObject.from_dict(user_data_exports_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


