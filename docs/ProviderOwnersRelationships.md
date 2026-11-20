# ProviderOwnersRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**ProviderOwnersOwnersMultiRelationshipDataDocument**](ProviderOwnersOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**provider** | [**ProviderOwnersProviderSingleRelationshipDataDocument**](ProviderOwnersProviderSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.provider_owners_relationships import ProviderOwnersRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderOwnersRelationships from a JSON string
provider_owners_relationships_instance = ProviderOwnersRelationships.from_json(json)
# print the JSON string representation of the object
print(ProviderOwnersRelationships.to_json())

# convert the object into a dict
provider_owners_relationships_dict = provider_owners_relationships_instance.to_dict()
# create an instance of ProviderOwnersRelationships from a dict
provider_owners_relationships_from_dict = ProviderOwnersRelationships.from_dict(provider_owners_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


