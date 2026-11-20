# UserCollectionPlaylistsItemsAddMultiRelationshipDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserCollectionPlaylistsItemsAddResourceIdentifier]**](UserCollectionPlaylistsItemsAddResourceIdentifier.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | [**UserCollectionPlaylistsItemsAddMultiRelationshipDataDocumentMeta**](UserCollectionPlaylistsItemsAddMultiRelationshipDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.user_collection_playlists_items_add_multi_relationship_data_document import UserCollectionPlaylistsItemsAddMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionPlaylistsItemsAddMultiRelationshipDataDocument from a JSON string
user_collection_playlists_items_add_multi_relationship_data_document_instance = UserCollectionPlaylistsItemsAddMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionPlaylistsItemsAddMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_collection_playlists_items_add_multi_relationship_data_document_dict = user_collection_playlists_items_add_multi_relationship_data_document_instance.to_dict()
# create an instance of UserCollectionPlaylistsItemsAddMultiRelationshipDataDocument from a dict
user_collection_playlists_items_add_multi_relationship_data_document_from_dict = UserCollectionPlaylistsItemsAddMultiRelationshipDataDocument.from_dict(user_collection_playlists_items_add_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


