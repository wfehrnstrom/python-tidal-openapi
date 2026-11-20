# PlayQueuesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlayQueuesResourceObject**](PlayQueuesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.play_queues_single_resource_data_document import PlayQueuesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesSingleResourceDataDocument from a JSON string
play_queues_single_resource_data_document_instance = PlayQueuesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesSingleResourceDataDocument.to_json())

# convert the object into a dict
play_queues_single_resource_data_document_dict = play_queues_single_resource_data_document_instance.to_dict()
# create an instance of PlayQueuesSingleResourceDataDocument from a dict
play_queues_single_resource_data_document_from_dict = PlayQueuesSingleResourceDataDocument.from_dict(play_queues_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


