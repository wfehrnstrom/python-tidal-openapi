# ArtworkFileMeta

Metadata about an artwork file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** | Height (in pixels) | 
**width** | **int** | Width (in pixels) | 

## Example

```python
from tidal.models.artwork_file_meta import ArtworkFileMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworkFileMeta from a JSON string
artwork_file_meta_instance = ArtworkFileMeta.from_json(json)
# print the JSON string representation of the object
print(ArtworkFileMeta.to_json())

# convert the object into a dict
artwork_file_meta_dict = artwork_file_meta_instance.to_dict()
# create an instance of ArtworkFileMeta from a dict
artwork_file_meta_from_dict = ArtworkFileMeta.from_dict(artwork_file_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


