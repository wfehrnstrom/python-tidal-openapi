# CreditsCategorySingleRelationshipDataDocument

Target resource types: `artistRoles`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.credits_category_single_relationship_data_document import CreditsCategorySingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CreditsCategorySingleRelationshipDataDocument from a JSON string
credits_category_single_relationship_data_document_instance = CreditsCategorySingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(CreditsCategorySingleRelationshipDataDocument.to_json())

# convert the object into a dict
credits_category_single_relationship_data_document_dict = credits_category_single_relationship_data_document_instance.to_dict()
# create an instance of CreditsCategorySingleRelationshipDataDocument from a dict
credits_category_single_relationship_data_document_from_dict = CreditsCategorySingleRelationshipDataDocument.from_dict(credits_category_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


