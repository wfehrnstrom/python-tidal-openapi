# UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_collection_save_for_laters_owners_multi_relationship_data_document import UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument from a JSON string
user_collection_save_for_laters_owners_multi_relationship_data_document_instance = UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_collection_save_for_laters_owners_multi_relationship_data_document_dict = user_collection_save_for_laters_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument from a dict
user_collection_save_for_laters_owners_multi_relationship_data_document_from_dict = UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument.from_dict(user_collection_save_for_laters_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


