# SourceProcessing

Available source-analysis results. Audio and waveform may be absent independently; presence does not indicate processing completion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio** | [**Audio**](Audio.md) |  | [optional] 
**waveform** | [**Waveform**](Waveform.md) |  | [optional] 

## Example

```python
from tidal.models.source_processing import SourceProcessing

# TODO update the JSON string below
json = "{}"
# create an instance of SourceProcessing from a JSON string
source_processing_instance = SourceProcessing.from_json(json)
# print the JSON string representation of the object
print(SourceProcessing.to_json())

# convert the object into a dict
source_processing_dict = source_processing_instance.to_dict()
# create an instance of SourceProcessing from a dict
source_processing_from_dict = SourceProcessing.from_dict(source_processing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


