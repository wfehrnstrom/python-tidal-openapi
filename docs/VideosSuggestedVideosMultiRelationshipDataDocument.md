# VideosSuggestedVideosMultiRelationshipDataDocument

Target resource types: `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VideosSuggestedVideosResourceIdentifier]**](VideosSuggestedVideosResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.videos_suggested_videos_multi_relationship_data_document import VideosSuggestedVideosMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of VideosSuggestedVideosMultiRelationshipDataDocument from a JSON string
videos_suggested_videos_multi_relationship_data_document_instance = VideosSuggestedVideosMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(VideosSuggestedVideosMultiRelationshipDataDocument.to_json())

# convert the object into a dict
videos_suggested_videos_multi_relationship_data_document_dict = videos_suggested_videos_multi_relationship_data_document_instance.to_dict()
# create an instance of VideosSuggestedVideosMultiRelationshipDataDocument from a dict
videos_suggested_videos_multi_relationship_data_document_from_dict = VideosSuggestedVideosMultiRelationshipDataDocument.from_dict(videos_suggested_videos_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


