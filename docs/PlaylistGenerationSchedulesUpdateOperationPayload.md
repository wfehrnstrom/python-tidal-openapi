# PlaylistGenerationSchedulesUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaylistGenerationSchedulesUpdateOperationPayloadData**](PlaylistGenerationSchedulesUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.playlist_generation_schedules_update_operation_payload import PlaylistGenerationSchedulesUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationSchedulesUpdateOperationPayload from a JSON string
playlist_generation_schedules_update_operation_payload_instance = PlaylistGenerationSchedulesUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationSchedulesUpdateOperationPayload.to_json())

# convert the object into a dict
playlist_generation_schedules_update_operation_payload_dict = playlist_generation_schedules_update_operation_payload_instance.to_dict()
# create an instance of PlaylistGenerationSchedulesUpdateOperationPayload from a dict
playlist_generation_schedules_update_operation_payload_from_dict = PlaylistGenerationSchedulesUpdateOperationPayload.from_dict(playlist_generation_schedules_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


