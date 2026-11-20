# PlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**reason** | **str** | Why the requested occurrence was not added: NOT_FOUND means it was not available; ALREADY_PRESENT means SKIP omitted it because the playlist already contained that resource type and id. | 
**type** | **str** |  | 

## Example

```python
from tidal.models.playlists_items_relationship_add_operation_response_meta_skipped_item import PlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem from a JSON string
playlists_items_relationship_add_operation_response_meta_skipped_item_instance = PlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem.to_json())

# convert the object into a dict
playlists_items_relationship_add_operation_response_meta_skipped_item_dict = playlists_items_relationship_add_operation_response_meta_skipped_item_instance.to_dict()
# create an instance of PlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem from a dict
playlists_items_relationship_add_operation_response_meta_skipped_item_from_dict = PlaylistsItemsRelationshipAddOperationResponseMetaSkippedItem.from_dict(playlists_items_relationship_add_operation_response_meta_skipped_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


