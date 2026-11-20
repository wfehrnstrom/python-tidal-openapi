# OfflineTasksCollectionResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**OfflineTasksCollectionResourceIdentifierMeta**](OfflineTasksCollectionResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.offline_tasks_collection_resource_identifier import OfflineTasksCollectionResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineTasksCollectionResourceIdentifier from a JSON string
offline_tasks_collection_resource_identifier_instance = OfflineTasksCollectionResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(OfflineTasksCollectionResourceIdentifier.to_json())

# convert the object into a dict
offline_tasks_collection_resource_identifier_dict = offline_tasks_collection_resource_identifier_instance.to_dict()
# create an instance of OfflineTasksCollectionResourceIdentifier from a dict
offline_tasks_collection_resource_identifier_from_dict = OfflineTasksCollectionResourceIdentifier.from_dict(offline_tasks_collection_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


