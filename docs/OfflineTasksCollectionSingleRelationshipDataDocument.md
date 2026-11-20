# OfflineTasksCollectionSingleRelationshipDataDocument

Target resource types: `albums`, `playlists`, `tracks`, `userCollectionTracks`, `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OfflineTasksCollectionResourceIdentifier**](OfflineTasksCollectionResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.offline_tasks_collection_single_relationship_data_document import OfflineTasksCollectionSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineTasksCollectionSingleRelationshipDataDocument from a JSON string
offline_tasks_collection_single_relationship_data_document_instance = OfflineTasksCollectionSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(OfflineTasksCollectionSingleRelationshipDataDocument.to_json())

# convert the object into a dict
offline_tasks_collection_single_relationship_data_document_dict = offline_tasks_collection_single_relationship_data_document_instance.to_dict()
# create an instance of OfflineTasksCollectionSingleRelationshipDataDocument from a dict
offline_tasks_collection_single_relationship_data_document_from_dict = OfflineTasksCollectionSingleRelationshipDataDocument.from_dict(offline_tasks_collection_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


