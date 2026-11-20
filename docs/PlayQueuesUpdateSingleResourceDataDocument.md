# PlayQueuesUpdateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlayQueuesResourceObject**](PlayQueuesResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | [**PlayQueuesUpdateSingleResourceDataDocumentMeta**](PlayQueuesUpdateSingleResourceDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.play_queues_update_single_resource_data_document import PlayQueuesUpdateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesUpdateSingleResourceDataDocument from a JSON string
play_queues_update_single_resource_data_document_instance = PlayQueuesUpdateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesUpdateSingleResourceDataDocument.to_json())

# convert the object into a dict
play_queues_update_single_resource_data_document_dict = play_queues_update_single_resource_data_document_instance.to_dict()
# create an instance of PlayQueuesUpdateSingleResourceDataDocument from a dict
play_queues_update_single_resource_data_document_from_dict = PlayQueuesUpdateSingleResourceDataDocument.from_dict(play_queues_update_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


