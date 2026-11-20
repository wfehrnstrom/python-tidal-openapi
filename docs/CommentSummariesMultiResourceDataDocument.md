# CommentSummariesMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommentSummariesResourceObject]**](CommentSummariesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.comment_summaries_multi_resource_data_document import CommentSummariesMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CommentSummariesMultiResourceDataDocument from a JSON string
comment_summaries_multi_resource_data_document_instance = CommentSummariesMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(CommentSummariesMultiResourceDataDocument.to_json())

# convert the object into a dict
comment_summaries_multi_resource_data_document_dict = comment_summaries_multi_resource_data_document_instance.to_dict()
# create an instance of CommentSummariesMultiResourceDataDocument from a dict
comment_summaries_multi_resource_data_document_from_dict = CommentSummariesMultiResourceDataDocument.from_dict(comment_summaries_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


