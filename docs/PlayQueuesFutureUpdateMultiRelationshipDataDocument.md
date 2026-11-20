# PlayQueuesFutureUpdateMultiRelationshipDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlayQueuesFutureUpdateResourceIdentifier]**](PlayQueuesFutureUpdateResourceIdentifier.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | [**PlayQueuesFutureUpdateMultiRelationshipDataDocumentMeta**](PlayQueuesFutureUpdateMultiRelationshipDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.play_queues_future_update_multi_relationship_data_document import PlayQueuesFutureUpdateMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesFutureUpdateMultiRelationshipDataDocument from a JSON string
play_queues_future_update_multi_relationship_data_document_instance = PlayQueuesFutureUpdateMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesFutureUpdateMultiRelationshipDataDocument.to_json())

# convert the object into a dict
play_queues_future_update_multi_relationship_data_document_dict = play_queues_future_update_multi_relationship_data_document_instance.to_dict()
# create an instance of PlayQueuesFutureUpdateMultiRelationshipDataDocument from a dict
play_queues_future_update_multi_relationship_data_document_from_dict = PlayQueuesFutureUpdateMultiRelationshipDataDocument.from_dict(play_queues_future_update_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


