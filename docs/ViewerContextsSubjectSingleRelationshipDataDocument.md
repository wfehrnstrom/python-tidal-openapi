# ViewerContextsSubjectSingleRelationshipDataDocument

Target resource types: `albums`, `artists`, `comments`, `folders`, `playlists`, `trackSourceFiles`, `tracks`, `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ViewerContextsSubjectResourceIdentifier**](ViewerContextsSubjectResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.viewer_contexts_subject_single_relationship_data_document import ViewerContextsSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerContextsSubjectSingleRelationshipDataDocument from a JSON string
viewer_contexts_subject_single_relationship_data_document_instance = ViewerContextsSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ViewerContextsSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
viewer_contexts_subject_single_relationship_data_document_dict = viewer_contexts_subject_single_relationship_data_document_instance.to_dict()
# create an instance of ViewerContextsSubjectSingleRelationshipDataDocument from a dict
viewer_contexts_subject_single_relationship_data_document_from_dict = ViewerContextsSubjectSingleRelationshipDataDocument.from_dict(viewer_contexts_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


