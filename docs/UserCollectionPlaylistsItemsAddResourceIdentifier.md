# UserCollectionPlaylistsItemsAddResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**UserCollectionPlaylistsItemsAddResourceIdentifierMeta**](UserCollectionPlaylistsItemsAddResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.user_collection_playlists_items_add_resource_identifier import UserCollectionPlaylistsItemsAddResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionPlaylistsItemsAddResourceIdentifier from a JSON string
user_collection_playlists_items_add_resource_identifier_instance = UserCollectionPlaylistsItemsAddResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(UserCollectionPlaylistsItemsAddResourceIdentifier.to_json())

# convert the object into a dict
user_collection_playlists_items_add_resource_identifier_dict = user_collection_playlists_items_add_resource_identifier_instance.to_dict()
# create an instance of UserCollectionPlaylistsItemsAddResourceIdentifier from a dict
user_collection_playlists_items_add_resource_identifier_from_dict = UserCollectionPlaylistsItemsAddResourceIdentifier.from_dict(user_collection_playlists_items_add_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


