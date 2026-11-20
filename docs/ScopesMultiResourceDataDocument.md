# ScopesMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ScopesResourceObject]**](ScopesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.scopes_multi_resource_data_document import ScopesMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ScopesMultiResourceDataDocument from a JSON string
scopes_multi_resource_data_document_instance = ScopesMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ScopesMultiResourceDataDocument.to_json())

# convert the object into a dict
scopes_multi_resource_data_document_dict = scopes_multi_resource_data_document_instance.to_dict()
# create an instance of ScopesMultiResourceDataDocument from a dict
scopes_multi_resource_data_document_from_dict = ScopesMultiResourceDataDocument.from_dict(scopes_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


