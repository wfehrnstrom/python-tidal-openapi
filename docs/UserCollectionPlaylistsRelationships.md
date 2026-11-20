# UserCollectionPlaylistsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**UserCollectionPlaylistsItemsMultiRelationshipDataDocument**](UserCollectionPlaylistsItemsMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**UserCollectionPlaylistsOwnersMultiRelationshipDataDocument**](UserCollectionPlaylistsOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.user_collection_playlists_relationships import UserCollectionPlaylistsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionPlaylistsRelationships from a JSON string
user_collection_playlists_relationships_instance = UserCollectionPlaylistsRelationships.from_json(json)
# print the JSON string representation of the object
print(UserCollectionPlaylistsRelationships.to_json())

# convert the object into a dict
user_collection_playlists_relationships_dict = user_collection_playlists_relationships_instance.to_dict()
# create an instance of UserCollectionPlaylistsRelationships from a dict
user_collection_playlists_relationships_from_dict = UserCollectionPlaylistsRelationships.from_dict(user_collection_playlists_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


