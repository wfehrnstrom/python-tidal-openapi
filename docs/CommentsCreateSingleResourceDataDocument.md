# CommentsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CommentsResourceObject**](CommentsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.comments_create_single_resource_data_document import CommentsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsCreateSingleResourceDataDocument from a JSON string
comments_create_single_resource_data_document_instance = CommentsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(CommentsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
comments_create_single_resource_data_document_dict = comments_create_single_resource_data_document_instance.to_dict()
# create an instance of CommentsCreateSingleResourceDataDocument from a dict
comments_create_single_resource_data_document_from_dict = CommentsCreateSingleResourceDataDocument.from_dict(comments_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


