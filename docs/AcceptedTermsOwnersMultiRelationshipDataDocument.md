# AcceptedTermsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.accepted_terms_owners_multi_relationship_data_document import AcceptedTermsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedTermsOwnersMultiRelationshipDataDocument from a JSON string
accepted_terms_owners_multi_relationship_data_document_instance = AcceptedTermsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(AcceptedTermsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
accepted_terms_owners_multi_relationship_data_document_dict = accepted_terms_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of AcceptedTermsOwnersMultiRelationshipDataDocument from a dict
accepted_terms_owners_multi_relationship_data_document_from_dict = AcceptedTermsOwnersMultiRelationshipDataDocument.from_dict(accepted_terms_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


