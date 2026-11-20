# PlaylistGenerationSchedulesUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PlaylistGenerationSchedulesUpdateOperationPayloadDataAttributes**](PlaylistGenerationSchedulesUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.playlist_generation_schedules_update_operation_payload_data import PlaylistGenerationSchedulesUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationSchedulesUpdateOperationPayloadData from a JSON string
playlist_generation_schedules_update_operation_payload_data_instance = PlaylistGenerationSchedulesUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationSchedulesUpdateOperationPayloadData.to_json())

# convert the object into a dict
playlist_generation_schedules_update_operation_payload_data_dict = playlist_generation_schedules_update_operation_payload_data_instance.to_dict()
# create an instance of PlaylistGenerationSchedulesUpdateOperationPayloadData from a dict
playlist_generation_schedules_update_operation_payload_data_from_dict = PlaylistGenerationSchedulesUpdateOperationPayloadData.from_dict(playlist_generation_schedules_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


