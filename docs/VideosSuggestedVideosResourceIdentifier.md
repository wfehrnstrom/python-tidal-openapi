# VideosSuggestedVideosResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**VideosSuggestedVideosResourceIdentifierMeta**](VideosSuggestedVideosResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.videos_suggested_videos_resource_identifier import VideosSuggestedVideosResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of VideosSuggestedVideosResourceIdentifier from a JSON string
videos_suggested_videos_resource_identifier_instance = VideosSuggestedVideosResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(VideosSuggestedVideosResourceIdentifier.to_json())

# convert the object into a dict
videos_suggested_videos_resource_identifier_dict = videos_suggested_videos_resource_identifier_instance.to_dict()
# create an instance of VideosSuggestedVideosResourceIdentifier from a dict
videos_suggested_videos_resource_identifier_from_dict = VideosSuggestedVideosResourceIdentifier.from_dict(videos_suggested_videos_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


