# UsageRulesCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | [optional] 
**free** | **List[str]** |  | [optional] 
**inherited** | **bool** | Tracks only. Set to true (with empty paid/subscription/free) to clear an explicit track-level override and inherit usage rules from the album. Must be omitted or false when providing explicit usage values. | [optional] 
**paid** | **List[str]** |  | [optional] 
**subscription** | **List[str]** |  | [optional] 
**valid_from** | **datetime** | Datetime from which these usage rules are valid (ISO 8601) | [optional] 

## Example

```python
from tidal.models.usage_rules_create_operation_payload_data_attributes import UsageRulesCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRulesCreateOperationPayloadDataAttributes from a JSON string
usage_rules_create_operation_payload_data_attributes_instance = UsageRulesCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(UsageRulesCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
usage_rules_create_operation_payload_data_attributes_dict = usage_rules_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of UsageRulesCreateOperationPayloadDataAttributes from a dict
usage_rules_create_operation_payload_data_attributes_from_dict = UsageRulesCreateOperationPayloadDataAttributes.from_dict(usage_rules_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


