# FoldersMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FoldersResourceObject]**](FoldersResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folders_multi_resource_data_document import FoldersMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersMultiResourceDataDocument from a JSON string
folders_multi_resource_data_document_instance = FoldersMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(FoldersMultiResourceDataDocument.to_json())

# convert the object into a dict
folders_multi_resource_data_document_dict = folders_multi_resource_data_document_instance.to_dict()
# create an instance of FoldersMultiResourceDataDocument from a dict
folders_multi_resource_data_document_from_dict = FoldersMultiResourceDataDocument.from_dict(folders_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


