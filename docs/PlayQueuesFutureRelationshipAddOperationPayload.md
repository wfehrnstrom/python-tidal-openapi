# PlayQueuesFutureRelationshipAddOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlayQueuesFutureRelationshipAddOperationPayloadData]**](PlayQueuesFutureRelationshipAddOperationPayloadData.md) |  | 
**meta** | [**PlayQueuesFutureRelationshipAddOperationPayloadMeta**](PlayQueuesFutureRelationshipAddOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.play_queues_future_relationship_add_operation_payload import PlayQueuesFutureRelationshipAddOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesFutureRelationshipAddOperationPayload from a JSON string
play_queues_future_relationship_add_operation_payload_instance = PlayQueuesFutureRelationshipAddOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesFutureRelationshipAddOperationPayload.to_json())

# convert the object into a dict
play_queues_future_relationship_add_operation_payload_dict = play_queues_future_relationship_add_operation_payload_instance.to_dict()
# create an instance of PlayQueuesFutureRelationshipAddOperationPayload from a dict
play_queues_future_relationship_add_operation_payload_from_dict = PlayQueuesFutureRelationshipAddOperationPayload.from_dict(play_queues_future_relationship_add_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


