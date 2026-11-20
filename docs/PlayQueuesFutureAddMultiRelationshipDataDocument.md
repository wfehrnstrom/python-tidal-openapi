# PlayQueuesFutureAddMultiRelationshipDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlayQueuesFutureAddResourceIdentifier]**](PlayQueuesFutureAddResourceIdentifier.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | [**PlayQueuesFutureAddMultiRelationshipDataDocumentMeta**](PlayQueuesFutureAddMultiRelationshipDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.play_queues_future_add_multi_relationship_data_document import PlayQueuesFutureAddMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesFutureAddMultiRelationshipDataDocument from a JSON string
play_queues_future_add_multi_relationship_data_document_instance = PlayQueuesFutureAddMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesFutureAddMultiRelationshipDataDocument.to_json())

# convert the object into a dict
play_queues_future_add_multi_relationship_data_document_dict = play_queues_future_add_multi_relationship_data_document_instance.to_dict()
# create an instance of PlayQueuesFutureAddMultiRelationshipDataDocument from a dict
play_queues_future_add_multi_relationship_data_document_from_dict = PlayQueuesFutureAddMultiRelationshipDataDocument.from_dict(play_queues_future_add_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


