# PlaylistGenerationSchedulesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_version** | **int** |  | 
**created_at** | **datetime** |  | 
**frequency** | **str** | Recurrence frequency defined by RFC 5545 | 
**last_modified_at** | **datetime** |  | 
**status** | **str** |  | 
**time_zone** | **str** | IANA Time Zone Database identifier used to evaluate local civil time. | 
**weekday** | **str** |  | 

## Example

```python
from tidal.models.playlist_generation_schedules_attributes import PlaylistGenerationSchedulesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationSchedulesAttributes from a JSON string
playlist_generation_schedules_attributes_instance = PlaylistGenerationSchedulesAttributes.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationSchedulesAttributes.to_json())

# convert the object into a dict
playlist_generation_schedules_attributes_dict = playlist_generation_schedules_attributes_instance.to_dict()
# create an instance of PlaylistGenerationSchedulesAttributes from a dict
playlist_generation_schedules_attributes_from_dict = PlaylistGenerationSchedulesAttributes.from_dict(playlist_generation_schedules_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


