# TrackFilesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_audio_normalization_data** | [**AudioNormalizationData**](AudioNormalizationData.md) |  | [optional] 
**format** | **str** | File&#39;s audio format | [optional] 
**track_audio_normalization_data** | [**AudioNormalizationData**](AudioNormalizationData.md) |  | [optional] 
**track_presentation** | **str** | Track presentation | [optional] 
**url** | **str** | File URL | [optional] 

## Example

```python
from tidal.models.track_files_attributes import TrackFilesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TrackFilesAttributes from a JSON string
track_files_attributes_instance = TrackFilesAttributes.from_json(json)
# print the JSON string representation of the object
print(TrackFilesAttributes.to_json())

# convert the object into a dict
track_files_attributes_dict = track_files_attributes_instance.to_dict()
# create an instance of TrackFilesAttributes from a dict
track_files_attributes_from_dict = TrackFilesAttributes.from_dict(track_files_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


