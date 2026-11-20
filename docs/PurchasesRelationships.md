# PurchasesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**PurchasesOwnersMultiRelationshipDataDocument**](PurchasesOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**subject** | [**PurchasesSubjectSingleRelationshipDataDocument**](PurchasesSubjectSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.purchases_relationships import PurchasesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PurchasesRelationships from a JSON string
purchases_relationships_instance = PurchasesRelationships.from_json(json)
# print the JSON string representation of the object
print(PurchasesRelationships.to_json())

# convert the object into a dict
purchases_relationships_dict = purchases_relationships_instance.to_dict()
# create an instance of PurchasesRelationships from a dict
purchases_relationships_from_dict = PurchasesRelationships.from_dict(purchases_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


