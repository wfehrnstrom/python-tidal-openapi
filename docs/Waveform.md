# Waveform

Available waveform for this source. May be absent independently of audio. Map playback progress as time/processing.audio.duration when available; catalogue and preview durations are not interchangeable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[int]** | 256 evenly selected 50 ms RMS windows across the entire source, in time order. Values range from 0 to 65535 relative to the largest selected amplitude. Short sources repeat windows; values are not duration/256 aggregates. | 

## Example

```python
from tidal.models.waveform import Waveform

# TODO update the JSON string below
json = "{}"
# create an instance of Waveform from a JSON string
waveform_instance = Waveform.from_json(json)
# print the JSON string representation of the object
print(Waveform.to_json())

# convert the object into a dict
waveform_dict = waveform_instance.to_dict()
# create an instance of Waveform from a dict
waveform_from_dict = Waveform.from_dict(waveform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


