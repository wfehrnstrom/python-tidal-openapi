# PlaylistGenerationSchedulesCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaylistGenerationSchedulesCreateOperationPayloadData**](PlaylistGenerationSchedulesCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.playlist_generation_schedules_create_operation_payload import PlaylistGenerationSchedulesCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationSchedulesCreateOperationPayload from a JSON string
playlist_generation_schedules_create_operation_payload_instance = PlaylistGenerationSchedulesCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationSchedulesCreateOperationPayload.to_json())

# convert the object into a dict
playlist_generation_schedules_create_operation_payload_dict = playlist_generation_schedules_create_operation_payload_instance.to_dict()
# create an instance of PlaylistGenerationSchedulesCreateOperationPayload from a dict
playlist_generation_schedules_create_operation_payload_from_dict = PlaylistGenerationSchedulesCreateOperationPayload.from_dict(playlist_generation_schedules_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


