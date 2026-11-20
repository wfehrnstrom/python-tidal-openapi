# UserCollectionTracksItemsAddMultiRelationshipDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserCollectionTracksItemsAddResourceIdentifier]**](UserCollectionTracksItemsAddResourceIdentifier.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | [**UserCollectionTracksItemsAddMultiRelationshipDataDocumentMeta**](UserCollectionTracksItemsAddMultiRelationshipDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.user_collection_tracks_items_add_multi_relationship_data_document import UserCollectionTracksItemsAddMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionTracksItemsAddMultiRelationshipDataDocument from a JSON string
user_collection_tracks_items_add_multi_relationship_data_document_instance = UserCollectionTracksItemsAddMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionTracksItemsAddMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_collection_tracks_items_add_multi_relationship_data_document_dict = user_collection_tracks_items_add_multi_relationship_data_document_instance.to_dict()
# create an instance of UserCollectionTracksItemsAddMultiRelationshipDataDocument from a dict
user_collection_tracks_items_add_multi_relationship_data_document_from_dict = UserCollectionTracksItemsAddMultiRelationshipDataDocument.from_dict(user_collection_tracks_items_add_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


