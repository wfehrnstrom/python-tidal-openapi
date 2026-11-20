# DownloadsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DownloadsResourceObject**](DownloadsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.downloads_single_resource_data_document import DownloadsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadsSingleResourceDataDocument from a JSON string
downloads_single_resource_data_document_instance = DownloadsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(DownloadsSingleResourceDataDocument.to_json())

# convert the object into a dict
downloads_single_resource_data_document_dict = downloads_single_resource_data_document_instance.to_dict()
# create an instance of DownloadsSingleResourceDataDocument from a dict
downloads_single_resource_data_document_from_dict = DownloadsSingleResourceDataDocument.from_dict(downloads_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


