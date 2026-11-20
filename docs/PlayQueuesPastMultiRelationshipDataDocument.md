# PlayQueuesPastMultiRelationshipDataDocument

Target resource types: `tracks`, `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlayQueuesPastResourceIdentifier]**](PlayQueuesPastResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.play_queues_past_multi_relationship_data_document import PlayQueuesPastMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesPastMultiRelationshipDataDocument from a JSON string
play_queues_past_multi_relationship_data_document_instance = PlayQueuesPastMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesPastMultiRelationshipDataDocument.to_json())

# convert the object into a dict
play_queues_past_multi_relationship_data_document_dict = play_queues_past_multi_relationship_data_document_instance.to_dict()
# create an instance of PlayQueuesPastMultiRelationshipDataDocument from a dict
play_queues_past_multi_relationship_data_document_from_dict = PlayQueuesPastMultiRelationshipDataDocument.from_dict(play_queues_past_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


