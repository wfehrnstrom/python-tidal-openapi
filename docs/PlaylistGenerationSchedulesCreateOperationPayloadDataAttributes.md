# PlaylistGenerationSchedulesCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zone** | **str** | IANA Time Zone Database identifier used to evaluate local civil time. | 
**weekday** | **str** |  | 

## Example

```python
from tidal.models.playlist_generation_schedules_create_operation_payload_data_attributes import PlaylistGenerationSchedulesCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationSchedulesCreateOperationPayloadDataAttributes from a JSON string
playlist_generation_schedules_create_operation_payload_data_attributes_instance = PlaylistGenerationSchedulesCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationSchedulesCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
playlist_generation_schedules_create_operation_payload_data_attributes_dict = playlist_generation_schedules_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of PlaylistGenerationSchedulesCreateOperationPayloadDataAttributes from a dict
playlist_generation_schedules_create_operation_payload_data_attributes_from_dict = PlaylistGenerationSchedulesCreateOperationPayloadDataAttributes.from_dict(playlist_generation_schedules_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


