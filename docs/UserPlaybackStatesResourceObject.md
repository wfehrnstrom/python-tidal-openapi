# UserPlaybackStatesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserPlaybackStatesAttributes**](UserPlaybackStatesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserPlaybackStatesRelationships**](UserPlaybackStatesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_playback_states_resource_object import UserPlaybackStatesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlaybackStatesResourceObject from a JSON string
user_playback_states_resource_object_instance = UserPlaybackStatesResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserPlaybackStatesResourceObject.to_json())

# convert the object into a dict
user_playback_states_resource_object_dict = user_playback_states_resource_object_instance.to_dict()
# create an instance of UserPlaybackStatesResourceObject from a dict
user_playback_states_resource_object_from_dict = UserPlaybackStatesResourceObject.from_dict(user_playback_states_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


