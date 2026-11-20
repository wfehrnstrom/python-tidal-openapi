# FoldersResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**FoldersAttributes**](FoldersAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**FoldersRelationships**](FoldersRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.folders_resource_object import FoldersResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersResourceObject from a JSON string
folders_resource_object_instance = FoldersResourceObject.from_json(json)
# print the JSON string representation of the object
print(FoldersResourceObject.to_json())

# convert the object into a dict
folders_resource_object_dict = folders_resource_object_instance.to_dict()
# create an instance of FoldersResourceObject from a dict
folders_resource_object_from_dict = FoldersResourceObject.from_dict(folders_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


