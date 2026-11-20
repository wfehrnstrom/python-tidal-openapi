# SquareItemsArtworksRelationshipUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ItemArtwork]**](ItemArtwork.md) |  | 
**meta** | [**SquareItemsArtworksRelationshipUpdateOperationPayloadMeta**](SquareItemsArtworksRelationshipUpdateOperationPayloadMeta.md) |  | 

## Example

```python
from tidal.models.square_items_artworks_relationship_update_operation_payload import SquareItemsArtworksRelationshipUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemsArtworksRelationshipUpdateOperationPayload from a JSON string
square_items_artworks_relationship_update_operation_payload_instance = SquareItemsArtworksRelationshipUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(SquareItemsArtworksRelationshipUpdateOperationPayload.to_json())

# convert the object into a dict
square_items_artworks_relationship_update_operation_payload_dict = square_items_artworks_relationship_update_operation_payload_instance.to_dict()
# create an instance of SquareItemsArtworksRelationshipUpdateOperationPayload from a dict
square_items_artworks_relationship_update_operation_payload_from_dict = SquareItemsArtworksRelationshipUpdateOperationPayload.from_dict(square_items_artworks_relationship_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


