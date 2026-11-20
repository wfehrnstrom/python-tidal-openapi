# PlaylistGenerationsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_generation** | [**PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument**](PlaylistGenerationsBaseGenerationSingleRelationshipDataDocument.md) |  | [optional] 
**playlist** | [**PlaylistGenerationsPlaylistSingleRelationshipDataDocument**](PlaylistGenerationsPlaylistSingleRelationshipDataDocument.md) |  | [optional] 
**track_preferences** | [**PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument**](PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.playlist_generations_relationships import PlaylistGenerationsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsRelationships from a JSON string
playlist_generations_relationships_instance = PlaylistGenerationsRelationships.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsRelationships.to_json())

# convert the object into a dict
playlist_generations_relationships_dict = playlist_generations_relationships_instance.to_dict()
# create an instance of PlaylistGenerationsRelationships from a dict
playlist_generations_relationships_from_dict = PlaylistGenerationsRelationships.from_dict(playlist_generations_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


