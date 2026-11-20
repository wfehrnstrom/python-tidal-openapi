# UserRecommendationBlocksVideosMultiRelationshipDataDocument

Target resource types: `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserRecommendationBlocksVideosResourceIdentifier]**](UserRecommendationBlocksVideosResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_recommendation_blocks_videos_multi_relationship_data_document import UserRecommendationBlocksVideosMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecommendationBlocksVideosMultiRelationshipDataDocument from a JSON string
user_recommendation_blocks_videos_multi_relationship_data_document_instance = UserRecommendationBlocksVideosMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserRecommendationBlocksVideosMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_recommendation_blocks_videos_multi_relationship_data_document_dict = user_recommendation_blocks_videos_multi_relationship_data_document_instance.to_dict()
# create an instance of UserRecommendationBlocksVideosMultiRelationshipDataDocument from a dict
user_recommendation_blocks_videos_multi_relationship_data_document_from_dict = UserRecommendationBlocksVideosMultiRelationshipDataDocument.from_dict(user_recommendation_blocks_videos_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


