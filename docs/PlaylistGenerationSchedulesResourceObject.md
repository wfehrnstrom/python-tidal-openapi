# PlaylistGenerationSchedulesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PlaylistGenerationSchedulesAttributes**](PlaylistGenerationSchedulesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**PlaylistGenerationSchedulesRelationships**](PlaylistGenerationSchedulesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.playlist_generation_schedules_resource_object import PlaylistGenerationSchedulesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationSchedulesResourceObject from a JSON string
playlist_generation_schedules_resource_object_instance = PlaylistGenerationSchedulesResourceObject.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationSchedulesResourceObject.to_json())

# convert the object into a dict
playlist_generation_schedules_resource_object_dict = playlist_generation_schedules_resource_object_instance.to_dict()
# create an instance of PlaylistGenerationSchedulesResourceObject from a dict
playlist_generation_schedules_resource_object_from_dict = PlaylistGenerationSchedulesResourceObject.from_dict(playlist_generation_schedules_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


