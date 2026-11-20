# PlaylistsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | Access type | 
**bounded** | **bool** | Indicates if the playlist has a duration and set number of tracks | 
**created_at** | **datetime** | Datetime of playlist creation (ISO 8601) | 
**description** | **str** | Playlist description | [optional] 
**duration** | **str** | Duration of playlist (ISO 8601) | [optional] 
**external_links** | [**List[ExternalLink]**](ExternalLink.md) |  | 
**has_generations** | **bool** | Whether the playlist has AI generations | [optional] 
**last_modified_at** | **datetime** | Datetime of last modification of the playlist (ISO 8601) | 
**name** | **str** | Playlist name | 
**number_of_followers** | **int** | The amount of followers of the playlist | 
**number_of_items** | **int** | Number of items in the items relationship | [optional] 
**number_of_track_items** | **int** | Number of track items in the items relationship | [optional] 
**number_of_video_items** | **int** | Number of video items in the items relationship | [optional] 
**playlist_type** | **str** | The type of the playlist | 

## Example

```python
from tidal.models.playlists_attributes import PlaylistsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsAttributes from a JSON string
playlists_attributes_instance = PlaylistsAttributes.from_json(json)
# print the JSON string representation of the object
print(PlaylistsAttributes.to_json())

# convert the object into a dict
playlists_attributes_dict = playlists_attributes_instance.to_dict()
# create an instance of PlaylistsAttributes from a dict
playlists_attributes_from_dict = PlaylistsAttributes.from_dict(playlists_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


