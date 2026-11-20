# PlaylistGenerationProgress

Recoverable AI playlist generation progress snapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committed_track_count** | **int** |  | [optional] 
**cover_art_status** | **str** |  | 
**failure_code** | **str** |  | [optional] 
**last_modified_at** | **datetime** |  | [optional] 
**playlist_ready** | **bool** |  | 
**selected_track_count** | **int** |  | [optional] 
**stage** | **str** |  | [optional] 
**target_track_count** | **int** |  | [optional] 

## Example

```python
from tidal.models.playlist_generation_progress import PlaylistGenerationProgress

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationProgress from a JSON string
playlist_generation_progress_instance = PlaylistGenerationProgress.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationProgress.to_json())

# convert the object into a dict
playlist_generation_progress_dict = playlist_generation_progress_instance.to_dict()
# create an instance of PlaylistGenerationProgress from a dict
playlist_generation_progress_from_dict = PlaylistGenerationProgress.from_dict(playlist_generation_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


