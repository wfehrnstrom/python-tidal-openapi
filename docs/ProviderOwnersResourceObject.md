# ProviderOwnersResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ProviderOwnersAttributes**](ProviderOwnersAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ProviderOwnersRelationships**](ProviderOwnersRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.provider_owners_resource_object import ProviderOwnersResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderOwnersResourceObject from a JSON string
provider_owners_resource_object_instance = ProviderOwnersResourceObject.from_json(json)
# print the JSON string representation of the object
print(ProviderOwnersResourceObject.to_json())

# convert the object into a dict
provider_owners_resource_object_dict = provider_owners_resource_object_instance.to_dict()
# create an instance of ProviderOwnersResourceObject from a dict
provider_owners_resource_object_from_dict = ProviderOwnersResourceObject.from_dict(provider_owners_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


