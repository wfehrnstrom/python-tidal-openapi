# TracksMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TracksResourceObject]**](TracksResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.tracks_multi_resource_data_document import TracksMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TracksMultiResourceDataDocument from a JSON string
tracks_multi_resource_data_document_instance = TracksMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(TracksMultiResourceDataDocument.to_json())

# convert the object into a dict
tracks_multi_resource_data_document_dict = tracks_multi_resource_data_document_instance.to_dict()
# create an instance of TracksMultiResourceDataDocument from a dict
tracks_multi_resource_data_document_from_dict = TracksMultiResourceDataDocument.from_dict(tracks_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


