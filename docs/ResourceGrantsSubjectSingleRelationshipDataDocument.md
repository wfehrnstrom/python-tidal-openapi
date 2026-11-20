# ResourceGrantsSubjectSingleRelationshipDataDocument

Target resource types: `albums`, `folders`, `playlists`, `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceGrantsSubjectResourceIdentifier**](ResourceGrantsSubjectResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.resource_grants_subject_single_relationship_data_document import ResourceGrantsSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsSubjectSingleRelationshipDataDocument from a JSON string
resource_grants_subject_single_relationship_data_document_instance = ResourceGrantsSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
resource_grants_subject_single_relationship_data_document_dict = resource_grants_subject_single_relationship_data_document_instance.to_dict()
# create an instance of ResourceGrantsSubjectSingleRelationshipDataDocument from a dict
resource_grants_subject_single_relationship_data_document_from_dict = ResourceGrantsSubjectSingleRelationshipDataDocument.from_dict(resource_grants_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


