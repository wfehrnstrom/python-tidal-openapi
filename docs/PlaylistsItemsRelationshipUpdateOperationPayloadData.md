# PlaylistsItemsRelationshipUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**PlaylistsItemsRelationshipUpdateOperationPayloadDataMeta**](PlaylistsItemsRelationshipUpdateOperationPayloadDataMeta.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.playlists_items_relationship_update_operation_payload_data import PlaylistsItemsRelationshipUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsRelationshipUpdateOperationPayloadData from a JSON string
playlists_items_relationship_update_operation_payload_data_instance = PlaylistsItemsRelationshipUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsRelationshipUpdateOperationPayloadData.to_json())

# convert the object into a dict
playlists_items_relationship_update_operation_payload_data_dict = playlists_items_relationship_update_operation_payload_data_instance.to_dict()
# create an instance of PlaylistsItemsRelationshipUpdateOperationPayloadData from a dict
playlists_items_relationship_update_operation_payload_data_from_dict = PlaylistsItemsRelationshipUpdateOperationPayloadData.from_dict(playlists_items_relationship_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


