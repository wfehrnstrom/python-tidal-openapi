# PlayQueuesCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlayQueuesResourceObject**](PlayQueuesResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | [**PlayQueuesCreateSingleResourceDataDocumentMeta**](PlayQueuesCreateSingleResourceDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.play_queues_create_single_resource_data_document import PlayQueuesCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesCreateSingleResourceDataDocument from a JSON string
play_queues_create_single_resource_data_document_instance = PlayQueuesCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
play_queues_create_single_resource_data_document_dict = play_queues_create_single_resource_data_document_instance.to_dict()
# create an instance of PlayQueuesCreateSingleResourceDataDocument from a dict
play_queues_create_single_resource_data_document_from_dict = PlayQueuesCreateSingleResourceDataDocument.from_dict(play_queues_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


