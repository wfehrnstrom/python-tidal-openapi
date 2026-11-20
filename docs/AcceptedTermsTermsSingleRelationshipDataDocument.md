# AcceptedTermsTermsSingleRelationshipDataDocument

Target resource types: `terms`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.accepted_terms_terms_single_relationship_data_document import AcceptedTermsTermsSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedTermsTermsSingleRelationshipDataDocument from a JSON string
accepted_terms_terms_single_relationship_data_document_instance = AcceptedTermsTermsSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(AcceptedTermsTermsSingleRelationshipDataDocument.to_json())

# convert the object into a dict
accepted_terms_terms_single_relationship_data_document_dict = accepted_terms_terms_single_relationship_data_document_instance.to_dict()
# create an instance of AcceptedTermsTermsSingleRelationshipDataDocument from a dict
accepted_terms_terms_single_relationship_data_document_from_dict = AcceptedTermsTermsSingleRelationshipDataDocument.from_dict(accepted_terms_terms_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


