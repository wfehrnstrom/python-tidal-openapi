# UserRecommendationBlocksVideosResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | When the item was blocked | 
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 

## Example

```python
from tidal.models.user_recommendation_blocks_videos_resource_identifier_meta import UserRecommendationBlocksVideosResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecommendationBlocksVideosResourceIdentifierMeta from a JSON string
user_recommendation_blocks_videos_resource_identifier_meta_instance = UserRecommendationBlocksVideosResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(UserRecommendationBlocksVideosResourceIdentifierMeta.to_json())

# convert the object into a dict
user_recommendation_blocks_videos_resource_identifier_meta_dict = user_recommendation_blocks_videos_resource_identifier_meta_instance.to_dict()
# create an instance of UserRecommendationBlocksVideosResourceIdentifierMeta from a dict
user_recommendation_blocks_videos_resource_identifier_meta_from_dict = UserRecommendationBlocksVideosResourceIdentifierMeta.from_dict(user_recommendation_blocks_videos_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


