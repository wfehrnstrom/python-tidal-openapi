# PlayQueuesUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlayQueuesUpdateOperationPayloadData**](PlayQueuesUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.play_queues_update_operation_payload import PlayQueuesUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesUpdateOperationPayload from a JSON string
play_queues_update_operation_payload_instance = PlayQueuesUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesUpdateOperationPayload.to_json())

# convert the object into a dict
play_queues_update_operation_payload_dict = play_queues_update_operation_payload_instance.to_dict()
# create an instance of PlayQueuesUpdateOperationPayload from a dict
play_queues_update_operation_payload_from_dict = PlayQueuesUpdateOperationPayload.from_dict(play_queues_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


