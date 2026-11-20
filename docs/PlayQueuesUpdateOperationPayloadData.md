# PlayQueuesUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PlayQueuesUpdateOperationPayloadDataAttributes**](PlayQueuesUpdateOperationPayloadDataAttributes.md) |  | [optional] 
**id** | **str** |  | 
**relationships** | [**PlayQueuesUpdateOperationPayloadDataRelationships**](PlayQueuesUpdateOperationPayloadDataRelationships.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.play_queues_update_operation_payload_data import PlayQueuesUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesUpdateOperationPayloadData from a JSON string
play_queues_update_operation_payload_data_instance = PlayQueuesUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesUpdateOperationPayloadData.to_json())

# convert the object into a dict
play_queues_update_operation_payload_data_dict = play_queues_update_operation_payload_data_instance.to_dict()
# create an instance of PlayQueuesUpdateOperationPayloadData from a dict
play_queues_update_operation_payload_data_from_dict = PlayQueuesUpdateOperationPayloadData.from_dict(play_queues_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


