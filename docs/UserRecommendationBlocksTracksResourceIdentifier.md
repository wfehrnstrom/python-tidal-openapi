# UserRecommendationBlocksTracksResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**UserRecommendationBlocksTracksResourceIdentifierMeta**](UserRecommendationBlocksTracksResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_recommendation_blocks_tracks_resource_identifier import UserRecommendationBlocksTracksResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecommendationBlocksTracksResourceIdentifier from a JSON string
user_recommendation_blocks_tracks_resource_identifier_instance = UserRecommendationBlocksTracksResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(UserRecommendationBlocksTracksResourceIdentifier.to_json())

# convert the object into a dict
user_recommendation_blocks_tracks_resource_identifier_dict = user_recommendation_blocks_tracks_resource_identifier_instance.to_dict()
# create an instance of UserRecommendationBlocksTracksResourceIdentifier from a dict
user_recommendation_blocks_tracks_resource_identifier_from_dict = UserRecommendationBlocksTracksResourceIdentifier.from_dict(user_recommendation_blocks_tracks_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


