# VideoManifestsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**VideoManifestsAttributes**](VideoManifestsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.video_manifests_resource_object import VideoManifestsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of VideoManifestsResourceObject from a JSON string
video_manifests_resource_object_instance = VideoManifestsResourceObject.from_json(json)
# print the JSON string representation of the object
print(VideoManifestsResourceObject.to_json())

# convert the object into a dict
video_manifests_resource_object_dict = video_manifests_resource_object_instance.to_dict()
# create an instance of VideoManifestsResourceObject from a dict
video_manifests_resource_object_from_dict = VideoManifestsResourceObject.from_dict(video_manifests_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


