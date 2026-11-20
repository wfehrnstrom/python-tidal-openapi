# ViewerContextsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ViewerContextsResourceObject**](ViewerContextsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.viewer_contexts_single_resource_data_document import ViewerContextsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerContextsSingleResourceDataDocument from a JSON string
viewer_contexts_single_resource_data_document_instance = ViewerContextsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ViewerContextsSingleResourceDataDocument.to_json())

# convert the object into a dict
viewer_contexts_single_resource_data_document_dict = viewer_contexts_single_resource_data_document_instance.to_dict()
# create an instance of ViewerContextsSingleResourceDataDocument from a dict
viewer_contexts_single_resource_data_document_from_dict = ViewerContextsSingleResourceDataDocument.from_dict(viewer_contexts_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


