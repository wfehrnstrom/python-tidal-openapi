# OfflineTasksRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**OfflineTasksCollectionSingleRelationshipDataDocument**](OfflineTasksCollectionSingleRelationshipDataDocument.md) |  | [optional] 
**item** | [**OfflineTasksItemSingleRelationshipDataDocument**](OfflineTasksItemSingleRelationshipDataDocument.md) |  | [optional] 
**owners** | [**OfflineTasksOwnersMultiRelationshipDataDocument**](OfflineTasksOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.offline_tasks_relationships import OfflineTasksRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineTasksRelationships from a JSON string
offline_tasks_relationships_instance = OfflineTasksRelationships.from_json(json)
# print the JSON string representation of the object
print(OfflineTasksRelationships.to_json())

# convert the object into a dict
offline_tasks_relationships_dict = offline_tasks_relationships_instance.to_dict()
# create an instance of OfflineTasksRelationships from a dict
offline_tasks_relationships_from_dict = OfflineTasksRelationships.from_dict(offline_tasks_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


