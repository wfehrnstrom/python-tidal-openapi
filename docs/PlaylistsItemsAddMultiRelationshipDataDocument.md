# PlaylistsItemsAddMultiRelationshipDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlaylistsItemsAddResourceIdentifier]**](PlaylistsItemsAddResourceIdentifier.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | [**PlaylistsItemsAddMultiRelationshipDataDocumentMeta**](PlaylistsItemsAddMultiRelationshipDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.playlists_items_add_multi_relationship_data_document import PlaylistsItemsAddMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsAddMultiRelationshipDataDocument from a JSON string
playlists_items_add_multi_relationship_data_document_instance = PlaylistsItemsAddMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsAddMultiRelationshipDataDocument.to_json())

# convert the object into a dict
playlists_items_add_multi_relationship_data_document_dict = playlists_items_add_multi_relationship_data_document_instance.to_dict()
# create an instance of PlaylistsItemsAddMultiRelationshipDataDocument from a dict
playlists_items_add_multi_relationship_data_document_from_dict = PlaylistsItemsAddMultiRelationshipDataDocument.from_dict(playlists_items_add_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


