# ContentClaimsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.content_claims_owners_multi_relationship_data_document import ContentClaimsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ContentClaimsOwnersMultiRelationshipDataDocument from a JSON string
content_claims_owners_multi_relationship_data_document_instance = ContentClaimsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ContentClaimsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
content_claims_owners_multi_relationship_data_document_dict = content_claims_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of ContentClaimsOwnersMultiRelationshipDataDocument from a dict
content_claims_owners_multi_relationship_data_document_from_dict = ContentClaimsOwnersMultiRelationshipDataDocument.from_dict(content_claims_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


