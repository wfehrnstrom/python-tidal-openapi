# PlaylistGenerationSchedulesCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaylistGenerationSchedulesResourceObject**](PlaylistGenerationSchedulesResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlist_generation_schedules_create_single_resource_data_document import PlaylistGenerationSchedulesCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationSchedulesCreateSingleResourceDataDocument from a JSON string
playlist_generation_schedules_create_single_resource_data_document_instance = PlaylistGenerationSchedulesCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationSchedulesCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
playlist_generation_schedules_create_single_resource_data_document_dict = playlist_generation_schedules_create_single_resource_data_document_instance.to_dict()
# create an instance of PlaylistGenerationSchedulesCreateSingleResourceDataDocument from a dict
playlist_generation_schedules_create_single_resource_data_document_from_dict = PlaylistGenerationSchedulesCreateSingleResourceDataDocument.from_dict(playlist_generation_schedules_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


