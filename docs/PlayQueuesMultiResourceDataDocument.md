# PlayQueuesMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlayQueuesResourceObject]**](PlayQueuesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.play_queues_multi_resource_data_document import PlayQueuesMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesMultiResourceDataDocument from a JSON string
play_queues_multi_resource_data_document_instance = PlayQueuesMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesMultiResourceDataDocument.to_json())

# convert the object into a dict
play_queues_multi_resource_data_document_dict = play_queues_multi_resource_data_document_instance.to_dict()
# create an instance of PlayQueuesMultiResourceDataDocument from a dict
play_queues_multi_resource_data_document_from_dict = PlayQueuesMultiResourceDataDocument.from_dict(play_queues_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


