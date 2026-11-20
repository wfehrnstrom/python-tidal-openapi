# ViewerContextsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ViewerContextsResourceObject]**](ViewerContextsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.viewer_contexts_multi_resource_data_document import ViewerContextsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerContextsMultiResourceDataDocument from a JSON string
viewer_contexts_multi_resource_data_document_instance = ViewerContextsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ViewerContextsMultiResourceDataDocument.to_json())

# convert the object into a dict
viewer_contexts_multi_resource_data_document_dict = viewer_contexts_multi_resource_data_document_instance.to_dict()
# create an instance of ViewerContextsMultiResourceDataDocument from a dict
viewer_contexts_multi_resource_data_document_from_dict = ViewerContextsMultiResourceDataDocument.from_dict(viewer_contexts_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


