# UserOfflineMixesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserOfflineMixesRelationships**](UserOfflineMixesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_offline_mixes_resource_object import UserOfflineMixesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserOfflineMixesResourceObject from a JSON string
user_offline_mixes_resource_object_instance = UserOfflineMixesResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserOfflineMixesResourceObject.to_json())

# convert the object into a dict
user_offline_mixes_resource_object_dict = user_offline_mixes_resource_object_instance.to_dict()
# create an instance of UserOfflineMixesResourceObject from a dict
user_offline_mixes_resource_object_from_dict = UserOfflineMixesResourceObject.from_dict(user_offline_mixes_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


