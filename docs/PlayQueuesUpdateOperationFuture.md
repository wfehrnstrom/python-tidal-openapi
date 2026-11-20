# PlayQueuesUpdateOperationFuture


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlayQueuesUpdateOperationFutureData]**](PlayQueuesUpdateOperationFutureData.md) |  | 
**meta** | [**PlayQueuesUpdateOperationFutureMeta**](PlayQueuesUpdateOperationFutureMeta.md) |  | 

## Example

```python
from tidal.models.play_queues_update_operation_future import PlayQueuesUpdateOperationFuture

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesUpdateOperationFuture from a JSON string
play_queues_update_operation_future_instance = PlayQueuesUpdateOperationFuture.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesUpdateOperationFuture.to_json())

# convert the object into a dict
play_queues_update_operation_future_dict = play_queues_update_operation_future_instance.to_dict()
# create an instance of PlayQueuesUpdateOperationFuture from a dict
play_queues_update_operation_future_from_dict = PlayQueuesUpdateOperationFuture.from_dict(play_queues_update_operation_future_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


