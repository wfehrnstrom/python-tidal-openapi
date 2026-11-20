# ThirdPartyLyricsProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_track_id** | **str** |  | 
**lyrics_id** | **str** |  | 
**name** | **str** |  | 
**source** | **str** |  | 

## Example

```python
from tidal.models.third_party_lyrics_provider import ThirdPartyLyricsProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyLyricsProvider from a JSON string
third_party_lyrics_provider_instance = ThirdPartyLyricsProvider.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyLyricsProvider.to_json())

# convert the object into a dict
third_party_lyrics_provider_dict = third_party_lyrics_provider_instance.to_dict()
# create an instance of ThirdPartyLyricsProvider from a dict
third_party_lyrics_provider_from_dict = ThirdPartyLyricsProvider.from_dict(third_party_lyrics_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


