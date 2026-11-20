# UserNewReleaseMixesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserNewReleaseMixesRelationships**](UserNewReleaseMixesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_new_release_mixes_resource_object import UserNewReleaseMixesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserNewReleaseMixesResourceObject from a JSON string
user_new_release_mixes_resource_object_instance = UserNewReleaseMixesResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserNewReleaseMixesResourceObject.to_json())

# convert the object into a dict
user_new_release_mixes_resource_object_dict = user_new_release_mixes_resource_object_instance.to_dict()
# create an instance of UserNewReleaseMixesResourceObject from a dict
user_new_release_mixes_resource_object_from_dict = UserNewReleaseMixesResourceObject.from_dict(user_new_release_mixes_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


