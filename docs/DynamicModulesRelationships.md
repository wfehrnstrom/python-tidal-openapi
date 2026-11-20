# DynamicModulesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**DynamicModulesItemsMultiRelationshipDataDocument**](DynamicModulesItemsMultiRelationshipDataDocument.md) |  | [optional] 
**seed_item** | [**DynamicModulesSeedItemSingleRelationshipDataDocument**](DynamicModulesSeedItemSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.dynamic_modules_relationships import DynamicModulesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicModulesRelationships from a JSON string
dynamic_modules_relationships_instance = DynamicModulesRelationships.from_json(json)
# print the JSON string representation of the object
print(DynamicModulesRelationships.to_json())

# convert the object into a dict
dynamic_modules_relationships_dict = dynamic_modules_relationships_instance.to_dict()
# create an instance of DynamicModulesRelationships from a dict
dynamic_modules_relationships_from_dict = DynamicModulesRelationships.from_dict(dynamic_modules_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


