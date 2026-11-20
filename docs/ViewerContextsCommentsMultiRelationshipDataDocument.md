# ViewerContextsCommentsMultiRelationshipDataDocument

Target resource types: `comments`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.viewer_contexts_comments_multi_relationship_data_document import ViewerContextsCommentsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerContextsCommentsMultiRelationshipDataDocument from a JSON string
viewer_contexts_comments_multi_relationship_data_document_instance = ViewerContextsCommentsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ViewerContextsCommentsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
viewer_contexts_comments_multi_relationship_data_document_dict = viewer_contexts_comments_multi_relationship_data_document_instance.to_dict()
# create an instance of ViewerContextsCommentsMultiRelationshipDataDocument from a dict
viewer_contexts_comments_multi_relationship_data_document_from_dict = ViewerContextsCommentsMultiRelationshipDataDocument.from_dict(viewer_contexts_comments_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


