# PurchasesSubjectSingleRelationshipDataDocument

Target resource types: `albums`, `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PurchasesSubjectResourceIdentifier**](PurchasesSubjectResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.purchases_subject_single_relationship_data_document import PurchasesSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PurchasesSubjectSingleRelationshipDataDocument from a JSON string
purchases_subject_single_relationship_data_document_instance = PurchasesSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PurchasesSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
purchases_subject_single_relationship_data_document_dict = purchases_subject_single_relationship_data_document_instance.to_dict()
# create an instance of PurchasesSubjectSingleRelationshipDataDocument from a dict
purchases_subject_single_relationship_data_document_from_dict = PurchasesSubjectSingleRelationshipDataDocument.from_dict(purchases_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


