# StudioHomeMusicTilesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**StudioHomeMusicTilesAttributes**](StudioHomeMusicTilesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.studio_home_music_tiles_resource_object import StudioHomeMusicTilesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of StudioHomeMusicTilesResourceObject from a JSON string
studio_home_music_tiles_resource_object_instance = StudioHomeMusicTilesResourceObject.from_json(json)
# print the JSON string representation of the object
print(StudioHomeMusicTilesResourceObject.to_json())

# convert the object into a dict
studio_home_music_tiles_resource_object_dict = studio_home_music_tiles_resource_object_instance.to_dict()
# create an instance of StudioHomeMusicTilesResourceObject from a dict
studio_home_music_tiles_resource_object_from_dict = StudioHomeMusicTilesResourceObject.from_dict(studio_home_music_tiles_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


