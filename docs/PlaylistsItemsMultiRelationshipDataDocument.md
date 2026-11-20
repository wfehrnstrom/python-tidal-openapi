# PlaylistsItemsMultiRelationshipDataDocument

Target resource types: `tracks`, `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlaylistsItemsResourceIdentifier]**](PlaylistsItemsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlists_items_multi_relationship_data_document import PlaylistsItemsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsMultiRelationshipDataDocument from a JSON string
playlists_items_multi_relationship_data_document_instance = PlaylistsItemsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
playlists_items_multi_relationship_data_document_dict = playlists_items_multi_relationship_data_document_instance.to_dict()
# create an instance of PlaylistsItemsMultiRelationshipDataDocument from a dict
playlists_items_multi_relationship_data_document_from_dict = PlaylistsItemsMultiRelationshipDataDocument.from_dict(playlists_items_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


