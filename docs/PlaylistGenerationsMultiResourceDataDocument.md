# PlaylistGenerationsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlaylistGenerationsResourceObject]**](PlaylistGenerationsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlist_generations_multi_resource_data_document import PlaylistGenerationsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsMultiResourceDataDocument from a JSON string
playlist_generations_multi_resource_data_document_instance = PlaylistGenerationsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsMultiResourceDataDocument.to_json())

# convert the object into a dict
playlist_generations_multi_resource_data_document_dict = playlist_generations_multi_resource_data_document_instance.to_dict()
# create an instance of PlaylistGenerationsMultiResourceDataDocument from a dict
playlist_generations_multi_resource_data_document_from_dict = PlaylistGenerationsMultiResourceDataDocument.from_dict(playlist_generations_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


