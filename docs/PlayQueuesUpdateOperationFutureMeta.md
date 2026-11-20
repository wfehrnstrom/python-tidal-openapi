# PlayQueuesUpdateOperationFutureMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**position_before** | **str** | Required for ADD_BEFORE. | [optional] 
**source** | [**PlayQueuesFutureRelationshipSource**](PlayQueuesFutureRelationshipSource.md) |  | [optional] 

## Example

```python
from tidal.models.play_queues_update_operation_future_meta import PlayQueuesUpdateOperationFutureMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesUpdateOperationFutureMeta from a JSON string
play_queues_update_operation_future_meta_instance = PlayQueuesUpdateOperationFutureMeta.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesUpdateOperationFutureMeta.to_json())

# convert the object into a dict
play_queues_update_operation_future_meta_dict = play_queues_update_operation_future_meta_instance.to_dict()
# create an instance of PlayQueuesUpdateOperationFutureMeta from a dict
play_queues_update_operation_future_meta_from_dict = PlayQueuesUpdateOperationFutureMeta.from_dict(play_queues_update_operation_future_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


