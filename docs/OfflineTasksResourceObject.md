# OfflineTasksResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**OfflineTasksAttributes**](OfflineTasksAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**OfflineTasksRelationships**](OfflineTasksRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.offline_tasks_resource_object import OfflineTasksResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineTasksResourceObject from a JSON string
offline_tasks_resource_object_instance = OfflineTasksResourceObject.from_json(json)
# print the JSON string representation of the object
print(OfflineTasksResourceObject.to_json())

# convert the object into a dict
offline_tasks_resource_object_dict = offline_tasks_resource_object_instance.to_dict()
# create an instance of OfflineTasksResourceObject from a dict
offline_tasks_resource_object_from_dict = OfflineTasksResourceObject.from_dict(offline_tasks_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


