# UserRecommendationBlocksRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artists** | [**UserRecommendationBlocksArtistsMultiRelationshipDataDocument**](UserRecommendationBlocksArtistsMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**UserRecommendationBlocksOwnersMultiRelationshipDataDocument**](UserRecommendationBlocksOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**tracks** | [**UserRecommendationBlocksTracksMultiRelationshipDataDocument**](UserRecommendationBlocksTracksMultiRelationshipDataDocument.md) |  | [optional] 
**videos** | [**UserRecommendationBlocksVideosMultiRelationshipDataDocument**](UserRecommendationBlocksVideosMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.user_recommendation_blocks_relationships import UserRecommendationBlocksRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecommendationBlocksRelationships from a JSON string
user_recommendation_blocks_relationships_instance = UserRecommendationBlocksRelationships.from_json(json)
# print the JSON string representation of the object
print(UserRecommendationBlocksRelationships.to_json())

# convert the object into a dict
user_recommendation_blocks_relationships_dict = user_recommendation_blocks_relationships_instance.to_dict()
# create an instance of UserRecommendationBlocksRelationships from a dict
user_recommendation_blocks_relationships_from_dict = UserRecommendationBlocksRelationships.from_dict(user_recommendation_blocks_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


