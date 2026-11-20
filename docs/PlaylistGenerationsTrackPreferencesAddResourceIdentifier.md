# PlaylistGenerationsTrackPreferencesAddResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**PlaylistGenerationsTrackPreferencesAddResourceIdentifierMeta**](PlaylistGenerationsTrackPreferencesAddResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.playlist_generations_track_preferences_add_resource_identifier import PlaylistGenerationsTrackPreferencesAddResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsTrackPreferencesAddResourceIdentifier from a JSON string
playlist_generations_track_preferences_add_resource_identifier_instance = PlaylistGenerationsTrackPreferencesAddResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsTrackPreferencesAddResourceIdentifier.to_json())

# convert the object into a dict
playlist_generations_track_preferences_add_resource_identifier_dict = playlist_generations_track_preferences_add_resource_identifier_instance.to_dict()
# create an instance of PlaylistGenerationsTrackPreferencesAddResourceIdentifier from a dict
playlist_generations_track_preferences_add_resource_identifier_from_dict = PlaylistGenerationsTrackPreferencesAddResourceIdentifier.from_dict(playlist_generations_track_preferences_add_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


