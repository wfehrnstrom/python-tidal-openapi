# PlaylistsItemsRelationshipAddOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**PlaylistsItemsRelationshipAddOperationPayloadDataMeta**](PlaylistsItemsRelationshipAddOperationPayloadDataMeta.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.playlists_items_relationship_add_operation_payload_data import PlaylistsItemsRelationshipAddOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsRelationshipAddOperationPayloadData from a JSON string
playlists_items_relationship_add_operation_payload_data_instance = PlaylistsItemsRelationshipAddOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsRelationshipAddOperationPayloadData.to_json())

# convert the object into a dict
playlists_items_relationship_add_operation_payload_data_dict = playlists_items_relationship_add_operation_payload_data_instance.to_dict()
# create an instance of PlaylistsItemsRelationshipAddOperationPayloadData from a dict
playlists_items_relationship_add_operation_payload_data_from_dict = PlaylistsItemsRelationshipAddOperationPayloadData.from_dict(playlists_items_relationship_add_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


