# ProviderProductInfosProviderSingleRelationshipDataDocument

Target resource types: `providers`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.provider_product_infos_provider_single_relationship_data_document import ProviderProductInfosProviderSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderProductInfosProviderSingleRelationshipDataDocument from a JSON string
provider_product_infos_provider_single_relationship_data_document_instance = ProviderProductInfosProviderSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ProviderProductInfosProviderSingleRelationshipDataDocument.to_json())

# convert the object into a dict
provider_product_infos_provider_single_relationship_data_document_dict = provider_product_infos_provider_single_relationship_data_document_instance.to_dict()
# create an instance of ProviderProductInfosProviderSingleRelationshipDataDocument from a dict
provider_product_infos_provider_single_relationship_data_document_from_dict = ProviderProductInfosProviderSingleRelationshipDataDocument.from_dict(provider_product_infos_provider_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


