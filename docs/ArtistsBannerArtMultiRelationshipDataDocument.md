# ArtistsBannerArtMultiRelationshipDataDocument

Target resource types: `artworks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_banner_art_multi_relationship_data_document import ArtistsBannerArtMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsBannerArtMultiRelationshipDataDocument from a JSON string
artists_banner_art_multi_relationship_data_document_instance = ArtistsBannerArtMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsBannerArtMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artists_banner_art_multi_relationship_data_document_dict = artists_banner_art_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistsBannerArtMultiRelationshipDataDocument from a dict
artists_banner_art_multi_relationship_data_document_from_dict = ArtistsBannerArtMultiRelationshipDataDocument.from_dict(artists_banner_art_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


