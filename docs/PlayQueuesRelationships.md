# PlayQueuesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_event_stream** | [**PlayQueuesChangeEventStreamSingleRelationshipDataDocument**](PlayQueuesChangeEventStreamSingleRelationshipDataDocument.md) |  | [optional] 
**current** | [**PlayQueuesCurrentSingleRelationshipDataDocument**](PlayQueuesCurrentSingleRelationshipDataDocument.md) |  | [optional] 
**future** | [**PlayQueuesFutureMultiRelationshipDataDocument**](PlayQueuesFutureMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**PlayQueuesOwnersMultiRelationshipDataDocument**](PlayQueuesOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**past** | [**PlayQueuesPastMultiRelationshipDataDocument**](PlayQueuesPastMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.play_queues_relationships import PlayQueuesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesRelationships from a JSON string
play_queues_relationships_instance = PlayQueuesRelationships.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesRelationships.to_json())

# convert the object into a dict
play_queues_relationships_dict = play_queues_relationships_instance.to_dict()
# create an instance of PlayQueuesRelationships from a dict
play_queues_relationships_from_dict = PlayQueuesRelationships.from_dict(play_queues_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


