# PlaylistsItemsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**PlaylistsItemsResourceIdentifierMeta**](PlaylistsItemsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.playlists_items_resource_identifier import PlaylistsItemsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsResourceIdentifier from a JSON string
playlists_items_resource_identifier_instance = PlaylistsItemsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsResourceIdentifier.to_json())

# convert the object into a dict
playlists_items_resource_identifier_dict = playlists_items_resource_identifier_instance.to_dict()
# create an instance of PlaylistsItemsResourceIdentifier from a dict
playlists_items_resource_identifier_from_dict = PlaylistsItemsResourceIdentifier.from_dict(playlists_items_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


