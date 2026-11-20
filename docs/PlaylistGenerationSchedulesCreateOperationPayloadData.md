# PlaylistGenerationSchedulesCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PlaylistGenerationSchedulesCreateOperationPayloadDataAttributes**](PlaylistGenerationSchedulesCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**PlaylistGenerationSchedulesCreateOperationPayloadDataRelationships**](PlaylistGenerationSchedulesCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.playlist_generation_schedules_create_operation_payload_data import PlaylistGenerationSchedulesCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationSchedulesCreateOperationPayloadData from a JSON string
playlist_generation_schedules_create_operation_payload_data_instance = PlaylistGenerationSchedulesCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationSchedulesCreateOperationPayloadData.to_json())

# convert the object into a dict
playlist_generation_schedules_create_operation_payload_data_dict = playlist_generation_schedules_create_operation_payload_data_instance.to_dict()
# create an instance of PlaylistGenerationSchedulesCreateOperationPayloadData from a dict
playlist_generation_schedules_create_operation_payload_data_from_dict = PlaylistGenerationSchedulesCreateOperationPayloadData.from_dict(playlist_generation_schedules_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


