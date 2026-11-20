# PlayQueuesFutureRelationshipUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlayQueuesFutureRelationshipUpdateOperationPayloadData]**](PlayQueuesFutureRelationshipUpdateOperationPayloadData.md) |  | 
**meta** | [**PlayQueuesFutureRelationshipUpdateOperationPayloadMeta**](PlayQueuesFutureRelationshipUpdateOperationPayloadMeta.md) |  | 

## Example

```python
from tidal.models.play_queues_future_relationship_update_operation_payload import PlayQueuesFutureRelationshipUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesFutureRelationshipUpdateOperationPayload from a JSON string
play_queues_future_relationship_update_operation_payload_instance = PlayQueuesFutureRelationshipUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesFutureRelationshipUpdateOperationPayload.to_json())

# convert the object into a dict
play_queues_future_relationship_update_operation_payload_dict = play_queues_future_relationship_update_operation_payload_instance.to_dict()
# create an instance of PlayQueuesFutureRelationshipUpdateOperationPayload from a dict
play_queues_future_relationship_update_operation_payload_from_dict = PlayQueuesFutureRelationshipUpdateOperationPayload.from_dict(play_queues_future_relationship_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


