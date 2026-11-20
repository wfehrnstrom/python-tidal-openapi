# UserCollectionFoldersResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserCollectionFoldersAttributes**](UserCollectionFoldersAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserCollectionFoldersRelationships**](UserCollectionFoldersRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_collection_folders_resource_object import UserCollectionFoldersResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionFoldersResourceObject from a JSON string
user_collection_folders_resource_object_instance = UserCollectionFoldersResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserCollectionFoldersResourceObject.to_json())

# convert the object into a dict
user_collection_folders_resource_object_dict = user_collection_folders_resource_object_instance.to_dict()
# create an instance of UserCollectionFoldersResourceObject from a dict
user_collection_folders_resource_object_from_dict = UserCollectionFoldersResourceObject.from_dict(user_collection_folders_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


