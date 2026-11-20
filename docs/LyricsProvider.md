# LyricsProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**source** | **str** |  | 
**common_track_id** | **str** |  | 
**lyrics_id** | **str** |  | 

## Example

```python
from tidal.models.lyrics_provider import LyricsProvider

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsProvider from a JSON string
lyrics_provider_instance = LyricsProvider.from_json(json)
# print the JSON string representation of the object
print(LyricsProvider.to_json())

# convert the object into a dict
lyrics_provider_dict = lyrics_provider_instance.to_dict()
# create an instance of LyricsProvider from a dict
lyrics_provider_from_dict = LyricsProvider.from_dict(lyrics_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


