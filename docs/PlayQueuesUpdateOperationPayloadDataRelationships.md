# PlayQueuesUpdateOperationPayloadDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | [**PlayQueuesUpdateOperationCurrent**](PlayQueuesUpdateOperationCurrent.md) |  | [optional] 
**future** | [**PlayQueuesUpdateOperationFuture**](PlayQueuesUpdateOperationFuture.md) |  | [optional] 

## Example

```python
from tidal.models.play_queues_update_operation_payload_data_relationships import PlayQueuesUpdateOperationPayloadDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesUpdateOperationPayloadDataRelationships from a JSON string
play_queues_update_operation_payload_data_relationships_instance = PlayQueuesUpdateOperationPayloadDataRelationships.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesUpdateOperationPayloadDataRelationships.to_json())

# convert the object into a dict
play_queues_update_operation_payload_data_relationships_dict = play_queues_update_operation_payload_data_relationships_instance.to_dict()
# create an instance of PlayQueuesUpdateOperationPayloadDataRelationships from a dict
play_queues_update_operation_payload_data_relationships_from_dict = PlayQueuesUpdateOperationPayloadDataRelationships.from_dict(play_queues_update_operation_payload_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


