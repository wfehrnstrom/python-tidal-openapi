# UserCollectionFoldersAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**last_modified_at** | **datetime** |  | 
**name** | **str** |  | 
**number_of_items** | **int** |  | [optional] 

## Example

```python
from tidal.models.user_collection_folders_attributes import UserCollectionFoldersAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionFoldersAttributes from a JSON string
user_collection_folders_attributes_instance = UserCollectionFoldersAttributes.from_json(json)
# print the JSON string representation of the object
print(UserCollectionFoldersAttributes.to_json())

# convert the object into a dict
user_collection_folders_attributes_dict = user_collection_folders_attributes_instance.to_dict()
# create an instance of UserCollectionFoldersAttributes from a dict
user_collection_folders_attributes_from_dict = UserCollectionFoldersAttributes.from_dict(user_collection_folders_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


