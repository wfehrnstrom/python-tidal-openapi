# ArtworkLibrariesArtworksMultiRelationshipDataDocument

Target resource types: `artworks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtworkLibrariesArtworksResourceIdentifier]**](ArtworkLibrariesArtworksResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artwork_libraries_artworks_multi_relationship_data_document import ArtworkLibrariesArtworksMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworkLibrariesArtworksMultiRelationshipDataDocument from a JSON string
artwork_libraries_artworks_multi_relationship_data_document_instance = ArtworkLibrariesArtworksMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtworkLibrariesArtworksMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artwork_libraries_artworks_multi_relationship_data_document_dict = artwork_libraries_artworks_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtworkLibrariesArtworksMultiRelationshipDataDocument from a dict
artwork_libraries_artworks_multi_relationship_data_document_from_dict = ArtworkLibrariesArtworksMultiRelationshipDataDocument.from_dict(artwork_libraries_artworks_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


