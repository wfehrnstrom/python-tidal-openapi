# PlaylistGenerationSchedulesUpdateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zone** | **str** | IANA Time Zone Database identifier used to evaluate local civil time. | [optional] 
**weekday** | **str** |  | [optional] 

## Example

```python
from tidal.models.playlist_generation_schedules_update_operation_payload_data_attributes import PlaylistGenerationSchedulesUpdateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationSchedulesUpdateOperationPayloadDataAttributes from a JSON string
playlist_generation_schedules_update_operation_payload_data_attributes_instance = PlaylistGenerationSchedulesUpdateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationSchedulesUpdateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
playlist_generation_schedules_update_operation_payload_data_attributes_dict = playlist_generation_schedules_update_operation_payload_data_attributes_instance.to_dict()
# create an instance of PlaylistGenerationSchedulesUpdateOperationPayloadDataAttributes from a dict
playlist_generation_schedules_update_operation_payload_data_attributes_from_dict = PlaylistGenerationSchedulesUpdateOperationPayloadDataAttributes.from_dict(playlist_generation_schedules_update_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


