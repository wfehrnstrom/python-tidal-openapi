# FoldersSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FoldersResourceObject**](FoldersResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folders_single_resource_data_document import FoldersSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersSingleResourceDataDocument from a JSON string
folders_single_resource_data_document_instance = FoldersSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(FoldersSingleResourceDataDocument.to_json())

# convert the object into a dict
folders_single_resource_data_document_dict = folders_single_resource_data_document_instance.to_dict()
# create an instance of FoldersSingleResourceDataDocument from a dict
folders_single_resource_data_document_from_dict = FoldersSingleResourceDataDocument.from_dict(folders_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


