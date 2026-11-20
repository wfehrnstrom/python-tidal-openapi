# TracksMetadataStatusSingleRelationshipDataDocument

Target resource types: `tracksMetadataStatus`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.tracks_metadata_status_single_relationship_data_document import TracksMetadataStatusSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TracksMetadataStatusSingleRelationshipDataDocument from a JSON string
tracks_metadata_status_single_relationship_data_document_instance = TracksMetadataStatusSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TracksMetadataStatusSingleRelationshipDataDocument.to_json())

# convert the object into a dict
tracks_metadata_status_single_relationship_data_document_dict = tracks_metadata_status_single_relationship_data_document_instance.to_dict()
# create an instance of TracksMetadataStatusSingleRelationshipDataDocument from a dict
tracks_metadata_status_single_relationship_data_document_from_dict = TracksMetadataStatusSingleRelationshipDataDocument.from_dict(tracks_metadata_status_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


