# ArtworkFile

Artwork files

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Artwork file href | 
**meta** | [**ArtworkFileMeta**](ArtworkFileMeta.md) |  | [optional] 
**type** | **str** | Media type hint for the artwork file | [optional] 

## Example

```python
from tidal.models.artwork_file import ArtworkFile

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworkFile from a JSON string
artwork_file_instance = ArtworkFile.from_json(json)
# print the JSON string representation of the object
print(ArtworkFile.to_json())

# convert the object into a dict
artwork_file_dict = artwork_file_instance.to_dict()
# create an instance of ArtworkFile from a dict
artwork_file_from_dict = ArtworkFile.from_dict(artwork_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


