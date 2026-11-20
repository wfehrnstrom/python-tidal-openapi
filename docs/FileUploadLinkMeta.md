# FileUploadLinkMeta

metadata for upload link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, str]** | HTTP headers that must be added to the operation | [optional] 
**method** | **str** | HTTP method | 

## Example

```python
from tidal.models.file_upload_link_meta import FileUploadLinkMeta

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadLinkMeta from a JSON string
file_upload_link_meta_instance = FileUploadLinkMeta.from_json(json)
# print the JSON string representation of the object
print(FileUploadLinkMeta.to_json())

# convert the object into a dict
file_upload_link_meta_dict = file_upload_link_meta_instance.to_dict()
# create an instance of FileUploadLinkMeta from a dict
file_upload_link_meta_from_dict = FileUploadLinkMeta.from_dict(file_upload_link_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


