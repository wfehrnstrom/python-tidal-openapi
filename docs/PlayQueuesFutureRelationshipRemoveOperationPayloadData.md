# PlayQueuesFutureRelationshipRemoveOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**PlayQueuesFutureRelationshipRemoveOperationPayloadDataMeta**](PlayQueuesFutureRelationshipRemoveOperationPayloadDataMeta.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.play_queues_future_relationship_remove_operation_payload_data import PlayQueuesFutureRelationshipRemoveOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesFutureRelationshipRemoveOperationPayloadData from a JSON string
play_queues_future_relationship_remove_operation_payload_data_instance = PlayQueuesFutureRelationshipRemoveOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesFutureRelationshipRemoveOperationPayloadData.to_json())

# convert the object into a dict
play_queues_future_relationship_remove_operation_payload_data_dict = play_queues_future_relationship_remove_operation_payload_data_instance.to_dict()
# create an instance of PlayQueuesFutureRelationshipRemoveOperationPayloadData from a dict
play_queues_future_relationship_remove_operation_payload_data_from_dict = PlayQueuesFutureRelationshipRemoveOperationPayloadData.from_dict(play_queues_future_relationship_remove_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


