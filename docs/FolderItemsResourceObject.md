# FolderItemsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**FolderItemsAttributes**](FolderItemsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**FolderItemsRelationships**](FolderItemsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.folder_items_resource_object import FolderItemsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsResourceObject from a JSON string
folder_items_resource_object_instance = FolderItemsResourceObject.from_json(json)
# print the JSON string representation of the object
print(FolderItemsResourceObject.to_json())

# convert the object into a dict
folder_items_resource_object_dict = folder_items_resource_object_instance.to_dict()
# create an instance of FolderItemsResourceObject from a dict
folder_items_resource_object_from_dict = FolderItemsResourceObject.from_dict(folder_items_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


