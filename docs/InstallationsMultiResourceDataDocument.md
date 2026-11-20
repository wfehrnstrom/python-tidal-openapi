# InstallationsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InstallationsResourceObject]**](InstallationsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.installations_multi_resource_data_document import InstallationsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsMultiResourceDataDocument from a JSON string
installations_multi_resource_data_document_instance = InstallationsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(InstallationsMultiResourceDataDocument.to_json())

# convert the object into a dict
installations_multi_resource_data_document_dict = installations_multi_resource_data_document_instance.to_dict()
# create an instance of InstallationsMultiResourceDataDocument from a dict
installations_multi_resource_data_document_from_dict = InstallationsMultiResourceDataDocument.from_dict(installations_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


