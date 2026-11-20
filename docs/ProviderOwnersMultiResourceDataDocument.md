# ProviderOwnersMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProviderOwnersResourceObject]**](ProviderOwnersResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.provider_owners_multi_resource_data_document import ProviderOwnersMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderOwnersMultiResourceDataDocument from a JSON string
provider_owners_multi_resource_data_document_instance = ProviderOwnersMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ProviderOwnersMultiResourceDataDocument.to_json())

# convert the object into a dict
provider_owners_multi_resource_data_document_dict = provider_owners_multi_resource_data_document_instance.to_dict()
# create an instance of ProviderOwnersMultiResourceDataDocument from a dict
provider_owners_multi_resource_data_document_from_dict = ProviderOwnersMultiResourceDataDocument.from_dict(provider_owners_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


