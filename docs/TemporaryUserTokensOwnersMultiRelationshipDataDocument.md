# TemporaryUserTokensOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.temporary_user_tokens_owners_multi_relationship_data_document import TemporaryUserTokensOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryUserTokensOwnersMultiRelationshipDataDocument from a JSON string
temporary_user_tokens_owners_multi_relationship_data_document_instance = TemporaryUserTokensOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TemporaryUserTokensOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
temporary_user_tokens_owners_multi_relationship_data_document_dict = temporary_user_tokens_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of TemporaryUserTokensOwnersMultiRelationshipDataDocument from a dict
temporary_user_tokens_owners_multi_relationship_data_document_from_dict = TemporaryUserTokensOwnersMultiRelationshipDataDocument.from_dict(temporary_user_tokens_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


