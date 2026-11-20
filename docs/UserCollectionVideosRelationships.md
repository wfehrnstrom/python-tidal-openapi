# UserCollectionVideosRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**UserCollectionVideosItemsMultiRelationshipDataDocument**](UserCollectionVideosItemsMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**UserCollectionVideosOwnersMultiRelationshipDataDocument**](UserCollectionVideosOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.user_collection_videos_relationships import UserCollectionVideosRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionVideosRelationships from a JSON string
user_collection_videos_relationships_instance = UserCollectionVideosRelationships.from_json(json)
# print the JSON string representation of the object
print(UserCollectionVideosRelationships.to_json())

# convert the object into a dict
user_collection_videos_relationships_dict = user_collection_videos_relationships_instance.to_dict()
# create an instance of UserCollectionVideosRelationships from a dict
user_collection_videos_relationships_from_dict = UserCollectionVideosRelationships.from_dict(user_collection_videos_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


