# UserRecommendationBlocksTracksMultiRelationshipDataDocument

Target resource types: `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserRecommendationBlocksTracksResourceIdentifier]**](UserRecommendationBlocksTracksResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_recommendation_blocks_tracks_multi_relationship_data_document import UserRecommendationBlocksTracksMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecommendationBlocksTracksMultiRelationshipDataDocument from a JSON string
user_recommendation_blocks_tracks_multi_relationship_data_document_instance = UserRecommendationBlocksTracksMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserRecommendationBlocksTracksMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_recommendation_blocks_tracks_multi_relationship_data_document_dict = user_recommendation_blocks_tracks_multi_relationship_data_document_instance.to_dict()
# create an instance of UserRecommendationBlocksTracksMultiRelationshipDataDocument from a dict
user_recommendation_blocks_tracks_multi_relationship_data_document_from_dict = UserRecommendationBlocksTracksMultiRelationshipDataDocument.from_dict(user_recommendation_blocks_tracks_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


