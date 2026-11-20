# UserCollectionTracksItemsMultiRelationshipDataDocument

Target resource types: `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserCollectionTracksItemsResourceIdentifier]**](UserCollectionTracksItemsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_collection_tracks_items_multi_relationship_data_document import UserCollectionTracksItemsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionTracksItemsMultiRelationshipDataDocument from a JSON string
user_collection_tracks_items_multi_relationship_data_document_instance = UserCollectionTracksItemsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionTracksItemsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_collection_tracks_items_multi_relationship_data_document_dict = user_collection_tracks_items_multi_relationship_data_document_instance.to_dict()
# create an instance of UserCollectionTracksItemsMultiRelationshipDataDocument from a dict
user_collection_tracks_items_multi_relationship_data_document_from_dict = UserCollectionTracksItemsMultiRelationshipDataDocument.from_dict(user_collection_tracks_items_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


