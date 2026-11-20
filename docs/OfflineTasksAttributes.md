# OfflineTasksAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action to perform | 
**position** | **int** | Collection position of item | 
**state** | **str** | Task state | 
**volume** | **int** | Collection volume of item | 

## Example

```python
from tidal.models.offline_tasks_attributes import OfflineTasksAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineTasksAttributes from a JSON string
offline_tasks_attributes_instance = OfflineTasksAttributes.from_json(json)
# print the JSON string representation of the object
print(OfflineTasksAttributes.to_json())

# convert the object into a dict
offline_tasks_attributes_dict = offline_tasks_attributes_instance.to_dict()
# create an instance of OfflineTasksAttributes from a dict
offline_tasks_attributes_from_dict = OfflineTasksAttributes.from_dict(offline_tasks_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


