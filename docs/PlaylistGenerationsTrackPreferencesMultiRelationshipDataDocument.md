# PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument

Target resource types: `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlaylistGenerationsTrackPreferencesResourceIdentifier]**](PlaylistGenerationsTrackPreferencesResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 
**meta** | [**PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocumentMeta**](PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.playlist_generations_track_preferences_multi_relationship_data_document import PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument from a JSON string
playlist_generations_track_preferences_multi_relationship_data_document_instance = PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument.to_json())

# convert the object into a dict
playlist_generations_track_preferences_multi_relationship_data_document_dict = playlist_generations_track_preferences_multi_relationship_data_document_instance.to_dict()
# create an instance of PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument from a dict
playlist_generations_track_preferences_multi_relationship_data_document_from_dict = PlaylistGenerationsTrackPreferencesMultiRelationshipDataDocument.from_dict(playlist_generations_track_preferences_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


