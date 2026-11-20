# FolderItemsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FolderItemsResourceObject]**](FolderItemsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folder_items_multi_resource_data_document import FolderItemsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsMultiResourceDataDocument from a JSON string
folder_items_multi_resource_data_document_instance = FolderItemsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(FolderItemsMultiResourceDataDocument.to_json())

# convert the object into a dict
folder_items_multi_resource_data_document_dict = folder_items_multi_resource_data_document_instance.to_dict()
# create an instance of FolderItemsMultiResourceDataDocument from a dict
folder_items_multi_resource_data_document_from_dict = FolderItemsMultiResourceDataDocument.from_dict(folder_items_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


