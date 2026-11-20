# PlayQueuesCurrentUpdateSingleRelationshipDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlayQueuesCurrentUpdateResourceIdentifier**](PlayQueuesCurrentUpdateResourceIdentifier.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | [**PlayQueuesCurrentUpdateSingleRelationshipDataDocumentMeta**](PlayQueuesCurrentUpdateSingleRelationshipDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.play_queues_current_update_single_relationship_data_document import PlayQueuesCurrentUpdateSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesCurrentUpdateSingleRelationshipDataDocument from a JSON string
play_queues_current_update_single_relationship_data_document_instance = PlayQueuesCurrentUpdateSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesCurrentUpdateSingleRelationshipDataDocument.to_json())

# convert the object into a dict
play_queues_current_update_single_relationship_data_document_dict = play_queues_current_update_single_relationship_data_document_instance.to_dict()
# create an instance of PlayQueuesCurrentUpdateSingleRelationshipDataDocument from a dict
play_queues_current_update_single_relationship_data_document_from_dict = PlayQueuesCurrentUpdateSingleRelationshipDataDocument.from_dict(play_queues_current_update_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


