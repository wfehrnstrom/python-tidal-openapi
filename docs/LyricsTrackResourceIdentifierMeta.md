# LyricsTrackResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 

## Example

```python
from tidal.models.lyrics_track_resource_identifier_meta import LyricsTrackResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsTrackResourceIdentifierMeta from a JSON string
lyrics_track_resource_identifier_meta_instance = LyricsTrackResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(LyricsTrackResourceIdentifierMeta.to_json())

# convert the object into a dict
lyrics_track_resource_identifier_meta_dict = lyrics_track_resource_identifier_meta_instance.to_dict()
# create an instance of LyricsTrackResourceIdentifierMeta from a dict
lyrics_track_resource_identifier_meta_from_dict = LyricsTrackResourceIdentifierMeta.from_dict(lyrics_track_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


