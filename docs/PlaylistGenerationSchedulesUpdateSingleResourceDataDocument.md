# PlaylistGenerationSchedulesUpdateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaylistGenerationSchedulesResourceObject**](PlaylistGenerationSchedulesResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlist_generation_schedules_update_single_resource_data_document import PlaylistGenerationSchedulesUpdateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationSchedulesUpdateSingleResourceDataDocument from a JSON string
playlist_generation_schedules_update_single_resource_data_document_instance = PlaylistGenerationSchedulesUpdateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationSchedulesUpdateSingleResourceDataDocument.to_json())

# convert the object into a dict
playlist_generation_schedules_update_single_resource_data_document_dict = playlist_generation_schedules_update_single_resource_data_document_instance.to_dict()
# create an instance of PlaylistGenerationSchedulesUpdateSingleResourceDataDocument from a dict
playlist_generation_schedules_update_single_resource_data_document_from_dict = PlaylistGenerationSchedulesUpdateSingleResourceDataDocument.from_dict(playlist_generation_schedules_update_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


