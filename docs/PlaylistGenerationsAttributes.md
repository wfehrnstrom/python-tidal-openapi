# PlaylistGenerationsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_generated_at** | **datetime** | Datetime the playlist content this generation produced was committed (ISO 8601). Unlike progress.lastModifiedAt, which any write moves, this only moves when a generation succeeds. Omitted while a generation is still running, when it failed, and for playlists generated before generation history was recorded | [optional] 
**preference_version** | **int** | Track-preference version snapshotted by this generation | 
**progress** | [**PlaylistGenerationProgress**](PlaylistGenerationProgress.md) |  | 
**prompt** | **str** | Prompt used to create the generation; omitted for legacy generations | [optional] 
**status** | **str** | Current prompted-playlist generation status | 

## Example

```python
from tidal.models.playlist_generations_attributes import PlaylistGenerationsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsAttributes from a JSON string
playlist_generations_attributes_instance = PlaylistGenerationsAttributes.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsAttributes.to_json())

# convert the object into a dict
playlist_generations_attributes_dict = playlist_generations_attributes_instance.to_dict()
# create an instance of PlaylistGenerationsAttributes from a dict
playlist_generations_attributes_from_dict = PlaylistGenerationsAttributes.from_dict(playlist_generations_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


