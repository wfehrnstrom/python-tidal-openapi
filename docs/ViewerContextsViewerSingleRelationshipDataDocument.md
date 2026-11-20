# ViewerContextsViewerSingleRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.viewer_contexts_viewer_single_relationship_data_document import ViewerContextsViewerSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerContextsViewerSingleRelationshipDataDocument from a JSON string
viewer_contexts_viewer_single_relationship_data_document_instance = ViewerContextsViewerSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ViewerContextsViewerSingleRelationshipDataDocument.to_json())

# convert the object into a dict
viewer_contexts_viewer_single_relationship_data_document_dict = viewer_contexts_viewer_single_relationship_data_document_instance.to_dict()
# create an instance of ViewerContextsViewerSingleRelationshipDataDocument from a dict
viewer_contexts_viewer_single_relationship_data_document_from_dict = ViewerContextsViewerSingleRelationshipDataDocument.from_dict(viewer_contexts_viewer_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


