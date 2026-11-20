# PurchasesSubjectResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**PurchasesSubjectResourceIdentifierMeta**](PurchasesSubjectResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.purchases_subject_resource_identifier import PurchasesSubjectResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PurchasesSubjectResourceIdentifier from a JSON string
purchases_subject_resource_identifier_instance = PurchasesSubjectResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(PurchasesSubjectResourceIdentifier.to_json())

# convert the object into a dict
purchases_subject_resource_identifier_dict = purchases_subject_resource_identifier_instance.to_dict()
# create an instance of PurchasesSubjectResourceIdentifier from a dict
purchases_subject_resource_identifier_from_dict = PurchasesSubjectResourceIdentifier.from_dict(purchases_subject_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


