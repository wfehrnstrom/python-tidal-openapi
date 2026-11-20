# CommentsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CommentsResourceObject**](CommentsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.comments_single_resource_data_document import CommentsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsSingleResourceDataDocument from a JSON string
comments_single_resource_data_document_instance = CommentsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(CommentsSingleResourceDataDocument.to_json())

# convert the object into a dict
comments_single_resource_data_document_dict = comments_single_resource_data_document_instance.to_dict()
# create an instance of CommentsSingleResourceDataDocument from a dict
comments_single_resource_data_document_from_dict = CommentsSingleResourceDataDocument.from_dict(comments_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


