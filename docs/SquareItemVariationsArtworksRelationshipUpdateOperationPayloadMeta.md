# SquareItemVariationsArtworksRelationshipUpdateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_revision** | **int** | Observed variation revision, read from attributes.revision or the relationship&#39;s meta.revision; a stale revision returns 409 and changes nothing. Does not guard the parent item, sibling variations or inventory quantity | 
**mode** | **str** | Relationship mutation mode. INCREMENTAL updates selected existing entries without adding or removing memberships; REPLACE_ALL replaces the complete membership and its order where applicable. Omission defaults to REPLACE_ALL. | [optional] [default to 'REPLACE_ALL']

## Example

```python
from tidal.models.square_item_variations_artworks_relationship_update_operation_payload_meta import SquareItemVariationsArtworksRelationshipUpdateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationsArtworksRelationshipUpdateOperationPayloadMeta from a JSON string
square_item_variations_artworks_relationship_update_operation_payload_meta_instance = SquareItemVariationsArtworksRelationshipUpdateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationsArtworksRelationshipUpdateOperationPayloadMeta.to_json())

# convert the object into a dict
square_item_variations_artworks_relationship_update_operation_payload_meta_dict = square_item_variations_artworks_relationship_update_operation_payload_meta_instance.to_dict()
# create an instance of SquareItemVariationsArtworksRelationshipUpdateOperationPayloadMeta from a dict
square_item_variations_artworks_relationship_update_operation_payload_meta_from_dict = SquareItemVariationsArtworksRelationshipUpdateOperationPayloadMeta.from_dict(square_item_variations_artworks_relationship_update_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


