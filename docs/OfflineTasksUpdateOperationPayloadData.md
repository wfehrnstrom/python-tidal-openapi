# OfflineTasksUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**OfflineTasksUpdateOperationPayloadDataAttributes**](OfflineTasksUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.offline_tasks_update_operation_payload_data import OfflineTasksUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineTasksUpdateOperationPayloadData from a JSON string
offline_tasks_update_operation_payload_data_instance = OfflineTasksUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(OfflineTasksUpdateOperationPayloadData.to_json())

# convert the object into a dict
offline_tasks_update_operation_payload_data_dict = offline_tasks_update_operation_payload_data_instance.to_dict()
# create an instance of OfflineTasksUpdateOperationPayloadData from a dict
offline_tasks_update_operation_payload_data_from_dict = OfflineTasksUpdateOperationPayloadData.from_dict(offline_tasks_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


