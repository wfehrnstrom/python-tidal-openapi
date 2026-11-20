# UsageRulesCreateResource403ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[UsageRulesCreateResource403ResponseBodyErrorsInner]**](UsageRulesCreateResource403ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.usage_rules_create_resource403_response_body import UsageRulesCreateResource403ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRulesCreateResource403ResponseBody from a JSON string
usage_rules_create_resource403_response_body_instance = UsageRulesCreateResource403ResponseBody.from_json(json)
# print the JSON string representation of the object
print(UsageRulesCreateResource403ResponseBody.to_json())

# convert the object into a dict
usage_rules_create_resource403_response_body_dict = usage_rules_create_resource403_response_body_instance.to_dict()
# create an instance of UsageRulesCreateResource403ResponseBody from a dict
usage_rules_create_resource403_response_body_from_dict = UsageRulesCreateResource403ResponseBody.from_dict(usage_rules_create_resource403_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


