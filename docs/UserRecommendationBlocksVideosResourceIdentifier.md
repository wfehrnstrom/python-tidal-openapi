# UserRecommendationBlocksVideosResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**UserRecommendationBlocksVideosResourceIdentifierMeta**](UserRecommendationBlocksVideosResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_recommendation_blocks_videos_resource_identifier import UserRecommendationBlocksVideosResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecommendationBlocksVideosResourceIdentifier from a JSON string
user_recommendation_blocks_videos_resource_identifier_instance = UserRecommendationBlocksVideosResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(UserRecommendationBlocksVideosResourceIdentifier.to_json())

# convert the object into a dict
user_recommendation_blocks_videos_resource_identifier_dict = user_recommendation_blocks_videos_resource_identifier_instance.to_dict()
# create an instance of UserRecommendationBlocksVideosResourceIdentifier from a dict
user_recommendation_blocks_videos_resource_identifier_from_dict = UserRecommendationBlocksVideosResourceIdentifier.from_dict(user_recommendation_blocks_videos_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


