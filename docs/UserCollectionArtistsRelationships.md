# UserCollectionArtistsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**UserCollectionArtistsItemsMultiRelationshipDataDocument**](UserCollectionArtistsItemsMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**UserCollectionArtistsOwnersMultiRelationshipDataDocument**](UserCollectionArtistsOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.user_collection_artists_relationships import UserCollectionArtistsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionArtistsRelationships from a JSON string
user_collection_artists_relationships_instance = UserCollectionArtistsRelationships.from_json(json)
# print the JSON string representation of the object
print(UserCollectionArtistsRelationships.to_json())

# convert the object into a dict
user_collection_artists_relationships_dict = user_collection_artists_relationships_instance.to_dict()
# create an instance of UserCollectionArtistsRelationships from a dict
user_collection_artists_relationships_from_dict = UserCollectionArtistsRelationships.from_dict(user_collection_artists_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


