# PlayQueuesCurrentRelationshipUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**PlayQueuesCurrentRelationshipUpdateOperationPayloadDataMeta**](PlayQueuesCurrentRelationshipUpdateOperationPayloadDataMeta.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.play_queues_current_relationship_update_operation_payload_data import PlayQueuesCurrentRelationshipUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesCurrentRelationshipUpdateOperationPayloadData from a JSON string
play_queues_current_relationship_update_operation_payload_data_instance = PlayQueuesCurrentRelationshipUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesCurrentRelationshipUpdateOperationPayloadData.to_json())

# convert the object into a dict
play_queues_current_relationship_update_operation_payload_data_dict = play_queues_current_relationship_update_operation_payload_data_instance.to_dict()
# create an instance of PlayQueuesCurrentRelationshipUpdateOperationPayloadData from a dict
play_queues_current_relationship_update_operation_payload_data_from_dict = PlayQueuesCurrentRelationshipUpdateOperationPayloadData.from_dict(play_queues_current_relationship_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


