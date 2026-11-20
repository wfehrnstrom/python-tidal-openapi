# TracksDownloadSingleRelationshipDataDocument

Target resource types: `downloads`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.tracks_download_single_relationship_data_document import TracksDownloadSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TracksDownloadSingleRelationshipDataDocument from a JSON string
tracks_download_single_relationship_data_document_instance = TracksDownloadSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TracksDownloadSingleRelationshipDataDocument.to_json())

# convert the object into a dict
tracks_download_single_relationship_data_document_dict = tracks_download_single_relationship_data_document_instance.to_dict()
# create an instance of TracksDownloadSingleRelationshipDataDocument from a dict
tracks_download_single_relationship_data_document_from_dict = TracksDownloadSingleRelationshipDataDocument.from_dict(tracks_download_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


