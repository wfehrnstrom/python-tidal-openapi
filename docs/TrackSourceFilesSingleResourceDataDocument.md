# TrackSourceFilesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TrackSourceFilesResourceObject**](TrackSourceFilesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.track_source_files_single_resource_data_document import TrackSourceFilesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TrackSourceFilesSingleResourceDataDocument from a JSON string
track_source_files_single_resource_data_document_instance = TrackSourceFilesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(TrackSourceFilesSingleResourceDataDocument.to_json())

# convert the object into a dict
track_source_files_single_resource_data_document_dict = track_source_files_single_resource_data_document_instance.to_dict()
# create an instance of TrackSourceFilesSingleResourceDataDocument from a dict
track_source_files_single_resource_data_document_from_dict = TrackSourceFilesSingleResourceDataDocument.from_dict(track_source_files_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


