# ViewerContextsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**ViewerContextsCommentsMultiRelationshipDataDocument**](ViewerContextsCommentsMultiRelationshipDataDocument.md) |  | [optional] 
**reactions** | [**ViewerContextsReactionsMultiRelationshipDataDocument**](ViewerContextsReactionsMultiRelationshipDataDocument.md) |  | [optional] 
**subject** | [**ViewerContextsSubjectSingleRelationshipDataDocument**](ViewerContextsSubjectSingleRelationshipDataDocument.md) |  | [optional] 
**viewer** | [**ViewerContextsViewerSingleRelationshipDataDocument**](ViewerContextsViewerSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.viewer_contexts_relationships import ViewerContextsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerContextsRelationships from a JSON string
viewer_contexts_relationships_instance = ViewerContextsRelationships.from_json(json)
# print the JSON string representation of the object
print(ViewerContextsRelationships.to_json())

# convert the object into a dict
viewer_contexts_relationships_dict = viewer_contexts_relationships_instance.to_dict()
# create an instance of ViewerContextsRelationships from a dict
viewer_contexts_relationships_from_dict = ViewerContextsRelationships.from_dict(viewer_contexts_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


