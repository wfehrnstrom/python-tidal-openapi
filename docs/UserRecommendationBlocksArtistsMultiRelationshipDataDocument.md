# UserRecommendationBlocksArtistsMultiRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserRecommendationBlocksArtistsResourceIdentifier]**](UserRecommendationBlocksArtistsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_recommendation_blocks_artists_multi_relationship_data_document import UserRecommendationBlocksArtistsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecommendationBlocksArtistsMultiRelationshipDataDocument from a JSON string
user_recommendation_blocks_artists_multi_relationship_data_document_instance = UserRecommendationBlocksArtistsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserRecommendationBlocksArtistsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_recommendation_blocks_artists_multi_relationship_data_document_dict = user_recommendation_blocks_artists_multi_relationship_data_document_instance.to_dict()
# create an instance of UserRecommendationBlocksArtistsMultiRelationshipDataDocument from a dict
user_recommendation_blocks_artists_multi_relationship_data_document_from_dict = UserRecommendationBlocksArtistsMultiRelationshipDataDocument.from_dict(user_recommendation_blocks_artists_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


