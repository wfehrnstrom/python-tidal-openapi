# ArtworkVisualMetadata

Color information extracted from artwork

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blur_hash** | **str** | BlurHash representation of the artwork for placeholder display | [optional] 
**selected_palette_color** | **str** | Selected color from the extracted artwork palette | [optional] 
**status** | **str** | Status of visual metadata extraction | [optional] 

## Example

```python
from tidal.models.artwork_visual_metadata import ArtworkVisualMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworkVisualMetadata from a JSON string
artwork_visual_metadata_instance = ArtworkVisualMetadata.from_json(json)
# print the JSON string representation of the object
print(ArtworkVisualMetadata.to_json())

# convert the object into a dict
artwork_visual_metadata_dict = artwork_visual_metadata_instance.to_dict()
# create an instance of ArtworkVisualMetadata from a dict
artwork_visual_metadata_from_dict = ArtworkVisualMetadata.from_dict(artwork_visual_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


