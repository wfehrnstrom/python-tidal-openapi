# PlaylistGenerationSchedulesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaylistGenerationSchedulesResourceObject**](PlaylistGenerationSchedulesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlist_generation_schedules_single_resource_data_document import PlaylistGenerationSchedulesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationSchedulesSingleResourceDataDocument from a JSON string
playlist_generation_schedules_single_resource_data_document_instance = PlaylistGenerationSchedulesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationSchedulesSingleResourceDataDocument.to_json())

# convert the object into a dict
playlist_generation_schedules_single_resource_data_document_dict = playlist_generation_schedules_single_resource_data_document_instance.to_dict()
# create an instance of PlaylistGenerationSchedulesSingleResourceDataDocument from a dict
playlist_generation_schedules_single_resource_data_document_from_dict = PlaylistGenerationSchedulesSingleResourceDataDocument.from_dict(playlist_generation_schedules_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


