# FolderItemsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FolderItemsResourceObject**](FolderItemsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folder_items_create_single_resource_data_document import FolderItemsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsCreateSingleResourceDataDocument from a JSON string
folder_items_create_single_resource_data_document_instance = FolderItemsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(FolderItemsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
folder_items_create_single_resource_data_document_dict = folder_items_create_single_resource_data_document_instance.to_dict()
# create an instance of FolderItemsCreateSingleResourceDataDocument from a dict
folder_items_create_single_resource_data_document_from_dict = FolderItemsCreateSingleResourceDataDocument.from_dict(folder_items_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


