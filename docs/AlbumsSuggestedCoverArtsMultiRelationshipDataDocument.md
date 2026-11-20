# AlbumsSuggestedCoverArtsMultiRelationshipDataDocument

Target resource types: `artworks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AlbumsSuggestedCoverArtsResourceIdentifier]**](AlbumsSuggestedCoverArtsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 
**meta** | [**AlbumsSuggestedCoverArtsMultiRelationshipDataDocumentMeta**](AlbumsSuggestedCoverArtsMultiRelationshipDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.albums_suggested_cover_arts_multi_relationship_data_document import AlbumsSuggestedCoverArtsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsSuggestedCoverArtsMultiRelationshipDataDocument from a JSON string
albums_suggested_cover_arts_multi_relationship_data_document_instance = AlbumsSuggestedCoverArtsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumsSuggestedCoverArtsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
albums_suggested_cover_arts_multi_relationship_data_document_dict = albums_suggested_cover_arts_multi_relationship_data_document_instance.to_dict()
# create an instance of AlbumsSuggestedCoverArtsMultiRelationshipDataDocument from a dict
albums_suggested_cover_arts_multi_relationship_data_document_from_dict = AlbumsSuggestedCoverArtsMultiRelationshipDataDocument.from_dict(albums_suggested_cover_arts_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


