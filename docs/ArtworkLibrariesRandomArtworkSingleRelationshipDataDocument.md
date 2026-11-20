# ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument

Target resource types: `artworks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtworkLibrariesRandomArtworkResourceIdentifier**](ArtworkLibrariesRandomArtworkResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artwork_libraries_random_artwork_single_relationship_data_document import ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument from a JSON string
artwork_libraries_random_artwork_single_relationship_data_document_instance = ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument.to_json())

# convert the object into a dict
artwork_libraries_random_artwork_single_relationship_data_document_dict = artwork_libraries_random_artwork_single_relationship_data_document_instance.to_dict()
# create an instance of ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument from a dict
artwork_libraries_random_artwork_single_relationship_data_document_from_dict = ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument.from_dict(artwork_libraries_random_artwork_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


