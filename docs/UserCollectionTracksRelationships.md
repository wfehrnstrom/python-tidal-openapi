# UserCollectionTracksRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**UserCollectionTracksItemsMultiRelationshipDataDocument**](UserCollectionTracksItemsMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**UserCollectionTracksOwnersMultiRelationshipDataDocument**](UserCollectionTracksOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.user_collection_tracks_relationships import UserCollectionTracksRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionTracksRelationships from a JSON string
user_collection_tracks_relationships_instance = UserCollectionTracksRelationships.from_json(json)
# print the JSON string representation of the object
print(UserCollectionTracksRelationships.to_json())

# convert the object into a dict
user_collection_tracks_relationships_dict = user_collection_tracks_relationships_instance.to_dict()
# create an instance of UserCollectionTracksRelationships from a dict
user_collection_tracks_relationships_from_dict = UserCollectionTracksRelationships.from_dict(user_collection_tracks_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


