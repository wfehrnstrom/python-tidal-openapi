# ArtworksAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[ArtworkFile]**](ArtworkFile.md) | Artwork files | 
**media_type** | **str** | Media type of artwork files | 
**source_file** | [**ArtworkSourceFile**](ArtworkSourceFile.md) |  | [optional] 
**visual_metadata** | [**ArtworkVisualMetadata**](ArtworkVisualMetadata.md) |  | [optional] 

## Example

```python
from tidal.models.artworks_attributes import ArtworksAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworksAttributes from a JSON string
artworks_attributes_instance = ArtworksAttributes.from_json(json)
# print the JSON string representation of the object
print(ArtworksAttributes.to_json())

# convert the object into a dict
artworks_attributes_dict = artworks_attributes_instance.to_dict()
# create an instance of ArtworksAttributes from a dict
artworks_attributes_from_dict = ArtworksAttributes.from_dict(artworks_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


