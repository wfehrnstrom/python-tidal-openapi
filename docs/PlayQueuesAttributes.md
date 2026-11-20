# PlayQueuesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | ISO 8601 creation timestamp | 
**last_modified_at** | **datetime** | ISO 8601 last modified timestamp | 
**repeat** | **str** | Queue&#39;s repeat mode | 
**revision** | **UUID** | Opaque queue-wide equality token. | 
**shuffle** | **str** | Queue&#39;s shuffle mode | 
**shuffled** | **bool** | Queue is shuffled or not | 

## Example

```python
from tidal.models.play_queues_attributes import PlayQueuesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesAttributes from a JSON string
play_queues_attributes_instance = PlayQueuesAttributes.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesAttributes.to_json())

# convert the object into a dict
play_queues_attributes_dict = play_queues_attributes_instance.to_dict()
# create an instance of PlayQueuesAttributes from a dict
play_queues_attributes_from_dict = PlayQueuesAttributes.from_dict(play_queues_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


