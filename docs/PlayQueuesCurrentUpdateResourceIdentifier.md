# PlayQueuesCurrentUpdateResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**PlayQueuesCurrentUpdateResourceIdentifierMeta**](PlayQueuesCurrentUpdateResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.play_queues_current_update_resource_identifier import PlayQueuesCurrentUpdateResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesCurrentUpdateResourceIdentifier from a JSON string
play_queues_current_update_resource_identifier_instance = PlayQueuesCurrentUpdateResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesCurrentUpdateResourceIdentifier.to_json())

# convert the object into a dict
play_queues_current_update_resource_identifier_dict = play_queues_current_update_resource_identifier_instance.to_dict()
# create an instance of PlayQueuesCurrentUpdateResourceIdentifier from a dict
play_queues_current_update_resource_identifier_from_dict = PlayQueuesCurrentUpdateResourceIdentifier.from_dict(play_queues_current_update_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


