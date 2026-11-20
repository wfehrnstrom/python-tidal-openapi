# DynamicPagesMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DynamicPagesResourceObject]**](DynamicPagesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.dynamic_pages_multi_resource_data_document import DynamicPagesMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicPagesMultiResourceDataDocument from a JSON string
dynamic_pages_multi_resource_data_document_instance = DynamicPagesMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(DynamicPagesMultiResourceDataDocument.to_json())

# convert the object into a dict
dynamic_pages_multi_resource_data_document_dict = dynamic_pages_multi_resource_data_document_instance.to_dict()
# create an instance of DynamicPagesMultiResourceDataDocument from a dict
dynamic_pages_multi_resource_data_document_from_dict = DynamicPagesMultiResourceDataDocument.from_dict(dynamic_pages_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


