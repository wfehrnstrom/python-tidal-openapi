# VideoManifestsReadById403ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[TrackFilesReadById403ResponseBodyErrorsInner]**](TrackFilesReadById403ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.video_manifests_read_by_id403_response_body import VideoManifestsReadById403ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of VideoManifestsReadById403ResponseBody from a JSON string
video_manifests_read_by_id403_response_body_instance = VideoManifestsReadById403ResponseBody.from_json(json)
# print the JSON string representation of the object
print(VideoManifestsReadById403ResponseBody.to_json())

# convert the object into a dict
video_manifests_read_by_id403_response_body_dict = video_manifests_read_by_id403_response_body_instance.to_dict()
# create an instance of VideoManifestsReadById403ResponseBody from a dict
video_manifests_read_by_id403_response_body_from_dict = VideoManifestsReadById403ResponseBody.from_dict(video_manifests_read_by_id403_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


