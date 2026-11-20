# StudioHomeMusicTilesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**StudioHomeMusicTilesResourceObject**](StudioHomeMusicTilesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.studio_home_music_tiles_single_resource_data_document import StudioHomeMusicTilesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of StudioHomeMusicTilesSingleResourceDataDocument from a JSON string
studio_home_music_tiles_single_resource_data_document_instance = StudioHomeMusicTilesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(StudioHomeMusicTilesSingleResourceDataDocument.to_json())

# convert the object into a dict
studio_home_music_tiles_single_resource_data_document_dict = studio_home_music_tiles_single_resource_data_document_instance.to_dict()
# create an instance of StudioHomeMusicTilesSingleResourceDataDocument from a dict
studio_home_music_tiles_single_resource_data_document_from_dict = StudioHomeMusicTilesSingleResourceDataDocument.from_dict(studio_home_music_tiles_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


