# SquareItemsVariationsRelationshipUpdateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_revision** | **int** |  | 
**mode** | **str** | Relationship mutation mode. INCREMENTAL updates selected existing entries without adding or removing memberships; REPLACE_ALL replaces the complete membership and its order where applicable. Omission defaults to INCREMENTAL. | [optional] [default to 'INCREMENTAL']
**position_before** | **str** | Variation before which the selected block is placed; omission appends | [optional] 

## Example

```python
from tidal.models.square_items_variations_relationship_update_operation_payload_meta import SquareItemsVariationsRelationshipUpdateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemsVariationsRelationshipUpdateOperationPayloadMeta from a JSON string
square_items_variations_relationship_update_operation_payload_meta_instance = SquareItemsVariationsRelationshipUpdateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(SquareItemsVariationsRelationshipUpdateOperationPayloadMeta.to_json())

# convert the object into a dict
square_items_variations_relationship_update_operation_payload_meta_dict = square_items_variations_relationship_update_operation_payload_meta_instance.to_dict()
# create an instance of SquareItemsVariationsRelationshipUpdateOperationPayloadMeta from a dict
square_items_variations_relationship_update_operation_payload_meta_from_dict = SquareItemsVariationsRelationshipUpdateOperationPayloadMeta.from_dict(square_items_variations_relationship_update_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


