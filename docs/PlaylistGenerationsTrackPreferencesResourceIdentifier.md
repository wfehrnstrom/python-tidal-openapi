# PlaylistGenerationsTrackPreferencesResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**PlaylistGenerationsTrackPreferencesResourceIdentifierMeta**](PlaylistGenerationsTrackPreferencesResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.playlist_generations_track_preferences_resource_identifier import PlaylistGenerationsTrackPreferencesResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsTrackPreferencesResourceIdentifier from a JSON string
playlist_generations_track_preferences_resource_identifier_instance = PlaylistGenerationsTrackPreferencesResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsTrackPreferencesResourceIdentifier.to_json())

# convert the object into a dict
playlist_generations_track_preferences_resource_identifier_dict = playlist_generations_track_preferences_resource_identifier_instance.to_dict()
# create an instance of PlaylistGenerationsTrackPreferencesResourceIdentifier from a dict
playlist_generations_track_preferences_resource_identifier_from_dict = PlaylistGenerationsTrackPreferencesResourceIdentifier.from_dict(playlist_generations_track_preferences_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


