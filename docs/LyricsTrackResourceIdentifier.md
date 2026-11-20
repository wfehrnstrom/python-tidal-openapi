# LyricsTrackResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**LyricsTrackResourceIdentifierMeta**](LyricsTrackResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.lyrics_track_resource_identifier import LyricsTrackResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsTrackResourceIdentifier from a JSON string
lyrics_track_resource_identifier_instance = LyricsTrackResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(LyricsTrackResourceIdentifier.to_json())

# convert the object into a dict
lyrics_track_resource_identifier_dict = lyrics_track_resource_identifier_instance.to_dict()
# create an instance of LyricsTrackResourceIdentifier from a dict
lyrics_track_resource_identifier_from_dict = LyricsTrackResourceIdentifier.from_dict(lyrics_track_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


