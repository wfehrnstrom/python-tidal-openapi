# AlbumsAlbumStatisticsSingleRelationshipDataDocument

Target resource types: `albumStatistics`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.albums_album_statistics_single_relationship_data_document import AlbumsAlbumStatisticsSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsAlbumStatisticsSingleRelationshipDataDocument from a JSON string
albums_album_statistics_single_relationship_data_document_instance = AlbumsAlbumStatisticsSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumsAlbumStatisticsSingleRelationshipDataDocument.to_json())

# convert the object into a dict
albums_album_statistics_single_relationship_data_document_dict = albums_album_statistics_single_relationship_data_document_instance.to_dict()
# create an instance of AlbumsAlbumStatisticsSingleRelationshipDataDocument from a dict
albums_album_statistics_single_relationship_data_document_from_dict = AlbumsAlbumStatisticsSingleRelationshipDataDocument.from_dict(albums_album_statistics_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


