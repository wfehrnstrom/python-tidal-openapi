# PlaylistGenerationsTrackPreferencesUpdateResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**PlaylistGenerationsTrackPreferencesUpdateResourceIdentifierMeta**](PlaylistGenerationsTrackPreferencesUpdateResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.playlist_generations_track_preferences_update_resource_identifier import PlaylistGenerationsTrackPreferencesUpdateResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsTrackPreferencesUpdateResourceIdentifier from a JSON string
playlist_generations_track_preferences_update_resource_identifier_instance = PlaylistGenerationsTrackPreferencesUpdateResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsTrackPreferencesUpdateResourceIdentifier.to_json())

# convert the object into a dict
playlist_generations_track_preferences_update_resource_identifier_dict = playlist_generations_track_preferences_update_resource_identifier_instance.to_dict()
# create an instance of PlaylistGenerationsTrackPreferencesUpdateResourceIdentifier from a dict
playlist_generations_track_preferences_update_resource_identifier_from_dict = PlaylistGenerationsTrackPreferencesUpdateResourceIdentifier.from_dict(playlist_generations_track_preferences_update_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


