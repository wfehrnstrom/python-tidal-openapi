# FolderItemsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FolderItemsResourceObject**](FolderItemsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folder_items_single_resource_data_document import FolderItemsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsSingleResourceDataDocument from a JSON string
folder_items_single_resource_data_document_instance = FolderItemsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(FolderItemsSingleResourceDataDocument.to_json())

# convert the object into a dict
folder_items_single_resource_data_document_dict = folder_items_single_resource_data_document_instance.to_dict()
# create an instance of FolderItemsSingleResourceDataDocument from a dict
folder_items_single_resource_data_document_from_dict = FolderItemsSingleResourceDataDocument.from_dict(folder_items_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


