# PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument

Target resource types: `artworks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlaylistsSuggestedCoverArtsResourceIdentifier]**](PlaylistsSuggestedCoverArtsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlists_suggested_cover_arts_multi_relationship_data_document import PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument from a JSON string
playlists_suggested_cover_arts_multi_relationship_data_document_instance = PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
playlists_suggested_cover_arts_multi_relationship_data_document_dict = playlists_suggested_cover_arts_multi_relationship_data_document_instance.to_dict()
# create an instance of PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument from a dict
playlists_suggested_cover_arts_multi_relationship_data_document_from_dict = PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument.from_dict(playlists_suggested_cover_arts_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


