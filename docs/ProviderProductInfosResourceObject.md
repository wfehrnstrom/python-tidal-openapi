# ProviderProductInfosResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ProviderProductInfosAttributes**](ProviderProductInfosAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ProviderProductInfosRelationships**](ProviderProductInfosRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.provider_product_infos_resource_object import ProviderProductInfosResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderProductInfosResourceObject from a JSON string
provider_product_infos_resource_object_instance = ProviderProductInfosResourceObject.from_json(json)
# print the JSON string representation of the object
print(ProviderProductInfosResourceObject.to_json())

# convert the object into a dict
provider_product_infos_resource_object_dict = provider_product_infos_resource_object_instance.to_dict()
# create an instance of ProviderProductInfosResourceObject from a dict
provider_product_infos_resource_object_from_dict = ProviderProductInfosResourceObject.from_dict(provider_product_infos_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


