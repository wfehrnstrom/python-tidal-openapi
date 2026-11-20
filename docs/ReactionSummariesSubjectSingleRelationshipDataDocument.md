# ReactionSummariesSubjectSingleRelationshipDataDocument

Target resource types: `comments`, `trackSourceFiles`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.reaction_summaries_subject_single_relationship_data_document import ReactionSummariesSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionSummariesSubjectSingleRelationshipDataDocument from a JSON string
reaction_summaries_subject_single_relationship_data_document_instance = ReactionSummariesSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ReactionSummariesSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
reaction_summaries_subject_single_relationship_data_document_dict = reaction_summaries_subject_single_relationship_data_document_instance.to_dict()
# create an instance of ReactionSummariesSubjectSingleRelationshipDataDocument from a dict
reaction_summaries_subject_single_relationship_data_document_from_dict = ReactionSummariesSubjectSingleRelationshipDataDocument.from_dict(reaction_summaries_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


