# PlaylistsItemsRelationshipAddOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlaylistsItemsRelationshipAddOperationPayloadData]**](PlaylistsItemsRelationshipAddOperationPayloadData.md) |  | 
**meta** | [**PlaylistsItemsRelationshipAddOperationPayloadMeta**](PlaylistsItemsRelationshipAddOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.playlists_items_relationship_add_operation_payload import PlaylistsItemsRelationshipAddOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsRelationshipAddOperationPayload from a JSON string
playlists_items_relationship_add_operation_payload_instance = PlaylistsItemsRelationshipAddOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsRelationshipAddOperationPayload.to_json())

# convert the object into a dict
playlists_items_relationship_add_operation_payload_dict = playlists_items_relationship_add_operation_payload_instance.to_dict()
# create an instance of PlaylistsItemsRelationshipAddOperationPayload from a dict
playlists_items_relationship_add_operation_payload_from_dict = PlaylistsItemsRelationshipAddOperationPayload.from_dict(playlists_items_relationship_add_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


