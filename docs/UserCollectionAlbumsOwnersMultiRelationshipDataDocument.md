# UserCollectionAlbumsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_collection_albums_owners_multi_relationship_data_document import UserCollectionAlbumsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionAlbumsOwnersMultiRelationshipDataDocument from a JSON string
user_collection_albums_owners_multi_relationship_data_document_instance = UserCollectionAlbumsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionAlbumsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_collection_albums_owners_multi_relationship_data_document_dict = user_collection_albums_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of UserCollectionAlbumsOwnersMultiRelationshipDataDocument from a dict
user_collection_albums_owners_multi_relationship_data_document_from_dict = UserCollectionAlbumsOwnersMultiRelationshipDataDocument.from_dict(user_collection_albums_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


