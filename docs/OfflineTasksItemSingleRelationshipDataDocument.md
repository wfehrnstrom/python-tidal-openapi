# OfflineTasksItemSingleRelationshipDataDocument

Target resource types: `albums`, `playlists`, `tracks`, `userCollectionTracks`, `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OfflineTasksItemResourceIdentifier**](OfflineTasksItemResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.offline_tasks_item_single_relationship_data_document import OfflineTasksItemSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineTasksItemSingleRelationshipDataDocument from a JSON string
offline_tasks_item_single_relationship_data_document_instance = OfflineTasksItemSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(OfflineTasksItemSingleRelationshipDataDocument.to_json())

# convert the object into a dict
offline_tasks_item_single_relationship_data_document_dict = offline_tasks_item_single_relationship_data_document_instance.to_dict()
# create an instance of OfflineTasksItemSingleRelationshipDataDocument from a dict
offline_tasks_item_single_relationship_data_document_from_dict = OfflineTasksItemSingleRelationshipDataDocument.from_dict(offline_tasks_item_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


