# PlayQueuesUpdateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repeat** | **str** |  | [optional] 
**shuffle** | **str** |  | [optional] 
**shuffled** | **bool** |  | [optional] 

## Example

```python
from tidal.models.play_queues_update_operation_payload_data_attributes import PlayQueuesUpdateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesUpdateOperationPayloadDataAttributes from a JSON string
play_queues_update_operation_payload_data_attributes_instance = PlayQueuesUpdateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesUpdateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
play_queues_update_operation_payload_data_attributes_dict = play_queues_update_operation_payload_data_attributes_instance.to_dict()
# create an instance of PlayQueuesUpdateOperationPayloadDataAttributes from a dict
play_queues_update_operation_payload_data_attributes_from_dict = PlayQueuesUpdateOperationPayloadDataAttributes.from_dict(play_queues_update_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


