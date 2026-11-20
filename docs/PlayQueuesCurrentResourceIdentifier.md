# PlayQueuesCurrentResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**PlayQueuesCurrentResourceIdentifierMeta**](PlayQueuesCurrentResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.play_queues_current_resource_identifier import PlayQueuesCurrentResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesCurrentResourceIdentifier from a JSON string
play_queues_current_resource_identifier_instance = PlayQueuesCurrentResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesCurrentResourceIdentifier.to_json())

# convert the object into a dict
play_queues_current_resource_identifier_dict = play_queues_current_resource_identifier_instance.to_dict()
# create an instance of PlayQueuesCurrentResourceIdentifier from a dict
play_queues_current_resource_identifier_from_dict = PlayQueuesCurrentResourceIdentifier.from_dict(play_queues_current_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


