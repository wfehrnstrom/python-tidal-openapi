# OfflineTasksUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OfflineTasksUpdateOperationPayloadData**](OfflineTasksUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.offline_tasks_update_operation_payload import OfflineTasksUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineTasksUpdateOperationPayload from a JSON string
offline_tasks_update_operation_payload_instance = OfflineTasksUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(OfflineTasksUpdateOperationPayload.to_json())

# convert the object into a dict
offline_tasks_update_operation_payload_dict = offline_tasks_update_operation_payload_instance.to_dict()
# create an instance of OfflineTasksUpdateOperationPayload from a dict
offline_tasks_update_operation_payload_from_dict = OfflineTasksUpdateOperationPayload.from_dict(offline_tasks_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


