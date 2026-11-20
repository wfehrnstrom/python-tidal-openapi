# LyricsTrackSingleRelationshipDataDocument

Target resource types: `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LyricsTrackResourceIdentifier**](LyricsTrackResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.lyrics_track_single_relationship_data_document import LyricsTrackSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsTrackSingleRelationshipDataDocument from a JSON string
lyrics_track_single_relationship_data_document_instance = LyricsTrackSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(LyricsTrackSingleRelationshipDataDocument.to_json())

# convert the object into a dict
lyrics_track_single_relationship_data_document_dict = lyrics_track_single_relationship_data_document_instance.to_dict()
# create an instance of LyricsTrackSingleRelationshipDataDocument from a dict
lyrics_track_single_relationship_data_document_from_dict = LyricsTrackSingleRelationshipDataDocument.from_dict(lyrics_track_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


