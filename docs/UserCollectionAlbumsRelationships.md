# UserCollectionAlbumsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**UserCollectionAlbumsItemsMultiRelationshipDataDocument**](UserCollectionAlbumsItemsMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**UserCollectionAlbumsOwnersMultiRelationshipDataDocument**](UserCollectionAlbumsOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.user_collection_albums_relationships import UserCollectionAlbumsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionAlbumsRelationships from a JSON string
user_collection_albums_relationships_instance = UserCollectionAlbumsRelationships.from_json(json)
# print the JSON string representation of the object
print(UserCollectionAlbumsRelationships.to_json())

# convert the object into a dict
user_collection_albums_relationships_dict = user_collection_albums_relationships_instance.to_dict()
# create an instance of UserCollectionAlbumsRelationships from a dict
user_collection_albums_relationships_from_dict = UserCollectionAlbumsRelationships.from_dict(user_collection_albums_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


