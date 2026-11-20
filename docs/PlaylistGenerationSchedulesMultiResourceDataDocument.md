# PlaylistGenerationSchedulesMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlaylistGenerationSchedulesResourceObject]**](PlaylistGenerationSchedulesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlist_generation_schedules_multi_resource_data_document import PlaylistGenerationSchedulesMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationSchedulesMultiResourceDataDocument from a JSON string
playlist_generation_schedules_multi_resource_data_document_instance = PlaylistGenerationSchedulesMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationSchedulesMultiResourceDataDocument.to_json())

# convert the object into a dict
playlist_generation_schedules_multi_resource_data_document_dict = playlist_generation_schedules_multi_resource_data_document_instance.to_dict()
# create an instance of PlaylistGenerationSchedulesMultiResourceDataDocument from a dict
playlist_generation_schedules_multi_resource_data_document_from_dict = PlaylistGenerationSchedulesMultiResourceDataDocument.from_dict(playlist_generation_schedules_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


