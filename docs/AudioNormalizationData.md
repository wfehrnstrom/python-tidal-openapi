# AudioNormalizationData

Track normalization data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peak_amplitude** | **float** |  | [optional] 
**replay_gain** | **float** |  | [optional] 

## Example

```python
from tidal.models.audio_normalization_data import AudioNormalizationData

# TODO update the JSON string below
json = "{}"
# create an instance of AudioNormalizationData from a JSON string
audio_normalization_data_instance = AudioNormalizationData.from_json(json)
# print the JSON string representation of the object
print(AudioNormalizationData.to_json())

# convert the object into a dict
audio_normalization_data_dict = audio_normalization_data_instance.to_dict()
# create an instance of AudioNormalizationData from a dict
audio_normalization_data_from_dict = AudioNormalizationData.from_dict(audio_normalization_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


