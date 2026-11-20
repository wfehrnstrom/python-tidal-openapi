# FoldersUpdateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FoldersResourceObject**](FoldersResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folders_update_single_resource_data_document import FoldersUpdateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersUpdateSingleResourceDataDocument from a JSON string
folders_update_single_resource_data_document_instance = FoldersUpdateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(FoldersUpdateSingleResourceDataDocument.to_json())

# convert the object into a dict
folders_update_single_resource_data_document_dict = folders_update_single_resource_data_document_instance.to_dict()
# create an instance of FoldersUpdateSingleResourceDataDocument from a dict
folders_update_single_resource_data_document_from_dict = FoldersUpdateSingleResourceDataDocument.from_dict(folders_update_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


