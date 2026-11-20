# TemporaryUserTokensRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**TemporaryUserTokensOwnersMultiRelationshipDataDocument**](TemporaryUserTokensOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.temporary_user_tokens_relationships import TemporaryUserTokensRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryUserTokensRelationships from a JSON string
temporary_user_tokens_relationships_instance = TemporaryUserTokensRelationships.from_json(json)
# print the JSON string representation of the object
print(TemporaryUserTokensRelationships.to_json())

# convert the object into a dict
temporary_user_tokens_relationships_dict = temporary_user_tokens_relationships_instance.to_dict()
# create an instance of TemporaryUserTokensRelationships from a dict
temporary_user_tokens_relationships_from_dict = TemporaryUserTokensRelationships.from_dict(temporary_user_tokens_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


