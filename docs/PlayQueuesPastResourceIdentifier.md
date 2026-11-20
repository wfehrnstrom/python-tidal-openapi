# PlayQueuesPastResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**PlayQueuesPastResourceIdentifierMeta**](PlayQueuesPastResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.play_queues_past_resource_identifier import PlayQueuesPastResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesPastResourceIdentifier from a JSON string
play_queues_past_resource_identifier_instance = PlayQueuesPastResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesPastResourceIdentifier.to_json())

# convert the object into a dict
play_queues_past_resource_identifier_dict = play_queues_past_resource_identifier_instance.to_dict()
# create an instance of PlayQueuesPastResourceIdentifier from a dict
play_queues_past_resource_identifier_from_dict = PlayQueuesPastResourceIdentifier.from_dict(play_queues_past_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


