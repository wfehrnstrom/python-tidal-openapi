# DynamicModulesSeedItemResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**DynamicModulesSeedItemResourceIdentifierMeta**](DynamicModulesSeedItemResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.dynamic_modules_seed_item_resource_identifier import DynamicModulesSeedItemResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicModulesSeedItemResourceIdentifier from a JSON string
dynamic_modules_seed_item_resource_identifier_instance = DynamicModulesSeedItemResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(DynamicModulesSeedItemResourceIdentifier.to_json())

# convert the object into a dict
dynamic_modules_seed_item_resource_identifier_dict = dynamic_modules_seed_item_resource_identifier_instance.to_dict()
# create an instance of DynamicModulesSeedItemResourceIdentifier from a dict
dynamic_modules_seed_item_resource_identifier_from_dict = DynamicModulesSeedItemResourceIdentifier.from_dict(dynamic_modules_seed_item_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


