# TrackFilesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TrackFilesResourceObject**](TrackFilesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.track_files_single_resource_data_document import TrackFilesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TrackFilesSingleResourceDataDocument from a JSON string
track_files_single_resource_data_document_instance = TrackFilesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(TrackFilesSingleResourceDataDocument.to_json())

# convert the object into a dict
track_files_single_resource_data_document_dict = track_files_single_resource_data_document_instance.to_dict()
# create an instance of TrackFilesSingleResourceDataDocument from a dict
track_files_single_resource_data_document_from_dict = TrackFilesSingleResourceDataDocument.from_dict(track_files_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


