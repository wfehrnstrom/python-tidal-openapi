# PlayQueuesFutureRelationshipAddOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **UUID** |  | [optional] 
**legacy_source** | [**LegacySource**](LegacySource.md) |  | [optional] 
**mode** | **str** |  | 
**position_before** | **str** |  | [optional] 
**source** | [**PlayQueuesFutureRelationshipSource**](PlayQueuesFutureRelationshipSource.md) |  | [optional] 

## Example

```python
from tidal.models.play_queues_future_relationship_add_operation_payload_meta import PlayQueuesFutureRelationshipAddOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesFutureRelationshipAddOperationPayloadMeta from a JSON string
play_queues_future_relationship_add_operation_payload_meta_instance = PlayQueuesFutureRelationshipAddOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesFutureRelationshipAddOperationPayloadMeta.to_json())

# convert the object into a dict
play_queues_future_relationship_add_operation_payload_meta_dict = play_queues_future_relationship_add_operation_payload_meta_instance.to_dict()
# create an instance of PlayQueuesFutureRelationshipAddOperationPayloadMeta from a dict
play_queues_future_relationship_add_operation_payload_meta_from_dict = PlayQueuesFutureRelationshipAddOperationPayloadMeta.from_dict(play_queues_future_relationship_add_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


