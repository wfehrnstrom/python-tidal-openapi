# UserRecommendationBlocksArtistsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**UserRecommendationBlocksArtistsResourceIdentifierMeta**](UserRecommendationBlocksArtistsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_recommendation_blocks_artists_resource_identifier import UserRecommendationBlocksArtistsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecommendationBlocksArtistsResourceIdentifier from a JSON string
user_recommendation_blocks_artists_resource_identifier_instance = UserRecommendationBlocksArtistsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(UserRecommendationBlocksArtistsResourceIdentifier.to_json())

# convert the object into a dict
user_recommendation_blocks_artists_resource_identifier_dict = user_recommendation_blocks_artists_resource_identifier_instance.to_dict()
# create an instance of UserRecommendationBlocksArtistsResourceIdentifier from a dict
user_recommendation_blocks_artists_resource_identifier_from_dict = UserRecommendationBlocksArtistsResourceIdentifier.from_dict(user_recommendation_blocks_artists_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


