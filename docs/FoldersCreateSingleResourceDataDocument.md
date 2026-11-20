# FoldersCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FoldersResourceObject**](FoldersResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folders_create_single_resource_data_document import FoldersCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersCreateSingleResourceDataDocument from a JSON string
folders_create_single_resource_data_document_instance = FoldersCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(FoldersCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
folders_create_single_resource_data_document_dict = folders_create_single_resource_data_document_instance.to_dict()
# create an instance of FoldersCreateSingleResourceDataDocument from a dict
folders_create_single_resource_data_document_from_dict = FoldersCreateSingleResourceDataDocument.from_dict(folders_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


