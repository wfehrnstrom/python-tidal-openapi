# UsageRulesCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UsageRulesCreateOperationPayloadData**](UsageRulesCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.usage_rules_create_operation_payload import UsageRulesCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRulesCreateOperationPayload from a JSON string
usage_rules_create_operation_payload_instance = UsageRulesCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(UsageRulesCreateOperationPayload.to_json())

# convert the object into a dict
usage_rules_create_operation_payload_dict = usage_rules_create_operation_payload_instance.to_dict()
# create an instance of UsageRulesCreateOperationPayload from a dict
usage_rules_create_operation_payload_from_dict = UsageRulesCreateOperationPayload.from_dict(usage_rules_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


