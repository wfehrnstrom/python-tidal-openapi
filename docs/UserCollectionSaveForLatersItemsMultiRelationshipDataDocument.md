# UserCollectionSaveForLatersItemsMultiRelationshipDataDocument

Target resource types: `albums`, `artists`, `playlists`, `tracks`, `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserCollectionSaveForLatersItemsResourceIdentifier]**](UserCollectionSaveForLatersItemsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_collection_save_for_laters_items_multi_relationship_data_document import UserCollectionSaveForLatersItemsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionSaveForLatersItemsMultiRelationshipDataDocument from a JSON string
user_collection_save_for_laters_items_multi_relationship_data_document_instance = UserCollectionSaveForLatersItemsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionSaveForLatersItemsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_collection_save_for_laters_items_multi_relationship_data_document_dict = user_collection_save_for_laters_items_multi_relationship_data_document_instance.to_dict()
# create an instance of UserCollectionSaveForLatersItemsMultiRelationshipDataDocument from a dict
user_collection_save_for_laters_items_multi_relationship_data_document_from_dict = UserCollectionSaveForLatersItemsMultiRelationshipDataDocument.from_dict(user_collection_save_for_laters_items_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


