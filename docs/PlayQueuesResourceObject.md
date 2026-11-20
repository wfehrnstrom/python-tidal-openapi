# PlayQueuesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PlayQueuesAttributes**](PlayQueuesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**PlayQueuesRelationships**](PlayQueuesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.play_queues_resource_object import PlayQueuesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesResourceObject from a JSON string
play_queues_resource_object_instance = PlayQueuesResourceObject.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesResourceObject.to_json())

# convert the object into a dict
play_queues_resource_object_dict = play_queues_resource_object_instance.to_dict()
# create an instance of PlayQueuesResourceObject from a dict
play_queues_resource_object_from_dict = PlayQueuesResourceObject.from_dict(play_queues_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


