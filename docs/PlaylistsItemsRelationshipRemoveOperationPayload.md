# PlaylistsItemsRelationshipRemoveOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlaylistsItemsRelationshipRemoveOperationPayloadData]**](PlaylistsItemsRelationshipRemoveOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.playlists_items_relationship_remove_operation_payload import PlaylistsItemsRelationshipRemoveOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsRelationshipRemoveOperationPayload from a JSON string
playlists_items_relationship_remove_operation_payload_instance = PlaylistsItemsRelationshipRemoveOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsRelationshipRemoveOperationPayload.to_json())

# convert the object into a dict
playlists_items_relationship_remove_operation_payload_dict = playlists_items_relationship_remove_operation_payload_instance.to_dict()
# create an instance of PlaylistsItemsRelationshipRemoveOperationPayload from a dict
playlists_items_relationship_remove_operation_payload_from_dict = PlaylistsItemsRelationshipRemoveOperationPayload.from_dict(playlists_items_relationship_remove_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


