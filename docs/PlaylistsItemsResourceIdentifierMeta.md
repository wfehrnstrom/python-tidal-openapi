# PlaylistsItemsResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_at** | **datetime** |  | [optional] 
**item_id** | **str** |  | [optional] 
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 

## Example

```python
from tidal.models.playlists_items_resource_identifier_meta import PlaylistsItemsResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsResourceIdentifierMeta from a JSON string
playlists_items_resource_identifier_meta_instance = PlaylistsItemsResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsResourceIdentifierMeta.to_json())

# convert the object into a dict
playlists_items_resource_identifier_meta_dict = playlists_items_resource_identifier_meta_instance.to_dict()
# create an instance of PlaylistsItemsResourceIdentifierMeta from a dict
playlists_items_resource_identifier_meta_from_dict = PlaylistsItemsResourceIdentifierMeta.from_dict(playlists_items_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


