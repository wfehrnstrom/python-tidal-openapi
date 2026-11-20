# ProviderProductInfosMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProviderProductInfosResourceObject]**](ProviderProductInfosResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.provider_product_infos_multi_resource_data_document import ProviderProductInfosMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderProductInfosMultiResourceDataDocument from a JSON string
provider_product_infos_multi_resource_data_document_instance = ProviderProductInfosMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ProviderProductInfosMultiResourceDataDocument.to_json())

# convert the object into a dict
provider_product_infos_multi_resource_data_document_dict = provider_product_infos_multi_resource_data_document_instance.to_dict()
# create an instance of ProviderProductInfosMultiResourceDataDocument from a dict
provider_product_infos_multi_resource_data_document_from_dict = ProviderProductInfosMultiResourceDataDocument.from_dict(provider_product_infos_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


