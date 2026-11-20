# CommentsRootSubjectSingleRelationshipDataDocument

Target resource types: `trackSourceFiles`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.comments_root_subject_single_relationship_data_document import CommentsRootSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsRootSubjectSingleRelationshipDataDocument from a JSON string
comments_root_subject_single_relationship_data_document_instance = CommentsRootSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(CommentsRootSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
comments_root_subject_single_relationship_data_document_dict = comments_root_subject_single_relationship_data_document_instance.to_dict()
# create an instance of CommentsRootSubjectSingleRelationshipDataDocument from a dict
comments_root_subject_single_relationship_data_document_from_dict = CommentsRootSubjectSingleRelationshipDataDocument.from_dict(comments_root_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


