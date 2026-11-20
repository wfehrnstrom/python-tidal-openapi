# DownloadsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DownloadsResourceObject]**](DownloadsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.downloads_multi_resource_data_document import DownloadsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadsMultiResourceDataDocument from a JSON string
downloads_multi_resource_data_document_instance = DownloadsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(DownloadsMultiResourceDataDocument.to_json())

# convert the object into a dict
downloads_multi_resource_data_document_dict = downloads_multi_resource_data_document_instance.to_dict()
# create an instance of DownloadsMultiResourceDataDocument from a dict
downloads_multi_resource_data_document_from_dict = DownloadsMultiResourceDataDocument.from_dict(downloads_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


