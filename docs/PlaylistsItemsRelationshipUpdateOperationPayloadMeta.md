# PlaylistsItemsRelationshipUpdateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Relationship mutation mode. INCREMENTAL updates selected existing entries without adding or removing memberships; REPLACE_ALL replaces the complete membership and its order where applicable. Omission defaults to INCREMENTAL. | [default to 'INCREMENTAL']
**position_before** | **str** |  | 

## Example

```python
from tidal.models.playlists_items_relationship_update_operation_payload_meta import PlaylistsItemsRelationshipUpdateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsRelationshipUpdateOperationPayloadMeta from a JSON string
playlists_items_relationship_update_operation_payload_meta_instance = PlaylistsItemsRelationshipUpdateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsRelationshipUpdateOperationPayloadMeta.to_json())

# convert the object into a dict
playlists_items_relationship_update_operation_payload_meta_dict = playlists_items_relationship_update_operation_payload_meta_instance.to_dict()
# create an instance of PlaylistsItemsRelationshipUpdateOperationPayloadMeta from a dict
playlists_items_relationship_update_operation_payload_meta_from_dict = PlaylistsItemsRelationshipUpdateOperationPayloadMeta.from_dict(playlists_items_relationship_update_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


