# AcceptedTermsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**AcceptedTermsOwnersMultiRelationshipDataDocument**](AcceptedTermsOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**terms** | [**AcceptedTermsTermsSingleRelationshipDataDocument**](AcceptedTermsTermsSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.accepted_terms_relationships import AcceptedTermsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedTermsRelationships from a JSON string
accepted_terms_relationships_instance = AcceptedTermsRelationships.from_json(json)
# print the JSON string representation of the object
print(AcceptedTermsRelationships.to_json())

# convert the object into a dict
accepted_terms_relationships_dict = accepted_terms_relationships_instance.to_dict()
# create an instance of AcceptedTermsRelationships from a dict
accepted_terms_relationships_from_dict = AcceptedTermsRelationships.from_dict(accepted_terms_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


