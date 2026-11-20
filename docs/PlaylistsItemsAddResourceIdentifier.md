# PlaylistsItemsAddResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**PlaylistsItemsAddResourceIdentifierMeta**](PlaylistsItemsAddResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.playlists_items_add_resource_identifier import PlaylistsItemsAddResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsAddResourceIdentifier from a JSON string
playlists_items_add_resource_identifier_instance = PlaylistsItemsAddResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsAddResourceIdentifier.to_json())

# convert the object into a dict
playlists_items_add_resource_identifier_dict = playlists_items_add_resource_identifier_instance.to_dict()
# create an instance of PlaylistsItemsAddResourceIdentifier from a dict
playlists_items_add_resource_identifier_from_dict = PlaylistsItemsAddResourceIdentifier.from_dict(playlists_items_add_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


