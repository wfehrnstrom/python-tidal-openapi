# VideoManifestsReadById404ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[TrackFilesReadById404ResponseBodyErrorsInner]**](TrackFilesReadById404ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.video_manifests_read_by_id404_response_body import VideoManifestsReadById404ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of VideoManifestsReadById404ResponseBody from a JSON string
video_manifests_read_by_id404_response_body_instance = VideoManifestsReadById404ResponseBody.from_json(json)
# print the JSON string representation of the object
print(VideoManifestsReadById404ResponseBody.to_json())

# convert the object into a dict
video_manifests_read_by_id404_response_body_dict = video_manifests_read_by_id404_response_body_instance.to_dict()
# create an instance of VideoManifestsReadById404ResponseBody from a dict
video_manifests_read_by_id404_response_body_from_dict = VideoManifestsReadById404ResponseBody.from_dict(video_manifests_read_by_id404_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


