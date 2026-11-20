# PlaylistGenerationsTrackPreferencesRelationshipPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**PlaylistGenerationsTrackPreferencesRelationshipPayloadDataMeta**](PlaylistGenerationsTrackPreferencesRelationshipPayloadDataMeta.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.playlist_generations_track_preferences_relationship_payload_data import PlaylistGenerationsTrackPreferencesRelationshipPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsTrackPreferencesRelationshipPayloadData from a JSON string
playlist_generations_track_preferences_relationship_payload_data_instance = PlaylistGenerationsTrackPreferencesRelationshipPayloadData.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsTrackPreferencesRelationshipPayloadData.to_json())

# convert the object into a dict
playlist_generations_track_preferences_relationship_payload_data_dict = playlist_generations_track_preferences_relationship_payload_data_instance.to_dict()
# create an instance of PlaylistGenerationsTrackPreferencesRelationshipPayloadData from a dict
playlist_generations_track_preferences_relationship_payload_data_from_dict = PlaylistGenerationsTrackPreferencesRelationshipPayloadData.from_dict(playlist_generations_track_preferences_relationship_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


