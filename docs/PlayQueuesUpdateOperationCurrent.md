# PlayQueuesUpdateOperationCurrent

Selects current from meta; data is ignored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PlayQueuesUpdateOperationCurrentMeta**](PlayQueuesUpdateOperationCurrentMeta.md) |  | 

## Example

```python
from tidal.models.play_queues_update_operation_current import PlayQueuesUpdateOperationCurrent

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesUpdateOperationCurrent from a JSON string
play_queues_update_operation_current_instance = PlayQueuesUpdateOperationCurrent.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesUpdateOperationCurrent.to_json())

# convert the object into a dict
play_queues_update_operation_current_dict = play_queues_update_operation_current_instance.to_dict()
# create an instance of PlayQueuesUpdateOperationCurrent from a dict
play_queues_update_operation_current_from_dict = PlayQueuesUpdateOperationCurrent.from_dict(play_queues_update_operation_current_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


