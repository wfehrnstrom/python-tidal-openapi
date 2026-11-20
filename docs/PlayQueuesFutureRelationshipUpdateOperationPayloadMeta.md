# PlayQueuesFutureRelationshipUpdateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Relationship mutation mode. INCREMENTAL updates selected existing entries without adding or removing memberships; REPLACE_ALL replaces the complete membership and its order where applicable. Omission defaults to INCREMENTAL. | [optional] [default to 'INCREMENTAL']
**position_before** | **str** |  | 

## Example

```python
from tidal.models.play_queues_future_relationship_update_operation_payload_meta import PlayQueuesFutureRelationshipUpdateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesFutureRelationshipUpdateOperationPayloadMeta from a JSON string
play_queues_future_relationship_update_operation_payload_meta_instance = PlayQueuesFutureRelationshipUpdateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesFutureRelationshipUpdateOperationPayloadMeta.to_json())

# convert the object into a dict
play_queues_future_relationship_update_operation_payload_meta_dict = play_queues_future_relationship_update_operation_payload_meta_instance.to_dict()
# create an instance of PlayQueuesFutureRelationshipUpdateOperationPayloadMeta from a dict
play_queues_future_relationship_update_operation_payload_meta_from_dict = PlayQueuesFutureRelationshipUpdateOperationPayloadMeta.from_dict(play_queues_future_relationship_update_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


