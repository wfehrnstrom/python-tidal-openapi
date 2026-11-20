# TrackSourceFilesOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.track_source_files_owners_multi_relationship_data_document import TrackSourceFilesOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TrackSourceFilesOwnersMultiRelationshipDataDocument from a JSON string
track_source_files_owners_multi_relationship_data_document_instance = TrackSourceFilesOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TrackSourceFilesOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
track_source_files_owners_multi_relationship_data_document_dict = track_source_files_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of TrackSourceFilesOwnersMultiRelationshipDataDocument from a dict
track_source_files_owners_multi_relationship_data_document_from_dict = TrackSourceFilesOwnersMultiRelationshipDataDocument.from_dict(track_source_files_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


