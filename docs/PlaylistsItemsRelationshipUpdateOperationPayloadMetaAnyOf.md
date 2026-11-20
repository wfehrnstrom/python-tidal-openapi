# PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Relationship mutation mode. INCREMENTAL updates selected existing entries without adding or removing memberships; REPLACE_ALL replaces the complete membership and its order where applicable. Omission defaults to INCREMENTAL. | [optional] [default to 'INCREMENTAL']
**position_before** | **str** |  | 

## Example

```python
from tidal.models.playlists_items_relationship_update_operation_payload_meta_any_of import PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf from a JSON string
playlists_items_relationship_update_operation_payload_meta_any_of_instance = PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf.to_json())

# convert the object into a dict
playlists_items_relationship_update_operation_payload_meta_any_of_dict = playlists_items_relationship_update_operation_payload_meta_any_of_instance.to_dict()
# create an instance of PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf from a dict
playlists_items_relationship_update_operation_payload_meta_any_of_from_dict = PlaylistsItemsRelationshipUpdateOperationPayloadMetaAnyOf.from_dict(playlists_items_relationship_update_operation_payload_meta_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


