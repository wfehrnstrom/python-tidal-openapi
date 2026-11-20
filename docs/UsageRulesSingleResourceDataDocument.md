# UsageRulesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UsageRulesResourceObject**](UsageRulesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.usage_rules_single_resource_data_document import UsageRulesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRulesSingleResourceDataDocument from a JSON string
usage_rules_single_resource_data_document_instance = UsageRulesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UsageRulesSingleResourceDataDocument.to_json())

# convert the object into a dict
usage_rules_single_resource_data_document_dict = usage_rules_single_resource_data_document_instance.to_dict()
# create an instance of UsageRulesSingleResourceDataDocument from a dict
usage_rules_single_resource_data_document_from_dict = UsageRulesSingleResourceDataDocument.from_dict(usage_rules_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


