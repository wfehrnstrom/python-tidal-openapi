# PlayQueuesCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlayQueuesCreateOperationPayloadData**](PlayQueuesCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.play_queues_create_operation_payload import PlayQueuesCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesCreateOperationPayload from a JSON string
play_queues_create_operation_payload_instance = PlayQueuesCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesCreateOperationPayload.to_json())

# convert the object into a dict
play_queues_create_operation_payload_dict = play_queues_create_operation_payload_instance.to_dict()
# create an instance of PlayQueuesCreateOperationPayload from a dict
play_queues_create_operation_payload_from_dict = PlayQueuesCreateOperationPayload.from_dict(play_queues_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


