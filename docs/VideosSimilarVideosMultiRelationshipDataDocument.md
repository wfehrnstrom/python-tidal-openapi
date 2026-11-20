# VideosSimilarVideosMultiRelationshipDataDocument

Target resource types: `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VideosSimilarVideosResourceIdentifier]**](VideosSimilarVideosResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.videos_similar_videos_multi_relationship_data_document import VideosSimilarVideosMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of VideosSimilarVideosMultiRelationshipDataDocument from a JSON string
videos_similar_videos_multi_relationship_data_document_instance = VideosSimilarVideosMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(VideosSimilarVideosMultiRelationshipDataDocument.to_json())

# convert the object into a dict
videos_similar_videos_multi_relationship_data_document_dict = videos_similar_videos_multi_relationship_data_document_instance.to_dict()
# create an instance of VideosSimilarVideosMultiRelationshipDataDocument from a dict
videos_similar_videos_multi_relationship_data_document_from_dict = VideosSimilarVideosMultiRelationshipDataDocument.from_dict(videos_similar_videos_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


