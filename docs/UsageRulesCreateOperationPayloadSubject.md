# UsageRulesCreateOperationPayloadSubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.usage_rules_create_operation_payload_subject import UsageRulesCreateOperationPayloadSubject

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRulesCreateOperationPayloadSubject from a JSON string
usage_rules_create_operation_payload_subject_instance = UsageRulesCreateOperationPayloadSubject.from_json(json)
# print the JSON string representation of the object
print(UsageRulesCreateOperationPayloadSubject.to_json())

# convert the object into a dict
usage_rules_create_operation_payload_subject_dict = usage_rules_create_operation_payload_subject_instance.to_dict()
# create an instance of UsageRulesCreateOperationPayloadSubject from a dict
usage_rules_create_operation_payload_subject_from_dict = UsageRulesCreateOperationPayloadSubject.from_dict(usage_rules_create_operation_payload_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


