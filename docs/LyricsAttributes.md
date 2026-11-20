# LyricsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** |  | [optional] 
**lrc_text** | **str** |  | [optional] 
**provider** | [**LyricsProvider**](LyricsProvider.md) |  | [optional] 
**technical_status** | **str** |  | 
**text** | **str** |  | [optional] 

## Example

```python
from tidal.models.lyrics_attributes import LyricsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsAttributes from a JSON string
lyrics_attributes_instance = LyricsAttributes.from_json(json)
# print the JSON string representation of the object
print(LyricsAttributes.to_json())

# convert the object into a dict
lyrics_attributes_dict = lyrics_attributes_instance.to_dict()
# create an instance of LyricsAttributes from a dict
lyrics_attributes_from_dict = LyricsAttributes.from_dict(lyrics_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


