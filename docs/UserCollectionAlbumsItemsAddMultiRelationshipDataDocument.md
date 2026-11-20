# UserCollectionAlbumsItemsAddMultiRelationshipDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserCollectionAlbumsItemsAddResourceIdentifier]**](UserCollectionAlbumsItemsAddResourceIdentifier.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | [**UserCollectionAlbumsItemsAddMultiRelationshipDataDocumentMeta**](UserCollectionAlbumsItemsAddMultiRelationshipDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.user_collection_albums_items_add_multi_relationship_data_document import UserCollectionAlbumsItemsAddMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionAlbumsItemsAddMultiRelationshipDataDocument from a JSON string
user_collection_albums_items_add_multi_relationship_data_document_instance = UserCollectionAlbumsItemsAddMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionAlbumsItemsAddMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_collection_albums_items_add_multi_relationship_data_document_dict = user_collection_albums_items_add_multi_relationship_data_document_instance.to_dict()
# create an instance of UserCollectionAlbumsItemsAddMultiRelationshipDataDocument from a dict
user_collection_albums_items_add_multi_relationship_data_document_from_dict = UserCollectionAlbumsItemsAddMultiRelationshipDataDocument.from_dict(user_collection_albums_items_add_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


