# UserCollectionVideosItemsAddMultiRelationshipDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserCollectionVideosItemsAddResourceIdentifier]**](UserCollectionVideosItemsAddResourceIdentifier.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | [**UserCollectionVideosItemsAddMultiRelationshipDataDocumentMeta**](UserCollectionVideosItemsAddMultiRelationshipDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.user_collection_videos_items_add_multi_relationship_data_document import UserCollectionVideosItemsAddMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionVideosItemsAddMultiRelationshipDataDocument from a JSON string
user_collection_videos_items_add_multi_relationship_data_document_instance = UserCollectionVideosItemsAddMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionVideosItemsAddMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_collection_videos_items_add_multi_relationship_data_document_dict = user_collection_videos_items_add_multi_relationship_data_document_instance.to_dict()
# create an instance of UserCollectionVideosItemsAddMultiRelationshipDataDocument from a dict
user_collection_videos_items_add_multi_relationship_data_document_from_dict = UserCollectionVideosItemsAddMultiRelationshipDataDocument.from_dict(user_collection_videos_items_add_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


