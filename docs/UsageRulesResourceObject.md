# UsageRulesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UsageRulesAttributes**](UsageRulesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.usage_rules_resource_object import UsageRulesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRulesResourceObject from a JSON string
usage_rules_resource_object_instance = UsageRulesResourceObject.from_json(json)
# print the JSON string representation of the object
print(UsageRulesResourceObject.to_json())

# convert the object into a dict
usage_rules_resource_object_dict = usage_rules_resource_object_instance.to_dict()
# create an instance of UsageRulesResourceObject from a dict
usage_rules_resource_object_from_dict = UsageRulesResourceObject.from_dict(usage_rules_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


