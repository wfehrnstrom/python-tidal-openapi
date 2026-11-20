# VideoManifestsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drm_data** | [**DrmData**](DrmData.md) |  | [optional] 
**link** | [**LinkObject**](LinkObject.md) |  | [optional] 
**preview_reason** | **str** | Why a preview is served instead of the full video | [optional] 
**video_presentation** | **str** | Video presentation | [optional] 

## Example

```python
from tidal.models.video_manifests_attributes import VideoManifestsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of VideoManifestsAttributes from a JSON string
video_manifests_attributes_instance = VideoManifestsAttributes.from_json(json)
# print the JSON string representation of the object
print(VideoManifestsAttributes.to_json())

# convert the object into a dict
video_manifests_attributes_dict = video_manifests_attributes_instance.to_dict()
# create an instance of VideoManifestsAttributes from a dict
video_manifests_attributes_from_dict = VideoManifestsAttributes.from_dict(video_manifests_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


