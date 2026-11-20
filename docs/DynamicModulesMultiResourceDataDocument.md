# DynamicModulesMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DynamicModulesResourceObject]**](DynamicModulesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.dynamic_modules_multi_resource_data_document import DynamicModulesMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicModulesMultiResourceDataDocument from a JSON string
dynamic_modules_multi_resource_data_document_instance = DynamicModulesMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(DynamicModulesMultiResourceDataDocument.to_json())

# convert the object into a dict
dynamic_modules_multi_resource_data_document_dict = dynamic_modules_multi_resource_data_document_instance.to_dict()
# create an instance of DynamicModulesMultiResourceDataDocument from a dict
dynamic_modules_multi_resource_data_document_from_dict = DynamicModulesMultiResourceDataDocument.from_dict(dynamic_modules_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


