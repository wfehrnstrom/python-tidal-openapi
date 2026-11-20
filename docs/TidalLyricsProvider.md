# TidalLyricsProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**source** | **str** |  | 

## Example

```python
from tidal.models.tidal_lyrics_provider import TidalLyricsProvider

# TODO update the JSON string below
json = "{}"
# create an instance of TidalLyricsProvider from a JSON string
tidal_lyrics_provider_instance = TidalLyricsProvider.from_json(json)
# print the JSON string representation of the object
print(TidalLyricsProvider.to_json())

# convert the object into a dict
tidal_lyrics_provider_dict = tidal_lyrics_provider_instance.to_dict()
# create an instance of TidalLyricsProvider from a dict
tidal_lyrics_provider_from_dict = TidalLyricsProvider.from_dict(tidal_lyrics_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


