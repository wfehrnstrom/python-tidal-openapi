# CommentSummariesSubjectSingleRelationshipDataDocument

Target resource types: `comments`, `trackSourceFiles`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.comment_summaries_subject_single_relationship_data_document import CommentSummariesSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CommentSummariesSubjectSingleRelationshipDataDocument from a JSON string
comment_summaries_subject_single_relationship_data_document_instance = CommentSummariesSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(CommentSummariesSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
comment_summaries_subject_single_relationship_data_document_dict = comment_summaries_subject_single_relationship_data_document_instance.to_dict()
# create an instance of CommentSummariesSubjectSingleRelationshipDataDocument from a dict
comment_summaries_subject_single_relationship_data_document_from_dict = CommentSummariesSubjectSingleRelationshipDataDocument.from_dict(comment_summaries_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


