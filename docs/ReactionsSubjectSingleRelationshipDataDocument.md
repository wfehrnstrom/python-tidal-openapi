# ReactionsSubjectSingleRelationshipDataDocument

Target resource types: `comments`, `trackSourceFiles`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.reactions_subject_single_relationship_data_document import ReactionsSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionsSubjectSingleRelationshipDataDocument from a JSON string
reactions_subject_single_relationship_data_document_instance = ReactionsSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ReactionsSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
reactions_subject_single_relationship_data_document_dict = reactions_subject_single_relationship_data_document_instance.to_dict()
# create an instance of ReactionsSubjectSingleRelationshipDataDocument from a dict
reactions_subject_single_relationship_data_document_from_dict = ReactionsSubjectSingleRelationshipDataDocument.from_dict(reactions_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


