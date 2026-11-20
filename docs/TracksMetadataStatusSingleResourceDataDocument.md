# TracksMetadataStatusSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TracksMetadataStatusResourceObject**](TracksMetadataStatusResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.tracks_metadata_status_single_resource_data_document import TracksMetadataStatusSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TracksMetadataStatusSingleResourceDataDocument from a JSON string
tracks_metadata_status_single_resource_data_document_instance = TracksMetadataStatusSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(TracksMetadataStatusSingleResourceDataDocument.to_json())

# convert the object into a dict
tracks_metadata_status_single_resource_data_document_dict = tracks_metadata_status_single_resource_data_document_instance.to_dict()
# create an instance of TracksMetadataStatusSingleResourceDataDocument from a dict
tracks_metadata_status_single_resource_data_document_from_dict = TracksMetadataStatusSingleResourceDataDocument.from_dict(tracks_metadata_status_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


