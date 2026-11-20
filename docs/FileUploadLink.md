# FileUploadLink

Upload link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Href to upload actual file to | 
**meta** | [**FileUploadLinkMeta**](FileUploadLinkMeta.md) |  | 

## Example

```python
from tidal.models.file_upload_link import FileUploadLink

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadLink from a JSON string
file_upload_link_instance = FileUploadLink.from_json(json)
# print the JSON string representation of the object
print(FileUploadLink.to_json())

# convert the object into a dict
file_upload_link_dict = file_upload_link_instance.to_dict()
# create an instance of FileUploadLink from a dict
file_upload_link_from_dict = FileUploadLink.from_dict(file_upload_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


