# PlaylistsItemsRelationshipUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlaylistsItemsRelationshipUpdateOperationPayloadData]**](PlaylistsItemsRelationshipUpdateOperationPayloadData.md) |  | 
**meta** | [**PlaylistsItemsRelationshipUpdateOperationPayloadMeta**](PlaylistsItemsRelationshipUpdateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.playlists_items_relationship_update_operation_payload import PlaylistsItemsRelationshipUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsRelationshipUpdateOperationPayload from a JSON string
playlists_items_relationship_update_operation_payload_instance = PlaylistsItemsRelationshipUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsRelationshipUpdateOperationPayload.to_json())

# convert the object into a dict
playlists_items_relationship_update_operation_payload_dict = playlists_items_relationship_update_operation_payload_instance.to_dict()
# create an instance of PlaylistsItemsRelationshipUpdateOperationPayload from a dict
playlists_items_relationship_update_operation_payload_from_dict = PlaylistsItemsRelationshipUpdateOperationPayload.from_dict(playlists_items_relationship_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


