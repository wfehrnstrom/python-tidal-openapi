# UserCollectionFoldersCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserCollectionFoldersResourceObject**](UserCollectionFoldersResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_collection_folders_create_single_resource_data_document import UserCollectionFoldersCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionFoldersCreateSingleResourceDataDocument from a JSON string
user_collection_folders_create_single_resource_data_document_instance = UserCollectionFoldersCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionFoldersCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
user_collection_folders_create_single_resource_data_document_dict = user_collection_folders_create_single_resource_data_document_instance.to_dict()
# create an instance of UserCollectionFoldersCreateSingleResourceDataDocument from a dict
user_collection_folders_create_single_resource_data_document_from_dict = UserCollectionFoldersCreateSingleResourceDataDocument.from_dict(user_collection_folders_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


