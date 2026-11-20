# OfflineTasksItemResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**OfflineTasksItemResourceIdentifierMeta**](OfflineTasksItemResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.offline_tasks_item_resource_identifier import OfflineTasksItemResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineTasksItemResourceIdentifier from a JSON string
offline_tasks_item_resource_identifier_instance = OfflineTasksItemResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(OfflineTasksItemResourceIdentifier.to_json())

# convert the object into a dict
offline_tasks_item_resource_identifier_dict = offline_tasks_item_resource_identifier_instance.to_dict()
# create an instance of OfflineTasksItemResourceIdentifier from a dict
offline_tasks_item_resource_identifier_from_dict = OfflineTasksItemResourceIdentifier.from_dict(offline_tasks_item_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


