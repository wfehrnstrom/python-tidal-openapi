# ArtworkSourceFile

Artwork source file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**md5_hash** | **str** | MD5 hash of file to be uploaded | 
**size** | **int** | File size of the artwork in bytes | 
**status** | [**FileStatus**](FileStatus.md) |  | 
**upload_link** | [**FileUploadLink**](FileUploadLink.md) |  | 

## Example

```python
from tidal.models.artwork_source_file import ArtworkSourceFile

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworkSourceFile from a JSON string
artwork_source_file_instance = ArtworkSourceFile.from_json(json)
# print the JSON string representation of the object
print(ArtworkSourceFile.to_json())

# convert the object into a dict
artwork_source_file_dict = artwork_source_file_instance.to_dict()
# create an instance of ArtworkSourceFile from a dict
artwork_source_file_from_dict = ArtworkSourceFile.from_dict(artwork_source_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


