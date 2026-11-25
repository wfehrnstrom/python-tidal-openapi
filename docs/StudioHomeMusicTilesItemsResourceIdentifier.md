# StudioHomeMusicTilesItemsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**StudioHomeMusicTilesItemsResourceIdentifierMeta**](StudioHomeMusicTilesItemsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.studio_home_music_tiles_items_resource_identifier import StudioHomeMusicTilesItemsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of StudioHomeMusicTilesItemsResourceIdentifier from a JSON string
studio_home_music_tiles_items_resource_identifier_instance = StudioHomeMusicTilesItemsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(StudioHomeMusicTilesItemsResourceIdentifier.to_json())

# convert the object into a dict
studio_home_music_tiles_items_resource_identifier_dict = studio_home_music_tiles_items_resource_identifier_instance.to_dict()
# create an instance of StudioHomeMusicTilesItemsResourceIdentifier from a dict
studio_home_music_tiles_items_resource_identifier_from_dict = StudioHomeMusicTilesItemsResourceIdentifier.from_dict(studio_home_music_tiles_items_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


