# UserCollectionFoldersRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**UserCollectionFoldersItemsMultiRelationshipDataDocument**](UserCollectionFoldersItemsMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**UserCollectionFoldersOwnersMultiRelationshipDataDocument**](UserCollectionFoldersOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**user_collection** | [**UserCollectionFoldersUserCollectionSingleRelationshipDataDocument**](UserCollectionFoldersUserCollectionSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.user_collection_folders_relationships import UserCollectionFoldersRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionFoldersRelationships from a JSON string
user_collection_folders_relationships_instance = UserCollectionFoldersRelationships.from_json(json)
# print the JSON string representation of the object
print(UserCollectionFoldersRelationships.to_json())

# convert the object into a dict
user_collection_folders_relationships_dict = user_collection_folders_relationships_instance.to_dict()
# create an instance of UserCollectionFoldersRelationships from a dict
user_collection_folders_relationships_from_dict = UserCollectionFoldersRelationships.from_dict(user_collection_folders_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


