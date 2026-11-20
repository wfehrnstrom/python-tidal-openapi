# ArtworkLibrariesRandomArtworkResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**ArtworkLibrariesRandomArtworkResourceIdentifierMeta**](ArtworkLibrariesRandomArtworkResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artwork_libraries_random_artwork_resource_identifier import ArtworkLibrariesRandomArtworkResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworkLibrariesRandomArtworkResourceIdentifier from a JSON string
artwork_libraries_random_artwork_resource_identifier_instance = ArtworkLibrariesRandomArtworkResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ArtworkLibrariesRandomArtworkResourceIdentifier.to_json())

# convert the object into a dict
artwork_libraries_random_artwork_resource_identifier_dict = artwork_libraries_random_artwork_resource_identifier_instance.to_dict()
# create an instance of ArtworkLibrariesRandomArtworkResourceIdentifier from a dict
artwork_libraries_random_artwork_resource_identifier_from_dict = ArtworkLibrariesRandomArtworkResourceIdentifier.from_dict(artwork_libraries_random_artwork_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


