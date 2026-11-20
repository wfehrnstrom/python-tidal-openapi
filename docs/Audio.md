# Audio

Available audio measurements for this source. May be absent independently of waveform.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bit_depth** | **int** | Source audio bit depth in bits per sample. Absent for lossy audio or when unknown. | [optional] 
**bitrate** | **int** | Source audio bitrate in bits per second. Absent when unknown. | [optional] 
**codec** | **str** | Source audio encoding. New values may be added. | [optional] 
**duration** | **str** | Duration of the source audio rounded up to 100 ms (ISO 8601), independent of catalogue or rendition duration. Absent when unknown. | [optional] 
**sample_rate** | **int** | Source audio sample rate in hertz. Absent when unknown. | [optional] 

## Example

```python
from tidal.models.audio import Audio

# TODO update the JSON string below
json = "{}"
# create an instance of Audio from a JSON string
audio_instance = Audio.from_json(json)
# print the JSON string representation of the object
print(Audio.to_json())

# convert the object into a dict
audio_dict = audio_instance.to_dict()
# create an instance of Audio from a dict
audio_from_dict = Audio.from_dict(audio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


