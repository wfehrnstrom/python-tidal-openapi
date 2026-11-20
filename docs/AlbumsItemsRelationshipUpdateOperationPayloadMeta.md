# AlbumsItemsRelationshipUpdateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Relationship mutation mode. INCREMENTAL updates selected existing entries without adding or removing memberships; REPLACE_ALL replaces the complete membership and its order where applicable. Omission defaults to INCREMENTAL. | [optional] [default to 'INCREMENTAL']
**position_index** | **int** | 1-based index | 

## Example

```python
from tidal.models.albums_items_relationship_update_operation_payload_meta import AlbumsItemsRelationshipUpdateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsItemsRelationshipUpdateOperationPayloadMeta from a JSON string
albums_items_relationship_update_operation_payload_meta_instance = AlbumsItemsRelationshipUpdateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(AlbumsItemsRelationshipUpdateOperationPayloadMeta.to_json())

# convert the object into a dict
albums_items_relationship_update_operation_payload_meta_dict = albums_items_relationship_update_operation_payload_meta_instance.to_dict()
# create an instance of AlbumsItemsRelationshipUpdateOperationPayloadMeta from a dict
albums_items_relationship_update_operation_payload_meta_from_dict = AlbumsItemsRelationshipUpdateOperationPayloadMeta.from_dict(albums_items_relationship_update_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


