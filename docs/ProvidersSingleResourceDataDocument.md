# ProvidersSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ProvidersResourceObject**](ProvidersResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.providers_single_resource_data_document import ProvidersSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ProvidersSingleResourceDataDocument from a JSON string
providers_single_resource_data_document_instance = ProvidersSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ProvidersSingleResourceDataDocument.to_json())

# convert the object into a dict
providers_single_resource_data_document_dict = providers_single_resource_data_document_instance.to_dict()
# create an instance of ProvidersSingleResourceDataDocument from a dict
providers_single_resource_data_document_from_dict = ProvidersSingleResourceDataDocument.from_dict(providers_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


