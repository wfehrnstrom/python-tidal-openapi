# PlayQueuesUpdateOperationCurrentMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Queue item identifier; required for ITEM. | [optional] 
**mode** | **str** | FIRST_FUTURE_ITEM follows shuffle/repeat; no-op when future is empty. | 

## Example

```python
from tidal.models.play_queues_update_operation_current_meta import PlayQueuesUpdateOperationCurrentMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesUpdateOperationCurrentMeta from a JSON string
play_queues_update_operation_current_meta_instance = PlayQueuesUpdateOperationCurrentMeta.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesUpdateOperationCurrentMeta.to_json())

# convert the object into a dict
play_queues_update_operation_current_meta_dict = play_queues_update_operation_current_meta_instance.to_dict()
# create an instance of PlayQueuesUpdateOperationCurrentMeta from a dict
play_queues_update_operation_current_meta_from_dict = PlayQueuesUpdateOperationCurrentMeta.from_dict(play_queues_update_operation_current_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


