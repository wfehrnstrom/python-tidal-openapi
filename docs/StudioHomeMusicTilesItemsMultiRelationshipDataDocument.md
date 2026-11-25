# StudioHomeMusicTilesItemsMultiRelationshipDataDocument

Target resource types: `albums`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[StudioHomeMusicTilesItemsResourceIdentifier]**](StudioHomeMusicTilesItemsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.studio_home_music_tiles_items_multi_relationship_data_document import StudioHomeMusicTilesItemsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of StudioHomeMusicTilesItemsMultiRelationshipDataDocument from a JSON string
studio_home_music_tiles_items_multi_relationship_data_document_instance = StudioHomeMusicTilesItemsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(StudioHomeMusicTilesItemsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
studio_home_music_tiles_items_multi_relationship_data_document_dict = studio_home_music_tiles_items_multi_relationship_data_document_instance.to_dict()
# create an instance of StudioHomeMusicTilesItemsMultiRelationshipDataDocument from a dict
studio_home_music_tiles_items_multi_relationship_data_document_from_dict = StudioHomeMusicTilesItemsMultiRelationshipDataDocument.from_dict(studio_home_music_tiles_items_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


