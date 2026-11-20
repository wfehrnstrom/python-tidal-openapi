# PlaylistGenerationsPlaylistSingleRelationshipDataDocument

Target resource types: `playlists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlist_generations_playlist_single_relationship_data_document import PlaylistGenerationsPlaylistSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsPlaylistSingleRelationshipDataDocument from a JSON string
playlist_generations_playlist_single_relationship_data_document_instance = PlaylistGenerationsPlaylistSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsPlaylistSingleRelationshipDataDocument.to_json())

# convert the object into a dict
playlist_generations_playlist_single_relationship_data_document_dict = playlist_generations_playlist_single_relationship_data_document_instance.to_dict()
# create an instance of PlaylistGenerationsPlaylistSingleRelationshipDataDocument from a dict
playlist_generations_playlist_single_relationship_data_document_from_dict = PlaylistGenerationsPlaylistSingleRelationshipDataDocument.from_dict(playlist_generations_playlist_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


