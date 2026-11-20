# PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument

Target resource types: `playlists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlist_generation_schedules_playlist_single_relationship_data_document import PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument from a JSON string
playlist_generation_schedules_playlist_single_relationship_data_document_instance = PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument.to_json())

# convert the object into a dict
playlist_generation_schedules_playlist_single_relationship_data_document_dict = playlist_generation_schedules_playlist_single_relationship_data_document_instance.to_dict()
# create an instance of PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument from a dict
playlist_generation_schedules_playlist_single_relationship_data_document_from_dict = PlaylistGenerationSchedulesPlaylistSingleRelationshipDataDocument.from_dict(playlist_generation_schedules_playlist_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


