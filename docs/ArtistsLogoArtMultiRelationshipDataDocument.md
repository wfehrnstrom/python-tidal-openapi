# ArtistsLogoArtMultiRelationshipDataDocument

Target resource types: `artworks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_logo_art_multi_relationship_data_document import ArtistsLogoArtMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsLogoArtMultiRelationshipDataDocument from a JSON string
artists_logo_art_multi_relationship_data_document_instance = ArtistsLogoArtMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsLogoArtMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artists_logo_art_multi_relationship_data_document_dict = artists_logo_art_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistsLogoArtMultiRelationshipDataDocument from a dict
artists_logo_art_multi_relationship_data_document_from_dict = ArtistsLogoArtMultiRelationshipDataDocument.from_dict(artists_logo_art_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


