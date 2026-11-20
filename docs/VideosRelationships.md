# VideosRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**albums** | [**VideosAlbumsMultiRelationshipDataDocument**](VideosAlbumsMultiRelationshipDataDocument.md) |  | [optional] 
**artists** | [**VideosArtistsMultiRelationshipDataDocument**](VideosArtistsMultiRelationshipDataDocument.md) |  | [optional] 
**credits** | [**VideosCreditsMultiRelationshipDataDocument**](VideosCreditsMultiRelationshipDataDocument.md) |  | [optional] 
**providers** | [**VideosProvidersMultiRelationshipDataDocument**](VideosProvidersMultiRelationshipDataDocument.md) |  | [optional] 
**replacement** | [**VideosReplacementSingleRelationshipDataDocument**](VideosReplacementSingleRelationshipDataDocument.md) |  | [optional] 
**similar_videos** | [**VideosSimilarVideosMultiRelationshipDataDocument**](VideosSimilarVideosMultiRelationshipDataDocument.md) |  | [optional] 
**suggested_videos** | [**VideosSuggestedVideosMultiRelationshipDataDocument**](VideosSuggestedVideosMultiRelationshipDataDocument.md) |  | [optional] 
**thumbnail_art** | [**VideosThumbnailArtMultiRelationshipDataDocument**](VideosThumbnailArtMultiRelationshipDataDocument.md) |  | [optional] 
**usage_rules** | [**VideosUsageRulesSingleRelationshipDataDocument**](VideosUsageRulesSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.videos_relationships import VideosRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of VideosRelationships from a JSON string
videos_relationships_instance = VideosRelationships.from_json(json)
# print the JSON string representation of the object
print(VideosRelationships.to_json())

# convert the object into a dict
videos_relationships_dict = videos_relationships_instance.to_dict()
# create an instance of VideosRelationships from a dict
videos_relationships_from_dict = VideosRelationships.from_dict(videos_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


