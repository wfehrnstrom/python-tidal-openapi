# UserCollectionFoldersMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserCollectionFoldersResourceObject]**](UserCollectionFoldersResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_collection_folders_multi_resource_data_document import UserCollectionFoldersMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionFoldersMultiResourceDataDocument from a JSON string
user_collection_folders_multi_resource_data_document_instance = UserCollectionFoldersMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionFoldersMultiResourceDataDocument.to_json())

# convert the object into a dict
user_collection_folders_multi_resource_data_document_dict = user_collection_folders_multi_resource_data_document_instance.to_dict()
# create an instance of UserCollectionFoldersMultiResourceDataDocument from a dict
user_collection_folders_multi_resource_data_document_from_dict = UserCollectionFoldersMultiResourceDataDocument.from_dict(user_collection_folders_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


