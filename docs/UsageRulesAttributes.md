# UsageRulesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | Country code (ISO 3166-1 alpha-2) | 
**free** | **List[str]** | Usage types allowed for free/ad-supported model | [optional] 
**inherited** | **bool** | Whether these usage rules are inherited from a parent (e.g. a track inheriting from its album). Tri-state: true means the rules are inherited, false means an explicit per-track override, null means the value is unknown or not applicable (albums, videos, and legacy data). | [optional] 
**paid** | **List[str]** | Usage types allowed for paid/purchase model | [optional] 
**subscription** | **List[str]** | Usage types allowed for subscription model | [optional] 
**valid_from** | **datetime** | Datetime from which these usage rules are valid (ISO 8601) | [optional] 

## Example

```python
from tidal.models.usage_rules_attributes import UsageRulesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRulesAttributes from a JSON string
usage_rules_attributes_instance = UsageRulesAttributes.from_json(json)
# print the JSON string representation of the object
print(UsageRulesAttributes.to_json())

# convert the object into a dict
usage_rules_attributes_dict = usage_rules_attributes_instance.to_dict()
# create an instance of UsageRulesAttributes from a dict
usage_rules_attributes_from_dict = UsageRulesAttributes.from_dict(usage_rules_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


