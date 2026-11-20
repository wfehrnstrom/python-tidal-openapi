# AlbumsItemsRelationshipUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AlbumsItemsRelationshipUpdateOperationPayloadData]**](AlbumsItemsRelationshipUpdateOperationPayloadData.md) |  | 
**meta** | [**AlbumsItemsRelationshipUpdateOperationPayloadMeta**](AlbumsItemsRelationshipUpdateOperationPayloadMeta.md) |  | 

## Example

```python
from tidal.models.albums_items_relationship_update_operation_payload import AlbumsItemsRelationshipUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsItemsRelationshipUpdateOperationPayload from a JSON string
albums_items_relationship_update_operation_payload_instance = AlbumsItemsRelationshipUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(AlbumsItemsRelationshipUpdateOperationPayload.to_json())

# convert the object into a dict
albums_items_relationship_update_operation_payload_dict = albums_items_relationship_update_operation_payload_instance.to_dict()
# create an instance of AlbumsItemsRelationshipUpdateOperationPayload from a dict
albums_items_relationship_update_operation_payload_from_dict = AlbumsItemsRelationshipUpdateOperationPayload.from_dict(albums_items_relationship_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


