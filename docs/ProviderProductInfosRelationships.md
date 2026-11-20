# ProviderProductInfosRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**ProviderProductInfosProviderSingleRelationshipDataDocument**](ProviderProductInfosProviderSingleRelationshipDataDocument.md) |  | [optional] 
**subject** | [**ProviderProductInfosSubjectSingleRelationshipDataDocument**](ProviderProductInfosSubjectSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.provider_product_infos_relationships import ProviderProductInfosRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderProductInfosRelationships from a JSON string
provider_product_infos_relationships_instance = ProviderProductInfosRelationships.from_json(json)
# print the JSON string representation of the object
print(ProviderProductInfosRelationships.to_json())

# convert the object into a dict
provider_product_infos_relationships_dict = provider_product_infos_relationships_instance.to_dict()
# create an instance of ProviderProductInfosRelationships from a dict
provider_product_infos_relationships_from_dict = ProviderProductInfosRelationships.from_dict(provider_product_infos_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


