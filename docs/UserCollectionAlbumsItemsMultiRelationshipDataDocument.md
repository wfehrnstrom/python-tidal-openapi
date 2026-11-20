# UserCollectionAlbumsItemsMultiRelationshipDataDocument

Target resource types: `albums`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserCollectionAlbumsItemsResourceIdentifier]**](UserCollectionAlbumsItemsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_collection_albums_items_multi_relationship_data_document import UserCollectionAlbumsItemsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionAlbumsItemsMultiRelationshipDataDocument from a JSON string
user_collection_albums_items_multi_relationship_data_document_instance = UserCollectionAlbumsItemsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionAlbumsItemsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_collection_albums_items_multi_relationship_data_document_dict = user_collection_albums_items_multi_relationship_data_document_instance.to_dict()
# create an instance of UserCollectionAlbumsItemsMultiRelationshipDataDocument from a dict
user_collection_albums_items_multi_relationship_data_document_from_dict = UserCollectionAlbumsItemsMultiRelationshipDataDocument.from_dict(user_collection_albums_items_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


