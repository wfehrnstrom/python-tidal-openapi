# UsageRulesCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UsageRulesResourceObject**](UsageRulesResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.usage_rules_create_single_resource_data_document import UsageRulesCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRulesCreateSingleResourceDataDocument from a JSON string
usage_rules_create_single_resource_data_document_instance = UsageRulesCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UsageRulesCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
usage_rules_create_single_resource_data_document_dict = usage_rules_create_single_resource_data_document_instance.to_dict()
# create an instance of UsageRulesCreateSingleResourceDataDocument from a dict
usage_rules_create_single_resource_data_document_from_dict = UsageRulesCreateSingleResourceDataDocument.from_dict(usage_rules_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


