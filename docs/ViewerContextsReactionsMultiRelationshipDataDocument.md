# ViewerContextsReactionsMultiRelationshipDataDocument

Target resource types: `reactions`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.viewer_contexts_reactions_multi_relationship_data_document import ViewerContextsReactionsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerContextsReactionsMultiRelationshipDataDocument from a JSON string
viewer_contexts_reactions_multi_relationship_data_document_instance = ViewerContextsReactionsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ViewerContextsReactionsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
viewer_contexts_reactions_multi_relationship_data_document_dict = viewer_contexts_reactions_multi_relationship_data_document_instance.to_dict()
# create an instance of ViewerContextsReactionsMultiRelationshipDataDocument from a dict
viewer_contexts_reactions_multi_relationship_data_document_from_dict = ViewerContextsReactionsMultiRelationshipDataDocument.from_dict(viewer_contexts_reactions_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


