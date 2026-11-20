# LyricsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**LyricsOwnersMultiRelationshipDataDocument**](LyricsOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**track** | [**LyricsTrackSingleRelationshipDataDocument**](LyricsTrackSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.lyrics_relationships import LyricsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsRelationships from a JSON string
lyrics_relationships_instance = LyricsRelationships.from_json(json)
# print the JSON string representation of the object
print(LyricsRelationships.to_json())

# convert the object into a dict
lyrics_relationships_dict = lyrics_relationships_instance.to_dict()
# create an instance of LyricsRelationships from a dict
lyrics_relationships_from_dict = LyricsRelationships.from_dict(lyrics_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


