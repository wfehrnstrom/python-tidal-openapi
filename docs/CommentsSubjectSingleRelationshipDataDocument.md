# CommentsSubjectSingleRelationshipDataDocument

Target resource types: `comments`, `trackSourceFiles`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.comments_subject_single_relationship_data_document import CommentsSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsSubjectSingleRelationshipDataDocument from a JSON string
comments_subject_single_relationship_data_document_instance = CommentsSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(CommentsSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
comments_subject_single_relationship_data_document_dict = comments_subject_single_relationship_data_document_instance.to_dict()
# create an instance of CommentsSubjectSingleRelationshipDataDocument from a dict
comments_subject_single_relationship_data_document_from_dict = CommentsSubjectSingleRelationshipDataDocument.from_dict(comments_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


