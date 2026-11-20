# UserCollectionFoldersOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_collection_folders_owners_multi_relationship_data_document import UserCollectionFoldersOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionFoldersOwnersMultiRelationshipDataDocument from a JSON string
user_collection_folders_owners_multi_relationship_data_document_instance = UserCollectionFoldersOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionFoldersOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_collection_folders_owners_multi_relationship_data_document_dict = user_collection_folders_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of UserCollectionFoldersOwnersMultiRelationshipDataDocument from a dict
user_collection_folders_owners_multi_relationship_data_document_from_dict = UserCollectionFoldersOwnersMultiRelationshipDataDocument.from_dict(user_collection_folders_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


