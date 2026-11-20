# PlayQueuesFutureRelationshipSource

Adds up to 1000 playable items from a relationship page and subsequent pages, reading at most 100 pages. Requires empty data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | API-relative self link of a TIDAL API to-many relationship page. | 
**start_index** | **int** | Zero-based index in the page&#39;s complete data array from which to start adding. | 

## Example

```python
from tidal.models.play_queues_future_relationship_source import PlayQueuesFutureRelationshipSource

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesFutureRelationshipSource from a JSON string
play_queues_future_relationship_source_instance = PlayQueuesFutureRelationshipSource.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesFutureRelationshipSource.to_json())

# convert the object into a dict
play_queues_future_relationship_source_dict = play_queues_future_relationship_source_instance.to_dict()
# create an instance of PlayQueuesFutureRelationshipSource from a dict
play_queues_future_relationship_source_from_dict = PlayQueuesFutureRelationshipSource.from_dict(play_queues_future_relationship_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


