# PlaylistGenerationSchedulesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playlist** | [**PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument**](PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.playlist_generation_schedules_relationships import PlaylistGenerationSchedulesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationSchedulesRelationships from a JSON string
playlist_generation_schedules_relationships_instance = PlaylistGenerationSchedulesRelationships.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationSchedulesRelationships.to_json())

# convert the object into a dict
playlist_generation_schedules_relationships_dict = playlist_generation_schedules_relationships_instance.to_dict()
# create an instance of PlaylistGenerationSchedulesRelationships from a dict
playlist_generation_schedules_relationships_from_dict = PlaylistGenerationSchedulesRelationships.from_dict(playlist_generation_schedules_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


