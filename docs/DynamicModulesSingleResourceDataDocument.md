# DynamicModulesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DynamicModulesResourceObject**](DynamicModulesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.dynamic_modules_single_resource_data_document import DynamicModulesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicModulesSingleResourceDataDocument from a JSON string
dynamic_modules_single_resource_data_document_instance = DynamicModulesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(DynamicModulesSingleResourceDataDocument.to_json())

# convert the object into a dict
dynamic_modules_single_resource_data_document_dict = dynamic_modules_single_resource_data_document_instance.to_dict()
# create an instance of DynamicModulesSingleResourceDataDocument from a dict
dynamic_modules_single_resource_data_document_from_dict = DynamicModulesSingleResourceDataDocument.from_dict(dynamic_modules_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


