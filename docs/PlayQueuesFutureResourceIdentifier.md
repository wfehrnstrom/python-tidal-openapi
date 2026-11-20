# PlayQueuesFutureResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**PlayQueuesFutureResourceIdentifierMeta**](PlayQueuesFutureResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.play_queues_future_resource_identifier import PlayQueuesFutureResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesFutureResourceIdentifier from a JSON string
play_queues_future_resource_identifier_instance = PlayQueuesFutureResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesFutureResourceIdentifier.to_json())

# convert the object into a dict
play_queues_future_resource_identifier_dict = play_queues_future_resource_identifier_instance.to_dict()
# create an instance of PlayQueuesFutureResourceIdentifier from a dict
play_queues_future_resource_identifier_from_dict = PlayQueuesFutureResourceIdentifier.from_dict(play_queues_future_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


