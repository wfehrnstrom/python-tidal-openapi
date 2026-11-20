# VideosSimilarVideosResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**VideosSimilarVideosResourceIdentifierMeta**](VideosSimilarVideosResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.videos_similar_videos_resource_identifier import VideosSimilarVideosResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of VideosSimilarVideosResourceIdentifier from a JSON string
videos_similar_videos_resource_identifier_instance = VideosSimilarVideosResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(VideosSimilarVideosResourceIdentifier.to_json())

# convert the object into a dict
videos_similar_videos_resource_identifier_dict = videos_similar_videos_resource_identifier_instance.to_dict()
# create an instance of VideosSimilarVideosResourceIdentifier from a dict
videos_similar_videos_resource_identifier_from_dict = VideosSimilarVideosResourceIdentifier.from_dict(videos_similar_videos_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


