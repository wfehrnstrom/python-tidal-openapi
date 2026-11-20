# UserDailyMixesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserDailyMixesRelationships**](UserDailyMixesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_daily_mixes_resource_object import UserDailyMixesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserDailyMixesResourceObject from a JSON string
user_daily_mixes_resource_object_instance = UserDailyMixesResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserDailyMixesResourceObject.to_json())

# convert the object into a dict
user_daily_mixes_resource_object_dict = user_daily_mixes_resource_object_instance.to_dict()
# create an instance of UserDailyMixesResourceObject from a dict
user_daily_mixes_resource_object_from_dict = UserDailyMixesResourceObject.from_dict(user_daily_mixes_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


