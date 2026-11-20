# AlbumsCoverArtMultiRelationshipDataDocument

Target resource types: `artworks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.albums_cover_art_multi_relationship_data_document import AlbumsCoverArtMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsCoverArtMultiRelationshipDataDocument from a JSON string
albums_cover_art_multi_relationship_data_document_instance = AlbumsCoverArtMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumsCoverArtMultiRelationshipDataDocument.to_json())

# convert the object into a dict
albums_cover_art_multi_relationship_data_document_dict = albums_cover_art_multi_relationship_data_document_instance.to_dict()
# create an instance of AlbumsCoverArtMultiRelationshipDataDocument from a dict
albums_cover_art_multi_relationship_data_document_from_dict = AlbumsCoverArtMultiRelationshipDataDocument.from_dict(albums_cover_art_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


