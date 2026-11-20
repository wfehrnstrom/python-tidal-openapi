# AlbumsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_statistics** | [**AlbumsAlbumStatisticsSingleRelationshipDataDocument**](AlbumsAlbumStatisticsSingleRelationshipDataDocument.md) |  | [optional] 
**artists** | [**AlbumsArtistsMultiRelationshipDataDocument**](AlbumsArtistsMultiRelationshipDataDocument.md) |  | [optional] 
**cover_art** | [**AlbumsCoverArtMultiRelationshipDataDocument**](AlbumsCoverArtMultiRelationshipDataDocument.md) |  | [optional] 
**genres** | [**AlbumsGenresMultiRelationshipDataDocument**](AlbumsGenresMultiRelationshipDataDocument.md) |  | [optional] 
**items** | [**AlbumsItemsMultiRelationshipDataDocument**](AlbumsItemsMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**AlbumsOwnersMultiRelationshipDataDocument**](AlbumsOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**price_config** | [**AlbumsPriceConfigSingleRelationshipDataDocument**](AlbumsPriceConfigSingleRelationshipDataDocument.md) |  | [optional] 
**providers** | [**AlbumsProvidersMultiRelationshipDataDocument**](AlbumsProvidersMultiRelationshipDataDocument.md) |  | [optional] 
**replacement** | [**AlbumsReplacementSingleRelationshipDataDocument**](AlbumsReplacementSingleRelationshipDataDocument.md) |  | [optional] 
**shares** | [**AlbumsSharesMultiRelationshipDataDocument**](AlbumsSharesMultiRelationshipDataDocument.md) |  | [optional] 
**similar_albums** | [**AlbumsSimilarAlbumsMultiRelationshipDataDocument**](AlbumsSimilarAlbumsMultiRelationshipDataDocument.md) |  | [optional] 
**suggested_cover_arts** | [**AlbumsSuggestedCoverArtsMultiRelationshipDataDocument**](AlbumsSuggestedCoverArtsMultiRelationshipDataDocument.md) |  | [optional] 
**usage_rules** | [**AlbumsUsageRulesSingleRelationshipDataDocument**](AlbumsUsageRulesSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.albums_relationships import AlbumsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsRelationships from a JSON string
albums_relationships_instance = AlbumsRelationships.from_json(json)
# print the JSON string representation of the object
print(AlbumsRelationships.to_json())

# convert the object into a dict
albums_relationships_dict = albums_relationships_instance.to_dict()
# create an instance of AlbumsRelationships from a dict
albums_relationships_from_dict = AlbumsRelationships.from_dict(albums_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


