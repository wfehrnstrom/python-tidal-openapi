# OfflineTasksOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.offline_tasks_owners_multi_relationship_data_document import OfflineTasksOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineTasksOwnersMultiRelationshipDataDocument from a JSON string
offline_tasks_owners_multi_relationship_data_document_instance = OfflineTasksOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(OfflineTasksOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
offline_tasks_owners_multi_relationship_data_document_dict = offline_tasks_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of OfflineTasksOwnersMultiRelationshipDataDocument from a dict
offline_tasks_owners_multi_relationship_data_document_from_dict = OfflineTasksOwnersMultiRelationshipDataDocument.from_dict(offline_tasks_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


