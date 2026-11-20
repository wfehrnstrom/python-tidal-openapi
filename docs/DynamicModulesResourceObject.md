# DynamicModulesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**DynamicModulesAttributes**](DynamicModulesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**DynamicModulesRelationships**](DynamicModulesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.dynamic_modules_resource_object import DynamicModulesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicModulesResourceObject from a JSON string
dynamic_modules_resource_object_instance = DynamicModulesResourceObject.from_json(json)
# print the JSON string representation of the object
print(DynamicModulesResourceObject.to_json())

# convert the object into a dict
dynamic_modules_resource_object_dict = dynamic_modules_resource_object_instance.to_dict()
# create an instance of DynamicModulesResourceObject from a dict
dynamic_modules_resource_object_from_dict = DynamicModulesResourceObject.from_dict(dynamic_modules_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


