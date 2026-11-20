# ArtworkLibrariesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artworks** | [**ArtworkLibrariesArtworksMultiRelationshipDataDocument**](ArtworkLibrariesArtworksMultiRelationshipDataDocument.md) |  | [optional] 
**random_artwork** | [**ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument**](ArtworkLibrariesRandomArtworkSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.artwork_libraries_relationships import ArtworkLibrariesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworkLibrariesRelationships from a JSON string
artwork_libraries_relationships_instance = ArtworkLibrariesRelationships.from_json(json)
# print the JSON string representation of the object
print(ArtworkLibrariesRelationships.to_json())

# convert the object into a dict
artwork_libraries_relationships_dict = artwork_libraries_relationships_instance.to_dict()
# create an instance of ArtworkLibrariesRelationships from a dict
artwork_libraries_relationships_from_dict = ArtworkLibrariesRelationships.from_dict(artwork_libraries_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


