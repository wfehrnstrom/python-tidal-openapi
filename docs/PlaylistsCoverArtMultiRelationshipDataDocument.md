# PlaylistsCoverArtMultiRelationshipDataDocument

Target resource types: `artworks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlists_cover_art_multi_relationship_data_document import PlaylistsCoverArtMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsCoverArtMultiRelationshipDataDocument from a JSON string
playlists_cover_art_multi_relationship_data_document_instance = PlaylistsCoverArtMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistsCoverArtMultiRelationshipDataDocument.to_json())

# convert the object into a dict
playlists_cover_art_multi_relationship_data_document_dict = playlists_cover_art_multi_relationship_data_document_instance.to_dict()
# create an instance of PlaylistsCoverArtMultiRelationshipDataDocument from a dict
playlists_cover_art_multi_relationship_data_document_from_dict = PlaylistsCoverArtMultiRelationshipDataDocument.from_dict(playlists_cover_art_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


