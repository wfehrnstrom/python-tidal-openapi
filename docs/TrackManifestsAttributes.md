# TrackManifestsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_audio_normalization_data** | [**AudioNormalizationData**](AudioNormalizationData.md) |  | [optional] 
**drm_data** | [**DrmData**](DrmData.md) |  | [optional] 
**formats** | **List[str]** | Formats present in manifest | [optional] 
**hash** | **str** | Unique manifest hash | [optional] 
**preview_reason** | **str** | Why a preview is served instead of the full track | [optional] 
**track_audio_normalization_data** | [**AudioNormalizationData**](AudioNormalizationData.md) |  | [optional] 
**track_presentation** | **str** | Track presentation | [optional] 
**uri** | **str** | Manifest URI | [optional] 

## Example

```python
from tidal.models.track_manifests_attributes import TrackManifestsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TrackManifestsAttributes from a JSON string
track_manifests_attributes_instance = TrackManifestsAttributes.from_json(json)
# print the JSON string representation of the object
print(TrackManifestsAttributes.to_json())

# convert the object into a dict
track_manifests_attributes_dict = track_manifests_attributes_instance.to_dict()
# create an instance of TrackManifestsAttributes from a dict
track_manifests_attributes_from_dict = TrackManifestsAttributes.from_dict(track_manifests_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


