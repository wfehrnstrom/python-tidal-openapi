# UsageRulesCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UsageRulesCreateOperationPayloadDataAttributes**](UsageRulesCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**UsageRulesCreateOperationPayloadDataRelationships**](UsageRulesCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.usage_rules_create_operation_payload_data import UsageRulesCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRulesCreateOperationPayloadData from a JSON string
usage_rules_create_operation_payload_data_instance = UsageRulesCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(UsageRulesCreateOperationPayloadData.to_json())

# convert the object into a dict
usage_rules_create_operation_payload_data_dict = usage_rules_create_operation_payload_data_instance.to_dict()
# create an instance of UsageRulesCreateOperationPayloadData from a dict
usage_rules_create_operation_payload_data_from_dict = UsageRulesCreateOperationPayloadData.from_dict(usage_rules_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


