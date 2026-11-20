# UserCollectionPlaylistsItemsMultiRelationshipDataDocument

Target resource types: `playlists`, `userCollectionFolders`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserCollectionPlaylistsItemsResourceIdentifier]**](UserCollectionPlaylistsItemsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_collection_playlists_items_multi_relationship_data_document import UserCollectionPlaylistsItemsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionPlaylistsItemsMultiRelationshipDataDocument from a JSON string
user_collection_playlists_items_multi_relationship_data_document_instance = UserCollectionPlaylistsItemsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionPlaylistsItemsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_collection_playlists_items_multi_relationship_data_document_dict = user_collection_playlists_items_multi_relationship_data_document_instance.to_dict()
# create an instance of UserCollectionPlaylistsItemsMultiRelationshipDataDocument from a dict
user_collection_playlists_items_multi_relationship_data_document_from_dict = UserCollectionPlaylistsItemsMultiRelationshipDataDocument.from_dict(user_collection_playlists_items_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


