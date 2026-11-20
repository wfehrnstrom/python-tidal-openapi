# PlaylistsItemsRelationshipRemoveOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**PlaylistsItemsRelationshipRemoveOperationPayloadDataMeta**](PlaylistsItemsRelationshipRemoveOperationPayloadDataMeta.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.playlists_items_relationship_remove_operation_payload_data import PlaylistsItemsRelationshipRemoveOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsRelationshipRemoveOperationPayloadData from a JSON string
playlists_items_relationship_remove_operation_payload_data_instance = PlaylistsItemsRelationshipRemoveOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsRelationshipRemoveOperationPayloadData.to_json())

# convert the object into a dict
playlists_items_relationship_remove_operation_payload_data_dict = playlists_items_relationship_remove_operation_payload_data_instance.to_dict()
# create an instance of PlaylistsItemsRelationshipRemoveOperationPayloadData from a dict
playlists_items_relationship_remove_operation_payload_data_from_dict = PlaylistsItemsRelationshipRemoveOperationPayloadData.from_dict(playlists_items_relationship_remove_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


