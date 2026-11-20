# UserCollectionFoldersUserCollectionSingleRelationshipDataDocument

Target resource types: `userCollectionPlaylists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_collection_folders_user_collection_single_relationship_data_document import UserCollectionFoldersUserCollectionSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionFoldersUserCollectionSingleRelationshipDataDocument from a JSON string
user_collection_folders_user_collection_single_relationship_data_document_instance = UserCollectionFoldersUserCollectionSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionFoldersUserCollectionSingleRelationshipDataDocument.to_json())

# convert the object into a dict
user_collection_folders_user_collection_single_relationship_data_document_dict = user_collection_folders_user_collection_single_relationship_data_document_instance.to_dict()
# create an instance of UserCollectionFoldersUserCollectionSingleRelationshipDataDocument from a dict
user_collection_folders_user_collection_single_relationship_data_document_from_dict = UserCollectionFoldersUserCollectionSingleRelationshipDataDocument.from_dict(user_collection_folders_user_collection_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


