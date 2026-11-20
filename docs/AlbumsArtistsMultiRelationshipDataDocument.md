# AlbumsArtistsMultiRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.albums_artists_multi_relationship_data_document import AlbumsArtistsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsArtistsMultiRelationshipDataDocument from a JSON string
albums_artists_multi_relationship_data_document_instance = AlbumsArtistsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumsArtistsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
albums_artists_multi_relationship_data_document_dict = albums_artists_multi_relationship_data_document_instance.to_dict()
# create an instance of AlbumsArtistsMultiRelationshipDataDocument from a dict
albums_artists_multi_relationship_data_document_from_dict = AlbumsArtistsMultiRelationshipDataDocument.from_dict(albums_artists_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


