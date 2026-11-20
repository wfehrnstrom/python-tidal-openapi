# AlbumsSimilarAlbumsMultiRelationshipDataDocument

Target resource types: `albums`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AlbumsSimilarAlbumsResourceIdentifier]**](AlbumsSimilarAlbumsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.albums_similar_albums_multi_relationship_data_document import AlbumsSimilarAlbumsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsSimilarAlbumsMultiRelationshipDataDocument from a JSON string
albums_similar_albums_multi_relationship_data_document_instance = AlbumsSimilarAlbumsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumsSimilarAlbumsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
albums_similar_albums_multi_relationship_data_document_dict = albums_similar_albums_multi_relationship_data_document_instance.to_dict()
# create an instance of AlbumsSimilarAlbumsMultiRelationshipDataDocument from a dict
albums_similar_albums_multi_relationship_data_document_from_dict = AlbumsSimilarAlbumsMultiRelationshipDataDocument.from_dict(albums_similar_albums_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


