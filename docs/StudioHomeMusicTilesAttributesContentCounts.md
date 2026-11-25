# StudioHomeMusicTilesAttributesContentCounts

Totals of the folders and albums in the user's uploads, at every folder level.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**albums** | **int** | Number of albums. | 
**folders** | **int** | Number of folders. | 

## Example

```python
from tidal.models.studio_home_music_tiles_attributes_content_counts import StudioHomeMusicTilesAttributesContentCounts

# TODO update the JSON string below
json = "{}"
# create an instance of StudioHomeMusicTilesAttributesContentCounts from a JSON string
studio_home_music_tiles_attributes_content_counts_instance = StudioHomeMusicTilesAttributesContentCounts.from_json(json)
# print the JSON string representation of the object
print(StudioHomeMusicTilesAttributesContentCounts.to_json())

# convert the object into a dict
studio_home_music_tiles_attributes_content_counts_dict = studio_home_music_tiles_attributes_content_counts_instance.to_dict()
# create an instance of StudioHomeMusicTilesAttributesContentCounts from a dict
studio_home_music_tiles_attributes_content_counts_from_dict = StudioHomeMusicTilesAttributesContentCounts.from_dict(studio_home_music_tiles_attributes_content_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


